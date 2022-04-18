# General import
import os
import json
import requests
import time
import pip


# Google api authentication import
# Check installed
try:
    import google.oauth2.credentials
    import googleapiclient.discovery
except ImportError:
    pip.main(['install', 'google-api-core', 'google-auth', 'google-api-python-client', 'google-auth-httplib2', 'google-auth-oauthlib', 'google-pasta', 'googleapis-common-protos'])
    import google.oauth2.credentials
    import googleapiclient.discovery

# Auth with google credential json
# Get credentials from json file
credentials = google.oauth2.credentials.Credentials.from_authorized_user_file('credentials.json')



# Create a youtube client
youtube = googleapiclient.discovery.build('youtube', 'v3', credentials=credentials)

# Get the channel id
channel_id = 'UC2ne9XqtBWKJKLfIAKtmjAg'
# Get the channel info
channel_info = youtube.channels().list( id=channel_id, part='snippet,statistics' ).execute()

print(channel_info)
