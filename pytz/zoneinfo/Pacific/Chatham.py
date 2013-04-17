'''tzinfo timezone information for Pacific/Chatham.'''
from pytz.tzinfo import DstTzInfo
from pytz.tzinfo import memorized_datetime as d
from pytz.tzinfo import memorized_ttinfo as i

class Chatham(DstTzInfo):
    '''Pacific/Chatham timezone definition. See datetime.tzinfo for details'''

    zone = 'Pacific/Chatham'

    _utc_transition_times = [
d(1,1,1,0,0,0),
d(1956,12,31,11,46,12),
d(1974,11,2,14,0,0),
d(1975,2,22,14,0,0),
d(1975,10,25,14,0,0),
d(1976,3,6,14,0,0),
d(1976,10,30,14,0,0),
d(1977,3,5,14,0,0),
d(1977,10,29,14,0,0),
d(1978,3,4,14,0,0),
d(1978,10,28,14,0,0),
d(1979,3,3,14,0,0),
d(1979,10,27,14,0,0),
d(1980,3,1,14,0,0),
d(1980,10,25,14,0,0),
d(1981,2,28,14,0,0),
d(1981,10,24,14,0,0),
d(1982,3,6,14,0,0),
d(1982,10,30,14,0,0),
d(1983,3,5,14,0,0),
d(1983,10,29,14,0,0),
d(1984,3,3,14,0,0),
d(1984,10,27,14,0,0),
d(1985,3,2,14,0,0),
d(1985,10,26,14,0,0),
d(1986,3,1,14,0,0),
d(1986,10,25,14,0,0),
d(1987,2,28,14,0,0),
d(1987,10,24,14,0,0),
d(1988,3,5,14,0,0),
d(1988,10,29,14,0,0),
d(1989,3,4,14,0,0),
d(1989,10,7,14,0,0),
d(1990,3,17,14,0,0),
d(1990,10,6,14,0,0),
d(1991,3,16,14,0,0),
d(1991,10,5,14,0,0),
d(1992,3,14,14,0,0),
d(1992,10,3,14,0,0),
d(1993,3,20,14,0,0),
d(1993,10,2,14,0,0),
d(1994,3,19,14,0,0),
d(1994,10,1,14,0,0),
d(1995,3,18,14,0,0),
d(1995,9,30,14,0,0),
d(1996,3,16,14,0,0),
d(1996,10,5,14,0,0),
d(1997,3,15,14,0,0),
d(1997,10,4,14,0,0),
d(1998,3,14,14,0,0),
d(1998,10,3,14,0,0),
d(1999,3,20,14,0,0),
d(1999,10,2,14,0,0),
d(2000,3,18,14,0,0),
d(2000,9,30,14,0,0),
d(2001,3,17,14,0,0),
d(2001,10,6,14,0,0),
d(2002,3,16,14,0,0),
d(2002,10,5,14,0,0),
d(2003,3,15,14,0,0),
d(2003,10,4,14,0,0),
d(2004,3,20,14,0,0),
d(2004,10,2,14,0,0),
d(2005,3,19,14,0,0),
d(2005,10,1,14,0,0),
d(2006,3,18,14,0,0),
d(2006,9,30,14,0,0),
d(2007,3,17,14,0,0),
d(2007,10,6,14,0,0),
d(2008,3,15,14,0,0),
d(2008,10,4,14,0,0),
d(2009,3,14,14,0,0),
d(2009,10,3,14,0,0),
d(2010,3,20,14,0,0),
d(2010,10,2,14,0,0),
d(2011,3,19,14,0,0),
d(2011,10,1,14,0,0),
d(2012,3,17,14,0,0),
d(2012,10,6,14,0,0),
d(2013,3,16,14,0,0),
d(2013,10,5,14,0,0),
d(2014,3,15,14,0,0),
d(2014,10,4,14,0,0),
d(2015,3,14,14,0,0),
d(2015,10,3,14,0,0),
d(2016,3,19,14,0,0),
d(2016,10,1,14,0,0),
d(2017,3,18,14,0,0),
d(2017,9,30,14,0,0),
d(2018,3,17,14,0,0),
d(2018,10,6,14,0,0),
d(2019,3,16,14,0,0),
d(2019,10,5,14,0,0),
d(2020,3,14,14,0,0),
d(2020,10,3,14,0,0),
d(2021,3,20,14,0,0),
d(2021,10,2,14,0,0),
d(2022,3,19,14,0,0),
d(2022,10,1,14,0,0),
d(2023,3,18,14,0,0),
d(2023,9,30,14,0,0),
d(2024,3,16,14,0,0),
d(2024,10,5,14,0,0),
d(2025,3,15,14,0,0),
d(2025,10,4,14,0,0),
d(2026,3,14,14,0,0),
d(2026,10,3,14,0,0),
d(2027,3,20,14,0,0),
d(2027,10,2,14,0,0),
d(2028,3,18,14,0,0),
d(2028,9,30,14,0,0),
d(2029,3,17,14,0,0),
d(2029,10,6,14,0,0),
d(2030,3,16,14,0,0),
d(2030,10,5,14,0,0),
d(2031,3,15,14,0,0),
d(2031,10,4,14,0,0),
d(2032,3,20,14,0,0),
d(2032,10,2,14,0,0),
d(2033,3,19,14,0,0),
d(2033,10,1,14,0,0),
d(2034,3,18,14,0,0),
d(2034,9,30,14,0,0),
d(2035,3,17,14,0,0),
d(2035,10,6,14,0,0),
d(2036,3,15,14,0,0),
d(2036,10,4,14,0,0),
d(2037,3,14,14,0,0),
d(2037,10,3,14,0,0),
        ]

    _transition_info = [
i(44040,0,'LMT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
i(45900,0,'CHAST'),
i(49500,3600,'CHADT'),
        ]

Chatham = Chatham()

