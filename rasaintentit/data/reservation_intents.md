onko tässä huoneessa varauksia
onko huone vapaana
http://avoindata.tamk.fi/en/rajapinnat/varaukset/#building


##intent:reservations
- Is [Demolatila](room) reserved
- Is [Demolatila](room) booked
- Is [Firmatila F](room) free
- Is [Firmatila F](room) free today
- Is [Firmatila F](room) free tomorrow
- Is [Firmatila F](room) free on [Monday](weekday)
- Is [Firmatila D](room) free at [13.37](time)
- Is [Firmatila F](room) available at [13.37](time)
- Is [Demolatila](room) free on [31.10.2018](date)
- Is [Demolatila](room) available on [31.10.2018](date)
- Are there any rooms available today
- Are there any rooms available on [Monday](weekday)
- Are there any rooms available at [13.37](time)
- Are there any free rooms today
- Are there any free rooms on [Monday](weekday)
- Are there any free rooms at [13.37](time)

##intent:computerReservations
- 

##regex: date
- ^\s*(3[01]|[12][0-9]|0?[1-9])\.(1[012]|0?[1-9])\.((?:19|20)\d{2})\s*$
- ^\s*(3[01]|[12][0-9]|0?[1-9])\.(1[012]|0?[1-9])$
- ^\s*(3[01]|[12][0-9]|0?[1-9])$

##regex time
- ^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$