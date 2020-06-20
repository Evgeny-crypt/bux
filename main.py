from datetime import datetime as date
from application.salary import calculate_salary
from application.db.people import get_employees


def date_time():
    time = date.today().strftime('%d/%m/%Y')
    print(time)


date_time()

if __name__ == '__main':
    get_employees()
    calculate_salary()
