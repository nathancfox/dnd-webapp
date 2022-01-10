from flask import (
    Blueprint, render_template, request
)

bp = Blueprint('blog', __name__)

@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        return(render_template('character/sheet.html'))
    else:
        return(render_template('character/sheet.html'))
