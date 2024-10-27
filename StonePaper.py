import random

def game():
    print('Игра камень, ножницы, бумага!')
    while True:
        changes = ['Камень', 'Ножницы', 'Бумага']
        comp_change = random.choice(changes)
        user_change = str(input('Выберите ваше действие: ')).lower()
        
        if user_change == 'камень':
            if comp_change == 'Ножницы':
                print('Вы выиграли!')
                print('Выбор пк:', comp_change)
            elif comp_change == 'Бумага':
                print('Вы проиграли!')
                print('Выбор пк:', comp_change)
            elif comp_change == 'Камень':
                print('Ничья!')
                print('Выбор пк:', comp_change)
        
        elif user_change == 'ножницы':
            if comp_change == 'Ножницы':
                print('Ничья!')
                print('Выбор пк:', comp_change)
            elif comp_change == 'Бумага':
                print('Вы выиграли!')
                print('Выбор пк:', comp_change)
            elif comp_change == 'Камень':
                print('Вы проиграли!')
                print('Выбор пк:', comp_change)
        elif user_change == 'бумага':
            if comp_change == 'Ножницы':
                print('Вы проиграли!')
                print('Выбор пк:', comp_change)
            elif comp_change == 'Камень':
                print('Вы выиграли!')
                print('Выбор пк:', comp_change)
            elif comp_change == 'Бумага':
                print('Ничья!')
                print('Выбор пк:', comp_change)
        elif user_change in ('стоп','хватит'):
            break
        else:
            print('Введите свое действие или команду стоп чтобы выйти.')
game()        




