def main():
    
    #PRIMERA FUNCIÓN EJECUTADA EN EL PROGRAMA, VERIFICA CONTRASEÑA Y USUARIO
    global P   #VARIABLE DONDE SE GUARDA EL NOMBRE DEL VENDEDOR
    CONTRASEÑAS= open('contraseña.txt','r')    #abre doc de contraseñas
    lineas = CONTRASEÑAS.readlines() #LEE LINEAS DEL DOC
    CONTRASEÑAS.close() #CIERRA (SON 3 LINEAS)
    print('--------------------------------------------------------------------------------------')
    print("-------------------------INGRESE USUARIO Y CONTRASEÑA O SALIR-------------------------")
    print('--------------------------------------------------------------------------------------')
    O=input("Si desea salir, escriba SALIR; si desea continuar, escriba CONTINUAR: ") #VARIABLE QUE REGISTRA SALIR O CUALQUIER OTRA COSA 
    if O == 'SALIR': #SALE DEL PROGRAMA
        exit()
    elif O == 'CONTINUAR':
        usuario=str(input("Usuario: ")) #INGRESA USUARIO
        contraseña=str(input("Contraseña: ")) #INGRESA CONTRASEÑA
        datoscontra=[] #LISTA DONDE SE GUARDAN LOS DATOS DE LA CONTRASEÑA, USUARIO Y NOMBRE
        for lista in lineas:
            items = lista.split()
            datoscontra.append(items) #SE AGREGAN A LISTA
        x=0
        y=1
        if usuario in datoscontra[x]: #SI EL USUARIO DADO ESTÁ ENTRE LOS USUARIOS DE LA LISTA
             I=datoscontra[x].index(usuario) #GUARDA SU POSICIÓN EN LA LISTA YA QUE EL USUARIO TENDRÁ LA MISMA POSICIÓN QUE SU CONTRASEÑA
             if contraseña in datoscontra[y]: # SI LA CONTRASEÑA ESTÁ EN LA LISTA DE CONTRASEÑAS
                if datoscontra[y].index(contraseña) == I: #Y SI TIENE LA MISMA POSICIÓM
                    P=nombre_trabajador(usuario,datoscontra) #GUARDA EN LA VARIABLE GLOBAL EL NOMBRE DEL USUARIO
                    print(P)
                    menu_principal() #VA A MENU PRINCIPAL
                
                else:
                    print("CONTRASEÑA NO VÁLIDA")
             else:
                print("CONTRASEÑA NO VÁLIDA")
        else:
            print("USUARIO NO SE ENCUENTRA EN LA BASE DE DATOS")
    else:
        print("OPCION NO VALIDA")
    main()
    return

def datos_de_venta(x): #X ES LA LISTA PRODUC[] DE VENTAS
    #SUMA EL NUMERO DE VENTAS Y DETERMINA LA GANANCIA TOTAL DADA POR UN PRODUCTO
    global BASEDEDATOS
    for i in x:
        for y in BASEDEDATOS: #AGREGA, TRAS EJECUTAR LA SECCIÓN DEL MENU 1.-REALIZAR VENTAS, LAS VENTAS REALIZADAS
                if y['CLAVE']==i:
                    p= y['VENTAS']+1
                    y['VENTAS']=p
                    q= y['VENTAS'] * y['PRECIO']
                    
                    y['TOTAL_GANANCIAS']= q  
    return BASEDEDATOS
                               
def nombre_trabajador(x,y):
    #GUARDA EL NOMBRE DEL TRABAJADOR
    I=y[0].index(x) #EL MISMO INDEX DEL USUARIO ES EL MISMO QUE EL DEL NOMBRE DEL TRABAJADOR
    A=y[2][I]
    return A
def ACTUALIZAR_BASE():
    global BASEDEDATOS
    Q=open('productosenventa.csv','w')
    for i in BASEDEDATOS:
        Q.write(i['CLAVE'])
        Q.write(' , ')
        Q.write(i['PRODUCTO'])
        Q.write(' , ')
        Q.write(str(i['PRECIO']))
        Q.write(' , ')
        Q.write(str(i['INVENTARIO']))
        Q.write(' , ')
        Q.write(str(i['VENTAS']))
        Q.write(' , ')
        Q.write(str(i['TOTAL_GANANCIAS']))
        
        Q.write('\n')
    Q.close()
    return
     
