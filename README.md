## InstaMe'
This is an instagram clone

## Author
Pauline Wafula

## Description
InstaMe' is a web application that mimics a popular photo app, instagram .This is through creationg posts with caption.A user is able to like and comment on other users post. The can also click one the users profile to follow them and see their posts.A new user can also search for a post  using title.

## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like to:

* Sign in to the application to start using it 
* upload my pictures to the application
* See my profile with all my pictures
* Follow other users and see there pictures on my timeline
* Like a picture and leave a comment on it

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display login form or sign up incase you dont have an account  | **On page load** | Displays the registration form on clicking sign up |
| Displays posts  | **On clicking a 'search' button** | Displays post under the searched title |
| Displays a form to create post | **Click a plus square icon** | add a new post with the image ,title and caption |
| profile page | **On clicking profile** | takes you to the use profile|
|  logout | **On clicking logout** |logs out a user from thhe page|


## SetUp / Installation Requirements
### Prerequisites
* python3.8
* pip
* activate virtual environment
### Cloning
* In your terminal:


        $ git clone https://github.com/paulinenanzala19/instagram.git
        $ cd instagram

## Running the Application
* Creating the virtual environment

        $ python3.8 -m venv --without-pip virtual
        $ source virtual/bin/activate
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Django and other Modules

        $ python3.8  pip install django
        $ python3.8  pip install django-bootstrap3
        $ python3.8  pip install pillow
        $ python3.8  pip install django-registration
        

* To run the application, in your terminal:

        $ python3.8 manage.py runserver
       
   
## Testing the Application
To run the tests for the class files:

        $ python3.8 manage.py test insta
        $ python3.8 manage.py test users

## Technologies Used
* Python3.8
* Django
* HTML
* CSS(Bootstrap)

## live link
['https://nanzalainsta.herokuapp.com/']

## known bugs
The user profile is not displaying the user posts.

## License
MIT License

Copyright (c) 2022 Pauline Nanzala

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.