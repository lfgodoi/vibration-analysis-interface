"""

Login page API

"""

# Importing packages and modules
from flask import (
    render_template,
    Blueprint,
    request,
    session,
    redirect,
    url_for
)

# Setting the API blueprint
login_bp = Blueprint("routes_login", __name__)

# Rendering the login page
@login_bp.route("/login")
def login():
    if "failed" in request.args:
        failed = request.args["failed"]
    else:
        failed = False
    return render_template("login.html", failed=failed)

# User authentication
@login_bp.route("/authenticate", methods=["POST",])
def authenticate():
    if request.form("user") == "username":
        if request.form("password") == "password":
            session["active_user"] = True
            return redirect(url_for("routes_index.index"))
        else:
            session["active_user"] = False
            return redirect(url_for("routes_login.login", failed=True))