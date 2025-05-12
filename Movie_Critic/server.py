from flask_app import app

# Imports from the controller
from flask_app.controllers import Users , Reviews


if __name__ == "__main__":
    app.run(debug=True)