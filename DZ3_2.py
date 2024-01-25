import random

def get_numbers_ticket(min, max, quantity):
    numbers = []
# поки довжина списку менша quantity
    while len(numbers) < quantity: 
        # генеруємо від мінімального значення до максимального (включно) чисел, 6 це скільки треба номерів 
        number = random.randint(min, max)
        # перевіряємо чи є номер в списку 
        if number not in numbers: 
            # якщо немає то додаємо до списку
            numbers.append(number)
    return numbers
# запускаємо функцію
ticket_numbers = get_numbers_ticket(1, 49, 6)

print(ticket_numbers)
