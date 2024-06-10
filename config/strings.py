from aiogram import html

greetings_name=f"{html.bold('Привет,')}"
greetings_action="Выбери действие из меню"
greetings_new=f"{html.bold('Похоже, что ты новенький у нас')}\n\nПоделись своим номером телефона для продолжения"

unknown=f"{html.bold('Я не знаю, как на это ответить')}"

def create_profile(name, surname, middlename, program, level, course):
    return f"{html.bold(f'{name} {surname} {middlename}')}\n\n" \
    f"{html.bold(f'Уровень образования: ')}{level}\n" \
    f"{html.bold(f'Образовательная программа (ОП): ')}{program}\n" \
    f"{html.bold(f'Номер курса: ')}{course}\n" \
    f"{html.bold(f'Количество кредитов: ')}0" \
    