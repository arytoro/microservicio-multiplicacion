from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/multiplicar', methods=['GET'])
def multiplicar():
	try:
		a = float(request.args.get('a'))
		b = float(request.args.get('b'))
		resultado = a * b
		return jsonify({
			"a": a,
			"b": b,
			"resultado": resultado
		})
	except (TypeError, ValueError):
		return jsonify({"error": "Parámetros inválidos"}), 400

if __name__ == '__main__':
	app.run(debug=True)
