

[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<br />

<p align="center">
  <a href="https://github.com/Artists-Forum-NITK/AF_Website">
    <img src="https://github.com/Artists-Forum-NITK/AF_Website/blob/master/mysite/static/images/af-small.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Artists' Forum</h3>

  <p align="center">
    <a href="http://example.com/"><strong>  Artists' Forum Website »</strong></a>
    <br>
    <br>
    <a href="http://137.116.134.135:8000/">View Demo</a>
    ·
    <a href="issues-url">Report Bug</a>
    ·
    <a href="https://github.com/Artists-Forum-NITK/AF_Website/issues/new">Request Feature</a>
  </p>
</p>

## Abstract

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design, that follows the model-template-view (MVT) architectural pattern. The framework emphasizes reusability and "pluggability" of components, less code, low coupling, rapid development, and the principle of don't repeat yourself. Python is used throughout, even for settings files and data models. 

Django provides a bridge between the data model and the database engine, and supports a large set of database systems including MySQL, Oracle, Postgres, etc. Django also supports NoSQL database through Django-nonrel fork. For now, the only NoSQL databases supported are MongoDB and google app engine.It consists of an object-relational mapper (ORM) that mediates between data models (defined as Python classes) and a relational database ("Model"), a system for processing HTTP requests with a web templating system ("View"), and a regular-expression-based URL dispatcher ("Controller"). 

Django REST framework is a powerful and flexible toolkit for building Web APIs. Django's configuration system allows third party code to be plugged into a regular project, provided that it follows the reusable app conventions. Django has built-in support for Ajax, RSS, Caching and various other frameworks.Django comes with a lightweight web server to facilitate end-to-end application development and testing.

The Model-View-Template (MVT) is slightly different from MVC. In fact the main difference between the two patterns is that Django itself takes care of the Controller part (Software Code that controls the interactions between the Model and View), leaving us with the template. The template is a HTML file mixed with Django Template Language (DTL)

## Models In the Website

### Content Regulation
- Member
- Image
- Event
- Art
- Blog
- Udaan
- Comment
- Gallery

### User Account Management
- Account
- Recruitment Applicant
- My Account Manager
- Volunteer
- Registration

## Functionalities to be Implemented

- The content in terms of team members' data, images, events, artworks, blog content,etc. can be uploaded via the admin dashboard by the superadmin or the user with admin permissions.

- ModelViewer HTML tag- <modelviewer> can been used in order to display the 3D models that are uploaded as .glb or .gltf files.

- There are appropriate filters in place for the content that is to be displayed on various pages. 

- A mailer can be implemented for the users to get latest updates via email.

- Dislaying Images corresponding to the events, blogs or Artworks in various sections on the website pages.

- Further implemented features to be based on the requirements specified by the core members.

## Contribution Guidelines

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. 
Any contributions you make are greatly appreciated! 

- Fork the Project and Clone it locally,
- Run the following commands in you teminal:
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver
```
- Now enter `localhost:8000` in the browser.
- Create your Feature Branch `git checkout -b feature/AmazingFeature`
- Commit your Changes `git commit -m 'Add some AmazingFeature'`
- Push to the Branch `git push origin feature/AmazingFeature`
- Open a Pull Request for further Reviews and suggestions.



[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/Artists-Forum-NITK/AF_Website/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/company/artists_forum_nitk/?originalSubdomain=in
[product-screenshot]: https://github.com/Artists-Forum-NITK/AF_Website/blob/master/mysite/static/images/af-small.png
