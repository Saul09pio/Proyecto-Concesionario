from Piezas import *
from time import *

class Carro:
    components_car = {'motor': "MotorX", 
                      'cajacamb': "CajaCambA",
                      'ruedas': "RuedasA",
                      'chasis': "ChasisA",
                      'carroceria': "CrrA"}
    temp_inventory = []
    def __init__(self, name_car, color, fuel):
        self.name_car = name_car
        self.color = color
        self.fuel = fuel
        
#Metodo para arrancar el carro    
    def start(components):
        pass

    def run():
        pass
#Metodo para agegar piezas(Roger cuando hagas lo de las pieza me avisas para empezar a trabajar en lo ue falta)
    def set_component():
                
        
        while True:
            menu = (input("Seleccione la pieza a cambiar (M,CC,R,Ch,Crr): "))
            
            if menu.upper() == "MA":
                print("Cambiando pieza vieja...")
                Carro.temp_inventory.insert(0, Carro.components_car.values())
#Roger aqui puse un loop para que vieras la lista del inventario temp, si quieres la quitas
                for piece in Carro.temp_inventory:
                    print(piece)
                print(Carro.temp_inventory)
            elif menu.upper() == "MB":
                print("Cambiando pieza vieja...")
                Carro.temp_inventory.insert()
            elif menu.upper() == "MC":
                print("Cambiando pieza vieja...")
                Carro.temp_inventory.insert()
            elif menu.upper() == "RA":
                print("Cambiando pieza vieja...")
                Carro.temp_inventory.insert()
            elif menu.upper() == "RB":
                print("Cambiando pieza vieja...")
                Carro.temp_inventory.insert()
            elif menu.upper() == "RC":
                print("Cambiando pieza vieja...")
                Carro.temp_inventory.insert()
            elif menu.upper() == "CAJACAMBA":
                print("Cambiando pieza vieja...")
                Carro.temp_inventory.insert()    
            elif menu.upper() == "CAJACAMBB":
                print("Cambiando pieza vieja...")
                Carro.temp_inventory.insert()
            elif menu.upper() == "CAJACAMBC":
                print("Cambiando pieza vieja...")
                Carro.temp_inventory.insert()
            elif menu.upper() == "CHA":
                print("Cambiando pieza vieja...")
                Carro.temp_inventory.insert()
            elif menu.upper() == "CHB":
                print("Cambiando pieza vieja...")
                Carro.temp_inventory.insert()
            elif menu.upper() == "CHC":
                print("Cambiando pieza vieja...")
                Carro.temp_inventory.insert() 
            elif menu.upper() == "CRRA":
                print("Cambiando pieza vieja...")
                Carro.temp_inventory.insert()
            elif menu.upper() == "CRRB":
                print("Cambiando pieza vieja...")
                Carro.temp_inventory.insert()
            elif menu.upper() == "CRRC":
                print("Cambiando pieza vieja...")
                Carro.temp_inventory.insert()
            elif menu.upper() == menu.isdigit():
                break
            else:
                break
print(Carro.set_component())              


