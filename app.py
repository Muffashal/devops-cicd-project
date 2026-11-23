from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Welcome to My DevOps Project!</h1>
    <h2>CI/CD Pipeline Using Jenkins and Docker</h2>
    <p>Application is running successfully!</p>
    """

@app.route('/health')
def health():
    return {"status": "healthy"}

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
