#                                          Calculadora de IMC

#IMC = PESO / (Altura x Altura)
# < 19 : Delgadez
# entre 20 y 25 : normal
# entre 26 y 30 : Sobrepeso
# > 30  : obesidad

# peso = int(input('ingrese su peso en kg: '))
# alturaEnCm = float(input('Ingrese su altura en cm: '))
# alturaEnMetros = alturaEnCm/100
# imc = peso / (alturaEnMetros * alturaEnMetros)

# if imc < 20:
#     print('Estado de delgadez')
# if imc >= 20 and imc <26:
#     print('Estado normal')
# if imc >= 26 and imc < 30:
#     print('Estado de sobrepeso')
# if imc >= 30:
#     print('Estado de Obesidad')

#                                          Chat con Emojis

# seguirChateando = True
# while seguirChateando:
#     texto = input('>')
#     if texto == ("salir" or "Salir"):
#         seguirChateando = False
#     texto = texto.replace(':)','🙂')
#     texto = texto.replace(':(','☹')
#     texto = texto.replace('xd','😆')
#     texto = texto.replace('Xd','😆')
#     texto = texto.replace('xD','😆')
#     texto = texto.replace('XD','😆')
#     texto = texto.replace(':D','😃')
#     texto = texto.replace(':d','😃')
#     print(texto)

#                                          Encriptador y Desencriptador

# def encriptar(texto):
#     textoFinal = ''
#     for letra in texto:
#         ascii = ord(letra)
#         ascii += 1
#         textoFinal += chr(ascii)
#     return(textoFinal)
# def desencriptar(texto):
#     textoFinal = ''
#     for letra in texto:
#         ascii = ord(letra)
#         ascii -= 1
#         textoFinal += chr(ascii)
#     return(textoFinal)

# def encriptarArchivo(nombreArchivo):
#     archivo = open(nombreArchivo,'r')
#     texto = archivo.read()
#     archivo.close()
#     textoEncriptado = encriptar(texto)
#     archivo = open(nombreArchivo, 'w')
#     archivo.write(textoEncriptado)
#     archivo.close()

# def desencriptarArchivo(nombreArchivo):
#     archivo = open(nombreArchivo,'r')
#     texto = archivo.read()
#     archivo.close()
#     textoDesencriptado = desencriptar(texto)
#     archivo = open(nombreArchivo,'w')
#     archivo.write(textoDesencriptado)
#     archivo.close()

# respuestaValida = True
# while respuestaValida:
#     respuestaUsuario = input('Presione la letra "E" para encriptar, o "D" para desencriptar: ')
#     if respuestaUsuario == "E" or respuestaUsuario == "e":
#         rutaArchivo = input('Ingrese la ruta del archivo: ')
#         encriptarArchivo(rutaArchivo)
#         print('El archivo se encripto correctamente!')
#         respuestaValida = False
#     if respuestaUsuario == "D" or respuestaUsuario == "d":
#         rutaArchivo = input('Ingrese la ruta del archivo: ')
#         desencriptarArchivo(rutaArchivo)
#         print('El archivo se desencripto correctamente!')
#         respuestaValida = False

#                                          OOP 1

# class Cuadrado:
#     def __init__(self,ancho,alto):
#         self.ancho = ancho
#         self.alto = alto
#     def calcularArea(self):
#         area = self.ancho * self.alto
#         return area

# figura = Cuadrado(10,12)
# print(figura.calcularArea())

#                                          OOP 2

class Persona:
    def __init__(self,nombre,apellido,rut,telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
        self.telefono = telefono
    def __str__(self):
        return self.nombre + ' ' + self.apellido + ', rut:' + self.rut

class Empleado(Persona):
    def __init__(self, nombre, apellido, rut, telefono, salario):
        super().__init__(nombre, apellido, rut, telefono)
        self.salario = salario
    
class Cliente(Persona):
    def __init__(self, nombre, apellido, rut, telefono, categoria):
        super().__init__(nombre, apellido, rut, telefono)
        self.categoria = categoria

        
def cargar():
    respuesta = input('Desea agregar un empleado?: ')
    nombre = input('Ingrese el Nombre: ')
    apellido = input('Ingrese el Apellido: ')
    rut = input('Ingrese el rut: ')
    telefono = input('Ingrese el telefono: ')
    if respuesta == 'si' or respuesta == 'Si' or respuesta == "SI" or respuesta == "sI":
        salario = input('Ingrese el salario correspondiente: ')
        emp = Empleado(nombre,apellido,rut,telefono,salario)
        return personas.append(emp)
    else:
        categoria = input('Ingrese la categoria del cliente: ')
        cli = Cliente(nombre,apellido,rut,telefono,categoria)
        return personas.append(cli)

personas = []
cargar()
cargar()
for persona in personas:
    print(persona)
