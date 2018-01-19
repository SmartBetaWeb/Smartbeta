from flask import Flask, session, redirect, url_for, flash
from flask import request
from flask_bootstrap import Bootstrap
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required,EqualTo,AnyOf

class NameForm(FlaskForm):
	name = StringField('用户名', validators=[Required()])
	# pw = PasswordField('密码', validators = [AnyOf(['tian18'], message = '输入密码错误')])
	submit = SubmitField('登录')


app = Flask(__name__)
Bootstrap(app)
app.config.update(SECRET_KEY='123456')  # 安全key，使用后方可使用warning
@app.route('/test', methods = ['GET', 'POST'])
def home_1():
	# print('Start home_1')
	# name = None
	# code = None
	form = NameForm()
	# print(form.name, form.submit,form.validate_on_submit())
	if form.validate_on_submit():
		old_name = session.get('name')
		print(old_name)
		if old_name is not None and old_name != form.name.data:
			print('flash')
			flash('Looks like you have changed your name!')
		session['name'] = form.name.data
		form.name.data = ''
		return redirect(url_for('home_1'))
		# pw = form.pw.data
	return render_template('echart_test1.html', form = form, name = session.get('name'))
if __name__ == '__main__':
	app.run(host = '127.0.0.1', port = 5000)