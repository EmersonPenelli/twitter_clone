# Documentação da API - Clone Twitter 🕊️

* Autor: Analice Leite
* Versão: 1.0
* Data: 30-10-2024

## Descrição da API ⚙️

Este projeto é uma API desenvolvida com Django Rest Framework que replica funcionalidades de uma rede social similar ao Twitter. A aplicação fornece endpoints para gerenciar usuários, seguidores, notificações e tweets, com autenticação de usuário e uma interface administrativa para gerenciamento. A API foi projetada para ser escalável e fácil de usar, permitindo integrações futuras.

## Estrutura dos Endpoints 🧱

Os endpoints estão divididos em duas categorias principais:

1. **Administração**: Rota `/admin/` para acessar o Django Admin, gerenciar grupos e permissões.
2. **API Pública**: Rota `/api/` para as principais operações CRUD (Criar, Ler, Atualizar, Excluir) nos módulos `follows`, `notifications`, `tweets`, e `users`.

## 1. Administração 🧑‍💼

### Objetivo 

A área administrativa é acessível apenas para usuários autorizados e fornece uma interface para gerenciar os dados e permissões da aplicação.

### Endpoints Detalhados 

- `/admin/`: Página principal da administração.
- `/admin/auth/group/`: Visualizar e gerenciar grupos de usuários.
    - **Métodos**: `GET` (lista) e `POST` (adicionar grupo).
- `/admin/auth/user/`: Visualizar e gerenciar usuários.
    - **Métodos**: `GET` (lista), `POST` (adicionar), `DELETE` (excluir), e `PUT/PATCH` (atualizar usuário).
- `/admin/logout/`: Logout do usuário administrativo autenticado.
- `/admin/password_change/`: Troca de senha do usuário autenticado no painel administrativo.

Esses endpoints incluem ainda detalhes para alterações, históricos de usuários e visualizações específicas para gerenciamento avançado.

## 2. API Pública (`/api/`) 🔓

Cada endpoint é gerenciado por ViewSets que realizam o CRUD dos dados. Os endpoints suportam o uso de formatos adicionais (`<format>`) como `.json` ou `.xml`.

### Endpoints e Modelos 

1. **Follows (`/api/follows/`)**
    
    - **Objetivo**: Gerencia as relações de seguidores entre usuários.
    - **Endpoints**:
        - `/api/follows/`: Lista e criação de relações de seguimento.
            - **Métodos**: `GET` para listar e `POST` para criar um novo seguimento.
        - `/api/follows/<pk>/`: Detalhes de uma relação específica.
            - **Métodos**: `GET`, `PUT/PATCH` (atualizar), `DELETE` (remover).
            
1. **Notifications (`/api/notifications/`)**
    
    - **Objetivo**: Gerencia notificações, permitindo que usuários vejam atualizações de interesse, como novos seguidores ou menções.
    - **Endpoints**:
        - `/api/notifications/`: Lista e criação de notificações.
            - **Métodos**: `GET` (listar notificações), `POST` (criar notificação).
        - `/api/notifications/<pk>/`: Acessa uma notificação específica.
            - **Métodos**: `GET`, `PUT/PATCH`, `DELETE`.
            
1. **Tweets (`/api/tweets/`)**
    
    - **Objetivo**: Gerencia tweets, fornecendo opções para criação, visualização, atualização e exclusão.
    - **Endpoints**:
        - `/api/tweets/`: Lista de tweets e criação de novos tweets.
            - **Métodos**: `GET` (listar todos os tweets), `POST` (criar um novo tweet).
        - `/api/tweets/<pk>/`: Detalhes de um tweet específico.
            - **Métodos**: `GET` (detalhes do tweet), `PUT/PATCH` (atualizar tweet), `DELETE` (excluir tweet).
            
1. **Users (`/api/users/`)**
    
    - **Objetivo**: Gerencia os perfis de usuários, incluindo a visualização de detalhes do usuário e operações de edição.
    - **Endpoints**:
        - `/api/users/`: Lista todos os usuários e permite a criação de novos perfis.
            - **Métodos**: `GET` para listar e `POST` para registrar um novo usuário.
        - `/api/users/<pk>/`: Detalhes de um usuário específico.
            - **Métodos**: `GET`, `PUT/PATCH`, `DELETE`.
            
## 3. Fluxo de Autenticação e Autorização 🔐

A aplicação utiliza autenticação baseada em tokens ou sessão para assegurar que apenas usuários autenticados possam acessar determinadas informações e funcionalidades.

1. **Usuários**: Podem realizar operações de login e gerenciar seus perfis, tweets, e seguidores.
2. **Permissões de Acesso**: Determinados endpoints, especialmente no painel administrativo, são restritos a usuários com permissões de superusuário.

## 4. Testes Automatizados 🚀

A aplicação inclui testes unitários e de integração para assegurar o funcionamento adequado das funcionalidades principais:

- **Testes de Modelos**: Verificação das relações e integridade dos modelos `User`, `Tweet`, `Follow`, e `Notification`.
- **Testes de Serializers**: Garantir que os dados de entrada e saída estejam corretos e formatados.
- **Testes de Views e Endpoints**: Validar o comportamento dos endpoints para ações CRUD e o retorno de respostas HTTP apropriadas.

