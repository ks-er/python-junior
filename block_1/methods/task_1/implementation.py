from block_1.common import (
    MyException
)

class Coffee:
    #Капучино - эспрессо, подогретое молоко и молочная пена
    #Гляссе - двойной эспрессо, мороженое
    #Латте - молоко и немного молочной пены

    double_espresso = "двойной эспрессо"
    espresso = "эспрессо"
    ice_cream = "мороженое"
    milk = "молоко"
    milk_foam = "молочная пена"    
    composition = []

    def __init__(self, coffee_name):
        self.coffee_name = coffee_name

    def get_cappuccino(self):
        self.composition = []
        return self.composition.extend([self.espresso, self.milk, self.milk_foam])
    
    def get_glasse(self):
        self.composition = []
        return self.composition.extend([self.double_espresso, self.ice_cream])
    
    def get_latte(self):
        self.composition = []
        return self.composition.extend([self.milk, self.milk_foam])

    

def print_coffee_composition(coffee_name):
    coffee = Coffee(coffee_name)
    
    if coffee_name =="Капучино":
        coffee.get_cappuccino()
    elif coffee_name =="Гляссе":
        coffee.get_glasse()
    elif coffee_name =="Латте":
        coffee.get_latte()    
    else:
        raise MyException

    print(coffee.coffee_name + ": " + ', '.join(coffee.composition))

print_coffee_composition("Капучино")
print_coffee_composition("Латте")    
print_coffee_composition("Гляссе")
print_coffee_composition("Раф")
