import tkinter as tk
from Automacao_Classes import AutomacaoWeb, EmpresaPage, GrupoPage, UsuariosPage, SelecionarUsuario, PolProcChamadasPage, PerfilUsuarioPage, RetornoUsuario
from selenium.common.exceptions import NoSuchElementException

def iniciar_automacao():
    login = login_entry.get()
    senha = senha_entry.get()
    emp = empresa_entry.get()
    grupo = grupo_entry.get()
    usuarios = usuarios_entry.get()
    telefone = telefone_entry.get()

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
                    perfil_usuario_page.configurar_perfil_usuario(telefone)  # Informe o número correto para o projeto.
                    retorno_usuario_instancia.retornar_usuario()
                    usuarios_page.buscar_usuarios_por_regiao(usuarios)  # Altere o pré-fixo novamente.
                    usuario_numero += 1
                    if usuario_numero == 21:
                        pagina_atual += 1
                        usuario_numero = 1

    
            elif pagina_atual == 2:
                sel_usuario.sel_usuario(usuario_numero)
                pol_chamadas_page.configurar_politica_chamadas()
                perfil_usuario_page.configurar_perfil_usuario(telefone) # Informe o número correto para o projeto.
                retorno_usuario_instancia.retornar_usuario()
                usuarios_page.buscar_usuarios_por_regiao(usuarios)  # Altere o pré-fixo novamente.
                usuarios_page.ir_para_proxima_pagina()
                usuario_numero += 1
                
            #Caso precise de mais paginas, copie e cole o codigo acima, Lembre-se fazer alterações necessarios.    
                
        except NoSuchElementException:
            print('todas as Rows executadas.')
            break

# Cria uma janela tkinter
janela = tk.Tk()
janela.title("Automação Web")

# Cria rótulos e campos de entrada para as informações
login_label = tk.Label(janela, text="Login:")
login_label.pack()
login_entry = tk.Entry(janela)
login_entry.pack()

senha_label = tk.Label(janela, text="Senha:")
senha_label.pack()
senha_entry = tk.Entry(janela, show="*")
senha_entry.pack()

empresa_label = tk.Label(janela, text="Empresa:")
empresa_label.pack()
empresa_entry = tk.Entry(janela)
empresa_entry.pack()

grupo_label = tk.Label(janela, text="Grupo:")
grupo_label.pack()
grupo_entry = tk.Entry(janela)
grupo_entry.pack()

usuarios_label = tk.Label(janela, text="Usuários:")
usuarios_label.pack()
usuarios_entry = tk.Entry(janela)
usuarios_entry.pack()

telefone_label = tk.Label(janela, text="Telefone:")
telefone_label.pack()
telefone_entry = tk.Entry(janela)
telefone_entry.pack()

# Botão para iniciar a automação
iniciar_button = tk.Button(janela, text="Iniciar Automação", command=iniciar_automacao)
iniciar_button.pack()

janela.mainloop()
