#!/usr/bin/python3

import os
import glob
import pymongo
from pymongo import MongoClient
import xml.etree.ElementTree as ET

MONGO_ADDR = os.environ["AMP_AMPDB_ADDR"]
VIEWSDB_ADDR = os.environ["AMP_VIEWSDB_ADDR"]
PICDB_ADDR = os.environ['AMP_PICDB_ADDR']

# ampDBClient = pymongo.MongoClient(MONGO_ADDR)
# db = ampDBClient.ampnadoDB

# ampVDBClient = pymongo.MongoClient(VIEWSDB_ADDR)
# viewsdb = ampVDBClient.ampviewsDB

# ampPDBClient = pymongo.MongoClient(PICDB_ADDR)
# pdb = ampPDBClient.picdb
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
        self.maindir = "/usr/share/Ampnado/AmpBackup/ampnadoDB/main/*.xml"
        self.credsdir = "/usr/share/Ampnado/AmpBackup/ampnadoDB/user_creds/*.xml"
        self.artview = "/usr/share/Ampnado/AmpBackup/ampviewsDB/artistView/*.xml"
        self.albview = "/usr/share/Ampnado/AmpBackup/ampviewsDB/albumView/*.xml"
        self.songview = "/usr/share/Ampnado/AmpBackup/ampviewsDB/songView/*.xml"
        self.artalpha = "/usr/share/Ampnado/AmpBackup/ampviewsDB/artalpha/*.xml"
        self.albalpha = "/usr/share/Ampnado/AmpBackup/ampviewsDB/albalpha/*.xml"
        self.songalpha = "/usr/share/Ampnado/AmpBackup/ampviewsDB/songalpha/*.xml"
        self.picdir = "/usr/share/Ampnado/AmpBackup/picdb/pics/*.xml"

    def parseMainXML(self):
        print("STARTNG PARSEMAIN")
        mglob = glob.glob(self.maindir)
        mlist = []
        for m in mglob:
            tree = ET.parse(m)
            root = tree.getroot()
            clubs = {}
            for child in root:
                clubs.update({child.tag:child.text})
                mlist.append(clubs)
        for m in mlist:
            try:
                db.main.insert(m)
            except pymongo.errors.DuplicateKeyError:
                pass

    def parseCredsXML(self):
        cglob = glob.glob(self.credsdir)
        clist = []
        for c in cglob:
            tree = ET.parse(c)
            root = tree.getroot()
            spades = {}
            for child in root:
                spades.update({child.tag:child.text})
                clist.append(spades)
        for c in clist:
            try:
                db.user_creds.insert(c)
            except pymongo.errors.DuplicateKeyError:
                pass

    def parseArtViewXML(self):
        arvglob = glob.glob(self.artview)
        arvlist = []
        for arv in arvglob:
            tree = ET.parse(arv)
            root = tree.getroot()
            spades = {}
            for child in root:
                spades.update({child.tag:child.text})
                arvlist.append(spades)
        for a in arvlist:
            try:
                viewsdb.albalpha.insert(a)
            except pymongo.errors.DuplicateKeyError:
                pass

    def parseAlbViewXML(self):
        avglob = glob.glob(self.albview)
        avlist = []
        for av in avglob:
            tree = ET.parse(av)
            root = tree.getroot()
            clubs = {}
            for child in root:
                clubs.update({child.tag:child.text})
                avlist.append(clubs)
        print(avlist)
        for a in avlist:
            try:
                viewsdb.albalpha.insert(a)
            except pymongo.errors.DuplicateKeyError:
                pass

    def parseSongViewXML(self):
        svglob = glob.glob(self.songview)
        svlist = []
        for sv in svglob:
            tree = ET.parse(sv)
            root = tree.getroot()
            hearts = {}
            for child in root:
                hearts.update({child.tag:child.text})
                svlist.append(hearts)
        for a in svlist:
            try:
                viewsdb.albalpha.insert(a)
            except pymongo.errors.DuplicateKeyError:
                pass

    def parseArtAlphaXML(self):
        arglob = glob.glob(self.artalpha)
        for ar in arglob:
            tree = ET.parse(ar)
            root = tree.getroot()
            diamonds = []
            for child in root:
                diamonds.append(child.text)
        bar = {"artalpha": diamonds}
        print('THIS IS ART ALPHA')
        print(bar)
        try:
            viewsdb.albalpha.insert(bar)
        except pymongo.errors.DuplicateKeyError:
            pass

    def parseAlbAlphaXML(self):
        aaglob = glob.glob(self.albalpha)
        spades = []
        for aa in aaglob:
            tree = ET.parse(aa)
            root = tree.getroot()
            
            for child in root:
                spades.append(child.text)
        foo = {"albalpha": spades}
        print('THIS IS ALB ALPHA')
        print(foo)
        try:
            viewsdb.albalpha.insert(foo)
        except pymongo.errors.DuplicateKeyError:
            pass

    def parseSongAlphaXML(self):
        saglob = glob.glob(self.songalpha)
        club = []
        for sa in saglob:
            tree = ET.parse(sa)
            root = tree.getroot()
            
            for child in root:
                club.append(child.text)
        zoo = {"songalpha": club}
        print('THIS IS SONG ALPHA')
        print(zoo)
        try:
            viewsdb.songalpha.insert(zoo)
        except pymongo.errors.DuplicateKeyError:
            pass

    def parsePicsXML(self):
        picglob = glob.glob(self.picdir)
        piclist = []
        for m in picglob:
            tree = ET.parse(m)
            root = tree.getroot()
            ace = {}
            for child in root:
                ace.update({child.tag:child.text})
                piclist.append(ace)
        for m in piclist:
            try:
                pdb.pics.insert(m)
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
    