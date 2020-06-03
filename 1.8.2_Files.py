# Description:
# Две функции. Одна (forma()) считывает файл и преобразует данные в cook_book.
# Вторая функция get_shop_list_by_dishes выводит финальный результат.
# dishes задан вручную. person_count вводится в консоли.
# Возникает ошибка при запуске (вывел в исключения). ValueError
# if isinstance(int(line_count), int) - ругается на это. Полагаю, что в строке присутствует пробел
# или форматирование какой-то, но strip мне не помог.
# Тем не менее, код выполняется даже без try-except.

import traceback


def forma():
    with open('recipes.txt', encoding='utf8') as f:
        while True:
            cook_notes = []
            key = f.readline().rstrip()
            #  line_count1 = f.readline().rstrip().split()
            #  line_count = int(line_count1[0])
            line_count = f.readline().rstrip()
            if isinstance(int(line_count), int):
                line_count = int(line_count)
            x = 0
            while x < line_count:
                cook = {}
                ingred = f.readline().rstrip()
                ingred = ingred.replace("|", "").rstrip().split()
            # разбиение на слова (split), формирование вывода
                if len(ingred) == 4:
                    abc = ingred[0] + ' ' + ingred[1]
                    ingred = [abc, ingred[2], ingred[3]]
                cook['ingredient_name'] = ingred[0]
                cook['quantity'] = ingred[1]
                cook['measure'] = ingred[2]
                cook_notes.append(cook)
                x = x + 1
            cook_book[key] = cook_notes
            f.readline().rstrip()
        return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    ingredient_for_order = {}
    ingredients = {}
    for keys, values in cook_book.items():
        if keys in dishes:
            for value in values:
                for k, v in value.items():
                    if k == 'ingredient_name':
                        name = v
                    if k == 'measure':
                        ingredients[k] = v
                for k, v in value.items():
                    if k == 'quantity':
                        v = int(v) * person_count
                        ingredients[k] = v
                ingredient_for_order.update([(name, ingredients)])
    print(ingredient_for_order)


# Main
cook_book = {}
try:
    forma()
except Exception as err:
    print('Возникла Ошибка:\n', traceback.format_exc())
dishes = ['Запеченный картофель', 'Омлет']
person_count = int(input("Input persons count: "))
print(dishes)
get_shop_list_by_dishes(dishes, person_count, cook_book)