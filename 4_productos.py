import cgi 

#headers
print("Content-Type: text/html")
print()

print("<html>")
form = cgi.FieldStorage()

option=form["operacion"].value


if option =="venta":
    print('selecciona el producto a vender')

elif option == "ingreso":
    print("ingresa el producto al sistema")
    print("""<html>
        <form method="post" action="5_form_ingreso.py">)
            <button>INGRESAR PRODUCTO</button>
        </form>
     </html>""")
    
elif option == "mostrar":
    print('aqui estan todos los productos')
else:
    print('no ingreso ninguna opcion')


