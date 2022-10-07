cook_book = {}

with open('Ingridients.txt', encoding='utf-8') as file:
    for food in file:
        food_c = food.strip()
        cook_book[food_c] = []
        ingridient_count = int(file.readline())
        for i in range(ingridient_count):
            ing = file.readline()
            name, quantity, measure = ing.strip().split(' | ')
            cook_book[food_c].append({'ingredient_name': name,
                                      'quantity': quantity,
                                      'measure': measure})
        file.readline()


def get_shop_list_by_dishes(dishes, person_count):
    dish_dict = {}
    for dish in dishes:
        for ing in cook_book[dish]:
            list_values = list(ing.values())
            list_keys = list(ing.keys())
            if list_values[0] in dish_dict.keys():
                dish_dict[list_values[0]][list_keys[1]] = dish_dict[list_values[0]][list_keys[1]]\
                                                          + int(list_values[1]) * person_count
            else:
                dish_dict[list_values[0]] = {list_keys[2]: list_values[2],\
                                             list_keys[1]: int(list_values[1]) * person_count}
    print(dish_dict)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
