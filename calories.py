fruit = input("Фрукт: ")
dict = {
    "Apple": "Калории: 130",
    "Avocado": "Калории: 50",
    "Banana": "Калории: 110",
    "Grapefuit": "Калории: 60",
    "Grapes": "Калории: 90",
    "Lime": "Калории: 20",
    "Orange": "Калории: 80"
}
if fruit in dict:
    print(dict.get(fruit))
else:
    print (" ")