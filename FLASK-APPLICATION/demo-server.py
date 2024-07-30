from flask import Flask

app = Flask(__name__)

# This is an example of api

@app.get('/')
def index():
    return 'Hello, Welcome to Python flask Server!'

@app.get('/student/<name>')
def get_student(name):
    return {
        "name": name,
        "http_method": "get",
        "server": "sample get method"
    }

@app.post('/student/<name>')
def post_student(name):
    return {
        "name": name,
        "http_method": "post",
        "server": "sample post method"
    }

@app.put('/student/<name>')
def put_student(name):
    return {
        "name": name,
        "http_method": "put",
        "server": "sample put method"
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
