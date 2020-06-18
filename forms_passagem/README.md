### Como faço para executar?

- Primeiro de tudo, certifique que há instalado em sua máquina:
  - Python 3
  - PostgreSQL

- Crie um ambiente virtual:
  - python3 -m venv .venv
- Instale as dependências:
  - pip install -r requirements.txt
  
- Vá até a pasta do projeto e modifique o arquivo de configurações, colocando o nome do seu banco e suas credenciais.

- Execute as migrations dos aplicativos na raiz do projeto:
  - python3 manage.py makemagrations nome_do_app
  - python3 migrate
- Execute o servidor e seja feliz: python3 manage.py runserver
