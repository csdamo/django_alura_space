# Django Alura Space
![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=status&message=em%20desenvolvimento&color=GREEN&style=flat)

Página web que permite que usuários publiquem fotos sobre o espaço e possam ver quais são as imagens mais visualizadas e as mais apreciadas pela comunidade de entusiastas de astronomia. As fotos ficam disponíveis em uma galeria que pode ser acessada por usuários cadastrados.

| :placard: Vitrine.Dev |     |
| -------------  | --- |
| :sparkles: Nome        | **django_alura_space**
| :label: Tecnologias | python, django, html, css
| :fire: Desafio     | https://cursos.alura.com.br/formacao-django
<!-- | :rocket: URL         | https://url-deploy.com.br  -->

![image](https://user-images.githubusercontent.com/64370426/220473926-7cd43a1c-ad77-4a47-9da4-30b3c92509c7.png)#vitrinedev)


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
>**Nota:** Essas melhorias podem ser diferentes das orientadas na Formação de Django da Alura. Se você está seguindo os pasos do curso, você deve buscar o repositório indicado pelo instrutor.

### Usuários
* Filtro do menu com acesso restrito aos usuários logados
* Link para acesso direto ao admin para usuários que tem permissão de acesso

### Galeria
* Exibição das tags na página principal de forma dinâmica: foi criado uma tabela no banco de dados para cadastrar as categorias possíveis, que corresponem às tags da página principal.
* As categorias (ou tags) passam a ser relacionadas às fotografias atrávés de um campo tipo chave estrangeira.
* As imagens podem ser filtradas pelas tags, basta clicar sobre a ela.
* São exibidas, na galeria e no detalhe da imagem, a quantidade de usuários que favoritaram e quantidade de visualizações da fotografia.
* Foi criado um campo de "ManyToMany" no model de "Fotografia", para criar uma relação de "muitos para muitos" entre usuários e fotografias, para representar as imagens "favoritas" do usuário

```python
class Fotografia(models.Model):
      
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=True)
    usuario = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=False, related_name='user')
    categoria = models.ForeignKey(to=Categoria, on_delete=models.PROTECT, null=True, blank=True)   
    favorito = models.ManyToManyField(User)
    total_favoritos = models.PositiveIntegerField(default=0)
    total_visualizacoes = models.PositiveIntegerField(default=0)
        
    def __str__(self):
        return self.nome
```
```python

def favorito(request, foto_id):
    user_id = request.user.id
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    favorito = fotografia.favorito.filter(user=user_id)
    total_favoritos = fotografia.total_favoritos
    
    if favorito:
       fotografia.favorito.remove(user_id)
       fotografia.total_favoritos = int(total_favoritos) - 1
    else:
        fotografia.favorito.add(user_id)
        fotografia.total_favoritos = int(total_favoritos) + 1
    fotografia.save()
    return redirect ('index')

```

* O usuário pode favoritar a imagem (um ícone de coração ficará alterado quando a imagem for curtida).
* Pode ver as suas fotos favoritas.
* Pode ver o ranque das imagens mais favoritadas.
* Cada vez que um usuário entra no detalhe da imagem, é adicionada uma visualização à fotografia
* O usuário pode ver quais são as imagens mais visualizadas

## Estrutura de dados

![image](https://user-images.githubusercontent.com/64370426/220458310-8de78c90-865c-4b09-9c9d-37ec9eb84024.png)
> Alguns campos da tabela de usuário não foram detalhados aqui. Esta tabela corresponde a tabela criada pelo Django para controle de usuários do sistema


## Principais tecnologias utilizadas
![django](https://user-images.githubusercontent.com/64370426/220480498-fc7293ed-912d-4cbd-82cf-14b621b883c9.png)   ![Python](https://user-images.githubusercontent.com/64370426/220479830-4eadb646-5a5f-4e98-822f-f08531868fcf.png)   ![SQLite370 svg](https://user-images.githubusercontent.com/64370426/220480506-74805175-d11a-4166-b0c8-262d56b7c65d.png)






## Como instalar o projeto na sua máquina:

### Requisitos:
* Instalação do Python (a partir da versão 3.9)
> https://www.python.org/

* Instalação do Git
> https://git-scm.com/book/pt-br/v2/Come%C3%A7ando-Instalando-o-Git


### Clonando projeto para máquina local:

* Criar repositório onde será mantido o projeto e posicione-se, via terminal, dentro dele. 
* Rode o comando
```
git clone https://github.com/csdamo/django_alura_space.git
```

### Criando ambiente virtual de desenvolvimento:

* No prompt de comando, executar o comando
```
pip install virtualenv
```

* Pelo prompt, vá até o diretório do projeto e execute o comando a seguir. Será criada uma pasta dentro do repositório com o nome "venv"
```
virtualenv venv
``` 
* Ative o ambiente virtual de desenvolvimento: ainda no prompt de comando (dentro do repositório do projeto) execute o comando
```
venv/Scripts/activate 
```
(Windows) 
```
source venv/bin/activate
```
(Linux) 

* Para você saber se o ambiente virtual foi ativado, perceba se antes do caminho do seu diretório, aparece o nome do ambiente entre parênteses. 
> Ex.: (venv) C:\Users\seunome\desenv\django_alura_space>


### Instalando bibliotecas

* Dentro do ambiente virtual, para instalar as bibliotecas na versão correta para o projeto , rodar o comando
```
pip install -r requirements.txt
```


### Criando Banco de dados e testando aplicação
* Teste a aplicação subindo o servidor: ainda com o seu ambiente virtual ativado, rode o comando ```python .\manage.py runserver```. Você deverá ver a mensagem:

![image](https://user-images.githubusercontent.com/64370426/220436468-d19f26a5-378a-4256-830e-42903878e22b.png)
* Saia do servidor apertando ```Ctrl``` + ```c``` para voltar para a linha de comando.
* Certifique-se de que continua com o ambiente virtual ativado, e rode o comando a seguir para riar obanco de dados e as tabelas necessárias para o projeto
```
python .\manage.py migrate
```

* Atualmente, não há uma interface personalizada para que qualquer usuário possa publicar suas fotos, sendo assim, isso deverá ser feito pelo console do admin. Para isso, crie um superusuário através do comando 
```
python .\manage.py createsuperuser
```
* Informe seu nome de usuário, e-mail (opcional) e senha.
* Agora, suba o servidor novamente (```python .\manage.py runserver```) e vá até o seu navegador e coloque o endereço: http://127.0.0.1:8000/admin. Você será direcionado para uma página de login.
* Com isso, você já pode cadastrar suas fotos e ver o resultado na página principal: http://127.0.0.1:8000
