# Exercício Prático de QA Automatizado com Selenium

## Descrição
Repositório dedicado a um exercício prático de QA automatizado utilizando Selenium WebDriver e Python, com o objetivo de testar funcionalidades do site Swag Labs. Este projeto inclui:
- Captura dinâmica de credenciais.
- Automação do login.
- Validação de elementos da página inicial, como os títulos dos produtos.

## Objetivo
Automatizar os seguintes passos:
1. Acessar o site e capturar os nomes de usuários disponíveis na tela de login.
2. Preencher o formulário de login com credenciais dinâmicas.
3. Obter o título da página de login e armazená-lo na variável login_header.
4. Capturar os títulos dos cinco primeiros produtos exibidos após o login.
5. Retornar como saída os seguintes dados:
    - Nomes de usuários disponíveis.
    - Senha.
    - login_header.
    - Títulos dos cinco primeiros produtos.

## Ferramentas e Tecnologias
- Python 3.13.2: Linguagem utilizada para desenvolver o teste.
- Selenium WebDriver 4.29.0: Biblioteca para automação de navegadores.
- Microsoft Edge: Versão utilizada: 115.0.1901.203.
- WebDriver para Edge: Compatível com a versão do navegador.
- pip 24.3.1: Gerenciador de pacotes Python.

## Como Executar
1. Instale as dependências:
    - Execute o comando abaixo para instalar o Selenium:
      pip install selenium
    - Certifique-se de que o WebDriver para Edge está configurado no PATH do sistema.
2. Execute o script:
    - Salve o arquivo TesteSwagLabsPythonSelenium.py ou main.py no diretório desejado.
    - Navegue até o diretório no terminal e execute: 
      python TesteSwagLabsPythonSelenium.py
      ou
      python main.py
3. Interação durante a execução:
    - Durante a execução, insira o nome de usuário e a senha dinamicamente conforme solicitado.
    - Consulte os nomes de usuários disponíveis no terminal para escolher uma opção.
4. Saída esperada:
    - Título da página de login armazenado como login_header.
    - Lista de nomes de usuários disponíveis.
    - Títulos dos cinco primeiros produtos exibidos após o login.

## Sobre o Arquivo main.py
O script principal para execução do exercício está estruturado no arquivo main.py. Este arquivo contém as funções necessárias para automatizar as etapas descritas no objetivo. Complete as funções em main.py para executar as seguintes tarefas:
- Capturar dinamicamente as credenciais.
- Realizar o login automatizado.
- Validar os elementos da página inicial.

## Observações
Credenciais públicas utilizadas:
  - Nome de Usuário: visual_user (ou outros listados durante a execução).
  - Senha: secret_sauce.
- Erros relacionados ao navegador (e.g., fallback_task_provider.cc) podem aparecer no terminal, mas não afetam a execução do script.
- Este exercício foi implementado para fins didáticos e segue uma abordagem simplificada.



