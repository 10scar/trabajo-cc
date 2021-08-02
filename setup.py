from flask import Flask, render_template,abort ,request
app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("formulario.html")

@app.route('/procesar', methods=['POST', 'GET'])
def procesar():
	if request.method == 'POST':
		ser = (request.form.get('pregunta-ser-1'),request.form.get('pregunta-ser-1'),request.form.get('pregunta-ser-1'))
		mundo = (request.form.get('pregunta-mundo-1'),request.form.get('pregunta-mundo-1'),request.form.get('pregunta-mundo-1'))
		altruismoegoismo = (request.form.get('pregunta-alt-1'),request.form.get('pregunta-alt-2'))
		laberintospasion = (request.form.get('pregunta-laberintos-1'),request.form.get('pregunta-laberintos-2'),request.form.get('pregunta-laberintos-3'))
		amor = request.form.get('pregunta-amor-1')
		verlaine = request.form.get('pregunta-Verlaine-1')
		return '<p>{0} {1} {2} {3} {4} {5}</p>'.format(ser, mundo, altruismoegoismo, laberintospasion, amor, verlaine)

app.run("0.0.0.0",5000,debug=True)
