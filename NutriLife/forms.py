from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from NutriLife.models import Nutricionista

class FormularioCadastrar(FlaskForm):
    username = StringField('Nome Completo', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao = PasswordField('Confirmação de Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_cadastrar = SubmitField('Cadastrar')

    def validate_email(self, email):
        nutricionista = Nutricionista.query.filter_by(email=email.data).first()
        if nutricionista:
            raise ValidationError('E-mail já cadastrado. Cadastre-se com outro e-mail ou faça login para continuar')


class FormularioLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    botao_submit_logar = SubmitField('Fazer Login')


class FormularioCadastrarPaciente(FlaskForm):
    nome = StringField('Nome Completo do Paciente', validators=[DataRequired()])
    sexo = StringField('Sexo do Paciente', validators=[DataRequired()])
    idade = IntegerField('Idade do Paciente', validators=[DataRequired()])
    email = StringField('E-mail do Paciente', validators=[DataRequired(), Email()])
    telefone = StringField('Telefone do Paciente', validators=[DataRequired()])
    peso = IntegerField('Peso do Paciente', validators=[DataRequired()])
    altura = FloatField('Altura do Paciente', validators=[DataRequired()])
    percentualGordura = StringField('Percentual de Gordura do Paciente', validators=[DataRequired()])
    percentualMuscular = StringField('Percentual Muscular do Paciente', validators=[DataRequired()])
    colesterolHdl = IntegerField('Colesterol HDL do Paciente', validators=[DataRequired()])
    colesterolLdl = IntegerField('Colesterol LDL do Paciente', validators=[DataRequired()])
    colesterolTotal = IntegerField('Colesterol Total do Paciente', validators=[DataRequired()])
    trigliceridios = StringField('Trigliceridios do Paciente', validators=[DataRequired()])
    botao_submit_cadastrar_paciente = SubmitField('Cadastrar')


