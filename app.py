from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_word():
	return "hello, world ! (from a docker container)"

if __name__ =='__main__':
	app.run(debug=True, host='0.0.0.0')
