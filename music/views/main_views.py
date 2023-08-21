from flask import Blueprint, render_template, request
from music.models import User, Recommendation, Artist

bp = Blueprint('main', __name__, url_prefix='/')
@bp.route('/')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/loginForm')
def login_form() :
    return render_template('login_form.html')


@bp.route('/login', methods=('POST', ))
def login() :

    form = request.form

    login_id = form['loginid']
    login_pw = form['loginpw']

    user = User.query.filter(User.loginid == login_id).first()
    is_error = False

    msg = ''

    if user == None :
        msg = '잘못된 아이디입니다.'
        is_error = True

    elif user.loginpw != login_pw :
        msg = '잘못된 비밀번호입니다.'
        is_error = True

    if is_error :
        return render_template('error.html', msg=msg)


    # 추천 목록 가져와서 넘겨주기

    rec_list = Recommendation.query.filter(Recommendation.userid == user.userid).all()

    result = []
    for rec in rec_list :
        artist = Artist.query.filter(Artist.artistid == rec.artistid).first()
        result.append(artist)


    return render_template('main.html', user=user, artist_list=result)