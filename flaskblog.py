from flask import Flask, render_template, url_for
from forms import RegistraionForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '93733d55670b2c9ed718ff5a44501a2d' 

posts = [
	{
		"author": "Tim Quiros",
		"title": "Blog Post 1",
		"content": "First post",
		"date_posted": "5/1/2020"
	},
	{
		"author": "Tom Quiros",
		"title": "Blog Post 2",
		"content": "Second post",
		"date_posted": "5/1/2020"
	},
]

@app.route('/')
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/register')
	form = RegistraionForm()

@app.route('/login')
	form = LoginForm()
	return render_template("login.html", title="Login", form=form)

if __name__ == "__main__":
    app.run(debug=True)