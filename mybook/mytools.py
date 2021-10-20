import mysql.connector as db



def convercion_aBinaryText(myfile):
    with open(myfile, 'rb') as archivo_text_bina:
        binaryData = archivo_text_bina.read()
    return binaryData


def insertar_archivoX(id, idemp, name, detalle, precio, fotoa, fotob, fecha):
    try:
        connection = db.connect(
            host='localhost', database='productos', user='root', password='azby')
        cursor = connection.cursor()
        queryx = """ INSERT INTO productos (id,idemp, name, detalle, precio, fotoa, fotob, fecha) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
        fotoak = convercion_aBinaryText(fotoa)
        fotobk = convercion_aBinaryText(fotob)
        myproductdates = (id, idemp, name, detalle,
                          precio, fotoak, fotobk, fecha)
        result = cursor.execute(queryx, myproductdates)
        connection.commit()
        connection.close()
        print("Guardaste con exito tu producto jefe", result)
    except db.Error as error:
        print("fallo cod-error: -- {}".format(error))

    finally:
        if connection.is_connected():
            connection.close()

# try:
 #   insertar_archivoX(2,"ecomycr","@ecomy-admin", "Mi primer aplicación al mercado.", "1.000.000.000.000.000,89", "src/asd.png", "src/asd.png", "19 de octubre")
  #  print("Si se guardo con exito")
   # time.sleep(2)

# except Exception as e:
 #   print("no funciono" + str(e))


def convertir_image_mysql_a_imageNormal(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)


def extraer_save_image_fromMySQL():
    print("obteniendo images de base de datos")

    try:
        connection = db.connect(host='localhost',
                                database='productos',
                                user='root',
                                password='azby')

        cursor = connection.cursor()
        sql_fetch_blob_query = """SELECT * from productos"""

        cursor.execute(sql_fetch_blob_query)
        record = cursor.fetchall()
        for row in record:
            IdK = str(row[0])
            print("idemp = ", row[1])
            print("name = ", row[2])
            print("detalle = ", row[3])
            print("precio = ", row[4])
            fotoak = row[5]
            fotobk = row[6]
            
            nameA = "mybook/productosImages/ecomyProductsA{}.png".format(IdK)
            nameB = "mybook/productosImages/ecomyProductsB{}.png".format(IdK)
            
            

            print(" Convert binary data a Imnagen y guardarla en carpeta \n\n")
            try:
                convertir_image_mysql_a_imageNormal(fotoak, nameA)
                convertir_image_mysql_a_imageNormal(fotobk, nameB)
            except Exception as e:
                print("No se puedo subir guardar imagens: " + nameA)
                print(str(e))
    except db.Error as error:
        print("Algo salio mal jefe {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL is closed")

