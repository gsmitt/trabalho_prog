from config import *
from cavalo import Cavalo

@app.route("/")
def padrao():
    return "Ok"



@app.route("/listar_cavalos")
def listar_cavalos():
    cavalos = db.session.query(Cavalo).all()
    retorno = []
    for c in cavalos:
        retorno.append(c.json())
    resposta = jsonify(retorno)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/incluir_cavalo")
def incluir_cavalo():
    dados = request.get_json()
    novo_cavalo = Cavalo(**dados)
    db.session.add(novo_cavalo)
    db.session.commit()
    return {"resultado": 'Ok'}
app.run(debug=True)