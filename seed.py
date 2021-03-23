from models import User, Post, Favorite, db
from app import app

db.drop_all()
db.create_all()

# Load users


u = User.signup(display_name='Ken Bork',
                    username='Borknator',
                    password="password",
                    caption="Love dogs.. It's been known in the family.")
                    
u1 = User.signup(display_name='Samantha Meow',
                    username='Meow321',
                    password="password",
                    caption="Please recommend next palce to visit.")

u2 = User.signup(display_name='Johnny Ribbit',
                    username='RibbitJ',
                    password="password",
                    caption="")

u3 = User.signup(display_name='Rebecca Quack',
                    username='DuckGoQ',
                    password="password",
                    caption="Hidden spots?")

u4 = User.signup(display_name='Berry Allen',
                    username='BerryFast',
                    password="password",
                    caption="I'm pretty fast")



db.session.add(u)
db.session.add(u1)
db.session.add(u2)
db.session.add(u3)
db.session.add(u4)

db.session.commit()


# post seeds
p1 = Post(title="This is SPAIN?!", image="https://images.unsplash.com/photo-1509840841025-9088ba78a826?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", lat=38.9196, lng=-2.0507, created_dt="2021-03-16 10:45:53.875247", place_name="Spain", user_id=1)
      
p2 = Post(title="Visted mountains of Croatia", image="https://images.unsplash.com/photo-1536419996793-7a9721c1f1da?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=700&q=80", description="Orci phasellus egestas tellus rutrum tellus pellentesque eu tincidunt tortor. Montes nascetur ridiculus mus mauris vitae ultricies leo integer. Duis tristique sollicitudin nibh sit amet. Nascetur ridiculus mus mauris vitae. Laoreet id donec ultrices tincidunt arcu non sodales neque. Egestas fringilla phasellus faucibus scelerisque eleifend donec pretium vulputate sapien. Quam quisque id diam vel quam. Sapien et ligula ullamcorper malesuada. Morbi tristique senectus et netus et malesuada. Dolor magna eget est lorem ipsum. Dignissim suspendisse in est ante in nibh. Tortor dignissim convallis aenean et. Nisl nunc mi ipsum faucibus vitae. Pic by Taneli Lahtinen on unsplash", lat=45.49171299209354, lng=16.60264488910269, created_dt="2021-03-15 10:45:53.875247", place_name="Croatia", user_id=1)
      
p3 = Post(title="Koreaa life", image="https://images.unsplash.com/photo-1526199119161-4be1e3368d52?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1267&q=80", description="Pic by @thoutbox, unsplash. Orci phasellus egestas tellus rutrum tellus pellentesque eu tincidunt tortor. Montes nascetur ridiculus mus mauris vitae ultricies leo integer. Duis tristique sollicitudin nibh sit amet. Nascetur ridiculus mus mauris vitae. Laoreet id donec ultrices tincidunt arcu non sodales neque. Egestas fringilla phasellus faucibus scelerisque eleifend donec pretium vulputate sapien. Quam quisque id diam vel quam. Sapien et ligula ullamcorper malesuada. Morbi tristique senectus et netus et malesuada. Dolor magna eget est lorem ipsum. Dignissim suspendisse in est ante in nibh. Tortor dignissim convallis aenean et. Nisl nunc mi ipsum faucibus vitae.", lat=35.79967702901689, lng=127.93426816051453, created_dt="2021-03-10 10:45:53.875247",place_name="Korea", user_id=4)
      
p4 = Post(title="Chicagooo", image="https://images.unsplash.com/photo-1579463236360-8bb6a60c0b5f?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80", description=" Pic by Jessica Fadel @ unsplash. Morbi tristique senectus et netus et malesuada. Dolor magna eget est lorem ipsum. Dignissim suspendisse in est ante in nibh. Tortor dignissim convallis aenean et. Nisl nunc mi ipsum faucibus vitae", lat=41.85838327561396, lng=-87.67452436522132, created_dt="2021-03-2 10:45:53.875247", place_name="Chicago,Illinois", user_id=2)
      
p5 = Post(title="Chilhowee Mt.", image="https://images.unsplash.com/photo-1590096598321-a42e180df31d?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=701&q=80", description=" Pic by Mitchell Hartley @ unsplash. Laoreet id donec ultrices tincidunt arcu non sodales neque. Egestas fringilla phasellus faucibus scelerisque eleifend donec pretium vulputate sapien. Quam quisque id diam vel quam. Sapien et ligula ullamcorper malesuada. Morbi tristique senectus et netus et malesuada. Dolor magna eget est lorem ipsum. Dignissim suspendisse in est ante in nibh. Tortor dignissim convallis aenean et. Nisl nunc mi ipsum faucibus vitae.", lat=35.7362657813314, lng=-86.52248546536788, created_dt="2020-03-9 10:45:53.875247", place_name="Chilhowee Mountain, Tennessee, USA", user_id=3)
      
p5 = Post(title="Sheeps. That is all", image="https://images.unsplash.com/photo-1501884742805-c94fc1d8985b?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1351&q=80", description=" Pic by Peter Hammer @ unsplash. Laoreet id donec ultrices tincidunt arcu non sodales neque. Egestas fringilla phasellus faucibus scelerisque eleifend donec pretium vulputate sapien. Quam quisque id diam vel quam. Sapien et ligula ullamcorper malesuada. Morbi tristique senectus et netus et malesuada. Dolor magna eget est lorem ipsum. Dignissim suspendisse in est ante in nibh. Tortor dignissim convallis aenean et. Nisl nunc mi ipsum faucibus vitae.", lat=-44.02278276330103, lng=170.1382899504108, created_dt="2021-03-19 10:45:53.875247", place_name="Lake Tekapo, New Zealand", user_id=1)
      
db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(p4)
db.session.add(p5)

db.session.commit()

# load favs

f1 = Favorite(post_id=5, user_id=1)
f2 = Favorite(post_id=5, user_id=2)
f3 = Favorite(post_id=5, user_id=3)
f4 = Favorite(post_id=2, user_id=4)
f5 = Favorite(post_id=1, user_id=4)
f6 = Favorite(post_id=2, user_id=2)
f7 = Favorite(post_id=1, user_id=4)
f8 = Favorite(post_id=3, user_id=3)

db.session.add(f1)
db.session.add(f2)
db.session.add(f3)
db.session.add(f4)
db.session.add(f5)
db.session.add(f6)
db.session.add(f6)
db.session.add(f8)
db.session.commit()