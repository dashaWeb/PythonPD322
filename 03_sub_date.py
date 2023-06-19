

day_start = 10
month_start = 3
year_start = 2023

day_end = 20
month_end = 5
year_end = 2023

daysAllStart = 0

month_start-=1

# 31 28 10 => 69

month = month_start
if month_start == 11:
    daysAllStart+=30
    month_start-=1
if month_start == 10:
    daysAllStart+=31
    month_start-=1
if month_start == 9:
    daysAllStart+=30
    month_start-=1
if month_start == 8:
    daysAllStart+=31
    month_start-=1
if month_start == 7:
    daysAllStart+=31
    month_start-=1
if month_start == 6:
    daysAllStart+=30
    month_start-=1
if month_start == 5:
    daysAllStart+=31
    month_start-=1
if month_start == 4:
    daysAllStart+=30
    month_start-=1
if month_start == 3:
    daysAllStart+=31
    month_start-=1
if month_start == 2:
    if year_start % 4 == 0 or year_start% 400== 0 and year_start % 100 != 0:
        daysAllStart+=29
    else:
        daysAllStart+=28
    month_start-=1
if month_start == 1:
    daysAllStart+=31
    month_start-=1

daysAllStart+= day_start
print(daysAllStart)

month_start = month
month = month_end
daysAllEnd = 0
if month_end == 11:
    daysAllEnd+=30
    month_end-=1
if month_end == 10:
    daysAllEnd+=31
    month_end-=1
if month_end == 9:
    daysAllEnd+=30
    month_end-=1
if month_end == 8:
    daysAllEnd+=31
    month_end-=1
if month_end == 7:
    daysAllEnd+=31
    month_end-=1
if month_end == 6:
    daysAllEnd+=30
    month_end-=1
if month_end == 5:
    daysAllEnd+=31
    month_end-=1
if month_end == 4:
    daysAllEnd+=30
    month_end-=1
if month_end == 3:
    daysAllEnd+=31
    month_end-=1
if month_end == 2:
    if year_end % 4 == 0 or year_end% 400== 0 and year_end % 100 != 0:
        daysAllEnd+=29
    else:
        daysAllEnd+=28
    month_end-=1
if month_end == 1:
    daysAllEnd+=31
    month_end-=1

daysAllEnd+= day_end
print(daysAllEnd)
print(daysAllEnd - daysAllStart)
