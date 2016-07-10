# 8tracks
Discovery Logic for Playlists based on the tags.

How to Run
---------------
1) clone the repository.

2) create the virtual environment using command - ``virtualenv <name of the environment>`` 

3) Activate the virtual environment using command - ``source <name of the environment>/bin/activate``

4) Install all the required packages by running command - ``pip install -r requirements.txt``

5) I tried dumping and undumping data in .sql file but got some errors. So one must have to do some work to give some data to the system::
    
    a) create a database named "tracks".
    b) Go to the settings file in the project and update your mysql user and password.
    ```
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tracks',
        'USER': 'root',
        'PASSWORD': 'alpha123',
        'HOST': 'localhost',
        'PORT': '',
    },
    }
    ```
    c) After updating mysql user and password sync the databases using command - python manage.py migrate

6) Run the server by managemant command - python manage.py runserver

7) Now it's time to populate the database. I have created two extra APIs to post playlists and tags directly from the browser::

    For Adding new PlayLists hit the API - localhost:8000/api/playlists/playlists/
    This API will list all the playlists in the system and one can also add new playlists into the system.
    For adding new tags hit the API - localhost:8000/api/playlists/tags/
    This API will list all the tags in the system and one can also add new tags into the system.
    

8) I have kept the relationship between Tags and PlayLists as flexible. I did not define an end-point API for creating relationships between these. This can be done by inserting some entries into the *playlists_playlist_tags* in the tracks database as this table contains the entries for many to many relationship between Playlists and tags.

9) IMPORTANT - Every time you add new Tag instances, you have to push Tag indices to the AWS instance by using management command - python manage.py update_index

10) For Search API - hit the URL ```http://localhost:8000/api/search/playlists/?q=<tag_name1><tag_name2>```.
   For Ex. - ```http://localhost:8000/api/search/playlists/?q=poprock```. here pop and rock are the two tag_names. This API will return the lists of playlists based on relevancy and sorted on basis of configuration 'ORGANIZE_BY' parameter in settings.py.



**Detail of any PlayList** can also be viewed via URL - *http://localhost:8000/api/playlists/playlists/<playlist_id>/* where playlist_id can be unique id of any playlist in the system. 

For ex - *http://localhost:8000/api/playlists/playlists/1/*  returned on my system - 

```json
HTTP 200 OK
Allow: GET, PUT, PATCH, HEAD, OPTIONS
Content - Type: application / json
Vary: Accept

{
    "playlist_id": 1,
    "playlist_name": "Led Zeppelin",
    "likes": 10,
    "plays": 3
}
``` 
Similarily  **Detail of any Tag** can also be viewed via URL - *http://localhost:8000/api/playlists/playlists/<tag_id>/*
where tag\_id can be unique_id of any Tag in the system.


**Methodology Used** - 

I have used the concept of Elastic Search and exposing APIs using django-rest-framework. Elastic search is used to do fast searching.

I have used a AWS Elastic search instance as a remote server for hosting elastic search. The index name is haystack and it stores the indices of Tag model. You can thus do a query search on thousand of tags.
