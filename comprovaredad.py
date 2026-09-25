'''
Autor: Joel Gonzalez Barraza - ASIXc1D
Asignatura: MDS 
Actividad: TA02
Programa: Programa basico en py que comprueba si el usuario es mayor de edad o no

'''

def comprobar():

     edad = input("Escribe tu edad:\n")

     if edad.isdigit():

            edad = int(edad)

            if edad >= 18:
                    
                    print("Eres mayor de edad")

            elif edad < 18:
            
                    print("Eres menor de edad")

     else: 

          print("El dato debe de ser un número entero")       


comprobar()
