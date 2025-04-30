#Calificacion de edad

edadCalificacion = int(input("Ingresa tu edad=>"))

if edadCalificacion >0 and edadCalificacion <18:
    print("Eres menor de edad.")

elif edadCalificacion >=18 and edadCalificacion <=30:
    print("Eres adulto joven.")
    
elif edadCalificacion >=31 and edadCalificacion <=65:
    print("Eres adulto maduro.")
    
elif edadCalificacion >=65 and edadCalificacion <=100:
    print("Eres un adulto mayor")
    
else:
    print("Ya eres un inmortal!.")


def calcular_tarifa(si_trabajo, hora):
    if si_trabajo == "N":
        return "Fin de semana,vez a descansar."
    elif si_trabajo == "S":
        if (7 <= hora <= 9) or (17 <= hora <= 19):
            return "Hora pico."
        else:
            return "Hora normal."
    else:
        return "Entrada invalida."
    
    
