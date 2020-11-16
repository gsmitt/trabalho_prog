from config import *

class Dono(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dono_nome = db.Column(db.String(254))
    telefone = db.Column(db.String(254))
    email = db.Column(db.String(254))
    def __str__(self):
        s = f"{self.dono_nome}, telefone {self.telefone}, email {self.email}"
        return s
    def json(self):
        return {
            "id" : self.id,
            "dono_nome" : self.dono_nome,
            "telefone" : self.telefone,
            "email" : self.email
        }
"""
if __name__ == "__main__": #teste dono
    db.create_all()
    novo = Dono(dono_nome = "Carlos", telefone = "(99) 99999-9999", email = "teste@teste.com")
    print(novo.telefone)
    db.session.add(novo)
    db.session.commit()
    todos = db.session.query(Dono).all()
    print(todos)

    for c in todos:
        print(c)
        print(c.json())
"""
class Estabulo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(254))
    endereco = db.Column(db.String(254))
    def __str__(self):
        s = f"estábulo {self.codigo}, localizado em {self.endereco}"
        return s
    def json(self):
        return {
            "id" : self.id,
            "codigo" : self.codigo,
            "endereco" : self.endereco
        }
"""
if __name__ == "__main__": #teste estabulo
    db.create_all()
    novo = Estabulo(codigo = "6B9A", endereco = "Rua Exemplo, 123")
    print(novo.codigo)
    db.session.add(novo)
    db.session.commit()
    todos = db.session.query(Estabulo).all()
    print(todos)

    for c in todos:
        print(c)
        print(c.json())
"""
class Cavalo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    cor = db.Column(db.String(254))
    idade_em_dias = db.Column(db.Integer)
    peso_em_gramas = db.Column(db.Integer)
    altura_em_cm = db.Column(db.Integer)
    dono_id = db.Column(db.Integer, db.ForeignKey(Dono.id))
    dono = db.relationship("Dono")
    estabulo_id = db.Column(db.Integer, db.ForeignKey(Estabulo.id))
    estabulo = db.relationship("Estabulo")
    def __str__(self):
        s = f"{self.nome}, {self.cor}, {str(self.idade_em_dias)} dias, {str(self.peso_em_gramas)} gramas, {str(self.altura_em_cm)} cm"
        if self.dono != None:
            s += f", cavalo de {self.dono_nome}"
        if self.estabulo != None:
            s += f"alojado no estábulo {self.codigo}"
        return s

    def json(self):
        if self.dono is None: # o cavalo não tem dono 
            dono_id = ""
            dono_nome = ""
            telefone = ""
            email = ""
        else: # o cavalo tem dono
            dono_id = self.dono_id
            dono_nome = self.dono_nome
            telefone = self.telefone
            email = self.email

        if self.estabulo is None: # o cavalo não está alojado em um estábulo
            estabulo_id = ""
            codigo = ""
            endereco = ""
        else: # o cavalo está alojado em um estábulo
            estabulo_id = self.estabulo_id
            codigo = self.codigo
            endereco = self.endereco

        return {
        "id": self.id,
        "nome" : self.nome,
        "cor" : self.cor,
        "idade_em_dias" : self.idade_em_dias,
        "peso_em_gramas" : self.peso_em_gramas,
        "altura_em_cm" : self.altura_em_cm,
        "dono_id" : self.dono_id,
        "dono_nome" : self.dono_nome,
        "telefone" : self.telefone,
        "email" : self.email,
        "estabulo_id" : self.estabulo_id,
        "codigo" : self.codigo,
        "endereco" : self.endereco
        }

'''
if __name__ == "__main__": #teste cavalo
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
'''

