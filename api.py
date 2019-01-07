from bottle import jinja2_view, route, run, request

@route('/<cadastro>')
@jinja2_view('views/cadastro.html')
def cadastro(cadastro):
    return dict(nome=cadastro)

run(port=8080)