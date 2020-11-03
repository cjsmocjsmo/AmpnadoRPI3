#!/usr/bin/python3

class CreateMyXML:

    def CreateMainXML(self, data):
        m1 = """<?xml version="1.0" encoding="UTF-8" standalone="yes" ?> \n"""
        m2 = "<main> \n"
        m3 = "\t <Filename>{}</Filename> \n".format(data["Filename"])
        m4 = "\t <Extension>{}</Extension> \n".format(data["Extension"])
        m5 = "\t <Size>{}</Size> \n".format(data["Size"])
        m6 = "\t <SongId>{}</SongId> \n".format(data["SongId"])
        m7 = "\t <Artist>{}</Artist> \n".format(data["Artist"])
        m8 = "\t <Album>{}</Album> \n".format(data["Album"])
        m9 = "\t <Song>{}</Song> \n".format(data["Song"])
        m10 = "\t <Track>{}</Track> \n".format(data["Track"])
        m11 = "\t <PicId>{}</PicId> \n".format(data["PicId"])
        m12 = "\t <ArtistId>{}</ArtistId> \n".format(data["ArtistId"])
        m13 = "\t <AlbumId>{}</lbumId> \n".format(data["AlbumId"])
        m14 = "\t <HttpMusicPath>{}</HttpMusicPath> \n".format(data["HttpMusicPath"])
        m15 = "</main> \n"
        mainXML = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15]
        return mainXML
# albalpha
# { "_id" : ObjectId("5fa08dff7bd25100016b189f"), "albalpha" : [ "1" ] }

#



