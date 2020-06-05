# Description:
# Две функции. Одна (forma()) считывает файл и преобразует данные в cook_book.
# Вторая функция get_shop_list_by_dishes выводит финальный результат.
# dishes задан вручную. person_count вводится в консоли.
# Возникает ошибка при запуске (вывел в исключения). ValueError
# if isinstance(int(line_count), int) - ругается на это. Полагаю, что в строке присутствует пробел
# или форматирование какой-то, но strip мне не помог.
# Тем не менее, код выполняется даже без try-except.

from pprint import pprint
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
    shop_list_by_dishes = {}
    ingredient_dict = {}
    for keys, values in cook_book.items():
        if keys in dishes:
            for value in values:
                for k, v in value.items():
                    if k == 'ingredient_name':
                        name = v
                        continue
                    if k == 'quantity':
                        v = int(v) * person_count
                        ingredient_dict[k] = v
                        continue
                    if k == 'measure':
                        ingredient_dict[k] = v
                    quantity_and_measure_dict = ingredient_dict.copy()
                    del ingredient_dict
                    ingredient_dict = {}
                    shop_list_by_dishes[name] = quantity_and_measure_dict
    pprint(shop_list_by_dishes)


# Main
cook_book = {}
try:
    forma()
except Exception as err:
    print('Возникла Ошибка:\n', traceback.format_exc())
dishes = ['Запеченный картофель', 'Омлет']
person_count = 2  #int(input("Input persons count: "))
print(dishes)
get_shop_list_by_dishes(dishes, person_count, cook_book)