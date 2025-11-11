from flask import Flask, render_template, request, redirect, url_for
from models import db, Task

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        tasks = Task.query.all()
        return render_template('index.html', tasks=tasks)

    @app.route('/add', methods=['POST'])
    def add():
        title = request.form.get('title')
        if title:
            new_task = Task(title=title)
            db.session.add(new_task)
            db.session.commit()
        return redirect(url_for('index'))

    @app.route('/delete/<int:id>')
    def delete(id):
        task = Task.query.get(id)
        if task:
            db.session.delete(task)
            db.session.commit()
        return redirect(url_for('index'))

    return app


if __name__ == '__main__':
    app = create_app()
    print("Démarrage du serveur Flask")
    app.run(debug=True)
