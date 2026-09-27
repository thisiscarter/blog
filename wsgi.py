from flaskblog import create_app

def app(environ, start_response):
    return create_app()