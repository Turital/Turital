import random

first  = ['A', 'B', 'C', 'D', 'E']
second = ['1', '2', '3', '4', '5']
third  = ['a', 'b', 'c', 'd', 'e']

zods = ['Овен', 'Весы', 'Близнецы', 'Рыбы', 'Стрелец', 'Скорпион', 'Телец', 'Рак', 'Лев', 'Дева', 'Козерог', 'Водолей']

def get_prediction():
    return f'{random.choice(first)} {random.choice(second)} {random.choice(third)}'