#!/usr/bin/env python
import os
from ricecooker.chefs import YoutubeSushiChef
from ricecooker.classes import licenses
from googleapiclient.discovery import build


# Run constants
################################################################################
CHANNEL_ID = "32e5033ebc7a456b91fccbd2747d4035"             # UUID of channel
CHANNEL_NAME = "Newz Beat"                           # Name of Kolibri channel
CHANNEL_SOURCE_ID = "Newz_Beat"                              # Unique ID for content source
CHANNEL_DOMAIN = "youtube.com"                         # Who is providing the content
CHANNEL_LANGUAGE = "en"                                     # Language of channel
CHANNEL_DESCRIPTION = 'ollow the beat, follow the beat. From the studio to the street....Tuula, kalira, wuliriza, nyumirwa amawulire! NewzBeat is a Ugandan rap-news programme delivering the latest information in verse and rhyme. Beeramu tosubwa amawulire gaffe mu bitontome! This bilingual English-Luganda news magazine show airs on NTV Uganda every weekend!'                                  # Description of the channel (optional)
CHANNEL_THUMBNAIL = os.path.join('files', 'logo.jpg')                                    # Local path or url to image file (optional)
CONTENT_ARCHIVE_VERSION = 1                                 # Increment this whenever you update downloaded content


# Additional constants
################################################################################
# Add Google API key here. Will need access to the Youtube API v3 in order for script to run.
GOOGLE_API_KEY = None
NEWZ_BEAT_CHANNEL_ID = 'UCgoXKBqkLrBau7dVpXFhWDA'


# The chef subclass
################################################################################
class NewzBeatChef(YouTubeSushiChef):
    """
    This class converts content from the content source into the format required by Kolibri,
    then uploads the {channel_name} channel to Kolibri Studio.
    Your command line script should call the `main` method as the entry point,
    which performs the following steps:
      - Parse command line arguments and options (run `./sushichef.py -h` for details)
      - Call the `SushiChef.run` method which in turn calls `pre_run` (optional)
        and then the ricecooker function `uploadchannel` which in turn calls this
        class' `get_channel` method to get channel info, then `construct_channel`
        to build the contentnode tree.
    For more info, see https://ricecooker.readthedocs.io
    """
    channel_info = {
        'CHANNEL_ID': CHANNEL_ID,
        'CHANNEL_SOURCE_DOMAIN': CHANNEL_DOMAIN,
        'CHANNEL_SOURCE_ID': CHANNEL_SOURCE_ID,
        'CHANNEL_TITLE': CHANNEL_NAME,
        'CHANNEL_LANGUAGE': CHANNEL_LANGUAGE,
        'CHANNEL_THUMBNAIL': CHANNEL_THUMBNAIL,
        'CHANNEL_DESCRIPTION': CHANNEL_DESCRIPTION,
    }



# CLI
################################################################################
if __name__ == '__main__':
    # This code runs when sushichef.py is called from the command line
    chef = NewzBeatChef()
    chef.main()