Para rodar os testes utilize o comando:

```shell
poetry run python manage.py test
```

Para detalhes de configuração do ambiente consulte o passo 6.
## 5. Tecnologias Utilizadas 👩‍💻

A aplicação foi construída com um conjunto de ferramentas e bibliotecas modernas que garantem sua robustez, escalabilidade e facilidade de manutenção:

- **Poetry**: Gerenciador de dependências e ferramenta de empacotamento para projetos Python, simplificando a instalação e gerenciamento de bibliotecas.
- **Django 5.1.2**: Framework web em Python usado para desenvolver a API.
- **Django Rest Framework 3.15.2**: Framework poderoso para construção de APIs em Django, facilitando a criação dos endpoints.
- **django-cors-headers 4.6.0**: Middleware para lidar com o compartilhamento de recursos entre origens diferentes (CORS), permitindo que a API seja acessada de outras origens.
- **django-debug-toolbar 4.4.6**: Ferramenta de depuração que ajuda no desenvolvimento, exibindo informações detalhadas sobre as requisições.
- **django-extensions 3.2.3**: Coleção de ferramentas e extensões para Django, facilitando tarefas de desenvolvimento.
- **Pillow 11.0.0**: Biblioteca de manipulação de imagens usada para processamento de mídia.
- **psycopg2-binary 2.9.10**: Adaptador de banco de dados PostgreSQL para Python, essencial para conectar a API ao banco de dados PostgreSQL.
- **pytest 8.3.3**: Ferramenta de testes em Python, usada aqui para testar a aplicação, garantindo que cada funcionalidade opere conforme esperado.

## 6. Configuração do Ambiente 💻

### 1. Clonar o Repositório

Abra seu terminal e execute o seguinte comando para clonar o repositório:

```shell
git clone https://github.com/analiceleite/twitter_clone.git
```
### 2. Navegar para o Diretório do Projeto

Entre no diretório do projeto:

```shell
cd twitter_clone
```
### 3. Iniciar o Docker

Certifique-se de ter o **Docker** e o **Docker Compose** instalados em seu sistema. Se ainda não tiver, você pode encontrar as instruções de instalação na documentação oficial do Docker.

Agora, inicie o banco de dados usando o `docker-compose`:

```shell
docker-compose up -d
```

Este comando levantará os serviços definidos no arquivo `docker-compose.yml`, incluindo o banco de dados PostgreSQL.
### 4. Instalar Dependências

Certifique-se de ter o **Poetry** instalado em seu sistema. Se ainda não tiver, você pode instalá-lo com:

```shell
curl -sSL https://install.python-poetry.org | python3 -
```

Agora, instale as dependências do projeto com o Poetry:

```shell
poetry install
```
### 5. Configurar o Banco de Dados

Antes de rodar o projeto, você pode precisar configurar o banco de dados. Crie as migrações e aplique-as:

```shell
poetry run python manage.py makemigrations 

poetry run python manage.py migrate
```

- **`makemigrations`**: Cria as migrações com base nas alterações feitas nos modelos.
- **`migrate`**: Aplica as migrações ao banco de dados.
### 6. Criar um Superusuário (Opcional)

Se você precisar acessar a área administrativa, crie um superusuário:

```shell
poetry run python manage.py createsuperuser
```
### 7. Rodar o Servidor 

Agora você pode rodar o servidor de desenvolvimento:

```shell
poetry run python manage.py runserver
```

### 8. Acessar a API

Abra seu navegador e acesse a API em:

```shell
http://localhost:8000/api/
```
### 9. Acesso ao Painel Administrativo

Para acessar o painel administrativo, use o URL:

```shell
http://localhost:8000/admin/
```

### 10. Parar os Serviços do Docker

Para parar os serviços em execução no Docker, execute:

```shell
docker-compose down
```

E para parar o servidor Django, pressione `Ctrl + C` no terminal.

## 7. Implementações Adicionais 🚩

- **Uso do Docker**: O ambiente de desenvolvimento utiliza Docker para gerenciar o container do PostgreSQL, facilitando a configuração e manutenção do banco de dados. Planejamos subir tanto o backend quanto o frontend em containers Docker também para garantir consistência.
- **Autenticação**: Implementar autenticação baseada em token para proteger os endpoints `POST`, `PUT` e `DELETE`, garantindo que apenas usuários autenticados possam fazer alterações.
- **Validação**: Adicionar validações nos serializers para garantir que os dados do Twitter estejam corretos antes de serem salvos no banco de dados.
- **Paginação**: Implementar paginação nos endpoints de listagem de tweets, caso a lista cresça significativamente.

## 8. Futuras Implementações ⏳

- **Frontend com React**: A aplicação planeja integrar um frontend em React para fornecer uma experiência de usuário interativa e moderna. O React facilitará a construção de componentes reutilizáveis e a gestão do estado da aplicação, melhorando a eficiência e a responsividade da interface do usuário.

## 9. Contribuições 🔝

Fique a vontade para contribuir, basta abrir um pull request ou uma issue.