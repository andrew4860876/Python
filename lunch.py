import time
import multiprocessing
import random
import os
import sys


# 1 = Breakfast
# 2 = Lunch
# 3 = Dinner

lunch_items = ['Peanut Butter and Honey Crackers', 'Oatmeal', 'Peanut Butter and Jelly Sandwich', 'Peach Yogurt with Granola', 'Key Lime Yogurt with Granola', 'Peanut Butter and Honey Toast', 'Cereal', 'Bacon, Egg, and Cheese Biscuit', 'Chicken Nuggets', 'Chicken Sandwich', 'Ham and Cheese Sandwich', 'Cinnamon Toast', 'Fruit']
# lunch_items = ['Cliff bar', 'Waffles with Nutella', 'Strawberries with Nutella']

standspace = '=========================================='

def random_lunch_item():
    item = random.choice(lunch_items)
    len_item = len(item)
    len_stand_space = len(standspace)
    added_space = len_stand_space - len_item
    added_space = added_space - 1
    item += ' ' * added_space
    item += '|'
    print(f'Your lunch item is:      {item}')
    print('===================================================================')

if __name__ == '__main__':
    # time.sleep(0.7)
    os.system('clear')
    print('===================================================================')
    p1 = multiprocessing.Process(target=random_lunch_item)
    p2 = multiprocessing.Process(target=random_lunch_item)
    p3 = multiprocessing.Process(target=random_lunch_item)
    p4 = multiprocessing.Process(target=random_lunch_item)
    p5 = multiprocessing.Process(target=random_lunch_item)
    p6 = multiprocessing.Process(target=random_lunch_item)
    p7 = multiprocessing.Process(target=random_lunch_item)
    p8 = multiprocessing.Process(target=random_lunch_item)
    p9 = multiprocessing.Process(target=random_lunch_item)
    p10 = multiprocessing.Process(target=random_lunch_item)
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()
    p10.start()
