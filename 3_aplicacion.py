import cgi 

#headers
print("Content-Type: text/html")
print()

print("<html>")


form = cgi.FieldStorage()

email=form.getvalue("email")
password=form.getvalue("passw")



if email=='gena123' and password=='gena123':
  print("""<html>
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
      <title>Document</title>
  </head>
  <body>
      

    <style>
    .titulo{
        margin-left:40%;
    }
    .ingreso_datos{
        margin-left:40%;
    }
    </style>
      
      <div class="titulo">
          <h1 class="title">STOCK-CONTROL</h1>
      </div>


      <!-- barra de navegacion -->
      <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
          <a class="navbar-brand" href="./vista_princ.py">INICIO</a>
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
            </ul>
          </div>
        </div>
      </nav>
    
<!-- formulario ingreso de acciones -->
    <h3 class="ingreso_datos">Ingresar la opcion que desees</h3>
      
    <form method="post" action="4_productos.py" class="ingreso_datos">
            <input type="radio" name="operacion" value="ingreso">Ingresar
            <br>
            <input type="radio" name="operacion" value="venta">Vender
            <br>
            <input type="radio" name="operacion" value="mostrar">Mostrar articulos
            <br>
            <button>Aceptar</button>
        </form>


      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>

</body>
  
   </html>""")
else:
  print('error de ingreso, intente nuevamente')
