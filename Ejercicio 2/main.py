from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/ayuda')
def acerca_de():
    return render_template('ayuda.html')

@app.route('/listado')
def listado_pcap():
  paises_pcap=[]
  conn = sqlite3.connect('co_emissions.db')
  cur = conn.execute(f"""SELECT Country 
          FROM emissions 
          WHERE Series = 'pcap' 
          ORDER BY Value DESC 
          LIMIT 10 """)
  
  for pais in cur:
    paises_pcap.append(pais)
  conn.close()

  return render_template('top10pcap.html', top10_pcap=paises_pcap)

@app.route('/listado/top')
def listado_total():
  paises_total=[]
  conn = sqlite3.connect('co_emissions.db')
  cur = conn.execute(f"""SELECT Country 
          FROM emissions 
          WHERE Series = 'total' 
          ORDER BY Value DESC 
          LIMIT 10 """)
  
  for pais in cur:
    paises_total.append(pais)
  conn.close()

  return render_template('top10total.html', top10_total=paises_total)

@app.route('/listado/<pais>')
def listado_paises(pais):
  paises=[]
  conn = sqlite3.connect('co_emissions.db')
  cur = conn.execute(f"""SELECT Country, Series, Value
          FROM emissions  
          WHERE Country ='{pais}'
          ORDER BY Value DESC """)
  
  for pais in cur:
    paises.append(pais)
  conn.close()

  return render_template('totalypcap.html', total_pcap=paises)
    
    
app.run(host='0.0.0.0', port=81)