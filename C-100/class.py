class Car(object):
    def __init__(self, model, color, company, speed_limit):
        self.color=color
        self.model=model
        self.company=company
        self.speed_limit=speed_limit
    
    def start(self):
        print("started")
    
    def stop(self):
        print("stoped")

    def accelarate(self):
        print("accelarating....")

    def change_gear(self, gear_type):
        print("gear changed")


audi=Car("A6", "blue", "audi", 80)
print(audi.model)
print(audi.color)
print(audi.start())
print(audi.stop())
print(audi.accelarate())
print(audi.change_gear())