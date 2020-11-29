#!/usr/bin/python3
import os
import glob
import json
import shutil
from pymongo import MongoClient

BDIR = "/usr/share/Ampnado/AmpBackup"

class CreateBackupDirs:
    def __init__(self):
        
        self.ampPaths = [
            "ampnadoDB/main", "ampnadoDB/user_creds", "ampviewsDB/artalpha", 
            "ampviewsDB/albalpha", "ampviewsDB/songalpha", "ampviewsDB/artistView", 
            "ampviewsDB/albumView", "ampviewsDB/songView", "picdb/pics"
        ]

    # def checkbdir(self):
    #     if os.path.isdir(BDIR):
    #         return True
    #     return False

    def createbdir(self):
        for a in self.ampPaths:
            p = "/".join((BDIR + a))
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

ampDBClient = MongoClient(MONGO_ADDR)
ampDBClient.drop_database("ampnadoDB")
db = ampDBClient.ampnadoDB

ampvDBClient = MongoClient(VIEWSDB_ADDR)
ampvDBClient.drop_database("ampviewsDB")
viewsdb = ampvDBClient.ampviewsDB

picDBClient = MongoClient(PICDB_ADDR)
picDBClient.drop_database("picdb")
pdb = picDBClient.picdb

class CreateBackups:

    def __init__(self):
        self.db = "ampnadoDB"
        self.avdb = "ampviewsDB"
        self.pdb = "picdb"
        self.p1 = "/".join((BDIR, self.db, "main"))
        self.p2 = "/".join((BDIR, self.db, "user_creds"))
        self.p3 = "/".join((BDIR, self.avdb, "artalpha"))
        self.p4 = "/".join((BDIR, self.avdb, "albalpha"))
        self.p5 = "/".join((BDIR, self.avdb, "songalpha"))
        self.p6 = "/".join((BDIR, self.avdb, "artistView"))
        self.p7 = "/".join((BDIR, self.avdb, "albumView"))
        self.p8 = "/".join((BDIR, self.avdb, "songView"))
        self.p9 = "/".join((BDIR, self.pdb, "pics"))

        self.dirlist = [
            self.p1, self.p2, self.p3, self.p4, self.p5, 
            self.p6, self.p7, self.p8, self.p9
        ]

    def makedirs(self):
        for d in self.dirlist:
            if not os.path.isdir(d):
                os.makedirs(d)

    def MainBackup(self):
        allmain = db.main.find({}, {"_id": 0})
        count = 0
        for a in allmain:
            count += 1
            newfile2 = self.p1 + "/ampJSONBackup_" + str(count) + ".json"
            with open(newfile2, "w+") as nff2:
                nff2.write(json.dumps(a, indent=4))

    def CredsBackup(self):
        allcreds = db.user_creds.find({}, {"_id": 0})
        count = 0
        for a in allcreds:
            count += 1
            newfile = self.p2 + "/ampJSONBackup_" + str(count) + ".json"
            with open(newfile, "w+") as nff2:
                nff2.write(json.dumps(a, indent=4))

    def ArtAlphaBackup(self):
        allartalpha = viewsdb.artalpha.find({}, {"_id": 0})
        count  = 0
        for a in allartalpha:
            count += 1
            newfile = self.p3 + "/ampJSONBackup_" + str(count) + ".json"
            with open(newfile, "w+") as nff2:
                nff2.write(json.dumps(a, indent=4))

    def AlbAlphaBackup(self):
        allalbalpha = viewsdb.albalpha.find({}, {"_id": 0})
        count = 0
        for a in allalbalpha:
            count += 1
            newfile = self.p4 + "/ampJSONBackup_" + str(count) + ".json"
            with open(newfile, "w+") as nff2:
                nff2.write(json.dumps(a, indent=4))

    def SongAlphaBackup(self):
        allsongalpha = viewsdb.songalpha.find({}, {"_id": 0})
        count = 0
        for s in allsongalpha:
            count += 1
            newfile = self.p5 + "/ampJSONBackup_" + str(count) + ".json"
            with open(newfile, "w+") as nff:
                nff.write(json.dumps(s, indent=4))

    def ArtViewBackup(self):
        allartview = viewsdb.artistView.find({}, {"_id": 0})
        count = 0
        for a in allartview:
            count += 1
            newfile = self.p6 + "/ampJSONBackup_" + str(count) + ".json"
            with open(newfile, "w+") as nf:
                nf.write(json.dumps(a, indent=4))

    def AlbViewBackup(self):
        allalbview = viewsdb.albumView.find({}, {"_id": 0})
        count = 0
        for al in allalbview:
            count += 1
            newfile2 = self.p7 + "/ampJSONBackup_" + str(count) + ".json"
            with open(newfile2, "w+") as nff2:
                foo = json.dumps(al, indent = 4)
                nff2.write(foo)

    def SongViewBackup(self):
        allsongview = viewsdb.songView.find({}, {"_id": 0})
        count = 0
        for a in allsongview:
            count += 1
            newfile = self.p8 + "/ampJSONBackup_" + str(count) + ".json"
            with open(newfile, "w+") as nff:
                nff.write(json.dumps(a, indent=4))

    def PicBackup(self):
        allpics = pdb.pics.find({}, {"_id": 0})
        count = 0
        for a in allpics:
            count += 1
            newfile = self.p9 + "/ampJSONBackup_" + str(count) + ".json"
            with open(newfile, "w+") as nff:
                nff.write(json.dumps(a, indent=4))

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

