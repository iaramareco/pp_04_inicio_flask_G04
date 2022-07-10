@app.route('/dado')
def dado():
    return str(random.randint(0,7))

@app.route('/fecha')
def fecha():
  dia = str(random.randint(1,31))
  mes = str(random.randint(1,12))
  año = str(random.randint(1969,2100))
  return (dia + "/" + mes + "/" + año)
  
@app.route('/color')  
def color():
  valor1 = str(random.randint(0,256))
  valor2 = str(random.randint(0,256))
  valor3 = str(random.randint(0,256))
  return (valor1 + ", " + valor2 + ", " + valor3)

@app.route('/dado/<n>')
def dadon(n):
  coleccion_numeros= ""
  try:
    n = int(n)
    if n == 0 or n < 0 or n > 10:
      return "Error"
    for i in range(0,n):
      numero = str(random.randint(0,7))
      coleccion_numeros += numero + " "
    return coleccion_numeros
  except ValueError: 
    return "Tiene que ingresar un número"

@app.route('/fecha/<y>')
def fechay(y):
  dia = str(random.randint(1,31))
  mes = str(random.randint(1,12))
  return (dia + "/" + mes + "/" + y)

@app.route('/fecha/<y>/<m>')
def fechaym(y,m):
  dia = str(random.randint(1,31))
  return (dia + "/" + m + "/" + y)