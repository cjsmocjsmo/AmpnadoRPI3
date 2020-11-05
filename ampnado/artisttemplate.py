#!/usr/bin/python3

class CreateMyXML:
    def __init__(self):
        self.m1 = """<?xml version="1.0" encoding="UTF-8" standalone="yes" ?> \n"""

    def CreateMainXML(self, data):
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
        m13 = "\t <AlbumId>{}</AlbumId> \n".format(data["AlbumId"])
        m14 = "\t <HttpMusicPath>{}</HttpMusicPath> \n".format(data["HttpMusicPath"])
        m15 = "</main> \n"
        mainXML = [
            self.m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15,
        ]
        return mainXML

    def CreateCredsXML(self, data):
        a1 = "<Creds> \n"
        a2 = "\t <username>{}</username> \n".format(data["username"])
        a3 = "\t <password>{}</password> \n".format(data["password"])
        a4 = "\t <user_id>{}</user_id> \n".format(data["user_id"])
        a5 = "</Creds> \n"
        credsxml = [self.m1, a1, a2, a3, a4, a5]
        return credsxml

    def CreatAlbumViewXML(self, data):
        # albumView
        av2 = "<AlbumView> \n"
        av3 = "\t <Artist>{}</Artist> \n".format(data["Artist"])
        av4 = "\t <Album>{}</Album> \n".format(data["Album"])
        av5 = "\t <ArtistId>{}</ArtistId> \n".format(data["ArtistId"])
        av6 = "\t <AlbumId>{}</AlbumId> \n".format(data["AlbumId"])
        av7 = "\t <AlbumArtHttpPath>{}</AlbumArtHttpPath> \n".format(data["AlbumArtHttpPath"])
        av8 = "\t <NumSongs>{}</NumSongs> \n".format(data["NumSongs"])
        av9 = "\t <Page>{}</Page> \n".format(data["Page"])
        av10 = "\t <Songs>"
        albumViewXML = [
            self.m1, av2, av3, av4, av5, av6, av7, av8, av9, av10,
        ]
        for s in data["Songs"]:
            av11 = "\t\t <Songname>{}</Songname> \n".format(s[0])
            albumViewXML.append(av11)
            av12 = "\t\t <SongId>{}</SongId> \n".format(s[0])
            albumViewXML.append(av12)
        albumViewXML.append("\t </Songs> \n")
        albumViewXML.append("</AlbumView> \n")
        return albumViewXML

    def CreatArtistViewXML(self, data):
        #artistView
        a2 = "<ArtistView> \n"
        a3 = "\t <Artist>{}</Artist> \n".format(data["Artist"])
        a4 = "\t <ArtistId>{}</ArtistId> \n".format(data["ArtistId"])
        a5 = "\t <Page>{}</Page> \n".format(data["Page"])
        a6 = "\t <Albums> \n"
        artistViewXML = [self.m1, a2, a3, a4, a5, a6]
        for a in data["Albums"]:
            a7 = "\t <Album>{}</Album> \n".format(a[0])
            artistViewXML.append(a7)
            a8 = "\t <AlbumId>{}</AlbumId> \n".format(a[1])
            artistViewXML.append(a8)
        a9 = "\t </Albums> \n"
        artistViewXML.append(a9)
        a10 = "</ArtistView> \n"
        artistViewXML.append(a10)
        return artistViewXML

    def CreateSongViewXML(self, data):
        #songView
        a2 = "<SongView> \n"
        a3 = "\t <Page>{}</Page> \n".format(data["Page"])
        a4 = "\t <Song>{}</Song> \n".format(data["Song"])
        a5 = "\t <SongId>{}</SongId> \n".format(data["SongId"])
        a6 = "\t <Artist>{}</Artist> \n".format(data["Artist"])
        a7 = "</SongView> \n"
        songviewxml = [self.m1, a2, a3, a4, a5, a6, a7]
        return songviewxml

    def CreatePicsXML(self, data):
        #pics
        a1 = "<Pics>"
        a2 = "\t <PicId>{}</PicId> \n".format(data["PicId"])
        a3 = "\t <DirPath>{}</DirPath> \n".format(data["DirPath"])
        a4 = "\t <NewPicPath>{}</NewPicPath> \n".format(data["NewPicPath"])
        a5 = "\t <AlbumArtHttpPath>{}</AlbumArtHttpPath> \n".format(data["AlbumArtHttpPath"])
        a6 = "\t <PicPath>{}</PicPath> \n".format(data["PicPath"])
        a7 = "\t <ext>{}</ext> \n".format(data["ext"])
        a8 = "\t <AlbumArtSize>{}</AlbumArtSize> \n".format(data["AlbumArtSize"])
        
        picsXML = [self.m1, a1, a2, a3, a4, a5, a6, a7, a8]
        a12 = "</Pics> \n"
        picsXML.append(a12)
        return picsXML

    def CreateArtAlphaXML(self, data):
        #artalpha
        a1 = "<ArtAlpha> \n"
        artalphaXML = [self.m1, a1]
        for s in data["artalpha"]:
            a2 = "\t <item>{}</item> \n".format(s)
            artalphaXML.append(a2)
        a3 = "</ArtAlpha>"
        artalphaXML.append(a3)
        return artalphaXML

    def CreateAlbAlphaXML(self, data):
        #artalpha
        a1 = "<AlbAlpha> \n"
        albalphaXML = [self.m1, a1]
        for s in data["albalpha"]:
            a2 = "\t <item>{}</item> \n".format(s)
            albalphaXML.append(a2)
        a3 = "</AlbAlpha>"
        albalphaXML.append(a3)
        return albalphaXML

    def CreateSongAlphaXML(self, data):
        #artalpha
        a1 = "<SongAlpha> \n"
        songalphaXML = [self.m1, a1]
        for s in data["songalpha"]:
            a2 = "\t <item>{}</item> \n".format(s)
            songalphaXML.append(a2)
        a3 = "</SongAlpha> \n"
        songalphaXML.append(a3)
        return songalphaXML
