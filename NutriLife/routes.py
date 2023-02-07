from NutriLife.forms import FormularioCadastrar, FormularioLogin, FormularioCadastrarPaciente
from flask import  render_template, url_for, request, flash , redirect
from NutriLife import app, DATABASE, bcrypt
from NutriLife.models import Nutricionista, Paciente
from flask_login import login_user, current_user


@app.route('/')
def home():
    
    return render_template('home.html')

    

@app.route('/login', methods=['GET', 'POST'])
def login():
    formLogin = FormularioLogin()

    if formLogin.validate_on_submit() and "botao_submit_logar" in request.form:
        nutricionista = Nutricionista.query.filter_by(email=formLogin.email.data).first()

        if nutricionista and bcrypt.check_password_hash(nutricionista.senha, formLogin.senha.data):
            login_user(nutricionista)
            flash('Login feito com sucesso')
            return redirect(url_for('mostrarPacientes'))

        else:
            flash(f'Falha no login, E-mail ou Senha Incorretos')

    return render_template("login.html", formLogin=formLogin)


@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    formCadastrar = FormularioCadastrar()

    if formCadastrar.validate_on_submit() and "botao_submit_cadastrar" in request.form:
        senha_cript = bcrypt.generate_password_hash(formCadastrar.senha.data)
        nutricionista = Nutricionista(username = formCadastrar.username.data, email = formCadastrar.email.data, senha = senha_cript)
        DATABASE.session.add(nutricionista)
        DATABASE.session.commit()
        flash('Cadastro feito com sucesso')
        return redirect(url_for('login'))

    return render_template("cadastrar.html", formCadastrar=formCadastrar)


@app.route('/initial')
def mostrarPacientes():
    meusPacientes = []
    pacientes = Paciente.query.order_by(Paciente.id.desc())
    for paciente in pacientes:
        if current_user == paciente.nutricionistaResponsavel:
            meusPacientes.append(paciente)
                
    return render_template("inicialpage.html", meusPacientes = meusPacientes, nutricionista = current_user)


@app.route('/cadastrar-paciente', methods=['GET', 'POST'])
def cadastrarPaciente():

    formCadastrarPaciente = FormularioCadastrarPaciente()

    if formCadastrarPaciente.validate_on_submit():
        
        paciente = Paciente(name = formCadastrarPaciente.nome.data, sexo = formCadastrarPaciente.sexo.data, idade = formCadastrarPaciente.idade.data,
        email = formCadastrarPaciente.email.data, telefone = formCadastrarPaciente.telefone.data, peso = formCadastrarPaciente.peso.data,
        altura = formCadastrarPaciente.altura.data, percentual_gordura = formCadastrarPaciente.percentualGordura.data, 
        percentual_muscular = formCadastrarPaciente.percentualMuscular.data, colesterol_hdl = formCadastrarPaciente.colesterolHdl.data,
        colesterol_ldl = formCadastrarPaciente.colesterolLdl.data, colesterol_total= formCadastrarPaciente.colesterolTotal.data, trigliceridios = formCadastrarPaciente.trigliceridios.data, nutricionistaResponsavel = current_user)
        

        DATABASE.session.add(paciente)
        DATABASE.session.commit()
        flash('Paciente Criado com Sucesso', 'alert-success')
        return redirect(url_for('mostrarPacientes'))

        
    return render_template("adicionarpaciente.html", formCadastrarPaciente = formCadastrarPaciente)
