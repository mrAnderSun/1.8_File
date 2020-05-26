def order(cook_book):
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
	get_shop_list_by_dishes(dishes, person_count, cook_book)


def get_shop_list_by_dishes(dishes, person_count, cook_book):
		cook_book2 = {}
		cook_book3 = {}
		cook_book4 = []
		#  создание словаря с выбранными блюдами
		for dish in dishes:
			for k, v in cook_book.items():
				if dish == k:
				    cook_book2.update([(k,v)])
		#  операция с количеством ингредиентов
		for values in cook_book2.values():
			for value in values:
				#  ниже написанный код (в комментариях) отрабатывает, о чем сообщает первый print,
				#  но в cook_book3 сохраняется лишь последний ингредиент из списка
				#  (на примере Омлета - это Помидор).
				#  Об этом говорит print с **** . Почему?
				#  А если добавить список (cook_book4), то там все ингредиенты.
				for k, v in value.items():
					if k == 'quantity':
						v = int(v)*person_count
					cook_book3.update([(k,v)])
					cook_book4.append([k,v])
					print(cook_book3)
		print(f'{cook_book3} ****')
		print(cook_book4)


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
				#  Почему-то при виде:
				#  cook_book_form()
				#  cook_book[name_dishes1] = list_cook
				#  запись продолжается исключительно в "Омлет":
				#  cook_book = {'Омлет':[{весь список ингредиентов в файле...}]},
				#  хотя name_dishes1 меняется (Омлет, утка, картофель и т.д.)
				#  Поэтому добавил name_dishes3 (выше), проверку на длину словаря и явное переименование.
				if len(cook_book[name_dishes3]) == count_ingredients:
					name_dishes3 = name_dishes1
					list_cook = []

#  формируем заказ
order(cook_book)