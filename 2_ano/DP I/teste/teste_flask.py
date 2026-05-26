app = Flask(__name__)

@app.route("/")
def hello_world():
    return '''<h1>Hello World</h1>
<p>Teste de coisa q n vou entender agr nem a pau</p>
<p>até q n deu ruim n</p>'''

#Uso do escape:
@app.route("/hello")
def hello():
    name = request.args.get("name", "Flask")
    #escape aqui,deve pegar a variável "nome"
    return f'''Hello, {escape(name)}!'''
#Ajuda em algum tipo de rendenização por texto para 
# caso algo que não deva ser mostrado ao usuário seja inserido, 
# de modo que esse "Hello" não vai ser mostrado como texto em si. 
# Ele roda em texto ao invés de parecer ao usuário.
#----------------------------------------------------------------------------
# É util como no exemplo abaixo:
#'def show_user_profile(username):
    # isso mostra a def como 'perfil' ao invés de texto (que seria um bug)
    #return f'User {escape(username)}'
#----------------------------------------------------------------------------
# Marcrar seções URL: (podendo usar nome de variável como chave principal para isso os tipos de conversão abaixo do exemplo)
@app.route('/user/<username>')
def show_user_profile(username):
    # exemplo 'profile'
    return f'User {escape(username)}' # Estes returns serão as páginas web(?).

@app.route('/post/<int:post_id>') 
# O artributo aprsentado em "@app.route('...')" é oq identifica o 'clique' do usuário, redirecionando o URL.
def show_post(post_id):
    # mostra algo com o id fornecido (definido especificamente à ele)
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # mostra o subcaminho após o caminho principal
    return f'Subpath {escape(subpath)}'
#----------------------------------------------------------------------------
#!!!string ---> aceita qualquer texto sem "quebra"                          |
#   int ---> aceita inteiros positivos                                      |
#   float ---> aceita valores de ponto flutuante positivos                  |
#   uuid ---> aceita strings UUID                                           |
#   path ---> funciona com string mas també aceita "quebras"(/ ou \)!!!     |
#----------------------------------------------------------------------------
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
# Atenção aos '/' pois assim como o caminho de um file tê-lo ou não pode gerar erro 404.
# !!!! MONTAR URL ----------------------------------------------------------------------------!!!
    # Usa "url_for('...')":
@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='Mário'))
''' 
Gera algo como: 
/
/login
/login?next=/
/user/John%20Doe
'''
# Importante ter concordância com métodos HTTP/HTTPS (GET, POST)