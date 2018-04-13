# by chuski1212
# 13/04/2018

import requests
import settings
import urllib.request
import os

# to override default user-agent of urllib
class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()

headers = {
    'Accept': 'application/vnd.twitchtv.v5+json',
    'Client-ID': settings.CLIENTID,
    'User-Agent': 'Mozilla/5.0'
}

def download_clip(url, broadcaster, title, lang, position):

    # tell the user where we're downloading to
    outputpath = (settings.BASEDIR + 'twitch/' + lang + '/' + str(position) + '_' + title + '_' + broadcaster + '.mp4').replace('\n', '')
    print(outputpath)

    # get html content from url
    html = str(opener.open(url).read())

    # extract the mp4 url for source quality
    mp4url = html.split('source\":\"')[1].split('\"}')[0].split('"')[0]
    print(mp4url)
    # download file to output path
    urllib.request.urlretrieve(mp4url, outputpath)

def get_clips_by_lang(lang):
    if lang != 'all':
        lang_request = '&language=' + lang
    else:
        lang_request = ''
    print('Downloading TOP 30 last 24h ' + lang + ' Fortnite clips')
    if not os.path.exists(settings.BASEDIR + 'twitch/' + lang + '/'):
        os.makedirs(settings.BASEDIR + 'twitch/' + lang + '/')

    response = requests.get('https://api.twitch.tv/kraken/clips/top?game=' + settings.GAME +
                            '&period=' + settings.PERIOD +
                            '&limit=' + settings.LIMIT +
                            lang_request, headers=headers)

    for i, clip in enumerate(response.json()['clips']):
        download_clip(clip['url'], clip['broadcaster']['name'], clip['title'], lang, i)

    print('Download finished')


for lang in settings.LANGS:
    get_clips_by_lang(lang)



