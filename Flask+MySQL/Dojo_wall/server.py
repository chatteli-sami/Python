from wall_app import app
from wall_app.controllers import users, posts

if __name__ == '__main__':
    app.run(debug=True)