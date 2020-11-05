#!/usr/bin/python3

import os
import glob
import pymongo
import xml.etree.ElementTree as ET

MONGO_ADDR = os.environ["AMP_AMPDB_ADDR"]
VIEWSDB_ADDR = os.environ["AMP_VIEWSDB_ADDR"]
PICDB_ADDR = os.environ['AMP_PICDB_ADDR']

ampDBClient = pymongo.MongoClient(MONGO_ADDR)
db = ampDBClient.ampnadoDB

ampVDBClient = pymongo.MongoClient(VIEWSDB_ADDR)
viewsdb = ampVDBClient.ampviewsDB

ampPDBClient = pymongo.MongoClient(PICDB_ADDR)
pdb = ampPDBClient.picdb

class ParseMyXML:
    def __init__(self):
        self.maindir = "/home/teresa/Desktop/AmpBackup/ampnadoDB/main/*.xml"
        self.artview = "/home/teresa/Desktop/AmpBackup/ampviewsDB/artistView/*.xml"
        self.albview = "/home/teresa/Desktop/AmpBackup/ampviewsDB/albumView/*.xml"
        self.songview = "/home/teresa/Desktop/AmpBackup/ampviewsDB/songView/*.xml"
        self.artalpha = "/home/teresa/Desktop/AmpBackup/ampviewsDB/artalpha/*.xml"
        self.albalpha = "/home/teresa/Desktop/AmpBackup/ampviewsDB/albalpha/*.xml"
        self.songalpha = "/home/teresa/Desktop/AmpBackup/ampviewsDB/songalpha/*.xml"
        self.picdir = "/home/teresa/Desktop/AmpBackup/picdb/pics/*.xml"

    def parseMainXML(self):
        mglob = glob.glob(self.maindir)
        mlist = []
        for m in mglob:
            tree = ET.parse(m)
            root = tree.getroot()
            clubs = {}
            for child in root:
                clubs.update({child.tag:child.text})
                mlist.append(clubs)
        print(mlist)
        for m in mlist:
            print("inserting main record")
            viewsdb.albalpha.insert(m)

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
        print(arvlist)
        for a in arvlist:
            print("inserting in to artview")
            viewsdb.albalpha.insert(a)

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
            print("inserting insto albumview")
            viewsdb.albalpha.insert(a)

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
        print(svlist)
        for a in svlist:
            viewsdb.albalpha.insert(a)

    def parseArtAlphaXML(self):
        arglob = glob.glob(self.artalpha)
        arlist = []
        for ar in arglob:
            tree = ET.parse(ar)
            root = tree.getroot()
            diamonds = {}
            for child in root:
                diamonds.update({child.tag:child.text})
                arlist.append(diamonds)
        print(arlist)
        for a in arlist:
            viewsdb.albalpha.insert(a)

    def parseAlbAlphaXML(self):
        aaglob = glob.glob(self.albalpha)
        aalist = []
        for aa in aaglob:
            tree = ET.parse(aa)
            root = tree.getroot()
            spades = {}
            for child in root:
                spades.update({child.tag:child.text})
                aalist.append(spades)
        print(aalist)
        for a in aalist:
            viewsdb.albalpha.insert(a)

    def parseSongAlphaXML(self):
        saglob = glob.glob(self.songalpha)
        salist = []
        for sa in saglob:
            tree = ET.parse(sa)
            root = tree.getroot()
            club = {}
            for child in root:
                club.update({child.tag:child.text})
                salist.append(club)
        print(salist)
        for s in salist:
            viewsdb.songalpha.insert(s)

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
        print(piclist)
        for m in piclist:
            pdb.pics.insert(m)

    def parseAllXML(self):
        self.parseMainXML()
        self.parseArtViewXML()
        self.parseAlbViewXML()
        self.parseSongViewXML()
        self.parseArtAlphaXML()
        self.parseAlbAlphaXML()
        self.parseSongAlphaXML()
        self.parsePicsXML()

if __name__ == "__main__":
    pmx = ParseMyXML()
    pmx.parseAllXML()
    