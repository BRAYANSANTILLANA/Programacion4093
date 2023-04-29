mujeres = int(input('Digite el total de mujeres: ')) 
hombres = int(input('Digite el total de hombres: ')) 
toltal = mujeres + hombres
porcentaje_mujer=mujeres/toltal*100
porcentaje_hombre=hombres/toltal*100
print('El porcentaje de mujeres es: %','{:.2f}'.format(porcentaje_mujer))
print('El porcentaje de hombres es: %','{:.2f}'.format(porcentaje_hombre))