def datos_person():
    identificacion = int(input("Digite Numero de cedula : "))
    nombre = input('Digite su nombre: ')
    edad = int(input('Edad : '))
    estadocivil = input('Estado: ')
    hijos = input('tiene hijos: ')
    estatura = float(input('digite la estatura: '))
    direccion = input('Direccion: ')
    telefono = int(input('Telefono: '))
    return identificacion, nombre, edad, estadocivil, hijos, estatura, direccion, telefono

def datos_lab():
    fecha_contratacion = input('Fecha contratacion: ')
    slbasic = float(input('Salario: '))
    dias_lab = int(input('Dias laborados: '))
    return fecha_contratacion, slbasic, dias_lab

datos = datos_person()
datos_labor = datos_lab()

resp = "si"
while resp.lower()== 'si': 
    resp = input('¿Desea continuar con más validaciones? (si/no) ')