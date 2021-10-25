from flask import (Blueprint,flash,g,redirect,render_template,request,url_for)
from werkzeug.exceptions import abort
from flaskr.auth import login_required
from flaskr.db import get_db

bp=Blueprint('Blog',__name__)

@bp.route('/')
def index():
	db=get_db()
	posts=db.execute(
		"""SELECT p.id,p.title,p.body,p.created,p.author_id,u.username
		FROM post p INNER JOIN user u ON p.author_id=u.id
		ORDER BY p.creatd desc """
	).fetchall()
	return render_template('blog/index.html',posts=posts)
