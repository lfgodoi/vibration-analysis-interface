"""

Main file

"""

# Importing packages and modules
import os
from flask import Flask
from sources.routes.login import login_bp
from sources.routes.index import index_bp

# Setting the app
template_folder = os.path.abspath('./sources/templates/pages')
app = Flask(__name__, template_folder=template_folder)
app.config["SECRET_KEY"] = "mYkEy"
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Registering routes
app.register_blueprint(login_bp)
app.register_blueprint(index_bp)

# Running the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)