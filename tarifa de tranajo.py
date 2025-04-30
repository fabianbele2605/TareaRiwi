# Tarifa de transporte según día y hora

dia_laborable = (input("Ingresa si el dia es laborable? (S/N): ")).upper()

if dia_laborable == "N":
    print("Fin de semana!.")
    
elif dia_laborable == "S":
    hora = int(input("Ingresa la hora (0-23): "))
    if (7 <= hora <= 9) or (17 <= hora <= 19):
        tarifa = "Hora pico"
    else:
        tarifa = "Hora normal"
    print(f"La tarifa aplicada es: {tarifa}")
        
else:
    tarifa = "Entrada invalida"
    
