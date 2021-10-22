from tinydb import TinyDB, Query
from flask import Flask, render_template, redirect

db = TinyDB('db.json')
Todo = Query()
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html', todos=db.all())


@app.route('/add/<todo>/<author>')
def add_todo(author, todo):
	db.insert({
		'todo': todo,
		'author': author
	})
	return redirect('/')


@app.route('/add')
def add():
	return render_template('add.html')


@app.route('/delete/<name>')
def delete(name):
	db.remove(Todo.todo == name)
	return redirect('/')

if __name__ == '__main__':
	app.run(port=8080)
