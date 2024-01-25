
import re
# варіант № 1
def normalize_phone_numbers(numbers):
    pattern = r"[^0-9\+[1]]" ## можна зробити [a-z\s\();\\,\-:!\.] 
    replacement = ""
    #видаляємо все лишнє
    modified_numbers = [re.sub(pattern, replacement, number) for number in numbers]
    # додаємо + або +38
    updated_numbers = [number if number.startswith("+") else "+38" + number[1:] for number in modified_numbers]
    return updated_numbers

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

normal_numbers = normalize_phone_numbers(raw_numbers)
print("Нормалізовані номери телефонів для SMS-розсилки:", normal_numbers)

# варіант № 2

import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "++++380 44 123 4567",
    "38050+++1234567",
    "    ++38(050)123-32-34",
    "     0503451234",
    "(050)88+89900",
    "38050-111-22-22",
    "38050 111 22 11   ",]

def normalize_phone(phone_number):
    p1=r"[\d]+" # забрав +
    phone_number=''.join(re.findall(p1,phone_number))
    if len(phone_number)==10:
        phone_number='+38'+phone_number
    elif len(phone_number)<=12: # зробив <= для того якщо ввели декілька + функція спрацювувала коректно
        phone_number='+'+phone_number
    # else:
    return phone_number



sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)



