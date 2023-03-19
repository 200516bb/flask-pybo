#서버 실행 flask run / 가상환경 접속 myproject
from flask import Blueprint, url_for
from werkzeug.utils import redirect

from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    3/0
    return redirect(url_for('question._list'))