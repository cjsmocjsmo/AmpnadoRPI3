#!/usr/bin/python3
import os
import glob
import shutil
import pymongo
import artisttemplate as AT

BDIR = "/usr/share/Ampnado/AmpBackup"

class CreateBackupDirs:
    def __init__(self):
        self.ampPaths = [
            "/ampnadoDB/main", "/ampnadoDB/user_creds", "/ampviewsDB/artalpha", 
            "/ampviewsDB/albalpha", "/ampviewsDB/songalpha", "/ampviewsDB/artistView", 
            "/ampviewsDB/albumView", "/ampviewsDB/songView", "/picdb/pics"
        ]

    # def checkbdir(self):
    #     if os.path.isdir(BDIR):
    #         return True
    #     return False

    def createbdir(self):
        for a in self.ampPaths:
            p = BDIR + a
            try:
                os.makedirs(p, mode=0o777)
            except FileExistsError:
                shutil.rmtree(p)
                os.makedirs(p, mode=0o777)
                print("Dir Already exists")
                pass

    def deletebdir(self):
        for a in self.ampPaths:
            try:
                os.remove(a)
            except:
                print("REMOVING BACKUP DIR AND ALL Its CONTENT")

MONGO_ADDR = os.environ["AMP_AMPDB_ADDR"]
VIEWSDB_ADDR = os.environ["AMP_VIEWSDB_ADDR"]
PICDB_ADDR = os.environ['AMP_PICDB_ADDR']

ampDBClient = pymongo.MongoClient(MONGO_ADDR)
db = ampDBClient.ampnadoDB

ampVDBClient = pymongo.MongoClient(VIEWSDB_ADDR)
viewsdb = ampVDBClient.ampviewsDB

ampPDBClient = pymongo.MongoClient(PICDB_ADDR)
pdb = ampPDBClient.picdb

CMXML = AT.CreateMyXML()

class CreateBackups:

    def __init__(self):
        self.adb = "/ampnadoDB"
        self.p1 = BDIR + self.adb + "/main"
        self.p2 = BDIR + self.adb + "/user_creds"

        self.avdb = "/ampviewsDB"
        self.p3 = BDIR + self.avdb + "/artalpha"
        self.p4 = BDIR + self.avdb + "/albalpha"
        self.p5 = BDIR + self.avdb + "/songalpha"
        self.p6 = BDIR + self.avdb + "/artistView"
        self.p7 = BDIR + self.avdb + "/albumView"
        self.p8 = BDIR + self.avdb + "/songView"

        self.pdb = "/picdb"
        self.p9 = BDIR + self.pdb + "/pics"

        self.dirlist = [
            self.p1, self.p2, self.p3, self.p4, 
            self.p5, self.p6, self.p7, self.p8, self.p9
        ]

    def makedirs(self):
        for d in self.dirlist:
            if not os.path.isdir(d):
                os.makedirs(d)

    def MainBackup(self):
        allmain = db.main.find({}, {"_id": 0})
        count = 0
        for a in allmain:

            dataxml = CMXML.CreateMainXML(a)
            count += 1
            newfile2 = self.p1 + "/ampBackup_" + str(count) + ".xml"
            with open(newfile2, "w+") as nff:
                for d in dataxml:
                    nff.writelines(d)

    def CredsBackup(self):
        allcreds = db.user_creds.find({})
        count = 0
        for a in allcreds:
            dataxml = CMXML.CreateCredsXML(a)
            count += 1
            newfile = self.p2 + "/ampBackup_" + str(count) + ".xml"
            with open(newfile, "w+") as nff:
                for d in dataxml:
                    nff.writelines(d)


# {
# 	"_id" : ObjectId("5fa386830b459b0001de6073"),
# 	"username" : "admin",
# 	"password" : "582d8c4c04ee2711a2b6c46ff29fdaa726671560424e879cd96f1c0c0735989723ecf379cd9f7fad19adaecb42405b5db62c980a1706dc3a38fa954683862212",
# 	"user_id" : "01a0aa0948a7ddf3a9e98c1ac5fe38e0426292ea9767a1f6a3c352e06d35cdef90acf3e0b57285f8635ccf535097d5cf82c04d90fbbdedd4618a0353d4532969"
# }






    def ArtAlphaBackup(self):
        allartalpha = viewsdb.artalpha.find({}, {"_id": 0})
        count  = 0
        for a in allartalpha:
            dataxml = CMXML.CreateArtAlphaXML(a)
            count += 1
            newfile = self.p3 + "/ampBackup_" + str(count) + ".xml"
            with open(newfile, "w+") as nff:
                for d in dataxml:
                    nff.writelines(d)

    def AlbAlphaBackup(self):
        allalbalpha = viewsdb.albalpha.find({}, {"_id": 0})
        count = 0
        for a in allalbalpha:
            dataxml = CMXML.CreateAlbAlphaXML(a)
            count += 1
            newfile = self.p4 + "/ampBackup_" + str(count) + ".xml"
            with open(newfile, "w+") as nff:
                for d in dataxml:
                    nff.writelines(d)

    def SongAlphaBackup(self):
        allsongalpha = viewsdb.songalpha.find({}, {"_id": 0})
        count = 0
        for a in allsongalpha:
            dataxml = CMXML.CreateSongAlphaXML(a)
            count += 1
            newfile = self.p5 + "/ampBackup_" + str(count) + ".xml"
            with open(newfile, "w+") as nff:
                for d in dataxml:
                    nff.writelines(d)

    def ArtViewBackup(self):
        allartview = viewsdb.artistView.find({}, {"_id": 0})
        count = 0
        for a in allartview:
            dataxml = CMXML.CreatArtistViewXML(a)
            count += 1
            newfile = self.p6 + "/ampBackup_" + str(count) + ".xml"
            with open(newfile, "w+") as nff:
                for d in dataxml:
                    nff.writelines(d)

    def AlbViewBackup(self):
        allalbview = viewsdb.albumView.find({}, {"_id": 0})
        count = 0
        for a in allalbview:
            dataxml = CMXML.CreatAlbumViewXML(a)
            count += 1
            newfile = self.p7 + "/ampBackup_" + str(count) + ".xml"
            with open(newfile, "w+") as nff:
                for d in dataxml:
                    nff.writelines(d)

    def SongViewBackup(self):
        allsongview = viewsdb.songView.find({}, {"_id": 0})
        count = 0
        for a in allsongview:
            dataxml = CMXML.CreateSongViewXML(a)
            count += 1
            newfile = self.p8 + "/ampBackup_" + str(count) + ".xml"
            with open(newfile, "w+") as nff:
                for d in dataxml:
                    nff.writelines(d)

    def PicBackup(self):
        allpics = pdb.pics.find({}, {"_id": 0})
        count = 0
        for a in allpics:
            dataxml = CMXML.CreatePicsXML(a)
            count += 1
            newfile = self.p9 + "/ampBackup_" + str(count) + ".xml"
            print("PRINTING TO FILE:")
            print(newfile)
            with open(newfile, "w+") as nff:
                for d in dataxml:
                    nff.writelines(d)

    def CreateAllBackups(self):
        self.makedirs()
        self.MainBackup()
        self.CredsBackup()
        self.ArtAlphaBackup()
        self.AlbAlphaBackup()
        self.SongAlphaBackup()
        self.AlbViewBackup()
        self.ArtViewBackup()
        self.SongViewBackup()
        self.PicBackup()

    def DelAllBackups(self):
        shutil.rmtree(BDIR)

