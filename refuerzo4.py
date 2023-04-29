
sueldo_base = float(input('Digite salario: '))
venta1 = float(input('Valor de venta 1 '))* 0.10
venta2 = float(input('Valor de venta 2 '))* 0.10
venta3 = float(input('Valor de venta 3 '))* 0.10
suma_ventas = venta1 + venta2 + venta3
comision = suma_ventas
total = sueldo_base + comision 
print('la comision es: ','{:.0f}'.format(comision))
print('Su sueldo mas comision es: ','{:.0f}'.format(total))