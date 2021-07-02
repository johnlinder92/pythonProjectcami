from Carros import Carros
from Comida import Comida

cars = []
foods = []
basket = []


def administergoods(choice):

    if choice == "1":
        car = Carros(input("Choose a price of this car:"),input("Choose a color of this car:"))
        cars.append(car)
    elif choice == "2":
        food = Comida(input("Choose a price of this food:"), input("Choose a description of this food:"))
        foods.append(food)
    elif choice == "3":
        for car in cars:
            print(car.precio, car.color)
        for food in foods:
            print(food.precio, food.description)


def store():
    print("store")
def viewGoods():
    print("viewgoods")

def selection(choice):
   if choice == "1":
       administergoods(input("Choose 1 to create a car, 2 to create food, 3 to print: "))
   elif choice == "2":
       store()
   elif choice == "3":
       viewGoods()
   elif choice == "4":
       f = open("store.txt", "w")
       f.write(cars)
       f.close()
   else:
       print("wrong input, try again!")

def myfunc(n):
    return lambda a: a * n



def online_count(statuses):
    p = 0
    list = statuses.values()
    for x in list:
        if x == 'online':
            p += 1
    return p


def remove_dots(string):
    string2 = ""
    slist = list(string)
    count = 0
    for y in slist:
        if (y == "."):
            del(slist[count])
        count += 1

    for ele in slist:
        string2 += ele

    return string2

def capital_indexes(inputstring):
    list= []
    x = -1
    for i in inputstring:
        x += 1
        if inputstring[x].isupper():
            list.append(x)
    return list

def mid(inputstring):
    x = 0
    for i in inputstring:

        x += 1
        if float(x) == (((len(inputstring))/2)+0.5):
            mid = inputstring[x-1]
            return mid
    else:
        return ""

def double_letters(string):
 x = 1
 for i in string:
        try:
            if i == string[x]:
                return True
                x += 1
        except:
            return False




 '''exitprogram = False
 while exitprogram == False:
    selection(input("Select 1 to administer available goods, 2 to go to store, 3 to see what goods you purchased:"))'''


def is_anagram(string1, string2):
    uno= list(string1)
    uno.sort()
    dos= list(string2)
    dos.sort()
    if uno == dos:
            return True
    else:
            return False

def largest_difference(list):
    list.sort()
    answer = list[-1]-list[0]
    return answer

if __name__ == '__main__':
    test = [-75, 5, 10, 15]
    print(largest_difference(test))
