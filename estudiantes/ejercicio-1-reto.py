import io
import json


def cargarInfo():
    try:
        dic={}
        with open("estudiantes.json","r+")as archivo:
            
            dic = json.load(archivo)
            return dic
    except:
        dic={}
        return dic


def menu():
    while True:
        try:
            print("""
\tMenu:
1.Estudiantes
2.Notas
3.Reportes
4.salir 
                """)
            
            opcion=int(input("Ingrese su opcion: "))
            if opcion <1 or opcion >4:
                print("!Error¡,digite una opcion valida")
                continue
            return opcion
        except ValueError:
            print("Error,digite un numero")

def estudiantes(dic):
    while True:
        try: 
            print("""
\tEstudiantes
1.Agregar
2.Modificar
3.Eliminar
4.Buscar
5.Salir 
                """)
            opcion=int(input("Ingrese su opcion: "))
            if opcion<1 and opcion>5:
                print("Error,digite una opcion valida")
                continue
            if opcion==1:
                dic=agEstudiantes(dic)
            elif opcion == 2:
                dic=modiEstudiantes(dic)
            elif opcion== 3:
                dic = elimEstudaintes(dic)
            elif opcion==4:
                busqEstudiantes(dic)

            
            elif opcion==5:
                break
            
            return dic
            
        except:
            print("Error,digite un numero")
            continue
        
def agEstudiantes(dic):
    while True:
        while True:
            try:
                id=input("Digite el id del estudiante : ")
                if not id.isdigit():
                    print("Error,digite un numero")
                    continue
                else:
                    break
            
            except ValueError:
                print("Error,Digite un id valido")
                continue
        while True: 
            try:
                nombre=input("Digite el nombre del estudiante: ")
                if nombre.isdigit():
                    print("Error,los numeros no son validos")
                    continue
                else:
                    break
            except:
                print("Error,Digite un nombre valido")
                continue
        while True:
            try:
                sexo=input("Ingrese el sexo del estudiante(h/m): ")
                if sexo.upper() == "H" or sexo.upper() == "M":
                    break
                else:
                    print("ERROR,Ingrese un sexo valido")
                    continue
                
            except ValueError:
                print("Error,Digite un sexo valido")
                continue
        while True:
            try:
                grado=input("Ingrese el grado del estudiante: ")
                break
            except Exception as e:
                print("Error,Digite un grado valido")
                continue
        
        try:
            dic[grado][id]={}
            dic[grado][id]["nombre"]=nombre
            dic[grado][id]["sexo"]=sexo
            dic[grado][id]["notas"]=""
            dic[grado][id]["promedioN"]=""
            
        except:
            dic[grado]={}
            dic[grado][id]={}
            dic[grado][id]["nombre"]=nombre
            dic[grado][id]["sexo"]=sexo
            dic[grado][id]["notas"]=""
            dic[grado][id]["promedioN"]=""
        
        with open("estudiantes.json","w")as archivo:
            enviar=json.dump(dic,archivo)
        return dic   