def IMPRIMIR_BASE_TOTAL():
    global BASEDEDATOS
    print('--------------------------------------------------------------------------------------')
    print('-------------------------------DATOS DE VENTAS----------------------------------------')
    print('--------------------------------------------------------------------------------------')
    x=0#CONTADOR 
    h=0#SIN USAR
    Y=0#SIN USAR
    print(len(BASEDEDATOS))
    while x<len(BASEDEDATOS):
        print('Clave:',BASEDEDATOS[x]['CLAVE'],' Precio:',BASEDEDATOS[x]['PRECIO'],' Inventario:',BASEDEDATOS[x]['INVENTARIO'],' Ventas:',BASEDEDATOS[x]['VENTAS'],' Total de ganancias:',BASEDEDATOS[x]['TOTAL_GANANCIAS'])
        h=h+BASEDEDATOS[x]['TOTAL_GANANCIAS']
        x=x+1
    print('---------------------------------------------------------------------------------------------')
    print('')  
    print('')
    x=x+1
    print("El total de ganancias es de",h)
    return

def IMPRIMIR_BASE():
    #Imprime el inventario disponible, al igual que los productos faltantes
    global BASEDEDATOS
    x=0#CONTADOR
    y=0#CONTADOR
    print('--------------------------------------------------------------------------------------')
    print('-------------------------------INVENTARIO DE PAPELEATEC-------------------------------')
    print('--------------------------------------------------------------------------------------')
    while x<len(BASEDEDATOS):
        
        print("| HAY UN TOTAL DE ",BASEDEDATOS[x]['INVENTARIO'],"DEL SIGUIENTE PRODUCTO,",BASEDEDATOS[x]['PRODUCTO'],"")
        x=x+1
        
    print('---------------------------------------------------------------------------------------------')
    print('')  
    print('')
    while y<len(BASEDEDATOS):
        z=BASEDEDATOS[y]['INVENTARIO']
        if z==0:
            print("EL PRODUCTO",BASEDEDATOS[y]['PRODUCTO']," ESTÁ AGOTADO, ADQUIERA MÁS")
        y=y+1
    return

def MODIFICAR_INV(x):
    #modifica inventario, agregando productos
    global CLAVE
    global BASEDEDATOS
    if x not in CLAVE:
        print("")
        print("")
        print("Valor no válido")
        print("")
        print("")
    else:
        for y in BASEDEDATOS:
            if y['CLAVE']==x:
                print(y['PRODUCTO'])
                z=int(input("Ingrese el valor a agregar para este producto ",))
                if z<0:
                    print("VALOR NO VALIDO")
                else:
                    h=z + int(y['INVENTARIO'])
                    y['INVENTARIO']=h
    return
    
def GENERAR_BASE():
    #genera la base de datos con la que se trabajaría el resto de la ejecución
    PRODUCTOS= open('productosenventa.csv','r')
    PRODUCTOS2=PRODUCTOS.readlines()
    dataBase=[]
    CLAVES=[]
    x=0
    for i in PRODUCTOS2:
        items = PRODUCTOS2[x].split(',')
        INVENTARIO={
            'CLAVE':(items[0].rstrip()),
            'PRODUCTO':items[1],
            'PRECIO':float(items[2].rstrip()),
            'INVENTARIO':int(items[3].rstrip()),
            'VENTAS':int(items[4].rstrip()),
            'TOTAL_GANANCIAS':float(items[5].rstrip())
            }
        dataBase.append(INVENTARIO)#GUARDA DICCIONARIOS
        CLAVES.append(INVENTARIO['CLAVE']) #GUARDA EXCLUSIVAMENTE LAS CLAVES DE TODOS LOS PRODUCTOS
        x=x+1 
    PRODUCTOS.close()
    for q in CLAVES:
            print(q)
    print(dataBase[0]['INVENTARIO'])
    return dataBase, CLAVES


def venta():
    #realiza la venta de productos, modificando inventario.
    global CLAVE
    for q in CLAVE:
        print(q)
    print("Ha seleccionado realizar una compra. Para ello, ingrese la clave de los productos que desea adquirir. Una vez haya terminado, escriba 'SALIR' ")
    COMPRAS=[] #LISTA DONDE SE GUARDAN CLAVES PARA LOS DATOS DE VENTAS
    PRODUC=[] #LISTA DONDE SE GUARDAN PRECIO Y NOMBRE DEL PRODUCTO PARA EL RECIBO
    nombre=input("Ingrese su nombre: ")
    COMPRAS.append(nombre)
    print("Cuando esté listo, escriba 'COMENZAR COMPRA'")
    compra=input("Escriba cuando esté listo: ")
    while compra != 'SALIR':
        print(COMPRAS)
        compra=input("Ingrese la clave ")
        if compra not in CLAVE and compra != 'SALIR' :
            print("CLAVE NO VÁLIDA")
        else:
            for y in BASEDEDATOS:
                producyprecio=[]
                if y['CLAVE']==compra:
                    if y['INVENTARIO']==0:
                        print("PRODUCTO NO DISPONIBLE")
                    else:
                        PRODUC.append(compra)
                        h=y['INVENTARIO']-1
                        y['INVENTARIO']=h
                        producyprecio.append(y['PRODUCTO'])
                        producyprecio.append(y['PRECIO'])
                        COMPRAS.append(producyprecio)
    
    return COMPRAS,PRODUC

