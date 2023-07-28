from datetime import datetime
from collections import defaultdict


users = [{'name':'Ivan', 'birthday': datetime(year=1991, month=7, day=3)},
        {'name':'Taras', 'birthday': datetime(year=1991, month=8, day=1)},
        {'name':'Petro', 'birthday': datetime(year=1991, month=7, day=30)},
        {'name':'Ivan2', 'birthday': datetime(year=1991, month=9, day=3)},
        {'name':'Ivan3', 'birthday': datetime(year=1991, month=10, day=3)},
        {'name':'Will', 'birthday': datetime(year=1991, month=8, day=1)}
        ]

days_name = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

def is_birthday_next_week (user: dict) -> bool:
    current_date = datetime.now()
    user_bd = user['birthday']
    user_bd = user_bd.replace(year=current_date.year)
    delta_days = user_bd - current_date 
    
    if current_date.weekday() == 0:
        condition = (delta_days.days <= 4) and (delta_days.days >= -2)
    else:
        condition = (delta_days.days <= 6) and (delta_days.days >= 0)

    if condition:
        return True
    return False  


def get_birthdays_per_week(users: list) -> None:
    current_date = datetime.now()
    result_dict = defaultdict(list)

    for user in users:

        if is_birthday_next_week (user):
            user_bd = user['birthday']
            user_bd = user_bd.replace(year=current_date.year)

            if user_bd.weekday() == 5 or user_bd.weekday() == 6:
                day = days_name.get(0)
            else:
                day = days_name.get(user_bd.weekday())
           
            result_dict[day].append(user['name'])

    for key, value in result_dict.items():    
        print (f'{key}:{",".join(value)}')


 
if __name__ == '__main__':

    get_birthdays_per_week(users)


        


