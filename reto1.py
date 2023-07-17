import io
import json

def fecha():
    cont=0
    while True:
        try:
            fecha=input("Ingrese la fecha de hoy (dd/mm/yyyy): ")
            for i in fecha:
                if i.isdigit():
                    cont+=1        
            return fecha
        except:
            print("Error,Ingrese un numero")

def leerDatos():
    dic={}
    try:
        with open("productos.json","r")as archivo:
            dic=json.load(archivo)
            return dic
    except:
        dic={}
        return dic

def leerFactura():
    dicFactura={}
    try:
        with open("facturas.json","r+")as archivo:
            dicFactura=json.load(archivo)
            return dicFactura
    except:
        dicFactura={}
        return dicFactura
 
def leerInforme(fecha):
    dicInforme={}
    try:
        with open("informe.json","r")as archivo:
            dicInforme=json.load(archivo)
            dicInforme[fecha]={}
            return dicInforme
    except:
        dicInforme={}
        dicInforme[fecha]={}
        return dicInforme

    
def menu():
    while True:
        try:
            print("""
1.Productos
2.Facturar
3.Informe
4.Salir
                """)
            opcion=int(input("Ingrese su opcion (1 a 4): "))
            if opcion < 1 or opcion >4:
                print("Error,ingrese un numero con un rango de 1 a 4")
                continue
            else:
                return opcion
        except ValueError:
            print("Error,Ingrese un numero")
        
            
def productos(dic):
    id=codigoP(dic)
    valorUniP=valorUnitario()
    cantidadC=cantidadComprada()
    iva=ivaP()
    
    lista=[0, 0.05 ,0.19]
    dic[id]={}
    dic[id]["valorU"]=valorUniP
    dic[id]["cantidadC"]=cantidadC
    dic[id]["iva"]=lista[iva-1]
    
    enviarProductos(dic)
    
    return dic

def enviarProductos(dic):
    with open("productos.json","w+") as archivo:
        json.dump(dic,archivo)
    
    
def codigoP(dic):
    flat=True
    while True:
        try:
            id=input("Ingrese el codigo del producto: ")
            if not id.isdigit():
                print("Ingrese un codigo valido que sea de tipo entero")
                continue
            flat=validacionCodigo(id,dic)
            if flat == True or flat ==None:
                return id
            else:
                print("error,ingrese un codigo valido")
        except:
            print("Error,")
            
def validacionCodigo(id,dic):
    flat=True
    for i in dic.keys():
        if id == i:
            flat=False
    return flat
        

def valorUnitario():
    flat=True
    while True:
        try:
            valorU=int(input("Ingrese el valor del producto: "))
            return valorU
        except ValueError:
            print("Error,Ingrese un numero")

def cantidadComprada():
    while True:
        try:
            cantidad=int(input("Ingrese el la cantidad de productos que hay: "))
            return cantidad
        except ValueError:
            print("Error,Ingrese un numero")

def ivaP():
    while True:
        try:
            print("""
1.Exento
2.Bienes
3.General
                """)
            opcion=int(input("Ingrese la opcion del IVA  (1 a 3): "))
            if opcion < 1 or opcion >3:
                print("Error,ingrese un numero con un rango de 1 a 3")
                continue
            else:
                return opcion
        except ValueError:
            print("Error,Ingrese un numero")



