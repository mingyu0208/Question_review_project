from flask import Blueprint, url_for
from werkzeug.utils import redirect
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/') #에너테이션 함수
def index(): #라우터 함수
    return redirect(url_for('question._list'))


