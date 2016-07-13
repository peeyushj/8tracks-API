# 8tracks(API)
Relavant Discovery Logic for 8-tracks Playlists.

-- Used Architecture --

Solr engine with Haystack indexing has been used and rest API has been exposed via django-rest-framework
SOLR is used to do fast searching. This design has been made by taking the consideration of amount of huge data (Even in sample data, I have used more than 1L playlist and their tags)

How to Run
---------------
1) First clone the repository. (git clone https://github.com/peeyushj/8tracks-API.git)

2) create the virtual environment using command - "virtualenv 8tracks-API" (OPTIONAL: you can define your own environment name)

3) Activate the virtual environment using command - "source 8tracks-API/bin/activate"

4) Install all the required packages by running command - "pip install -r requirements.txt"

5) Create a database
    
    a) create a database named "tracks".
    b) Go to the settings file in the project and update your mysql user and password.
        ```
        DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'tracks',
            'USER': 'root',
            'PASSWORD': 'root',
            'HOST': '',
            'PORT': '',
        },
        }
        ```
    c) After updating mysql user and password sync the databases using command - python manage.py migrate

6) [OPTIONAL:] insert sample data sql file(playlist_data.sql) to get 1L playlist data and every playlist has around 10 tags each.

7) I have used SOLR to store the data of playlist with correspoding tags. To install SOLR use follwoing step:
    a) Download solr-4.10.4 version from http://archive.apache.org/dist/lucene/solr/4.10.4/ and unzip it make the folder name as 'solr-4.10.4' (you can use other version also, but i was using this only so I continued with that.)
    b) Build the schema out for solr and save it to schema.xml
        python manage.py build_solr_schema > schema.xml (- Note: Do this is your django project directory)
    c) Replace the solr schema in  "solr-4.10.4/example/solr/conf/schema.xml" with the one you made in the previous step
    d) Go into SOLR directory and start the solr server
        cd solr-4.0.0/example
        java -jar start.jar

8) Run the python server - python manage.py runserver

9) If you have not done step 6, then we can use the API to generate new playlists and tags accordingly

    a) For Adding new PlayLists hit the API - http://localhost:8000/api/playlists/playlists/
    This API will list all the playlists in the system and one can also add new playlists into the system.

    b) For adding new tags hit the API - http://localhost:8000/api/playlists/tags/
    This API will list all the tags in the system and one can also add new tags into the system.

    c) Tags and playlist relationship can be inserted directly from the database also.

10) Once you have completed adding data, you need to reindex the playlist's tag data into SOLR. So use the command for indexing - python manage.py update_index

11) Run the python server again - python manage.py runserver

12) APIs for getting 8-tracks data
    a) Getting playlist for a tag(sorted by likes) - http://localhost:8000/api/search/playlists/?q=<tag_name>
    b) Getting relavent tags for a tag (sorted by relavency) - http://localhost:8000/api/search/tags/?q=<tag_name>

