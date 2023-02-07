from NutriLife import DATABASE, loginManager
from flask_login import UserMixin


@loginManager.user_loader
def loadUsuario(id_nutricionista):
    return Nutricionista.query.get(int(id_nutricionista))


class Nutricionista(DATABASE.Model, UserMixin):
    

    id = DATABASE.Column(DATABASE.Integer, primary_key=True)
    id = DATABASE.Column(DATABASE.Integer, primary_key=True)
    username = DATABASE.Column(DATABASE.String, nullable=False)  
    email = DATABASE.Column(DATABASE.String, nullable=False, unique=True)
    senha = DATABASE.Column(DATABASE.String, nullable=False)
    pacientes = DATABASE.relationship("Paciente", backref="nutricionistaResponsavel", lazy=True)


class Paciente(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer,primary_key=True)
    name = DATABASE.Column(DATABASE.String, nullable=False)
    sexo = DATABASE.Column(DATABASE.String, nullable=False)
    idade = DATABASE.Column(DATABASE.Integer)
    email = DATABASE.Column(DATABASE.String, nullable=False, unique=True)
    telefone = DATABASE.Column(DATABASE.Integer, nullable=False, unique=True)
    peso = DATABASE.Column(DATABASE.Integer, nullable=False)
    altura = DATABASE.Column(DATABASE.Float, nullable=False)
    percentual_gordura = DATABASE.Column(DATABASE.String, nullable=False)
    percentual_muscular =  DATABASE.Column(DATABASE.String, nullable=False)
    colesterol_hdl =  DATABASE.Column(DATABASE.Integer, nullable=False)
    colesterol_ldl =  DATABASE.Column(DATABASE.Integer, nullable=False)
    colesterol_total =  DATABASE.Column(DATABASE.Integer, nullable=False)
    trigliceridios =  DATABASE.Column(DATABASE.Integer, nullable=False)
    id_nutricionista = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey("nutricionista.id"), nullable=False)



