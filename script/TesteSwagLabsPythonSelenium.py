from selenium import webdriver
from selenium.webdriver.common.by import By

print("Inicializando o WebDriver para o Edge...")
# Inicializar o WebDriver para o Edge
driver = webdriver.Edge()

try:
    print("Abrindo o site do Swag Labs...")
    # Abrir o site do Swag Labs
    driver.get("https://www.saucedemo.com")

    print("Configurando o tamanho da janela do navegador...")
    # Configurar o tamanho da janela
    driver.set_window_size(1024, 768)

    print("Obtendo o título da página de login...")
    # Obter o título da página de login e armazenar na variável 'login_header'
    login_header = driver.title
    print(f"Título armazenado em 'login_header': {login_header}")

    print("Listando os nomes de usuários disponíveis na página...")
    # Simular captura dos nomes de usuários disponíveis
    available_users = [
        "standard_user",
        "locked_out_user",
        "problem_user",
        "performance_glitch_user",
        "visual_user"
    ]
    print("Nomes de usuários disponíveis:")
    for user in available_users:
        print(f"- {user}")

    # Solicitar ao usuário o nome de usuário e a senha dinamicamente
    print("Insira os dados de login.")
    username = input("Nome de usuário: ")
    password = input("Senha: ")

    print("Localizando o campo de nome de usuário...")
    # Localizar o campo de nome de usuário e inserir o valor
    username_field = driver.find_element(By.ID, "user-name")
    print("Inserindo o nome de usuário...")
    username_field.send_keys(username)

    print("Localizando o campo de senha...")
    # Localizar o campo de senha e inserir o valor
    password_field = driver.find_element(By.ID, "password")
    print("Inserindo a senha...")
    password_field.send_keys(password)

    print("Localizando o botão de login...")
    # Localizar o botão de login e clicar nele
    login_button = driver.find_element(By.ID, "login-button")
    print("Clicando no botão de login...")
    login_button.click()

    print("Login efetuado com sucesso (se as credenciais forem válidas).")

    print("Capturando os títulos dos cinco primeiros produtos...")
    product_titles = driver.find_elements(By.CLASS_NAME, "inventory_item_name")

    print("Produtos encontrados (cinco primeiros):")
    displayed_products = [title.text for title in product_titles[:5]]
    for product in displayed_products:
        print(f"- {product}")

    # Exibir todos os dados coletados como saída
    print("\n--- Resumo dos dados retornados ---")
    print(f"Login Header: {login_header}")
    print(f"Nomes de Usuários: {', '.join(available_users)}")
    print("Títulos dos Produtos:")
    for product in displayed_products:
        print(f"- {product}")

finally:
    print("Fechando o navegador...")
    # Fechar o navegador
    driver.quit()
