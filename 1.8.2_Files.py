# Description:
# Функция main() - Ввод данных и запуск forma().
# Функция forma() - преобразование содержимого текстового файла в словарь.
# Функция get_shop_list_by_dishes() - создание словаря на основе введенных данных и результатов forma().


from pprint import pprint
import traceback


def main_def():
    cook_book = {}
    try:
        forma(cook_book)
    except Exception as err:
        print('Возникла Ошибка:\n', traceback.format_exc())
    dishes = ['Омлет', 'Омлет', 'Омлет']
    person_count = 2  #int(input("Input persons count: "))
    print(dishes)
    get_shop_list_by_dishes(dishes, person_count, cook_book)


def forma(cook_book):
    with open('recipes.txt', encoding='utf8') as f:
        while True:
            cook_notes = []
            key = f.readline().rstrip()
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
    ingredient_name = []
    for keys, values in cook_book.items():
        if keys in dishes:
            keys_count = dishes.count(keys)
            for value in values:
                for k, v in value.items():
                    if k == 'ingredient_name':
                        ingredient_name.append(v)
                        ingredient_count = ingredient_name.count(v)
                        continue
                    if k == 'quantity':
                        v = int(v) * person_count*keys_count*ingredient_count
                        ingredient_dict[k] = v
                        continue
                    if k == 'measure':
                        ingredient_dict[k] = v
                    quantity_and_measure_dict = ingredient_dict.copy()
                    del ingredient_dict
                    ingredient_dict = {}
                    shop_list_by_dishes[ingredient_name[-1]] = quantity_and_measure_dict
    pprint(shop_list_by_dishes)


# Main
main_def()
