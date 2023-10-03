import cgi 

#headers
print("Content-Type: text/html")
print()

print("<html>")
form = cgi.FieldStorage()

print("""<html> 

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
    <title>Document</title>
</head>
<body>
       


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
      
</html>""")


print("""<html>
<!-- formulario ingreso de usuario-->
      
    <h1>INGRESO DE USUARIO</h1>
    <form method="post" action="3_aplicacion.py">
        <p>Email: <input type="text" name="email"  size="50"></p>
        <p>password: <input type="text" name="passw" ></p>

  <p>
    <input type="submit" value="Enviar">
  </p>
</form>
     </html>""")