#scratch
if __name__ == "__main__":

    mm, dd = map(int, input().split())

    wday = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    month = [31,28,31,30,31,30,31,31,30,31,30,31]
    day = 0

    for i in range(mm-1):
        day += month[i]
    day = day + dd
    print(wday[day % 7])


#calender module
import calendar

wday = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
index = calendar.weekday(2007,mm,dd)
print(wday[index])