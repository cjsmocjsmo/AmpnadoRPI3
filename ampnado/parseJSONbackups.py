#!/usr/bin/python3

import os
import glob
import json
import pymongo
from pymongo import MongoClient

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

class ParseMyXML:
    def __init__(self):
        self.basedir = "/usr/share/Ampnado/AmpBackup"
        self.amp = "ampnadoDB"
        self.ampv = "ampviewsDB"
        self.pic = "picdb"
        self.maindir = "/".join((self.basedir, self.amp, "main/*.xml"))
        self.credsdir = "/".join((self.basedir, self.amp, "user_creds/*.xml"))
        self.artview = "/".join((self.basedir, self.ampv, "artistView/*.xml"))
        self.albview = "/".join((self.basedir, self.ampv, "albumView/*.xml"))
        self.songview = "/".join((self.basedir, self.ampv, "songView/*.xml")) 
        self.artalpha = "/".join((self.basedir, self.ampv, "artalpha/*.xml"))
        self.albalpha = "/".join((self.basedir, self.ampv, "albalpha/*.xml"))
        self.songalpha = "/".join((self.basedir, self.ampv, "songalpha/*.xml"))
        self.picdir = "/".join((self.basedir, self.pic, "pics/*.xml"))

    def parseMainXML(self):
        mglob = glob.glob(self.maindir)
        for m in mglob:
            with open(m, "r") as mf:
                myfile = mf.read()
            data = json.loads(myfile)
            try:
                db.main.insert(data)
            except pymongo.errors.DuplicateKeyError:
                pass

    def parseCredsXML(self):
        cglob = glob.glob(self.credsdir)
        for c in cglob:
            with open(c, "r") as mf:
                myfile = mf.read()
            data = json.loads(myfile)
            try:
                db.user_creds.insert(data)
            except pymongo.errors.DuplicateKeyError:
                pass

    def parseArtViewXML(self):
        arvglob = glob.glob(self.artview)
        for arv in arvglob:
            with open(arv, "r") as mf:
                myfile = mf.read()
            data =  json.loads(myfile)
            try:
                viewsdb.albalpha.insert(data)
            except pymongo.errors.DuplicateKeyError:
                pass

    def parseAlbViewXML(self):
        avglob = glob.glob(self.albview)
        for av in avglob:
            with open(av, "r") as mf:
                myfile = mf.read()
            data = json.loads(myfile)
            try:
                viewsdb.albalpha.insert(data)
            except pymongo.errors.DuplicateKeyError:
                pass

    def parseSongViewXML(self):
        svglob = glob.glob(self.songview)
        for sv in svglob:
            with open(sv, "r") as mf:
                myfile = mf.read()
            data = json.loads(myfile)
            try:
                viewsdb.albalpha.insert(data)
            except pymongo.errors.DuplicateKeyError:
                pass

    def parseArtAlphaXML(self):
        arglob = glob.glob(self.artalpha)
        for ar in arglob:
            with open(ar, "r") as mf:
                myfile = mf.read()
            data = json.loads(myfile)
            try:
                viewsdb.albalpha.insert(data)
            except pymongo.errors.DuplicateKeyError:
                pass

    def parseAlbAlphaXML(self):
        aaglob = glob.glob(self.albalpha)
        for aa in aaglob:
            with open(aa, "r") as mf:
                myfile = mf.read()
            data = json.load(myfile)
            try:
                viewsdb.albalpha.insert(data)
            except pymongo.errors.DuplicateKeyError:
                pass

    def parseSongAlphaXML(self):
        saglob = glob.glob(self.songalpha)
        for sa in saglob:
            with open(sa, "r") as mf:
                myfile = mf.read()
            data = json.loads(myfile)
            try:
                viewsdb.songalpha.insert(data)
            except pymongo.errors.DuplicateKeyError:
                pass

    def parsePicsXML(self):
        picglob = glob.glob(self.picdir)
        for m in picglob:
            with open(m, "r") as mf:
                myfile = mf.read()
            data = json.loads(myfile)
            try:
                pdb.pics.insert(data)
            except pymongo.errors.DuplicateKeyError:
                pass

    def parseAllXML(self):
        print("STARTING PARSEALLXML")
        self.parseMainXML()
        self.parseCredsXML()
        self.parseArtViewXML()
        self.parseAlbViewXML()
        self.parseSongViewXML()
        self.parseArtAlphaXML()
        self.parseAlbAlphaXML()
        self.parseSongAlphaXML()
        self.parsePicsXML()
        print('PARSEALLXML IS COMPLETE')

if __name__ == "__main__":
    pmx = ParseMyXML()
    pmx.parseAllXML()
    