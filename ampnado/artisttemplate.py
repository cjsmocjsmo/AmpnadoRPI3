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
        av10 = "\t <Songs> \n"
        albumViewXML = [
            self.m1, av2, av3, av4, av5, av6, av7, av8, av9, av10,
        ]
        songlist = []
        for s in data["Songs"]:
            songitem = [
                "<Songname>{}</Songname> \n".format(s[0]),
                "<SongId>{}</SongId> \n".format(s[1]),
            ]
            songlist.append(songitem)
        albumViewXML.append(songlist)
        albumViewXML.append("\t </Songs> \n")
        albumViewXML.append("</AlbumView> \n")
        return albumViewXML



# {
# 	"_id" : ObjectId("5fa50ff18bea3100ace0b437"),
# 	"Artist" : "Alan Jackson",
# 	"Album" : "Good Time",
# 	"ArtistId" : "f5ae8c3c84464be9b24735c7b28d2ad6",
# 	"AlbumId" : "cc1d7314eb2343bd9863c07210c0836b",
# 	"AlbumArtHttpPath" : "/static/images/thumbnails/2e9c76fa8856429cab33e393eb06c3f7.jpg",
# 	"NumSongs" : 15,
# 	"Songs" : [
# 		[
# 			"Long Long Way",
# 			"99cbd87db2aa43ea9cb6a04fd23e8c7c"
# 		],
# 		[
# 			"Good Time",
# 			"8abbae01d86a407793918ad8727583dc"
# 		],
# 		[
# 			"Right Where I Want You",
# 			"e71f9d170a7443b9a56fe05217864ab9"
# 		],
# 		[
# 			"If Jesus Walked The World Today",
# 			"39b237fb0e334dfc81c56893f6dbb196"
# 		],
# 		[
# 			"This Time",
# 			"dc8e058b821545a3aaf218dd99b8ca7b"
# 		],
# 		[
# 			"Laid Back 'n Low Key",
# 			"b5864371dd4e4697886135c5cd4085ed"
# 		],
# 		[
# 			"Country Boy",
# 			"3cc799343b8946a5a1349a8506661444"
# 		],
# 		[
# 			"I Still Like Bologna",
# 			"480e197159564754b37910ca5ac0866e"
# 		],
# 		[
# 			"When The Love Factor's High",
# 			"039cdabebd9d413ebea02d856711339a"
# 		],
# 		[
# 			"Listen To Your Senses",
# 			"aeea69ebdc864c38a8df3f5f36b3fce5"
# 		],
# 		[
# 			"I Wish I Could Back Up",
# 			"8029208f4d444f59aac6120d4b1ff316"
# 		],
# 		[
# 			"Never Loved Before With Martina Mcbride",
# 			"2d09dd7da85b46e4b04085222d6f90d4"
# 		],
# 		[
# 			"If You Want To Make Me Happy",
# 			"6c47762662bf40aab7957369f2366273"
# 		],
# 		[
# 			"Small Town Southern Man",
# 			"7222166eb08448d681ade9276ea548bc"
# 		],
# 		[
# 			"1976",
# 			"80f120109039416d9943e22b4fb6afa5"
# 		]
# 	],
# 	"Page" : "1"
# }


















    def CreatArtistViewXML(self, data):
        #artistView
        a2 = "<ArtistView> \n"
        a3 = "\t <Artist>{}</Artist> \n".format(data["Artist"])
        a4 = "\t <ArtistId>{}</ArtistId> \n".format(data["ArtistId"])
        a5 = "\t <Page>{}</Page> \n".format(data["Page"])
        a6 = "\t <Albums> \n"
        artistViewXML = [self.m1, a2, a3, a4, a5, a6]
        artistlist = []
        for a in data["Albums"]:
            artistitem = [
                "\tt <Album>{}</Album> \n".format(a[0]),
                "\tt <AlbumId>{}</AlbumId> \n".format(a[1])
            ]
            artistlist.append(artistitem)
        artistViewXML.append(artistlist)
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
