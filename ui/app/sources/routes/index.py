"""

Initial page API

"""

# Importing packages and modules
from flask import (
    render_template,
    Blueprint,
    session,
    redirect,
    url_for
)

# Setting the API blueprint
index_bp = Blueprint("routes_index", __name__)

# Rendering the login page
@index_bp.route("/")
def index():
    if "active_user" in session:
        if session["active_user"]:
            return render_template("index.html")
    return redirect(url_for("routes_login.login"))