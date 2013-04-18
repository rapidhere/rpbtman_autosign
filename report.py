# -*- coding: utf-8 -*-

# Copyright (C) 2013 ~ 2014 rapidhere
#
# Author:     rapidhere@gmail.com
# Maintainer: rapidhere@gmail.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from google.appengine.ext import db
from task_list import TASK_LIST
import datetime,pytz,email

class SignResult(db.Model):
    user = db.StringProperty()
    tkwd = db.StringProperty()
    erro = db.IntegerProperty()
    time = db.DateProperty()
    rtim = db.DateTimeProperty()

class SignDoneMark(db.Model):
    user = db.StringProperty()
    time = db.DateProperty()

ctime = datetime.datetime.now(pytz.timezone("Asia/Chongqing")).date()

def clear_data_store():
    qu = db.Query(SignResult)
    qu.filter("time <",ctime)

    db.delete(qu.fetch(None))

    qu = db.Query(SignDoneMark)
    qu.filter("time <",ctime)
    db.delete(qu.fetch(None))

def report():
    msgbuf = "Sign result report\nDate : %s\n" % str(ctime)

    for usr,psw in TASK_LIST:
        qu = db.Query(SignResult)
        qu.filter("time =",ctime).filter("user = ",usr)
        msgbuf += "=" * 80
        msgbuf += "\nUSER %s :\n" % usr

        for ret in qu.fetch(None):
            msgbuf += "    " + ret.tkwd
            msgbuf += "    " + str(ret.rtim)
            msgbuf += "  errno = " + str(ret.erro)
            msgbuf += "\n"

    import email
    from google.appengine.api import mail

    mail.send_mail(
            "Auto sign <rapidhere@gmail.com>",
            "1012278279@qq.com",
            "Auto sign log : %s" % str(ctime),
            msgbuf
        )

def main():
    clear_data_store()
    report()

if __name__ == "__main__":
    main()
