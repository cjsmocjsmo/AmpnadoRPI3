#!/usr/bin/python3
import os
import yaml
import glob
import shutil
import pymongo
import artisttemplate as AT

BDIR = "/home/AmpBackups"

class CreateBackupDirs:
    def __init__(self):
        self.ampPaths = [
            "/ampnadoDB", "/ampnadoDB/main", "/ampnadoDB/user_creds"
            "/ampviewsDB", "/ampviewsDB/artalpha", "/ampviewsDB/albalpha"
            "/ampviewsDB/songalpha", "/ampviewsDB/artistView", "/ampviewsDB/albumView"
            "/ampviewsDB/songView", "/picdb/pics"
        ]

    def checkbdir(self):
        if os.path.isdir(BDIR):
            return True
        return False

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

    def createpages(self, aitem, addr):
        count = 0
        for a in aitem:
            count += 1
            newfile = addr + "/ampBackup_" + str(count) + ".yaml"
            with open(newfile, "w+") as nf:
                yaml.dump(a, nf)

    def makedirs(self):
        for d in self.dirlist:
            if not os.path.isdir(d):
                os.makedirs(d)


    def MainBackup(self):
        allmain = db.main.find({}, {"_id": 0})
        cmx = AT.CreateMyXML()
        count = 0
        for a in allmain:
            dataxml = cmx.CreateMainXML(a)
            count += 1
            newfile2 = self.p1 + "/ampBackup_" + str(count) + ".xml"
            with open(newfile2, "w+") as nff:
                for d in dataxml:
                    nff.writelines(d)

       

    def UserCredsBackup(self):
        allcreds = db.user_creds.find({}, {"_id": 0})
        self.createpages(allcreds, self.p2)

    def ArtAlphaBackup(self):
        allartalpha = viewsdb.artalpha.find({}, {"_id": 0})
        self.createpages(allartalpha, self.p3)

    def AlbAlphaBackup(self):
        allalbalpha = viewsdb.albalpha.find({}, {"_id": 0})
        self.createpages(allalbalpha, self.p4)

    def SongAlphaBackup(self):
        allsongalpha = viewsdb.songalpha.find({}, {"_id": 0})
        self.createpages(allsongalpha, self.p5)

    def ArtViewBackup(self):
        allartview = viewsdb.artistView.find({}, {"_id": 0})
        self.createpages(allartview, self.p6)

    def AlbViewBackup(self):
        allalbview = viewsdb.albumView.find({}, {"_id": 0})
        self.createpages(allalbview, self.p7)

    def SongViewBackup(self):
        allsongview = viewsdb.songView.find({}, {"_id": 0})
        self.createpages(allsongview, self.p8)

    def PicBackup(self):
        allpics = pdb.pics.find({}, {"_id": 0})
        self.createpages(allpics, self.p9)

    def CreateAllBackups(self):
        self.makedirs()
        self.MainBackup()
        self.UserCredsBackup()
        self.ArtAlphaBackup()
        self.AlbAlphaBackup()
        self.SongAlphaBackup()
        self.AlbViewBackup()
        self.ArtViewBackup()
        self.SongViewBackup()
        self.PicBackup()

    def DelAllBackups(self):
        shutil.rmtree(BDIR)

# if __name__ == "__main__":
#     dbb = CreateBackupDirs()
#     if not dbb.checkbdir():
#         dbb.createbdir()