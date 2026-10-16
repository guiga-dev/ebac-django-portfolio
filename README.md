# Portfólio Django — Setup

Python 3.12 e Django 5.2 LTS. Este primeiro marco preserva a página inicial padrão do Django.

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python manage.py migrate
.venv\Scripts\python manage.py runserver
```

Abra http://127.0.0.1:8000/ para ver a mensagem de instalação concluída. A configuração é exclusivamente de desenvolvimento.

Entrega: branch `Setup`, pull request com base `main`, com a captura `evidencias/setup.jpg` na descrição.

