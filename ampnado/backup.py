#!/usr/bin/python3
import os
import yaml
import glob
import pymongo

BDIR = "/home/pi/AmpBackups"

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
                os.mkdir(p)
            except FileExistsError:
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
        self.p1 = BDIR + "/ampnadoDB/main"
        self.p2 = BDIR + "/ampnadoDB/user_creds"

        self.p3 = BDIR + "/ampviewsDB/artalpha"
        self.p4 = BDIR + "/ampviewsDB/albalpha"
        self.p5 = BDIR + "/ampviewsDB/songalpha"

        self.p6 = BDIR + "/ampviewsDB/artistView"
        self.p7 = BDIR + "/ampviewsDB/albumView"
        self.p8 = BDIR + "/ampviewsDB/songView"
        self.p9 = BDIR + "/picdb/pics"

        self.dirlist = [
            self.p1, self.p2, self.p3, self.p4, 
            self.p5, self.p6, self.p7, self.p8, self.p9
        ]

    def createpages(self, aitem, addr):
        count = 0
        for a in aitem:
            count += 1
            newfile = addr + "/ampBackup_" + count + ".yaml"
            with open(newfile, "w") as nf:
                yaml.dump(a, nf)

    def MainBackup(self):
        allmain = db.main.find({}, {"_id": 0})
        self.createpages(allmain, self.p1)

    def DelMainBackup(self):
        gpat = self.p1 + "/*.yaml"
        mglob = glob.glob(gpat)
        [os.remove(m) for m in mglob]



    def UserCredsBackup(self):
        allcreds = db.user_creds.find({}, {"_id": 0})
        self.createpages(allcreds, self.p2)

    def DelUserCredsBackup(self):
        gpat = self.p2 + "/*.yaml"
        ucglob = glob.glob(gpat)
        [os.remove(uc) for uc in ucglob]



    def ArtAlphaBackup(self):
        allartalpha = viewsdb.artalpha.find({}, {"_id": 0})
        self.createpages(allartalpha, self.p3)

    def DelArtAlphaBackup(self):
        gpat = self.p3 + "/*.yaml"
        aaglob = glob.glob(gpat)
        [os.remove(aa) for aa in aaglob]



    def AlbAlphaBackup(self):
        allalbalpha = viewsdb.albalpha.find({}, {"_id": 0})
        self.createpages(allalbalpha, self.p4)

    def DelAlbAlphaBackup(self):
        gpat = self.p4 + "/*.yaml"
        aalglob = glob.glob(gpat)
        [os.remove(aal) for aal in aalglob]



    def SongAlphaBackup(self):
        allsongalpha = viewsdb.songalpha.find({}, {"_id": 0})
        self.createpages(allsongalpha, self.p5)

    def DelSongAlphaBackup(self):
        gpat = self.p5 + "/*.yaml"
        saglob = glob.glob(gpat)
        [os.remove(sa) for sa in saglob]


    def ArtViewBackup(self):
        allartview = viewsdb.artistView.find({}, {"_id": 0})
        self.createpages(allartview, self.p6)

    def DelArtViewBackup(self):
        gpat = self.p6 + "/*.yaml"
        avglob = glob.glob(gpat)
        [os.remove(av) for av in avglob]


    def AlbViewBackup(self):
        allalbview = viewsdb.albumView.find({}, {"_id": 0})
        self.createpages(allalbview, self.p7)

    def DelAlbViewBackup(self):
        gpat = self.p7 + "/*.yaml"
        alvglob = glob.glob(gpat)
        [os.remove(alv) for alv in alvglob]



    def SongViewBackup(self):
        allsongview = viewsdb.songView.find({}, {"_id": 0})
        self.createpages(allsongview, self.p8)

    def DelSongViewBackup(self):
        gpat = self.p8 + "/*.yaml"
        sglob = glob.glob(gpat)
        [os.remove(s) for s in sglob]


    def PicBackup(self):
        allpics = pdb.pics.find({}, {"_id": 0})
        self.createpages(allpics, self.p9)

    def DelPicBackup(self):
        gpat = self.p9 + "/*.yaml"
        pglob = glob.glob(gpat)
        [os.remove(p) for p in pglob]


    def CreateAllBackups(self):
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
        self.DelMainBackup()
        self.DelUserCredsBackup()
        self.DelArtAlphaBackup()
        self.DelAlbAlphaBackup()
        self.DelSongAlphaBackup()
        self.DelAlbViewBackup()
        self.DelArtViewBackup()
        self.DelSongViewBackup()
        self.DelPicBackup()

# if __name__ == "__main__":
#     dbb = CreateBackupDirs()
#     if not dbb.checkbdir():
#         dbb.createbdir()