def modiEstudiantes(dic):
    flat=False
    flat2=False
    cont=0
    while True:
        try:
            id=input("Digite el id del estudiante que desea cambiar : ")
            for i in dic.keys():
                for l in dic[i].keys():
                    if id == l:
                        flat2=True
            if flat2==False:
                print("Error,Digite un id valido")
                continue
        except ValueError:
            print("Error,Digite un id valido")
            continue
        try:
            print("""

1.Nombre
2.Sexo
3.Notas
4.Grado
                """)
            opcion=int(input("Digite la opcion que desea modificar: "))
        except:
            print("ERROR")
        
        for i in dic.keys():
            for l in dic[i].keys():
                if str(id) == l:
                    curso=i
        
        if opcion==1:
            nombre=input("Digite el nombre que desea modificar: ")
            dic[curso][id]["nombre"]=nombre
        elif opcion == 2:
            sexo=input("Digite el sexo que desea modificar (H/M) : ")
            dic[curso][id]["sexo"]=sexo
        elif opcion == 3:
                for i in dic[curso][id]["notas"]:
                    cont+=1
                    print(f"{cont}.{i}")
                while True:
                    try:    
                        op=int(input("Digite la nota que desee cambiar: "))
                        if op > cont or op <1:
                            continue
                        else: 
                            break
                    except ValueError:
                        print("Error digite un numero")
                        
                notaNew=float(input("Digite la nota que deseas cambiar: "))
                dic[curso][id]["notas"][op-1]=notaNew
                        
        elif opcion==4:
            while True:
                try:
                    grado=input("Digite el grado que desea cambiar: ")
                    for i in dic.keys():
                        if grado == i:
                            flat= True
                    if flat == False:
                        print("Error,el grado no existe")
                        continue
                    else: 
                        break
                except:
                    print("ERROR")
                    
            nombre= dic[curso][id]["nombre"]
            sexo= dic[curso][id]["sexo"]
            notas= dic[curso][id]["notas"]
            PromedioN= dic[curso][id]["promedioN"]
            
            dic[curso].pop(id)
            dic[grado][id]={}
            dic[grado][id]["nombre"]=nombre
            dic[grado][id]["sexo"]=sexo
            dic[grado][id]["notas"]=notas
            dic[grado][id]["grado"]=PromedioN
        dic= enviarJson(dic)
        return dic

def busqEstudiantes(dic):
    flat2=False
    cont=0
    while True:
        try:
            id=input("Digite el id del estudiante que desea cambiar : ")
            for i in dic.keys():
                for l in dic[i].keys():
                    if id == l:
                        curso=i
                        flat2=True
            if flat2==False:
                print("Error,Digite un id valido")
                continue
        except ValueError:
            print("Error,Digite un id valido")
            continue
        print("-"*50)
        print("Nombre:",dic[curso][id]["nombre"])
        print("Sexo:",dic[curso][id]["sexo"])
        print("Grado:",curso)
        for i in dic[curso][id]["notas"]:
            if i!="":
                cont+=1
                print(f"Nota {cont}:",i)
            else:
                print("Notas:No han ingresado notas")
        if dic[curso][id]["promedioN"] != "":
            print("Promedio:",dic[curso][id]["promedioN"])
        else:
            print("Promedio: No se ha ingresado alguna nota para sacar el promedio")
        print()
 
def elimEstudaintes(dic):
    flat2=False
    while True:
        try:
            id=input("Digite el id del estudiante que desea cambiar : ")
            for i in dic.keys():
                for l in dic[i].keys():
                    if id == l:
                        curso=i
                        flat2=True
            if flat2==False:
                print("Error,Digite un id valido")
                continue
        except ValueError:
            print("Error,Digite un id valido")
            continue
        
        dic[curso].pop(id)
        
        enviarJson(dic)
        print("se ha borrado exitosamente")        
        return dic

def notas(dic):
    cont=0
    flat=False
    while True:
        try:
            curso=input("Digite el curso : ")
            for i in dic.keys():
                if curso == i:
                    flat= True
            if flat==False:
                print("Error,ingrese un curso existente")
                continue                
        except:
            print("Error,Digite un curso valido")
            continue
        
        listaNew=[]
        for l in dic[curso].keys():
                listaNew.append(dic[curso][l]["nombre"])
                
        listaAlf=sorted(listaNew)
        cont=0
        for l in listaAlf:
            cont+=1
            print(f"{cont}.{l}")
        
        while True:
            opcion=int(input("Digite la opcion del estudiante que desea ingresar: "))
            if opcion >20 or opcion < 1:
                print("Error,Digite una opcion valida")
                continue 
            else:
                break
        
        for i in dic[curso].keys():
            if dic[curso][i]["nombre"]== listaAlf[opcion-1]:
                codi= i
        
        codiCur=[codi,curso]
        
        dic=agregarNotas(codiCur,dic)       

        agMas=input("Desea Ingresar Notas de otro estudiante: (Si/No): ")
        if agMas.upper() == "SI":
            continue
        elif agMas.upper()=="NO":
            return dic
        else:
            print("Error,Tiene que ingresar (Si o No)")
            break

