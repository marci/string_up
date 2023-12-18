from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

#In order for this to work, following things are required:
#   flask
#   Flask-SQLAlchemy
#   flask-login
# lots of patience :)