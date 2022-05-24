from youtube_dl import YoutubeDL

YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
def Search_yt(item):
    with YoutubeDL(YDL_OPTIONS) as ydl:
        try:
            info = ydl.extract_info("ytsearch:%s" % item, download = False)['entries'][0]
        except Exception:
            return False
        
    return {'source': info['formats'][0]['url'], 'title': info['title']}

def GetLink(query):
    #print(args)
    #query = " ".join(args)
    print(query)
    song = Search_yt(query)
    print(song)
    # error checking
    if type(song) == type(True):
        return "Could not get song. It was not found or a playlist was found"
    else:
        return song

#getLink("rks devil like me")