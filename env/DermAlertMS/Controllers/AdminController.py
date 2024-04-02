from flask import Blueprint

admin = Blueprint("admin", __name__)

@admin.route("/")
def endpoint1_index():
  return "index.html"
