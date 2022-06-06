## InstaMe'
This is an instagram clone

## Author
Pauline Wafula

## Description
InstaMe' is a web application that mimics a popular .This is through showing images in different categories and location. On clicking on an image, it is able to take you to a bigger image with description, category and location.A new user can also search an image using category. They can also copy and paste the link of the image.

## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like to:

* See images that interest me 
* Click on a photo to expand it and also view description of the photo
* Search for different categories
* Copy the images link

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display images posted by other users  | **On page load** | Display images of various categories |
| Display images  | **On clicking a 'search' button** | Displays images under the searched category |
| Display description, location and category | **Click a photo** |  Expanded version of the photo with description,location and category|
| Copy link | **On clicking copy link button** | link copied|

## SetUp / Installation Requirements
### Prerequisites
* python3.8
* pip
* activate virtual environment
### Cloning
* In your terminal:


        $ git clone https://github.com/paulinenanzala19/Picture_Patch.git
        $ cd gallery

## Running the Application
* Creating the virtual environment

        $ python3.8 -m venv --without-pip virtual
        $ source virtual/bin/activate
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Django and other Modules

        $ python3.8  pip install django
        $ python3.8  pip install django-bootstrap3
        $ python3.8  pip install pillow
        

* To run the application, in your terminal:

        $ python3.8 manage.py runserver
       
   
## Testing the Application
To run the tests for the class files:

        $ python3.8 manage.py test pictures

## Technologies Used
* Python3.8
* Django
* HTML
* CSS(Bootstrap)

## live link
['']

## known bugs
Not any at the moment but am open to suggestion

## License
MIT License

Copyright (c) 2022 Pauline Nanzala

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.