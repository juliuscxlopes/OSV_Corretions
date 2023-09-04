from Automacao_Classes import Info_basic, AutomacaoWeb, EmpresaPage, GrupoPage, UsuariosPage, SelecionarUsuario, PolProcChamadasPage, PerfilUsuarioPage, RetornoUsuario
from selenium.common.exceptions import NoSuchElementException

def main():
    
    info = Info_basic()
    login, senha = info.dados_login()
    emp = info.empresa()
    grupo = info.group()
    usuarios, telefone = info.pré_fixo_e_telefone()
    
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
                    perfil_usuario_page.configurar_perfil_usuario("") #telefone  # Informe o número correto para o projeto.
                    retorno_usuario_instancia.retornar_usuario()
                    usuarios_page.buscar_usuarios_por_regiao(usuarios)  # Altere o pré-fixo novamente.
                    usuario_numero += 1
                    if usuario_numero == 21:
                        pagina_atual += 1
                        usuario_numero = 1

    
            elif pagina_atual == 2:
                sel_usuario.sel_usuario(usuario_numero)
                pol_chamadas_page.configurar_politica_chamadas()
                perfil_usuario_page.configurar_perfil_usuario("") #telefone # Informe o número correto para o projeto.
                retorno_usuario_instancia.retornar_usuario()
                usuarios_page.buscar_usuarios_por_regiao(usuarios)  # Altere o pré-fixo novamente.
                usuarios_page.ir_para_proxima_pagina()
                usuario_numero += 1
                
            #Caso precise de mais paginas, copie e cole o codigo acima, Lembre-se fazer alterações necessarios.    
                
        except NoSuchElementException:
            print('todas as Rows executadas.')
            break


if __name__ == "__main__":
    main()