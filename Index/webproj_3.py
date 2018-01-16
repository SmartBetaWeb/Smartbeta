# 尝试使用echart
from flask import Flask, session, redirect, url_for, flash
from flask import request
from flask_bootstrap import Bootstrap
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required,EqualTo,AnyOf


class NameForm(FlaskForm):
	name = StringField('输入绘图名称', validators=[Required()])
	submit = SubmitField('绘制')

app = Flask(__name__)
Bootstrap(app)
app.config.update(SECRET_KEY='123456')  # 安全key，使用后方可使用warning
@app.route('/test', methods = ['GET', 'POST'])
def home_1():
	form = NameForm()
	if form.validate_on_submit:
		session['name'] = form.name.data
	return render_template('base_new.html',form = form, name = session['name'])

if __name__ == '__main__':
	app.run(host = '127.0.0.1', port = 5000)