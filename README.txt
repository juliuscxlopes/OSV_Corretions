README.txt
Visão Geral
Este script é projetado para automatizar a manutenção e correção de dados de usuários cadastrados na plataforma OSV (PABX Voice Manager). Ele utiliza a biblioteca Selenium para interagir com a interface web da plataforma, permitindo a automação de tarefas como seleção de empresas, grupos e configuração de perfis de usuários.

Estrutura do Código
O código é dividido em duas partes principais:

Aplicação Flask: Responsável por fornecer uma interface web onde o usuário pode inserir as credenciais de login e outras informações necessárias para iniciar o processo de automação.
Classes de Automação: Implementam a lógica de automação usando o Selenium. Essas classes são utilizadas pela função iniciar_automacao para navegar e executar ações na plataforma OSV.
Classes Principais
AutomacaoWeb: Inicializa o WebDriver do Selenium e faz login na plataforma OSV.
EmpresaPage: Manipula a seleção de empresas dentro da plataforma.
GrupoPage: Manipula a seleção de grupos dentro da empresa selecionada.
UsuariosPage: Gerencia a navegação e busca de usuários dentro do grupo.
SelecionarUsuario: Seleciona usuários específicos para edição.
PolProcChamadasPage: Configura a política de processamento de chamadas para o usuário.
PerfilUsuarioPage: Configura o perfil do usuário, incluindo o número de telefone.
RetornoUsuario: Retorna à lista de usuários após a configuração.
Fluxo de Trabalho
O usuário acessa a interface web (Flask) e insere as credenciais de login, o nome da empresa, grupo, prefixo de usuários, e o número de telefone a ser configurado.
O Flask chama a função iniciar_automacao, que:
Realiza o login na plataforma.
Navega para a empresa e o grupo especificados.
Busca usuários pelo prefixo e aplica configurações de política de chamadas e perfil.
Repetidamente processa usuários em páginas subsequentes até que todos os usuários tenham sido processados.
Dependências
Python: Certifique-se de ter o Python instalado.
Selenium: Biblioteca necessária para a automação de navegação web.
Flask: Utilizado para criar a interface web.
Como Executar
Instale as dependências:


pip install selenium flask
Inicie o servidor Flask:


python <nome_do_seu_script>.py
Acesse a interface web:

Abra o navegador e vá para http://127.0.0.1:5000.
Preencha o formulário:

Insira suas credenciais e as outras informações solicitadas, então clique em "Submit".
Monitoramento:

O script iniciará a automação e exibirá mensagens de progresso no console.
Manutenção e Atualizações
Correções de Erros: Se você encontrar erros como elementos não encontrados (NoSuchElementException), verifique se os seletores dos elementos HTML utilizados no código são válidos e atualize-os conforme necessário.
Novas Funcionalidades: Para adicionar novos fluxos de trabalho, crie novas classes ou métodos dentro das classes existentes para encapsular a nova lógica, seguindo o padrão estabelecido no código.
Observações Finais
Este código é uma ferramenta poderosa para automatizar tarefas repetitivas na plataforma OSV. Certifique-se de testar bem em um ambiente seguro antes de utilizar em produção.