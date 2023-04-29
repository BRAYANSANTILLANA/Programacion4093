#DATOS DE EMPLEADO
def comision_sal(slbasic):
    comision = 0
    if slbasic >=1000000 and slbasic <= 1500000:  # Condicional de rango salarial 
       comision = slbasic * 0.02
    elif slbasic > 1500001 and slbasic <= 2000000:
        comision = slbasic * 0.05        
    return comision

def bon_alim(slbasic, dias_lab):
    alimentacion = 0
    if dias_lab == 20 and slbasic < 1000000:        # Condicional si su salario es inferior a $1000.0000 y si trabajo los 20 dias
       alimentacion = 100000
    return alimentacion

def pre_pension(slbasic, edad):
    bono = 0
    if edad >= 56:                                #Condicional de edad
       bono = slbasic * 0.05
    return bono   

resp = "si"
while resp.lower()== 'si':
    identificacion = int(input("Digite Numero de cedula : "))
    nombre = input('Digite su nombre: ')
    direccion = input('Direccion: ')
    telefono = int(input('Telefono: '))
    estatura = float(input('digite la estatura: '))
    fecha_contratacion = input('Fecha contratacion: ')
    estadocivil = input('Estado: ')
    hijos = input('tiene hijos: ')
    if estadocivil.lower() == "casado" and hijos.lower() == "si":  # Condicional si esta casado y si tiene hijos
        print("Ganaste un viaje para diciembre")
    dias_lab = int(input('Dias laborados: '))
    slbasic = float(input('Salario: '))
    edad = int(input('Edad : '))
    
    bono_alim = bon_alim(slbasic, dias_lab)
    bono_pre_pension = pre_pension(slbasic, edad)
    comision = comision_sal(slbasic)
    
    resul1 = slbasic + bono_alim
    resultado = slbasic + bono_alim + bono_pre_pension + comision
    
    print('Recibe bono alimentacion por valor $', bono_alim)
    print('Bono pre-pension: $', '{:.0f}'.format(bono_pre_pension))
    print('Comision por salario: $', '{:.0f}'.format(comision))
    print('Su salario si aplica bono: $', '{:.0f}'.format(resul1))
    print('Salario todo incluido: $', '{:.0f}'.format(resultado))
    
    resp = input('¿¿Desea continuar con más validaciones? (si/no) ')