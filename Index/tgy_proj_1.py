from flask import Flask, session, redirect, url_for, flash
from flask import request
from flask_bootstrap import Bootstrap
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required,EqualTo,AnyOf
import tushare as ts
def reset_tables():
	origin_html = ts.day_boxoffice()
	origin_html = pd_to_bootstraptabels(origin_html)
	return origin_html
	# html_table = open('D:\\git_repos\\flasktest\\templates\\includes\\_tb1.html', 'w',
	# 	encoding = 'utf-8')
	# html_table.write(origin_html)
	# html_table.close()
def pd_to_bootstraptabels(pdinput):
	raw_html =  '''<table class="table table-hover">
					  <thead>
					  <tr>
					     {}
					  </tr>
					  </thead>
					  <tbody>
					     {}
					  </tbody>
					</table>
					'''
	colNames = pdinput.columns.tolist()
	head_html = ""
	for col in colNames:
		tmp_head = "<th>{}</th>".format(col)
		head_html += tmp_head
	len_pd = len(pdinput)
	body_html = ""
	for row_num in range(len_pd):
		tmp_rowinfo = pdinput.iloc[row_num].tolist()
		tmp_row_html = "<tr> {}</tr>"
		tmp_row_html_core = ""
		for tmp_rowinfo_col in tmp_rowinfo:
			tmp_row_html_core += "<td>{}</td>".format(tmp_rowinfo_col)
		tmp_row_html = tmp_row_html.format(tmp_row_html_core)
		body_html +=tmp_row_html
	raw_html = raw_html.format(head_html, body_html)
	return raw_html

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.update(SECRET_KEY = 'tgy test1')

@app.route('/home', methods = ['get'])
def home_main():
	# html_table = open('D:\\git_repos\\flasktest\\templates\\includes\\_tb1.html', 'w',
	# 	encoding = 'utf-8')
	# html_table.write(" ")
	# html_table.close()
	return render_template('home_page_static.html')

@app.route('/home', methods = ['post'])
def home_main_post():
	# reset_tables()
	origin_html = reset_tables()
	return render_template('home_page_static.html', info = origin_html)

@app.route('/test1')
def test1_web():
	return "<h1> Test1</h1>"

if __name__ == '__main__':
	app.run(host = '127.0.0.1', port = 5000)