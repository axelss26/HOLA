def switch_case(option):
    switcher = {
        1: "opcion 1 seleccionada",
        2: "opcion 2 seleccionada",
        3: "opcion 3 seleccionada"
    }
    return switcher.get(option, "opcion no valida")

opcion = int(input("ingrese una opcion (1-3): "))
print(switch_case(opcion))
