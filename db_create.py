from server import db
from model.models import Users

db.drop_all()
db.create_all()
user = Users(username='solly', email='leeh28@dell.com', password="password")
db.session.add(user)
db.session.commit()
