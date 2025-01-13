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

dia 09/01
https://www.notion.so/Dia-09-01-e-Django-176bc5c3824d8017ae50cce6f8a13bec

Hoje vimos sobre o método request, que é da função django.shortcuts, ele tem
como papel renderizar a nossa pagina web, recebendo um request(parâmetro) e um
html, ele também pode renderizar CSS.
A variável TEMPLATE, por padrão nos permite criar templates em nossos apps, 
facilitando a forma de caminho entre as views e eles, ela também aceita que nós 
criemos uma base BASE_DIR / "base", onde fica a base da programação. Sempre que 
criarmos um app, já é recomendável que nos instalamos ele em INSTALLED_APPS. em
project/settings.py, o nome de cada app é dado através apps.py(dentro do app), 
ele nos retorna um name, e este name é introduzido lá. Conseguimos evitar 
colisões de nome usando o NAME_SPACE(uma pasta dentro da outra, em app, esta sub
pasta tem que estar criada em templates e dentro de templates ela tem que ter 
o mesmo nome do app ex; home/template/"home"). Conseguimos também re-aproveitar
partes do código com o include, que é uma função do djangohtml. Vimos também o 
block que retorna um texto. Vimos também o extends, que herda coisa de uma SUPER
HTML KKKKKKKK

dia 10/01
https://www.notion.so/10-01-and-django-177bc5c3824d804290c3ef96e31a82ed

Hoje vimos sobre os arquivos estáticos, como usar eles de maneira mais simples
hora de importação, eles são pré-definidos no settings, podendo ser alterados,
static, é um app que ja vem por padrão do django, onde ele tem o feito de 
fazer essa importação de maneira estática. Vimos também os contextos em views,
que são voltados a usar dicionários com seus valores de maneira mais dinâmica 
e claro, utilizando-se muito da chave, para fazer a sua execução; {{ chave }},
são muitos usados em textos, e títulos ou até mesmo algo que possa ser repassado. 
Vimos também sobre as url's dinâmicas, que também são muito parecidas com contexto,
dando a liberdade de serem passados como um nome para as urlspatterns de cada app
assim fazendo um melhor uso dinâmico, podendo repassar e alterar de forma automática,
elas também aceitam name_space; app_name = blog 
a href" url "blog:blog",
lembrando que sempre temos que colocar o nome do name_space igual do app, que ele
reside. 
load static; importa itens com mais dinamismo.
context; podem ser feitos em corpos de dict, ou até mesmo em variável
{{}}; executa a chave do contexto.
{% url "blog:exemplo" %}; utiliza as url's de maneira mais dinâmica.

dia 12/01
https://www.notion.so/12-01-Django-179bc5c3824d80beb64ff16f72421ece

Resumo da opera;
Template são view engines que podem ter os seus comandos, como rotulações ejs;
Comparando em sí com o  para o 
Model View Template:
  Em python: Model; modela os dados.
  View; controla as execuções de cada rota.
  Template; parte visualizadora e estática, podendo definir condicionais. 
Model View Controller:
  Em JavaScript:
  Model; modela os dados
  View; parte visualizadora e estática, podendo definir condicionais.
  controller: contra as execuções de cada rota.
Em base o django tem a sua propria view engine, e o JS tem o seu, sem precisar 
alterar de View para Template.
Include não precisa de uma execução, ao chamar ele, ele ja se executa,.
Quando formos fazer importação de algo, precisamos passar o caminho completo em
django.
Podemos fazer for em django, lembrando que ele precisa de um corpo no começo e 
no fim, assim como o if.
Quando nos utilizamos o context, facilita para pegar chaves.
Corpo de uma condicional pode ter o primeiro if e if's, elif e else dentro dela.
