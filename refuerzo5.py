compra = float(input('Digite el valor de la compra: '))
op_dcto= compra * 0.15
descuento = op_dcto
total = compra - descuento
print('Su descuento es: ','{:.0f}'.format(descuento))
print('Valor total: ','{:.0f}'.format(total))
