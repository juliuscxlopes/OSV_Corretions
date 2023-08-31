
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

    #Classe Página:
class AutomacaoWeb:   
    def __init__(self):
        self.driver = chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=chrome_options)

    def fazer_login(self, username, password):
        url = 'https://xsp.gc.italk.net.br/GPOperator/Profile/'
        self.driver.get(url)
        username_field = self.driver.find_element(By.NAME, "EnteredUserID")
        password_field = self.driver.find_element(By.NAME, "Password")
        username_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
    
    def fechar_nav(self):
        self.driver.quit()
        
class EmpresaPage:
    def __init__(self, driver):
        self.driver = driver
        
    def selecionar_empresa(self, empresa_nome):
        b_empresa = self.driver.find_element(By.NAME, "/Operator/ServiceProviders/index.jsp?enterprise=true")
        b_empresa.click()
        time.sleep(1)
        empresa_input = self.driver.find_element(By.ID, "findValue0")
        empresa_input.click()
        time.sleep(1)
        empresa_input.send_keys(empresa_nome)
        buscar_button = self.driver.find_element(By.ID, "search0")
        buscar_button.click()
        time.sleep(1)
        s_empresa = self.driver.find_element(By.ID, "Row1Col0")
        s_empresa.click()
        time.sleep(1)

class GrupoPage:
    def __init__(self, driver):
        self.driver = driver

    def selecionar_grupo(self, nome_grupo):
        b_grupo = self.driver.find_element(By.NAME, "/ServiceProvider/Members/")
        b_grupo.click()
        time.sleep(1)
        buscar = self.driver.find_element(By.ID, "search0")
        buscar.click()
        time.sleep(1)
        s_grupo = self.driver.find_element(By.ID, "Row1Col0")
        s_grupo.click()
        time.sleep(1)
        
class UsuariosPage:
    def __init__(self, driver):
        self.driver = driver

    def sel_pagina_usuarios(self):
        b_usuarios = self.driver.find_element(By.NAME, "/Group/Members/")
        b_usuarios.click()

    def buscar_usuarios_por_regiao(self, regiao_prefixo):
        reg = self.driver.find_element(By.ID, "findValue0")
        reg.click()
        time.sleep(1)
        reg.send_keys(regiao_prefixo)
        buscar = self.driver.find_element(By.ID, "search0")
        buscar.click()
        time.sleep(1)
        # Aqui você pode implementar um loop para iterar sobre os usuários encontrados
        # e realizar as ações desejadas em cada um deles. 
 
class SelecionarUsuario:
    def __init__(self, driver):
        self.driver = driver
    
    def sel_usuario(self, usuario_numero):     
        user_id = f"Row{usuario_numero}Col0"
        b_usuarios = self.driver.find_element(By.ID, user_id)
        b_usuarios.click()
        time.sleep(1) 
        
class PolProcChamadasPage:
    def __init__(self, driver):
        self.driver = driver

    def configurar_politica_chamadas(self):
        b_politica_chamadas = self.driver.find_element(By.NAME, "/User/CallProcessingPolicy/")
        b_politica_chamadas.click()
        time.sleep(1)
        flag_1 = self.driver.find_element(By.NAME, "useUserClidSetting")
        flag_1.click()
        time.sleep(1)
        flag_2 = self.driver.find_elements(By.NAME, "clidPolicy")
        if len(flag_2) >= 2:
            flag_2[1].click()
            time.sleep(1)
        ok = self.driver.find_element(By.NAME, "ok")
        ok.click()
        time.sleep(1)   
        
class PerfilUsuarioPage:
    def __init__(self, driver):
        self.driver = driver

    def configurar_perfil_usuario(self, telefone_saida):
        p_usuarios = self.driver.find_element(By.NAME, "/User/Profile/")
        p_usuarios.click()
        time.sleep(1)
        Telefone_saida = self.driver.find_element(By.ID, "clidPhone")
        Telefone_saida.click()
        time.sleep(1)
        Telefone_saida.send_keys(telefone_saida)
        ok = self.driver.find_element(By.NAME, "ok")
        ok.click()
        time.sleep(1)
        
class RetornoUsuario:
    def __init__(self, driver):
        self.driver = driver
    
    def retornar_usuario(self):        
        u_retorno = self.driver.find_elements(By.CLASS_NAME, "headerAuthLevelLink")
        if len(u_retorno) >= 4:
            u_retorno[3].click()
            time.sleep(1)


#Fim Classes

# Inicialize a automação
automacao = AutomacaoWeb()
automacao.fazer_login("", "")

# Página de seleção de empresa
empresa_page = EmpresaPage(automacao.driver)
empresa_page.selecionar_empresa("EMP_GOVERNO_MINAS")

# Página de seleção de grupo (vazio)
grupo_page = GrupoPage(automacao.driver)
grupo_page.selecionar_grupo("")

# Página de usuários
usuarios_page = UsuariosPage(automacao.driver)
usuarios_page.sel_pagina_usuarios()
time.sleep(1)
usuarios_page.buscar_usuarios_por_regiao("323301")

# Inicie um loop para iterar pelos usuários
usuario_numero = 1

# Crie instâncias das classes fora do loop
pol_chamadas_page = PolProcChamadasPage(automacao.driver)
perfil_usuario_page = PerfilUsuarioPage(automacao.driver)
retorno_usuario_instancia = RetornoUsuario(automacao.driver)

while True:
    # Execute as ações específicas para cada usuário
    sel_usuario = SelecionarUsuario(automacao.driver)
    sel_usuario.sel_usuario(usuario_numero)
    pol_chamadas_page.configurar_politica_chamadas()
    perfil_usuario_page.configurar_perfil_usuario("3231120648")
    
    time.sleep(1)

    retorno_usuario_instancia.retornar_usuario()
    
    time.sleep(1)
        
    usuarios_page.buscar_usuarios_por_regiao("323301")
     
    time.sleep(1)
    # Verifique se há mais páginas de usuários
    usuario_numero += 1
    next_user_id = f"Row{usuario_numero}Col0"
    next_user = automacao.driver.find_elements(By.ID, next_user_id)
    
    if not next_user:
        # Se não houver mais usuários, saia do loop
        break

# Feche o navegador quando o loop terminar
automacao.fechar_nav()