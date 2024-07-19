import os
from flask import Flask
from productApp.configuration import init_app, db

app = Flask(__name__)
init_app(app)

if __name__ == "__main__":
    from productApp.controllers import productRoute
    app.register_blueprint(productRoute)
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
    with app.app_context():
        db.create_all()
