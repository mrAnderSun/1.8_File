# Description:
# Проверяем на пустые строки, проверяем на числа (помещаем в count_ingredients), проверяем на символ "|", если
# да, то выполняем функцию cook_book_form(), где создаем список ингредиентов, если нет, то это название блюда
# (помещаем в name_dishes). Создаем словарь cook_book из name_dishes : результат(cook_book_form).
# Запускаем функцию order, где пользователь сам выбирает блюда и количество персон. Эти данные передаем в
# функцию get_shop_list_by_dishes(). И финальный вывод.

from pprint import pprint


def order():
    dishes = []
    # ВВод пользовательских данных (количество людей и выбор блюд)
    person_count = int(input("\nHow many persons wants to eat (number)? "))
    person_dishes = list(cook_book.keys())
    print(f'Menu: \n')
    while True:
        operation = input(
              f"{person_dishes[0]} - press [O]melet \n"
              f"{person_dishes[1]} - press [D]uck \n"
              f"{person_dishes[2]} - press [P]otatoes \n"
              f"{person_dishes[3]} - press [F]ahitos \n"
              f"EXIT  -  press [Q] \n")
        if operation.title() == 'O':
                dishes.append(person_dishes[0])
                print(f'Your order: {dishes} \n')
        elif operation.title() == 'D':
                dishes.append(person_dishes[1])
                print(f'Your order: {dishes} \n')
        elif operation.title() == 'P':
                dishes.append(person_dishes[2])
                print(f'Your order: {dishes} \n')
        elif operation.title() == 'F':
                dishes.append(person_dishes[3])
                print(f'Your order: {dishes} \n')
        elif operation.title() == 'Q':
            break
        else:
                print("Wrong command. Try again! \n")
    #  запуск функции с введенными данными пользователя
    get_shop_list_by_dishes(dishes, person_count)


def get_shop_list_by_dishes(dishes, person_count):
    cook_book2 = {}
    ingredients = {}
    shop_list_by_dishes = {}
    name = []
    #  создание словаря с выбранными блюдами
    for dish in dishes:
        for k, v in cook_book.items():
            if dish == k:
                cook_book2.update([(k,v)])
                dishes_count = dishes.count(k)
                #print(dishes_count)
        #  операция с количеством ингредиентов
        for values in cook_book2.values():
            for value in values:
                for k, v in value.items():
                    if k == 'ingredient_name':
                        #name = v
                        name.append(v)
                        name_count = name.count(v)
                        print(name_count, v)
                        continue
                    if k == 'quantity':
                        print(name_count)
                        v = int(v) * person_count*name_count
                        ingredients[k] = v
                        continue
                    if k == 'measure':
                        ingredients[k] = v
                    cook_book3 = ingredients
                    ingredients = {}
                    shop_list_by_dishes.update([(name[-1], cook_book3)])
    pprint(shop_list_by_dishes)


def cook_book_form():
    cook = {}
    # создание словаря из входных данных (ингредиентов)
    ingred = line.rstrip()
    ingred = ingred.replace("|", "").rstrip().split()
    # разбиение на слова (split), формирование вывода
    if len(ingred) == 4:
        abc = ingred[0] + ' ' + ingred[1]
        ingred = [abc, ingred[2], ingred[3]]
    cook['ingredient_name'] = ingred[0]
    cook['quantity'] = ingred[1]
    cook['measure'] = ingred[2]
    list_cook.append(cook)
    return list_cook


#  Main
with open('recipes.txt', encoding='utf-8') as f:
    cook_book = {}
    list_cook = []
    for line in f:
        # проверка на пустые строки. Почему код не работает при len(line) == 0, хотя длина пустой строки = 0 ?
        if len(line) <= 1:
            pass
        # проверка на число в строке. Почему код не работает при len(line) == 1, хотя длина одного числа = 1 ?
        elif len(line) <= 2:
            count_ingredients = line.rstrip()
            count_ingredients = int(count_ingredients)
        else:
            #  проверка на разделитель "|", если нет, то
            if "|" not in line:
                # наименование блюда
                name_dishes1 = line.rstrip()
                #ввел name_dishes3
                name_dishes3 = name_dishes1
            #  если да, то запуск функции для работы с ингредиентами
            else:
                cook_book_form()
                cook_book[name_dishes3] = list_cook
                if len(cook_book[name_dishes3]) == count_ingredients:
                    name_dishes3 = name_dishes1
                    list_cook = []

    #  формируем заказ
    order()