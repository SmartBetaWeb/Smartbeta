from flask import Flask,request,render_template, flash
import jinja2
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.secret_key = '123456'
app.config.update(SECRET_KEY='123456')  
# @app.route('/login', methods = ['get'])
# def login_get():
#     return render_template('login.html')

# @app.route("/login",methods=["POST"])
# def loginPost():
# 	username = request.form.get("username","")
# 	password = request.form.get("password","")
# 	print(username, password)
# 	if username=="index" and password=="tgy" :
# 		return "登录成功"
# 	else:
# 		return "登录"+username+password

@app.route("/login",methods=["GET"])
def login():
	return render_template('login.html')
	# html="<form method='post'>" \
	# "<table>" \
	# "<tr><td>请输入用户名</td><td><input type='text' name='username'/></td></tr>" \
	# "<tr><td>请输入密码</td><td><input type='password' name='password'/></td></tr>" \
	# "<tr><td><input type='submit' value='登录'/></td></tr>" \
	# "</table>" \
	# "</post>"
	return html
@app.route("/login",methods=["POST"])
def loginPost():
	print(request.method, request.form)
	username = request.form.get("username","")
	password = request.form.get("password","")
	print(username, password)
	if username=="test" and password=="123" :
		return "登录成功" + username + password
	else:
		flash("输入的用户或密码错误")
		return render_template('login.html')
if __name__ == '__main__':
	app.run(host = '10.6.38.179', port = 5000)