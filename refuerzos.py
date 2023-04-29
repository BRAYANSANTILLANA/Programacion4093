def bon_sal(salario):
    bon= 0
    if salario<=655000:
        bon = salario * 0.04        
    else:
        print('No gana comision') 
    return bon

resp = "si"
while resp.lower() == "si":
    salario= float(input('digite su salario: '))
    bon = bon_sal(salario)  
    resul = salario + bon
    print('su bonificacion es de: $','{:.0f}'.format(bon))
    print('Su Salario sin bonificacion es: $','{:.0f}'.format(salario))
    print('su salario todo incluido es: $','{:.0f}'.format(resul))  
    resp = input('¿¿Desea continuar con más validaciones? (si/no) ')