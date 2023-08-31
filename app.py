from flask import Flask

app = Flask("meu app")

@app.route('/')  #para definir a rota do cod, posso dar qlqr nome entre aspas simples
def hello():                  #conjunto de ações
    return "Hello Word"       #conjunto de ações
