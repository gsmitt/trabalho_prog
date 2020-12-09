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
            s += f", cavalo de {self.dono.dono_nome}"
        if self.estabulo != None:
            s += f"alojado no estábulo {self.estabulo.codigo}"
        return s

    def json(self):
        if self.dono is None: # o cavalo não tem dono 
            dono_id = ""
            dono_nome = ""
            telefone = ""
            email = ""
        else: # o cavalo tem dono
            dono_id = self.dono_id
            dono_nome = self.dono.dono_nome
            telefone = self.dono.telefone
            email = self.dono.email

        if self.estabulo is None: # o cavalo não está alojado em um estábulo
            estabulo_id = ""
            codigo = ""
            endereco = ""
        else: # o cavalo está alojado em um estábulo
            estabulo_id = self.estabulo_id
            codigo = self.estabulo.codigo
            endereco = self.estabulo.endereco

        return {
        "id": self.id,
        "nome" : self.nome,
        "cor" : self.cor,
        "idade_em_dias" : self.idade_em_dias,
        "peso_em_gramas" : self.peso_em_gramas,
        "altura_em_cm" : self.altura_em_cm,
        "dono_id" : self.dono_id,
        "dono" : self.dono.json(),
        "estabulo_id" : self.estabulo_id,
        "estabulo" : self.estabulo.json()
        }


if __name__ == "__main__": 

    db.create_all()
    novo_dono = Dono(dono_nome = "Carlos", telefone = "(99) 99999-9999", email = "teste@teste.com")
    print(novo_dono.telefone)

    novo_estabulo = Estabulo(codigo = "6B9A", endereco = "Rua Exemplo, 123")
    print(novo_estabulo.codigo)
    
    novo_cavalo = Cavalo(nome = "Jorje", cor = "Marrom", idade_em_dias = 2469,
     peso_em_gramas= 177013, altura_em_cm = 40028922, dono = novo_dono, estabulo = novo_estabulo)
    print (novo_cavalo.cor)
    
    db.session.add(novo_dono)
    db.session.add(novo_estabulo)
    db.session.add(novo_cavalo)
    
    db.session.commit()
    
    lista_donos = db.session.query(Dono).all()
    lista_estabulos = db.session.query(Estabulo).all()
    lista_cavalos = db.session.query(Cavalo).all()
    print(lista_donos)
    print(lista_estabulos)
    print(lista_cavalos)
    
    for c in lista_donos:
        print(c)
        print(c.json())

    for c in lista_estabulos:
        print(c)
        print(c.json())


    for c in lista_cavalos:
        print(c)
        print(c.json())
