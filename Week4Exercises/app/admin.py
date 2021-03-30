from flask import Blueprint, render_template, request, redirect, abort, current_app

admin = Blueprint('admin', __name__)


@admin.route("/admin", methods=["GET"])
def admin_home():
    if not current_app.db.is_admin(request):
        abort(403, description="Wooow, chill down. No access on here.")
    return render_template("admin.html", user="admin")


@admin.route("/admin/top-secret", methods=["GET"])
def view_content():
    if not current_app.db.is_admin(request):
        abort(403, description="Wooow, chill down. No access on here.")
    return '"Every secret creates a potential failure point." — Bruce Schneier'
