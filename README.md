# django_alura_space

Página web que permite que usuários publiquem fotos sobre o espaço e possam ver quais são as imagens mais visualizadas e as mais apreciadas pela comunidade de entusiastas de astronomia. As fotos ficam disponíveis em uma galeria que pode ser acessada por usuários cadastrados.

| :placard: Vitrine.Dev |     |
| -------------  | --- |
| :sparkles: Nome        | **django_alura_space**
| :label: Tecnologias | python, django, html, css
| :fire: Desafio     | https://cursos.alura.com.br/formacao-django
<!-- | :rocket: URL         | https://url-deploy.com.br  -->

![image](https://user-images.githubusercontent.com/64370426/220421722-29110d3d-e5b1-4cf7-a755-99dee5aa6f70.png#vitrinedev)


## Sobre o Projeto

O projeto **django_alura_space**, como fica evidenciado em seu nome, utiliza como principal tecnologia o framework Django, desenvolvido na linguagem Python. O banco de dados utilizado para persistência dos dados é o SQLite.

A aplicação está sendo desenvolvido durante a Formação em Django da escola de Programação da Alura, que atualmente está disponível até o módulo 3. Conforme o avanço dos estudos na Formação, outras funcionalidades do projeto serão lieradas.


## Funcionalidades desenvolvidas
### Usuários
* Cadastro de usuário
* Login de usuário
* Logout


### Galeria
* Galeria de imagens: no index são exibidas as fotos ordenadas pelo campo 'data_fotografia' e filtradas pelo campo "publicada=True".
* Detalhe: são exibidas mais informações sobre a imagem publicada ao clicar sobre ela.
* Imput de busca: é feito um filtro das imagens que contém a palavra informada na redação do seu nome.

## Melhorias Feitas
>**Nota:** Essas melhorias podem ser diferentes das orientadas na Formação de Django da Alura

### Usuários
* Filtro do menu com acesso restrito aos usuários logados
* Link para acesso direto ao admin para usuários que tem permissão de acesso

### Galeria
* Exibição das tags na página principal de forma dinâmica: foi criado uma tabela no banco de dados para cadastrar as categorias possíveis, que corresponem às tags da página principal.
* As categorias (ou tags) passam a ser relacionadas às fotografias atrávés de um campo tipo chave estrangeira.
* As imagens podem ser filtradas pelas tags, basta clicar sobre a ela.
* São exibidas na galeria e no detalhe das imagens a quantidade de usuários que favoritaram e quantidade de visualizações da fotografia.
* Foi criado um campo de "many_to_many" no model de "Fotografia", para criar uma relação de "muitos para muitos" dos usuários com as fotografias, para representar as imagens "favoritas" do usuário

![image](https://user-images.githubusercontent.com/64370426/220451884-5c09ec89-8622-43d0-9f12-f4d67d092b62.png)

![image](https://user-images.githubusercontent.com/64370426/220452166-0063fc37-ab3d-4654-a9ce-d1e827adc6fb.png)

* O usuário pode favoritar a imagem (um ícone de coração ficará alterado quando a imagem for favoritada).
* Pode ver as suas fotos favoritas.
* Pode ver o ranque das imagens mais favoritadas.
* Cada vez que um usuário entra no detalhe da imagem, é adicionada uma visualização à fotografia
* O usuário pode ver quais são as imagens mais visualizadas

## Como instalar o projeto na sua máquina:

* Para instalar o projeto na sua máquina você deverá ter o Python instalado (site oficial do Python para download: https://www.python.org/).
* Para clonar o projeto a partir deste repositório, você também precisará ter o Git instalado (site do oficial do Git para dowload: https://git-scm.com/).
* Abra o terminar no seu computador e posicione-se dentro do diretório em que você quer manter o projeto.
* Rode o comando ```git clone https://github.com/csdamo/django_alura_space.git ```
* Ainda no terminal, posicione-se entro do diretório do projeto (```cd django_alura_space```) e rode o comando para instalar a biblioteca virtualenv, caso ele ainda não esteja instalada ```pip install virtualenv```.
* Crie um ambiente virtual através do comando ```virtualenv venv``` (o nome do ambiente pode ser qualquer um, mas é recomendado que use o nome padão "venv")
* Ative seu ambiente virtual: ```venv/Scripts/activate``` (Windows) / ```source venv/bin/activate``` (Linux).
* Com o ambiente ativado, rode o comando pip install -r requirements.txt (no arquivo requirements. estão todas as bibliotecas necessárias para rodas o projeto)
* Teste a aplicação subindo o servidor: ainda com o seu ambiente virtual ativado, rode o comando ```python .\manage.py runserver```. Você deverá ver a mensagem:

![image](https://user-images.githubusercontent.com/64370426/220436468-d19f26a5-378a-4256-830e-42903878e22b.png)
* Saia do servidor apertando ```Ctrl``` + ```c``` para voltar para a linha de comando.
* Certifique-se de que continua com o ambiente virtual ativado, e rode o comando ```python .\manage.py migrate```. Isso fará com que um banco de dados seja criado com as tabelas necessárias para o projeto
* Atualmente, não há uma interface personalizada para que qualquer usuário possa publicar suas fotos, sendo assim, isso deverá ser feito pelo console do admin. Para isso, crie um superusuário através do comando ```python .\manage.py createsuperuser```. Informe seu nome de usuário, e-mail (opcional) e senha.
* Agora, suba o servidor novamente (```python .\manage.py runserver```) e vá até o seu navegador e coloque o endereço: http://127.0.0.1:8000/admin. Você será direcionado para uma página de login.
* Com isso, você já pode cadastrar suas fotos e ver o resultado na página principal: http://127.0.0.1:8000
