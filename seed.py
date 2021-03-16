from models import User, Post, db
from app import app

db.drop_all()
db.create_all()

# Load users


u = User.signup(display_name='tester1',
                    username='tester1',
                    password="password",
                    area="",
                    caption="Hello there1")
                    
u1 = User.signup(display_name='tester2',
                    username='tester2',
                    password="password",
                    area="",
                    caption="what to say?")

u2 = User.signup(display_name='tester3',
                    username='tester3',
                    password="password",
                    area="hawaii",
                    caption="Hello3")

u3 = User.signup(display_name='tester4',
                    username='tester4',
                    password="password",
                    area="alaska",
                    caption="mahalo?!")

u4 = User.signup(display_name='tester5',
                    username='tester5',
                    password="password",
                    area="spain",
                    caption="")



db.session.add(u)
db.session.add(u1)
db.session.add(u2)
db.session.add(u3)
db.session.add(u4)

db.session.commit()


# post seeds
p1 = Post(title="wow", image="https://cdn.getyourguide.com/img/location/5c9f29710b6f9.jpeg/88.jpg", description="test tes test", lat=45.51908164248076, lng=70.01538750541044, created_dt="2021-03-16 10:45:53.875247", place_name="Hawaii", user_id=1)
      
p2 = Post(title="HELLO", image="https://www.usnews.com/dims4/USNEWS/f39e4a7/2147483647/thumbnail/640x420/quality/85/?url=http%3A%2F%2Fmedia.beam.usnews.com%2Fff%2F6d%2Fabb5206e42b4932cf58355abad4b%2F1-intro-iguazu-falls.jpg", description="I DONT HAVE ONE", lat=43.45016050294154, lng=36.88062188041016, created_dt="2021-03-15 10:45:53.875247", place_name="Nevada", user_id=1)
      
p3 = Post(title="TESTING1", image="https://previews.123rf.com/images/carloscastilla/carloscastilla1806/carloscastilla180600098/103664285-nature-scenic-seascape-in-canary-island-travel-adventures-landscape-tenerife-island-scenery-.jpg", description="lorem ipsum blah blah blah", lat=39.50110889948181, lng=20.01538750541044, created_dt="2021-03-10 10:45:53.875247",place_name="Kyunhla, Sagaing, Myanmar", user_id=4)
      
p4 = Post(title="TEST2", image="https://www.10wallpaper.com/wallpaper/medium/1601/Europe_Germany_Sunset_Glow-Travel_scenery_HD_Wallpaper_medium.jpg", description="lorem ipsum blah blah blah", lat=120.51908164248076, lng=32.01538750541044, created_dt="2021-03-2 10:45:53.875247", place_name="Sagaing", user_id=2)
      
p5 = Post(title="TESTIN3", image="https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/screen-shot-2018-07-11-at-5-10-02-pm-1531412351.png", description="lorem ipsum blah blah blah", lat=23.51908164248076, lng=95.01538750541044, created_dt="2021-03-9 10:45:53.875247", place_name="Kyunhla", user_id=3)
      
db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(p4)
db.session.add(p5)

db.session.commit()

