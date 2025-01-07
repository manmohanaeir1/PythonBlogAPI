from flask  import Flask
from routes.BlogRoutes import blog_bp

app = Flask(__name__)
app.register_blueprint(blog_bp)

if __name__ == '__main__':
    app.run(port= 5000, debug= True)
    