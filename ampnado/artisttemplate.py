#!/usr/bin/python3

class CreateMyXML:

    def CreateMainXML(self, data):
        maindata = """
<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<main>
    <Filename>{}</Filename>
    <Extension>{}</Extension>
    <Size>{}</Size>
    <SongId>{}</SongId>
    <Artist>{}</Artist>
    <Album>{}</Album>
    <Song>{}</Song>
    <Track>{}</Track>
    <PicId>{}</PicId>
    <ArtistId>{}</ArtistId>
    <AlbumId>{}</lbumId>
    <HttpMusicPath>{}</HttpMusicPath>
</main>""".format(data.Filename, data.Extension, data.Size, data.SongId, 
            data.Artist, data.Album, data.Song, data.Track, data.PicId,
            data.ArtistId, data.AlbumId, data.HttpMusicPath,
            )
        return maindata

# albalpha
# { "_id" : ObjectId("5fa08dff7bd25100016b189f"), "albalpha" : [ "1" ] }

#



