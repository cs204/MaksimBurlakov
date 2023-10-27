def main():
    capacity = get_capacity()
    if capacity <= 1:
        print("E")
    elif capacity >= 99:
        print("F")
    else:
        print(str(capacity) +"%")

def get_capacity():
    while True:
        try:
            fuel = input("Дробь: ")
            x, y = fuel.split("/")
            if int(x) > int(y):
                continue
            else:
                capacity = round(int(x) / int(y) * 100)
        except ZeroDivisionError:
                print("Can not divide by zero")
        except ValueError:
                print("Please enter a fraction")
        else:
            break
    return capacity
main()