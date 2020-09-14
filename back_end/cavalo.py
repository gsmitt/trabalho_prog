from config import *

class Cavalo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    cor = db.Column(db.String(254))
    idade_em_dias = db.Column(db.Integer)
    peso_em_gramas = db.Column(db.Integer)
    altura_em_cm = db.Column(db.Integer)
    def __str__(self):
        return self.nome + ", " + self.cor + ", " + \
         str(self.idade_em_dias) + ", " + str(self.peso_em_gramas) + ", " + \
         str(self.altura_em_cm)
    def json(self):
        return {
        "nome" : self.nome,
        "cor" : self.cor,
        "idade_em_dias" : self.idade_em_dias,
        "peso_em_gramas" : self.peso_em_gramas,
        "altura_em_cm" : self.altura_em_cm
        }

if __name__ == "__main__":
    db.create_all()
    novo = Cavalo(nome = "Jorje", cor = "Marrom", idade_em_dias = 2469,
     peso_em_gramas= 177013, altura_em_cm = 40028922)
    print (novo.cor)
    db.session.add(novo)
    db.session.commit()
    todos = db.session.query(Cavalo).all()
    print(todos)

    for c in todos:
        print(c)
        print(c.json())
        