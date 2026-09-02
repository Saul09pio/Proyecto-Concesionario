#ESTE ARCHIVO LO PUSE PARA HACER SUS PRUEBAS SIN INTERFERRIR EN EL CODIGO PRINCIPAL
while True:



    ca_piece = {1: 'MotorX',2: 'Ruedasf', 3: "CrrA"}
    menu = (input("Seleccione la pieza a cambiar (M,CC,R,Ch,Crr): ")) 
    salir = print(input("Desea continuar(Y/N): "))
    salir = str(salir)
    Motor = ("MotorA", "MotorB", "MotorC")
    Caja_Camb = ( 'CajCambA', "CajCambB", "CajaCambC")
    Ruedas = ( "RuedasA", "RuedasB", "RuedasC")
    Chasis = ("ChasisA", "ChasisB", "ChasisC")
    Carroceria = ("CrrA", "CrrB", "CrrC")
    components = (Motor, Caja_Camb, Ruedas, Chasis, Carroceria)

    
        
    if menu.upper() == "MA":
        print("Poniendo pieza..")
        ca_piece.pop(1)
        print(ca_piece)
        ca_piece.update({1: components[0][0]})
        for key, value in ca_piece.items():
            print(f"{key}:{value}")
    elif menu.upper() == menu.isdigit():
        break
    elif menu.upper() == "MB":
        print("Poniendo pieza..")
        ca_piece.pop(1)
        ca_piece.update({ 1: "MotorB"})
        for key, value in ca_piece.items():
            print(f"{key}:{value}")



#if menu.upper() == "MA":
#              sleep(4)
#              print("La pieza ha sido cambiada con normalidad")
#             Carro.temp_inventory.insert(0, Carro.components_car.items())
#                Carro.components_car.update(0, Pieces.components[0][0] )