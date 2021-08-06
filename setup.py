from flask import Flask, render_template,abort ,request
from fragments import functions

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("formulario.html")

@app.route('/procesar', methods=['POST', 'GET'])
def procesar():
	if request.method == 'POST':
		ser = (request.form.get('pregunta-ser-1'),request.form.get('pregunta-ser-2'),request.form.get('pregunta-ser-3'))
		mundo = (request.form.get('pregunta-mundo-1'),request.form.get('pregunta-mundo-2'),request.form.get('pregunta-mundo-3'))
		altruismoegoismo = (request.form.get('pregunta-alt-1'),request.form.get('pregunta-alt-2'))
		laberintospasion = (request.form.get('pregunta-laberintos-1'),request.form.get('pregunta-laberintos-2'),request.form.get('pregunta-laberintos-3'))
		amor = request.form.get('pregunta-amor-1')
		verlaine = request.form.get('pregunta-Verlaine-1')

		world = (functions.world_maze(mundo, altruismoegoismo))
		(string, value,a,b,g) = functions.individual_maze(ser, altruismoegoismo)
		loved = functions.loved_maze(laberintospasion,altruismoegoismo)
		lam = functions.lambd(value, world, loved)
		anguish = functions.anguish(lam,int(amor), int(verlaine))
		return render_template("resultados.html",anguish=anguish, string=string, a=a,b=b, g=g )
app.run("0.0.0.0",5000,debug=True)
