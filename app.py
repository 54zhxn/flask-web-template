from app import create_app, db
from app.models import User

app = create_app()
app.app_context().push()

if __name__ == "__main__":
    app.run()

# 赛阿
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}
