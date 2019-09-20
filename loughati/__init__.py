from .resources import app
from .resources import model

model.db.init_app(app)

@app.cli.command()
def initdb():
    model.initdb()