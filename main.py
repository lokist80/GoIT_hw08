from datetime import datetime, timedelta
import collections

NOW = datetime.now()
start_data = datetime(year=NOW.year, month=NOW.month, day=NOW.day, hour=0)
calend = {(start_data + timedelta(days=i)).strftime('%A'): [] for i in range(7) if i not in (4, 5)}
Users = collections.namedtuple('Users', ['name', 'birthday'])
users = [
    {'name': 'Joye', 'birthday': datetime(year=1991, month=3, day=18)},
    {'name': 'Rudolph', 'birthday': datetime(year=1981, month=3, day=21)},
    {'name': 'Bill', 'birthday': datetime(year=1982, month=12, day=23)},
    {'name': 'Rosco', 'birthday': datetime(year=1988, month=11, day=13)},
    {'name': 'Jill', 'birthday': datetime(year=1980, month=3, day=4)},
    {'name': 'Kim', 'birthday': datetime(year=1995, month=3, day=14)},
    {'name': 'Jan', 'birthday': datetime(year=2005, month=3, day=15)},
    {'name': 'Rachel', 'birthday': datetime(year=2015, month=3, day=15)},
    {'name': 'John', 'birthday': datetime(year=1980, month=3, day=16)},
    {'name': 'Ramirez', 'birthday': datetime(year=1991, month=3, day=20)},
    {'name': 'Monica', 'birthday': datetime(year=1993, month=3, day=18)},
    {'name': 'Chandler', 'birthday': datetime(year=1991, month=3, day=19)},
    {'name': 'Till', 'birthday': datetime(year=1991, month=3, day=22)},
    {'name': 'Kaleb', 'birthday': datetime(year=1985, month=4, day=1)},

]


def get_birthdays_per_week(users):
    users_nt = [Users(**i) for i in users]
    for i in range(len(users_nt)):
        check_data = datetime(year=NOW.year, month=users_nt[i][1].month, day=users_nt[i][1].day)
        end_data = start_data + timedelta(weeks=1)
        if start_data <= check_data <= end_data:
            if check_data.weekday() == 5:
                check_data += timedelta(days=2)
                calend[check_data.strftime('%A')].append(users_nt[i][0])
                continue
            if check_data.weekday() == 6:
                check_data += timedelta(days=1)
                calend[check_data.strftime('%A')].append(users_nt[i][0])
                continue
            else:
                calend[check_data.strftime('%A')].append(users_nt[i][0])

    for k, v in calend.items():
        if v:
            print(f'{k}: {", ".join(v)}')


if __name__ == '__main__':
    get_birthdays_per_week(users)
