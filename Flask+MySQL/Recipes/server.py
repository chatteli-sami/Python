from recipes_app import app
from recipes_app.controllers import users, recipes

if __name__ == '__main__':
    app.run(debug=True)