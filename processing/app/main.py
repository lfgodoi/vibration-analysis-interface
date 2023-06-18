"""

Main file

"""

# Importing packages and modules
from flask import Flask

# Setting the app
app = Flask(__name__)
app.config["SECRET_KEY"] = "VAIpRoCeSsInG"

# Running the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)