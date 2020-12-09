from config import *
from cavalo import Cavalo, Dono, Estabulo

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

@app.route("/incluir_cavalo", methods=["POST"])
def incluir_cavalo():
    dados = request.get_json()
    novo_cavalo = Cavalo(**dados)
    db.session.add(novo_cavalo)
    db.session.commit()
    return {"resultado": 'Ok'}

@app.route("/excluir_cavalo/<int:cavalo_id>", methods=["DELETE"])
def excluir_cavalo(cavalo_id):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    try:
        Cavalo.query.filter(Cavalo.id == cavalo_id).delete()
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado": "erro", "detalhes":str(e)})
    
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/listar_donos")
def listar_donos():
    donos = db.session.query(Dono).all()
    retorno = []
    for d in donos:
        retorno.append(d.json())
    resposta = jsonify(retorno)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/listar_estabulos")
def listar_estabulos():
    estabulos = db.session.query(Estabulo).all()
    retorno = []
    for e in estabulos:
        retorno.append(e.json())
    resposta = jsonify(retorno)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta


app.run(debug=True)
