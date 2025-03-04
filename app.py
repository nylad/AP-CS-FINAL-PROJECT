from flask import Flask 

app = Flask(__name__)

@app.route("/nyla")
def hello_world(): 
    return "hello Nyla" 


if __name__ == '__main__':
    app.run(host= '127.0.0.1')