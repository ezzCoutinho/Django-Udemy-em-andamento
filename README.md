# Django-Udemy-em-andamento

dia 07/01
https://www.notion.so/Django-07-01-174bc5c3824d80f7872efdd62f0a043b

Hoje vimos como instala o django e oq é um django e seus aquivos.
Django é um framework, voltado a aplicações web de uma forma geral, sendo
um framework antigo(maduro) e de código aberto, ele tem seus comandos. Precisa
de um ambiente virtal, e comandos para criar as suas dependências
(django-admin startproject nomeDoProjeto), tem suporte a ORM, URL e TEMPLATE.
manage.py, onde definimos as configurações rasas do nosso projeto, ele é quase 
igual ao comando django-admin, só que para dar um runserver no django admin, 
é necessário mexer na settings.py, a settings.py é o coração da nossa aplicação,
desde escolhas de idioma a arquivos estáticos. urls.py é o módulo mãe de urls
do nosso django. wsgi é a interface de comunicação entre o django e o servidor(web)
asgi.py, é uma interface de comunicação entre o django e o servidor(assíncrono). 

dia 08;01 
https://www.notion.so/Dia-08-01-and-Django-175bc5c3824d8050b547e5950b337bfb

Hoje aprendemos a criar um APP, dependendo da APP, podemos usar um APP só, onde
todos as url's são relacionais.
admin.py;
apps.py;
models.py;
tests.py;
views.py;
Aprendemos como funciona a requisição em django,
 oq é V do MVT;
é o viewer, ele comanda oq a resposta vai ser perante a requisição e seus tipos.
Vimos também as urlspatterns, como criar uma url, sem barra no começo e sim no final,
ela espera receber dois elementos, a própria url e a função/classe viewer. Vimos
também como exportar usando o caminho absoluto(path) a nossa viewer de cada app.
Vimos também aninhamento de urls, que precisamos criar uma urls.py, dentro do app
assim ele pode receber "/blog/today". Vimos o método include do django, que nos
ajuda exportar melhor a nossa viewer aninhada.