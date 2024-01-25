import datetime

def get_days_from_today(date_str):
    current_date = datetime.datetime.now()
    try:
        input_date = datetime.datetime.strptime(date_str, '%d.%m.%Y') #переводимо у формат datetime
        days_difference = (current_date - input_date).days
        return days_difference
    except ValueError:
        print('Введіть у правильному форматі дд.мм.рррр')

days_difference = get_days_from_today("15.1.2022")

if days_difference > 0:
    print(f'Цей день був {days_difference} днів тому')
elif days_difference == 0:
    print('Цей день сьогодні!')
else:
    print(f'Цей день наступить через {days_difference * (-1)} днів')