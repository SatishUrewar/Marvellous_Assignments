class Vehicle:        
    def start(self):
        print("Vehicle start ")


class car(Vehicle):
    def start(self):
        print("derives class car override")

def main():
    obj1=Vehicle()
    obj1.start()

    obj2=car()
    obj2.start()


if __name__=="__main__":
    main()