def recibo(x): #X ES LA LISTA COMPRAS[]
    #despliega el recibo de la compra realizada
    global P #NOMBRE DEL TRABAJADOR
    RECIBO=[]
    TOTAL=0
    print('--------------------------------------------------------------------------------------')
    print('|---------------------------------RECIBO DE COMPRA-----------------------------------|')
    print('|----------------------------CLIENTE:...........',x[0],'-----------------------------|')
    y=1
    print('|-----------------------------ATENDIDO POR---',P,'-----------------------------------|')
    RECIBO.append(x[0])
    while y<len(x):
        print('|-----',x[y][0],'----------------------------------  ',x[y][1])
        TOTAL=TOTAL+x[y][1]
        RECIBO.append(x[y][0])
        RECIBO.append(x[y][1])
        y=y+1
    print('|----------TOTAL--------------------------------------',TOTAL,'-------------------------|')
    print('|-------------------------------GRACIAS POR SU COMPRA-------------------------------------|')
    RECIBO.append(TOTAL)
    RECIBO.append(P)
    
   
    return RECIBO

def menu_principal():
    #menu principal, se accede tras ingresar contraseña y usuario correcto
    global DATOSdeventas
    global datosdeventas
    global P
    global recibos
    print("")
    print("")
    print ('Trabajador en turno: ' ,P)
    print("")
    print("")
    print('--------------------------------------------------------------------------------------')
    print("----------------------------BIENVENIDO A PAPELEATEC-----------------------------------")
    print('--------------------------------------------------------------------------------------')
    print("Escoge una de las opciones disponibles para continuar")
    print("1.- Realizar compra")
    print("2.- Revisar datos de ventas")
    print("3.- Revisar reporte de ventas")
    print("4.- Modificar inventario")
    print("5.- Revisar inventario")
    print("6.- Cerrar sesión")
    print("")
    
    opcion=int(input("Seleccione alguna de las opciones: "))
    
        
    if opcion == 1:
        lista_de_compras,IDs=venta()
        datosdeventas.extend(IDs)
        datos_de_venta(datosdeventas)
        recibos.append(recibo(lista_de_compras))
        menu_principal()
        
    if opcion == 2:
        IMPRIMIR_BASE_TOTAL()
        menu_principal()
        
        
    if opcion == 3:
        CONT=0
        y=0
        while y<len(recibos):
            
            print('--------------------------------------------------------------------------------------')
            print('-------------------------Cliente: ',recibos[y][0],'----------------------------------')
            x=1
            while x<((len(recibos[y]))-2):
                print('-------------',recibos[y][x],'-----------',recibos[y][x+1],'-----------------------')
                x=x+2
            print('-------------TOTAL ES:-----------------',recibos[y][-2],'-----------------------')
            print('-------------ATENDIDO POR-----------',recibos[y][-1],'-----------------------')
            print('--------------------------------------------------------------------------------------')
            y=y+1
            
            print('')  
            print('')
            print('')  
            print('')
        menu_principal()
    if opcion == 4:
        print('Ingrese la clave del producto cuyo inventario desea modificar')
        PR=input("Clave: ")
        MODIFICAR_INV(PR)
        menu_principal()
    if opcion == 5:
        IMPRIMIR_BASE()
        menu_principal()
    if opcion == 6:
        ACTUALIZAR_BASE()
        main()
        
    if opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4 and opcion != 5 and opcion != 6:
        print("OPCIÓN NO VÁLIDA, regresando a menú principal")
        menu_principal()
    return


BASEDEDATOS, CLAVE =GENERAR_BASE() #SE GENERA LA BASE, Y SE GUARDAN LAS CLAVES
recibos=[] #se agrega toda la info de los recibos
datosdeventas=[] #claves que, al contarlas, son la cantidad de ventas
main()