def agregarNotas(codiCur,dic):
    cont=0
    cont2=0
    sumador=0
    listaNotas=[]
    codi=codiCur[0]
    curso=codiCur[1]
    while True:
        sumador=0
        cont+=1
        try:
            notas=float(input(f"Ingrese la nota {cont} : "))
            if notas <1 or notas > 5:
                print("Error,Digite un nota del (1 al 5)")
                continue
        except ValueError:
            print("Error digite un numero")
            continue
        
        listaNotas.append(notas)
        
        agMas=input("Desea seguir Ingresando Notas (Si/No): ")
        if agMas.upper() == "SI":
            continue
        elif agMas.upper()=="NO":
            break
        else:
            print("Error,Tiene que ingresar (Si o No)")
            break
    if dic[curso][codi]["notas"]=="":    
        dic[curso][codi]["notas"]=listaNotas
    else:
        for i in listaNotas:
            dic[curso][codi]["notas"].append(i)
        
        
    for i in dic[curso][codi]["notas"]:
        cont2+=1
        sumador+=i
    promedio=sumador/cont2
    
    dic[curso][codi]["promedioN"]=promedio
    
    enviarJson(dic)
    
    return dic
 
  
def enviarJson(dic):
     with open("estudiantes.json","w")as archivo:
        enviar=json.dump(dic,archivo)
          
    
def reportes(dic):
    while True:
        try:
            print("""
        \tReportes:
1.Promedios
2.Terna Grado
3.Terna Colegio
4.salir
            """)
            opcion=int(input("Digite la opcion que deseas ver:"))
            if opcion <1 or opcion > 4:
                print("Error,Digite una opcion valida")
                continue
        except ValueError:
            print("Error,Digite un numero")
        
        if opcion==1:
            promGrado(dic)
        elif opcion == 2:
            gradoTerna(dic)
        elif opcion== 3:
            colTerna(dic)
        elif opcion ==4:
            break
        
def promGrado(dic):
    flat=False
    while True:
        try:
            grado=input("Ingrese el grado para ver los promedios: ")
            for i in dic.keys():
                if grado == i:
                    flat=True
            if flat==False:
                print("Error,El grado no existe")
                continue
            else:
                break
        except:
            print("Error")
    
    

    print(grado,":")
    print("ID | Nombre | Promedio")
    for l in dic[grado]:
        print(l,dic[grado][l]["nombre"],dic[grado][l]["promedioN"])
                
def gradoTerna(dic):
    promedioCur=[]
    datos=[]
    flat=False
    cont=0
    while True:
        try:
            grado=input("Ingrese el grado para ver la terna de excelencia:  ")
            for i in dic.keys():
                if grado == i:
                    flat=True
            if flat==False:
                print("Error,El grado no existe")
                continue
            else:
                break
        except:
            print("Error")
    

    for l in dic[grado]:
        promedioCur.append(dic[grado][l]["promedioN"])
        datos.append(l)
    promedioCur.sort(reverse=True)
    for d in promedioCur:
        for i in datos:
            if d == dic[grado][i]["promedioN"]:
                cont+=1
                print(cont,". ",dic[grado][i]["nombre"],dic[grado][i]["promedioN"])
            if cont==5:
                break
def colTerna(dic):
    promedioCur=[]
    datos=[]
    cont=0
    for i in dic.keys():
        for l in dic[i]:
            promedioCur.append(dic[i][l]["promedioN"])
            datos.append([l,i])
    promedioCur.sort(reverse=True)
    for d in promedioCur:
        for i in datos:
            if d == dic[i[1]][i[0]]["promedioN"]:
                cont+=1
                print(cont,". ",dic[i[1]][i[0]]["nombre"] ,i[1], dic[i[1]][i[0]]["promedioN"])
            if cont==5:
                break
    
def salir():
    flat=False
    return flat

dic=cargarInfo()
flat=True
while flat == True:
    opcion=menu()
    
    if opcion==1:
        dic=estudiantes(dic)
    elif opcion == 2:
        dic=notas(dic)
    elif opcion== 3:
        reportes(dic)
    elif opcion==4:
        flat=salir()