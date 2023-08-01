     # 1
countries = {'Россия', 'Китай', 'Казахстан', 'Белорусь'}

def add_country(country):
    countries.add(country)
def remove_country(country):
    countries.discard(country)
def find_country(characters):
    matches = [country for country in countries if characters in country]
    return matches
def is_country_in_set(country):
    return country in countries

while True:
    print(' 1 - Добавить страну; \n 2 - Удалить страну; \n 3 - Поиск страны по введенны символам; \n 4 - Проверка существует ли страна внутри множества; \n 0 - Выход. ')
    command = input('Что необоходимо сделать: ')
    if command == '0':
        break
    elif command == '1':
        country = input('Введите страну для добавления: ')
        add_country(country)
    elif command == '2':
        country = input('Введите страну для удаления: ')
        remove_country(country)
    elif command == '3':
        characters = input('Введите страну для поиска: ')
        found_countries = find_country(characters)
        print('Наличие страны: ', found_countries)
    elif command == '4':
        country = input('Введите страну для проверки существует ли она в списке: ')
        is_in_list = is_country_in_set(country)
        if is_in_list:
            print('Да, страна в списке.')
        else:
            print('Страны нет в списке.')
    else:
        print('Введите команду от 0 до 4..')
    print('Так список стран выглядит сейчас: ', countries)

    # Два множества городов
city1 = {'Пермь', 'Москва', 'Самара', 'Владивосток', 'Челябинск'}
city2 = {'Брест', 'Тюмень', 'Москва', 'Белогорск', 'Пермь'}

    # 2
city3 = city1.intersection(city2)
print('Города, которые есть в обоих множествах:', city3)

    # 3
city4 = city1.difference(city2)
print('Города, которые есть в первом множестве, но нет во втором:', city4)

    # 4
city5 = city2.difference(city1)
print('Города, которые есть во втором множестве, но нет в первом:', city5)

    # 5
city6 = city1.symmetric_difference(city2)
print('Уникальные города: ', city6)

    # 6
countries = {"Россия": "Москва", "США": "Вашингтон"}

while True:
    print(' 1 - Добавить страну; \n 2 - Удалить; \n 3 - Найти; \n 4 - Заменить; \n 0 - Выйти')
    choise = input("Что необходимо сделать: ")
    if choise == '0':
        break
    elif choise == '1':
        one = input("Какую страну добавить: ")
        one1 = input("Введите столицу: ")
        countries[one] = one1
    elif choise == '2':
        two = input("Какую страну удалить: ")
        countries.pop(two)
    elif choise == '3':
        three = countries[input('Какую страну найти: ')]
    elif choise == '4':
        four = input("Какую страну заменить: ")
        countries.pop(four)
        one = input("Какую страну добавить: ")
        one1 = input("Введите столицу: ")
        countries[one] = one1
    else:
        print('Введите значение от 1 до 4. 0 для выхода.')
    print('Актуальный список стран', countries)