u = User(name='tester1', username="testerUN", password="testpw1")

p1 = Post(location="california", description="Greate scene here!", user_id="1")


db.session.add(u)
db.session.add(p1)

db.session.commit()