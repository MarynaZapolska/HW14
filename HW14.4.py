""" Створіть клас, який описує автомобіль. Створіть клас автосалону, що містить в собі список автомобілів,
доступних для продажу, і функцію продажу заданого автомобіля."""

class Car:
    my_count = 0
    def __init__(self, marka, model, year, transmission, code, status):
        self.marka = marka
        self.model = model
        self.year = year
        self.transmission = transmission
        self.code = code
        self.status = status

        Car.my_count += 1
        print( f"Марка: {self.marka}, Модель:  {self.model}, рік випуску:  {self.year}, трансмісія:  {self.transmission}, код: {self.code}, {self.status}")

    def __repr__(self):
        return f"Марка: {self.marka}, Модель:  {self.model}, рік випуску:  {self.year}, трансмісія:  {self.transmission}, код: {self.code}, {self.status}"
class Avtosalon:
    all_cars= list()
    def __init__(self,cars):
        self.all_cars = cars

    def getCarByCode(self, code):
        self.code = code
        for car in self.all_cars:
            if int(self.code) == car.code:
              return car

    def setStatusCar(self, car):
        self.car = car
        if self.car:
            print("Продано: ", self.car)
            self.all_cars.remove(self.car)
            for car in self.all_cars:
                print(car)
        else:
            print("Невірно заданий код ")
cars_list = []
cars_list.append(Car("Volkswagen", "Golf", 2017, "автоматична", 1234, "в доступі"))
cars_list.append(Car("Volkswagen", "Passat", 2012, "автоматична", 1525, "в доступі"))
cars_list.append(Car("Volkswagen", "T-Roc", 2022, "автоматична", 1423, "в доступі"))

code = input("Для купівлі введіть код автомобіля: ")
autoS = Avtosalon(cars_list)
selected_car = autoS.getCarByCode(code)
autoS.setStatusCar(selected_car)