from flask import redirect, render_template, request, url_for
from flask import render_template, request, url_for, redirect, flash, session
from models.database import db, Usuario
from werkzeug.security import generate_password_hash, check_password_hash
from markupsafe import Markup
import urllib
import json

userList = []

def init_app(app):
    
    @app.before_request
    def check_auth():
        # Rotas que não precisam de autenticação
        routes = ['login', 'cadastro', 'home', 'perfil','curso','video','editar' ]

        # Se a rota atual não requer autenticação, permite o acesso
        if request.endpoint in routes or request.path.startswith('/static/'):
            return

        # Se o usuário não estiver autenticado, redireciona para a página de login
        if 'user_id' not in session:
            return redirect(url_for('home'))

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']

            user = Usuario.query.filter_by(email=email).first()
            
            if user and check_password_hash(user.password, password):
                session['user_id'] = user.id
                session['email'] = user.email
                nickname = user.email.split('@')
                flash(f'Login bem-sucedido! Bem-vindo {nickname[0]}!', 'success')
                return redirect(url_for('home'))
            else:
                flash('Falha no login. Verifique seu nome de usuário e senha.', 'danger') 
        return render_template('login.html')
    
    # @app.route('/logout', methods=['GET', 'POST'])
    # def logout():
    #     session.clear()
    #     flash('Desconectado com sucesso!', 'warning')
    #     return redirect(url_for('home'))    
    
    @app.route('/cadastro', methods=['GET', 'POST'])
    def cadastro():
        if request.method == 'POST':
            if request.form.get('nome') and request.form.get('email') and request.form.get('password'): userList.append({'Nome' : request.form.get('nome'), 'E-mail' : request.form.get('email'), 'Senha' : request.form.get('password')})
        return render_template('cadastro.html')       
                    
        
    @app.route('/home')
    def home():
        return render_template('Home.html')
    
    @app.route('/video')
    def video():
        return render_template('Video.html')
 
    @app.route('/perfil')
    def perfil():
        return render_template('Perfil.html')
    
    
    @app.route('/loading')
    def loading():
        return render_template('Loading.html')
    
    @app.route('/editar')
    def editar():
        return render_template('Editar.html')
    
    @app.route('/curso')
    def curso():
        return render_template('Curso.html')
    
    
    
  