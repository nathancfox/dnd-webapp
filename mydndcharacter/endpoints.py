from flask import (
    Blueprint, render_template, request
)

from .charactersheet import CharacterSheet

import os
import pickle

bp = Blueprint('blog', __name__)

@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        post_sheet = CharacterSheet(dict(request.form))
        with open('sheet.pickle', 'wb') as pf:
            pickle.dump(post_sheet, pf)
        return(render_template('character/sheet.html', sheet=post_sheet))
    else:
        if os.path.exists('sheet.pickle'):
            with open('sheet.pickle', 'rb') as pf:
                get_sheet = pickle.load(pf)
        else:
            get_sheet = CharacterSheet(dict())
        return(render_template('character/sheet.html', sheet=get_sheet))
