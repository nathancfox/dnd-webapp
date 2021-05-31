from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from mydndcharacter.auth import login_required
from mydndcharacter.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/', methods=('GET', 'POST'))
@login_required
def index():
    if request.method == 'POST':
        return(render_template('character/sheet.html'))
    else:
        return(render_template('character/sheet.html'))