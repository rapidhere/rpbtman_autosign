#!/usr/bin/python
#-*- coding: utf-8 -*-

import tieba,err,sign
import time,threading,urllib2,random
import datetime,pytz
from task_list import TASK_LIST

# Multi Thread Sign Support for sign
# Not use in this version
# Beacause www.baidu.com's server will refuse the frequency sign
# class SignThread(threading.Thread):
#    def __init__(self,tb,tb_kwd):
#        threading.Thread.__init__(self)
#        self._tb = tb
#        self._kw = tb_kwd
#
#    def run(self):
#        self.RunState = 0
#
#        print "Signing %s [tb = %s]" % (self._tb.get_username(),self._kw)
#        try:
#            self._tb.sign(self._kw)
#        except sign.SignError,s:
#            print s.FormatStr()
#            self.RunState = s.eid
#
#        print "Sign Done %s [tb = %s]" % (self._tb.get_username(),self._kw)
#
#    def state(self):
#        return self.RunState

# Store datas on Google App Engine Datastore
# Avoid multi-sign
from google.appengine.ext import db
class SignResult(db.Model):
    user = db.StringProperty()
    tkwd = db.StringProperty()
    erro = db.IntegerProperty()
    time = db.DateProperty()
    rtim = db.DateTimeProperty()

class SignDoneMark(db.Model):
    user = db.StringProperty()
    time = db.DateProperty()

#Sign a user
def mark_usr(usr,ctime):
    umark = SignDoneMark(
        user = usr.decode("utf-8"),
        time = ctime
    )
    umark.put()

def sign_usr(usr,psw):
    ctime = datetime.datetime.now(pytz.timezone("Asia/Chongqing")).date()
    qu = db.Query(SignDoneMark,keys_only = True)
    qu.filter("user =",usr.decode("utf-8")).filter("time =",ctime)

    # Has done,so return
    if qu.get(): return

    # sign the user
    try:
        # login and get favo_list
        tb = tieba.Tieba(usr,psw)
        tb.login()
        favo = tb.get_favolist()
    except err.EXC_rpbtman,e:
        print e.FormatStr()
        return

    usr_sign_flg = True
    for t in favo:
        qu = db.Query(SignResult)
        qu.filter("user =",usr.decode("utf-8"))
        qu.filter("time =",ctime)
        qu.filter("tkwd =",t.decode("utf-8"))
        qu.order("-rtim")

        p = qu.fetch(None)
        if p:
            p = p[0]
            if p.erro in [0,1101,1007]:  # success,has_signed,sign_too_much
                continue

        errno = 0
        try:
            tb.sign(t)
        except err.EXC_rpbtman,e:
            errno = e.eid

        if errno == 1007: # sign_too_much
            mark_usr(usr,ctime)
            return
        elif not (errno in [0,1101]):
            usr_sign_flg = False # sign failed

        # store the result
        sret = SignResult(
            user = usr.decode("utf-8"),
            tkwd = t.decode("utf-8"),
            erro = errno,
            time = ctime,
            rtim = datetime.datetime.now(pytz.timezone("Asia/Chongqing"))
        )
        sret.put()

    if usr_sign_flg: #usr sign done
        mark_usr(usr,ctime)

# Main function
def main():
    for usr,psw in TASK_LIST:
        sign_usr(usr,psw)
        time.sleep(2)

# Entry
if __name__ == "__main__":
    main()
