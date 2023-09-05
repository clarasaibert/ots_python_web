from flask import Flask, render_template

app = Flask("meu app")

posts = [
    {
        "Titulo":"Minha primeira postagem!",
        "Texto":"teste texto"
    },
    {
        "Titulo" : "Segundo post",
        "Texto" : "teste texto 2"
    }
]

@app.route('/')                      #para definir a rota do codigo, posso dar qlqr nome entre aspas simples
def exibir_entradas():               #conjunto de ações
    entradas = posts                 #mock das postagens
    return render_template('exibir_entradas.html', entradas=entradas)           #conjunto de ações
