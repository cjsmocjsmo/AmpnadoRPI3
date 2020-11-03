#!/usr/bin/python3

class CreateMyXML:

    def CreateMainXML(self, data):
        m1 = """<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>"""
        m2 = "<main>"
        m3 = "    <Filename>{}</Filename>".format(data.Filename)
        m4 = "    <Extension>{}</Extension>".format(data.Extension)
        m5 = "    <Size>{}</Size>".format(data.Size)
        m6 = "    <SongId>{}</SongId>".format(data.SongId)
        m7 = "    <Artist>{}</Artist>".format(data.Artist)
        m8 = "    <Album>{}</Album>".format(data.Album)
        m9 = "    <Song>{}</Song>".format(data.Song)
        m10 = "    <Track>{}</Track>".format(data.Track)
        m11 = "    <PicId>{}</PicId>".format(data.PicId)
        m12 = "    <ArtistId>{}</ArtistId>".format(data.ArtistId)
        m13 = "    <AlbumId>{}</lbumId>".format(data.AlbumId)
        m14 = "    <HttpMusicPath>{}</HttpMusicPath>".format(data.HttpMusicPath)
        m15 = "</main>"
        mainXML = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15]
        return mainXML
# albalpha
# { "_id" : ObjectId("5fa08dff7bd25100016b189f"), "albalpha" : [ "1" ] }

#



