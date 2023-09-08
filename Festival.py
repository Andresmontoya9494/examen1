
print("***** FESTIVAL DE BANDAS****")
print("************")
print("0. Salir")
print("1. Registrar agrupacion musical")
print("2. Mostrar todas las bandas que se han presentado")
print("3. Cambiar la hora de agrupacion")
print("4. Retirar una agrupacion por falta de integrantes")
print("****************")

opcion=90
estado= bool
bandas=[]
0
while opcion!=0:
  banda={}

  opcion=int(input("Digite una opcion: "))

  if opcion==1:
    banda["Nombre"]=input("Ingrese el nombre de la banda: ")
    banda["Id"]=input("Ingrese el id de la banda: ")
    banda["Genero"]=input("Ingrese el genero de la banda: ")
    banda["Hora"]=input("Ingrese la hora de presentacion de la banda: ")
    banda["Pago"]=input("Ingrese el pago que se le da a la agrupacion: ")
    banda["Estado"]=int(input("Ya se presento: ?, 0. No, 1. Si  "))
    bandas.append(banda)
  elif opcion==2:
    for agrupacion in bandas:
        if agrupacion["Estado"]==1:
          print(f"Nombre: {agrupacion['Nombre']}")
          print(f"Id: {agrupacion['Id']}")
          print(f"Genero: {agrupacion['Genero']}")
          print(f"Hora: {agrupacion['Hora']}")
        elif agrupacion["Estado"]==0:
           print ("La banda no se ha presentado")
  elif opcion==3:
     id_buscar = input("Ingrese el id de la agrupacion que desea cambiar la hora de presentacion: ")

     for agrupacion in bandas: 
        if agrupacion["Id"]== id_buscar and agrupacion["Estado"]==0:
           nueva_hora= input("ingrese la nueva hora de presentacion para la banda: ")
           banda["Hora"]= nueva_hora
           print("La hora se ha modificado correctamente")
           print("La hora actualizada quedo a las: ",banda["Hora"])
        else:
           print("La banda ya se presento")
  elif opcion==4:
     id_remover= input("Ingrese el id de la agrupacion que desea retirar del evento: ")
     for agrupacion in bandas:
        if agrupacion["Id"]== id_remover and agrupacion["Estado"]==0:
          banda["Id"]= id_remover
          print("La banda se ha eliminado correctamente")
     else: 
        print("La banda ya se presento")




           
    
    
        
      



       
        
           


        
  

        
       


