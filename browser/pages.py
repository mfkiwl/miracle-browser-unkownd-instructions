
"""
This module is responsible for simple static pages with no dynamic content.
"""

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for,
    current_app
)

bp = Blueprint('pages', __name__)

@bp.route("/")
def index():

    return render_template(
        "index.html",
        git_commit=current_app.config["GIT_COMMIT"]
    )


