from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

class AutomacaoWeb:
    def __init__(self):
        self.driver = chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=chrome_options)

    def fazer_login(self, username, password):
        url = '' 
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

        empresa_input = self.driver.find_element(By.ID, "findValue0")
        empresa_input.click()

        empresa_input.send_keys(empresa_nome)
        buscar_button = self.driver.find_element(By.ID, "search0")
        buscar_button.click()

        s_empresa = self.driver.find_element(By.ID, "Row1Col0")
        s_empresa.click()
        
class GrupoPage:
    def __init__(self, driver):
        self.driver = driver

    def selecionar_grupo(self, nome_grupo):
        b_grupo = self.driver.find_element(By.NAME, "/ServiceProvider/Members/")
        b_grupo.click()

        buscar = self.driver.find_element(By.ID, "search0")
        buscar.click()

        s_grupo = self.driver.find_element(By.ID, "Row1Col0")
        s_grupo.click()
     
class UsuariosPage:
    def __init__(self, driver):
        self.driver = driver
        self.pagina_atual = 1
        self.usuario_atual = 1

    def sel_pagina_usuarios(self):
        b_usuarios = self.driver.find_element(By.NAME, "/Group/Members/")
        b_usuarios.click()

    def buscar_usuarios_por_regiao(self, regiao_prefixo):
        reg = self.driver.find_element(By.ID, "findValue0")
        reg.click()
        reg.send_keys(regiao_prefixo)
        buscar = self.driver.find_element(By.ID, "search0")
        buscar.click()

    def ir_para_pagina_1(self):
        try:
            prox = self.driver.find_elements(By.CLASS_NAME, "headerLink")
            if len(prox) > 2:
                elemento = prox[23] #Há um erro aqui, quando ele está na segunda tela não pode ser esse codigo. Pois o elemento muda de lado.
                elemento.click()
                self.pagina_atual += 1
                self.usuario_atual = 1
                return True
        except NoSuchElementException:
            return False
        
    def ir_para_proximas_paginas(self):
        try:
            prox = self.driver.find_elements(By.CLASS_NAME, "headerLink")
            if len(prox) > 2:
                elemento = prox[25] #Há um erro aqui, quando ele está na segunda tela não pode ser esse codigo. Pois o elemento muda de lado.
                elemento.click()
                self.pagina_atual += 1
                self.usuario_atual = 1
                return True
        except NoSuchElementException:
            return False

    def encontrar_proximo_usuario(self):
        user_id = f"Row{self.usuario_atual}Col0"
        user = self.driver.find_element(By.ID, user_id)
        self.usuario_atual += 1
        return user
    
class SelecionarUsuario:
    def __init__(self, driver):
        self.driver = driver
    
    def sel_usuario(self, usuario_numero):     
        user_id = f"Row{usuario_numero}Col0"
        b_usuarios = self.driver.find_element(By.ID, user_id)
        b_usuarios.click()
        print(f"usuario em edição é:{usuario_numero}")
       
class PolProcChamadasPage:
    def __init__(self, driver):
        self.driver = driver

    def configurar_politica_chamadas(self):
        b_politica_chamadas = self.driver.find_element(By.NAME, "/User/CallProcessingPolicy/")
        b_politica_chamadas.click()

        flag_1 = self.driver.find_element(By.NAME, "useUserClidSetting")
        flag_1.click()

        flag_2 = self.driver.find_elements(By.NAME, "clidPolicy")
        if len(flag_2) >= 2:
            flag_2[1].click()

        ok = self.driver.find_element(By.NAME, "ok")
        ok.click()
         
class PerfilUsuarioPage:
    def __init__(self, driver):
        self.driver = driver

    def configurar_perfil_usuario(self, telefone_saida):
        p_usuarios = self.driver.find_element(By.NAME, "/User/Profile/")
        p_usuarios.click()

        Telefone_saida = self.driver.find_element(By.ID, "clidPhone")
        Telefone_saida.click()

        if Telefone_saida.get_attribute("value"):
            Telefone_saida.clear()

        Telefone_saida.send_keys(telefone_saida)
        ok = self.driver.find_element(By.NAME, "ok")
        ok.click()
class RetornoUsuario:
    def __init__(self, driver):
        self.driver = driver
    
    def retornar_usuario(self):        
        u_retorno = self.driver.find_elements(By.CLASS_NAME, "headerAuthLevelLink")
        if len(u_retorno) >= 4:
            u_retorno[3].click()
