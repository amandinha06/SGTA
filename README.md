# SGTA - Sistema de Gerenciamento de Tarefas Acadêmicas

Projeto desenvolvido na disciplina **Laboratório de Programação Backend**.

O objetivo do sistema é permitir o gerenciamento de tarefas acadêmicas, onde alunos podem criar e acompanhar suas tarefas e professores podem atribuir atividades.

---

# Tecnologias Utilizadas

- Python
- Django
- Django REST Framework
- PostgreSQL
- Docker
- Git

---

# Estrutura do Projeto
sgta/
│
├── backend/
│ ├── config/
│ ├── tarefas/
│ ├── manage.py
│ └── requirements.txt
│
├── docker/
│ └── postgres/
│
├── docker-compose.yml
├── README.md
└── .gitignore

# ⚙️ Funcionalidades
Cadastro de usuários
Gerenciamento de tarefas
Atualização de tarefas
Exclusão de tarefas
Controle e organização das atividades
Interface administrativa do Django

# 🐳 Executando com Docker

Pré-requisitos
Docker Desktop
Docker Compose

Clonar o repositório
git clone https://github.com/amandinha06/SGTA.git
cd SGTA

Subir os containers
docker compose up --

Executar as migrações
Em outro terminal:

docker compose exec web python manage.py migrate

Criar usuário administrador
docker compose exec web python manage.py createsuperuser
Acessar a aplicação

Sistema:

http://localhost:8000

Painel administrativo:

http://localhost:8000/admin

# 🗄️ Banco de Dados

O projeto utiliza PostgreSQL como banco de dados principal, executado em um container Docker.

Configuração padrão:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sgta_db',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': '5432',
    }
}
