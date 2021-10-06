# [SnapSpot](https://snap-spot.herokuapp.com/)

- Users are able to post about sights and scenery they have visited and wish to share with others. 
- They are also able to read other posts from other users. 
- Posts are pinned to a map where the relative location is shared for others to have the opportunity to visit. 
- App has sucessfully deployed onto Heroku and can be view by clicking on the 'SnapShot' header above!

## Features 

- Flask-Login is implemented to allow for session management and making posts.
- User login/authentication is supplemented using bcrypt.
- [MapBox GL JS](https://docs.mapbox.com/mapbox-gl-js/api/) used to display a visual map canvas and pinpoint new posts.
- Database uses SQLAlchemy.

## User flow

- Users start on the landing page where recent and trending(by favorites) posts are displayed.
- Users are able to view the posts but favoriting will require registeration. 
- When user is registered and loggedin, they have the addititional option to make a post. 
- Post page requires users to drag a marker to their desired place and continues onto a form where they are able to add additional information. 
- The explore page shows markers of the location that other users have posted.
- Users are able to edit and delete both their posts or their entire account. 

## API
* [MapBox](https://docs.mapbox.com/help/how-mapbox-works/web-apps/)
  - Requires registeration in order to obtain a mapbox token.

## Tech Stack 
- Made on windows os
- PostgreSQL
- Flask
- JS