def factura(dic,dicFactura):
    ivaAcum=0
    valorT=0
    valorAcum=0
    cont=0
    
    while True:
        try:
            dni=input("Digite el DNI del cliente: ")
            break
        except ValueError:
            print("ERROR,digite un numero")
    cantidad={}
    while True:
        flat=True
        id=codigoP2(dic)
        for i in cantidad.keys():
            
            if dic[id]["cantidadC"]<1:
                print("ya se acabo el producto")
                dic.pop(id)
                break
            else:
                if id == i:
                    cont+=1
                    cantidad[id]["canti"]+=1
                    flat=False
                    break
        if flat:
            cont+=1
            cantidad[id]={}
            cantidad[id]["canti"]=0
            cantidad[id]["canti"]+=1
            
        print(cantidad)
        agMas=input("Desea ingresar mas productos (si / no)?: ")
        if agMas.upper == "SI":
            pass
        elif agMas.upper() == "NO":
            break
    
    
    
    dicFactura[dni]={}
    for i in cantidad.keys():
        dicFactura[dni][i]={}
        valorP=dic[i]["valorU"]*cantidad[i]["canti"]
        valorAcum+=valorP
        dicFactura[dni][i]["valorP"]=valorP
        
        cantidades=dic[i]["cantidadC"]-cantidad[i]["canti"]
        dic[i]["cantidadC"]=cantidades
        
        iva=dicFactura[dni][i]["valorP"]*dic[i]["iva"]
        ivaT=iva+dicFactura[dni][i]["valorP"]
        ivaAcum+=dicFactura[dni][i]["valorP"]+dic[i]["iva"]
        
        dicFactura[dni][i]["valorIvaF"]=ivaT
        valorT+=dicFactura[dni][i]["valorIvaF"]
        
    dicFactura[dni]["valorT"]=valorT
    dicFactura[dni]["valorIvaT"]=ivaT
    dicFactura[dni]["valorAcum"]=valorAcum
    dicFactura[dni]["ProductosV"]=cont


    enviarFactura(dicFactura)
    enviarProductos(dic)
    for i in cantidad.keys():
        print("-"*60)
        print("Codigo:",i)
        print("valor Por Unidad:",dic[i]["valorU"])
        print("iva:",dic[i]["iva"]*100,"%")
        print("Valor Producto:",dicFactura[dni][i]["valorP"])
        print("Valor Producto con iva:",dicFactura[dni][i]["valorIvaF"])
        print("-"*60)
        
    print("Valor Total Compra: ",dicFactura[dni]["valorT"])
    print("Valor Iva Total: ",dicFactura[dni]["valorIvaT"])
    
    return dicFactura
        
        
        


def enviarFactura(dicFactura):
    with open("facturas.json","w+") as archivo:
        json.dump(dicFactura,archivo)
        

def codigoP2(dic):
    while True:
        try:
            id=input("Ingrese el codigo del producto: ")
            if not id.isdigit():
                print("Ingrese un codigo valido que sea de tipo entero")
                continue
            flat=validacionCodigo(id,dic)
            if flat == False :
                return id
            else:
                print("error,ingrese un codigo Existente")
        except:
            print("Error,")

def informe(dicFactura,dicInforme,fecha):
    print(fecha)
    
    cantidaP=productosV(dicFactura)
    sinIvaTotal=sinIva(dicFactura)
    conIvaTotal=conIva(dicFactura)
    totalP=productosTotalV(dicFactura)
        
    dicInforme[fecha]["cantidadP"]=cantidaP
    dicInforme[fecha]["sinIvaTotal"]=sinIvaTotal
    dicInforme[fecha]["conIvaTotal"]=conIvaTotal
    dicInforme[fecha]["totalP"]=totalP
        
    enviarInforme(dicInforme)    
    while True:
        flat=False
        try:
            fecha2=input("Digite una fecha : ")
            for i in dicInforme.keys():
                if fecha2 == i:
                    flat=True
            if flat == False:
                print("Error,Digite una fecha existente")
                continue
            break
        except:
            print("error")
            
    imprimirInforme(dicInforme,fecha2)  

def imprimirInforme(dicInforme,fecha):
    print("-"*50)
    print(fecha)
    print("Productos Vendidos: ",dicInforme[fecha]["cantidadP"])
    print("Valor Total de Productos: ",dicInforme[fecha]["sinIvaTotal"])
    print("Valor Total de Productos con Iva: ",dicInforme[fecha]["conIvaTotal"])
    print("Total Valor Productos: ",dicInforme[fecha]["totalP"])
    print("-"*50)
    
    

def enviarInforme(dicInforme):
    with open("informe.json","w+") as archivo:
        json.dump(dicInforme,archivo)

def productosV(dicFactura):
    cantidadP=0
    for i in dicFactura.keys():
            cantidadP+=dicFactura[i]["ProductosV"]
    return cantidadP

def sinIva(dicFactura):
    sinIvaTotal=0
    for i in dicFactura.keys():
            sinIvaTotal+=dicFactura[i]["valorAcum"]
    return sinIvaTotal


def conIva(dicFactura):
    conIvaTotal=0
    for i in dicFactura.keys():
            conIvaTotal+=dicFactura[i]["valorIvaT"]
    return conIvaTotal


def productosTotalV(dicFactura):
    totalP=0
    for i in dicFactura.keys():
            totalP+=dicFactura[i]["valorT"]
    return totalP
               

def salir(flat):
    flat=False
    return flat
fechaHoy=fecha()
dic=leerDatos()
dicFactura=leerFactura()
dicInforme=leerInforme(fechaHoy)

flat=True
while flat:
    opcion = menu()
    
    if opcion ==1:
        dic=productos(dic)
    elif opcion == 2:
        dicFactura=factura(dic,dicFactura)
    elif opcion == 3:
        informe(dicFactura,dicInforme,fechaHoy)
    else:
        flat=salir(flat)