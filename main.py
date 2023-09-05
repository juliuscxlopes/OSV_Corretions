from Automacao_Classes import AutomacaoWeb, EmpresaPage, GrupoPage, UsuariosPage, SelecionarUsuario, PolProcChamadasPage, PerfilUsuarioPage, RetornoUsuario
from selenium.common.exceptions import NoSuchElementException
from flask import Flask, request, render_template
import webbrowser

app = Flask(__name__, template_folder='templates')

# Definição da função iniciar_automacao
def iniciar_automacao(login, senha, emp, grupo, usuarios, telefone):
    automacao = AutomacaoWeb()
    automacao.fazer_login(login, senha)  # Login e senha de acesso.

    empresa_page = EmpresaPage(automacao.driver)
    empresa_page.selecionar_empresa(emp)  # Especifique a empresa

    grupo_page = GrupoPage(automacao.driver)
    grupo_page.selecionar_grupo(grupo)  # Caso precise especifique o grupo.

    usuarios_page = UsuariosPage(automacao.driver)
    usuarios_page.sel_pagina_usuarios()

    usuarios_page.buscar_usuarios_por_regiao(usuarios)  # Informe o Pré-fixo de busca do Usuário.

    pol_chamadas_page = PolProcChamadasPage(automacao.driver)
    perfil_usuario_page = PerfilUsuarioPage(automacao.driver)
    retorno_usuario_instancia = RetornoUsuario(automacao.driver)
    sel_usuario = SelecionarUsuario(automacao.driver)
    
    usuario_numero = 1
    pagina_atual = 1
    
    while True:
        try:
            if pagina_atual == 1:
                    sel_usuario.sel_usuario(usuario_numero)
                    pol_chamadas_page.configurar_politica_chamadas()
                    perfil_usuario_page.configurar_perfil_usuario(telefone) #telefone  # Informe o número correto para o projeto.
                    retorno_usuario_instancia.retornar_usuario()
                    usuarios_page.buscar_usuarios_por_regiao(usuarios)  # Altere o pré-fixo novamente.
                    usuario_numero += 1
                    if usuario_numero == 21:
                        pagina_atual += 1
                        usuario_numero = 1

    
            elif pagina_atual == 2:
                sel_usuario.sel_usuario(usuario_numero)
                pol_chamadas_page.configurar_politica_chamadas()
                perfil_usuario_page.configurar_perfil_usuario(telefone) #telefone # Informe o número correto para o projeto.
                retorno_usuario_instancia.retornar_usuario()
                usuarios_page.buscar_usuarios_por_regiao(usuarios)  # Altere o pré-fixo novamente.
                usuarios_page.ir_para_proxima_pagina()
                usuario_numero += 1
                
            #Caso precise de mais paginas, copie e cole o codigo acima, Lembre-se fazer alterações necessarios.    
                
        except NoSuchElementException:
            print('todas as Rows executadas.')
            break        
        
@app.route('/')
def home():
    return render_template('formulario.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    login = request.form['login']
    senha = request.form['senha']
    emp = request.form['empresa']
    grupo = request.form['grupo']
    usuarios = request.form['usuarios']
    telefone = request.form['telefone']
    
    iniciar_automacao(login, senha, emp, grupo, usuarios, telefone)

if __name__ == "__main__":
    # Abre o navegador padrão automaticamente
    webbrowser.open('http://127.0.0.1:5000')

    # Executa o aplicativo Flask
    app.run(debug=True)
