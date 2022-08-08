from encodings import utf_8
from imp import init_builtin
from turtle import width
from pprint import pprint

cook_book = {}

with open('recipes.txt', encoding='utf-8') as f:
    for line in f:
        amount_ingredients = int(f.readline().strip())
        ingredients = []
        count = 0
        for ingredient in f:
            count += 1
            if count <= amount_ingredients:
                ingredient = ingredient.split(" | ")
                ingredient_dict = {}
                ingredient_dict['ingredient_name'] = ingredient[0].strip()
                ingredient_dict['quantity'] = ingredient[1].strip()
                ingredient_dict['measure'] = ingredient[2].strip()
                ingredients.append(ingredient_dict)
            else:
                break
        cook_book[line.strip()] = ingredients
pprint(cook_book,width=200)
print()

def get_shop_list_by_dishes(dishes, person_count):
    ingredients_in_query = {}
    for dishe in dishes:
        if dishe in cook_book:
            comp_of_dishe = cook_book[dishe]
            for dishes_ing in comp_of_dishe:
                ingredient_name = dishes_ing['ingredient_name']
                if ingredient_name in ingredients_in_query:
                    quantity_of_ingredients = ingredients_in_query[ingredient_name]
                    sum_ingredients = int(quantity_of_ingredients['quantity']) + person_count * int(dishes_ing['quantity'])
                    ingredients_in_query[ingredient_name]['quantity'] = sum_ingredients
                else:    
                    dict_ing = {'measure': dishes_ing['measure'] , 'quantity': person_count * int(dishes_ing['quantity'])}
                    ingredients_in_query[ingredient_name] = dict_ing
        else:
            print(f'Блюдо "{dishe}" отсутствует в книге рецептов')
    pprint(ingredients_in_query)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)