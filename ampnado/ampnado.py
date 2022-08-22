 #!/usr/bin/python3
###############################################################################
###############################################################################
	# LICENSE: GNU General Public License, version 2 (GPLv2)
	# Copyright 2015, Charlie J. Smotherman
	#
	# This program is free software; you can redistribute it and/or
	# modify it under the terms of the GNU General Public License v2
	# as published by the Free Software Foundation.
	#
	# This program is distributed in the hope that it will be useful,
 	# but WITHOUT ANY WARRANTY; without even the implied warranty of
	# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	# GNU General Public License for more details.
	#
	# You should have received a copy of the GNU General Public License
	# along with this program; if not, write to the Free Software
	# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
###############################################################################
###############################################################################
import os, time, argparse, glob
#import inputs as gp
import functions as fun
import findjpgs as fj
# import backup as BUP
# import parseJSONbackups as PJB
from data import Data
from pymongo import MongoClient
from pprint import pprint

MONGO_ADDR = os.environ["AMP_AMPDB_ADDR"]
VIEWSDB_ADDR = os.environ["AMP_VIEWSDB_ADDR"]
PICDB_ADDR = os.environ['AMP_PICDB_ADDR']

ampDBClient = MongoClient(MONGO_ADDR)
ampDBClient.drop_database("ampnadoDB")

ampvDBClient = MongoClient(VIEWSDB_ADDR)
ampvDBClient.drop_database("ampviewsDB")

picDBClient = MongoClient(PICDB_ADDR)
picDBClient.drop_database("picdb")

# db = ampDBClient.ampnadoDB

class SetUp():
	def __init__(self):
		print("SetUp HAS STARTED")
		FUN = fun.FindMedia()
		self.FUN = FUN
		FUNKY = fun.Functions()
		FUNKY.insert_user(os.environ["AMP_USERNAME"], os.environ["AMP_PASSWORD"])

	def gettime(self, at): return (time.time() - at)

	def main(self):
		atime = time.time()
		# print(os.environ)
		#self.set_env_vars()


		print("STARTING MAIN")
		# ckdir = "/usr/share/Ampnado/AmpBackup/ampnadoDB/main/*.json"
		# if len(glob.glob(ckdir)) != 0:
		# 	boo = PJB.ParseMyXML()
		# 	print('STARTING PARSE XML')
		# 	boo.parseAllXML()
		# else:
		print("THIS IS ELSE BLOCK")
		self.FUN.find_music(os.environ["AMP_MEDIA_PATH"])
		
		FJ = fj.FindMissingArt()
		FJ.globstuff()
		picdics = FJ.PicDics
		Data().tags_update_artID(picdics)
		btime = time.time()
		maintime = btime - atime
		print("Main DB setup time %s" % maintime)
		
		from functions import AddArtistId
		AddArtistId().add_artistids()
		ctime = time.time()
		artidtime = ctime - atime
		print("AddArtistId time %s" % artidtime)
		from functions import AddAlbumId
		AddAlbumId().add_albumids()
		dtime = time.time()
		albidtime = dtime - atime
		print("AddAlbumId time %s" % albidtime)
		from artistview import ArtistView
		from artistview import ArtistChunkIt
		AV = ArtistView().main()
		ArtistChunkIt().main(AV, os.environ["AMP_OFFSET_SIZE"])
		etime = time.time()
		artistviewtime = etime - atime
		print("Artistview time %s" % artistviewtime)		
		from albumview import AlbumView
		from albumview import AlbumChunkIt
		ALBV = AlbumView().main()
		AlbumChunkIt().main(ALBV, os.environ["AMP_OFFSET_SIZE"])
		ftime = time.time()
		albviewtime = ftime - atime
		print("Albumview time %s" % albviewtime)		
		from songview import SongView
		SongView().create_songView_db(os.environ["AMP_OFFSET_SIZE"])
		gtime = time.time()
		songviewtime = gtime - atime
		print("Songview time %s" % songviewtime)
		
		# bdirs = BUP.CreateBackupDirs()
		# bdirs.createbdir()
		# backup = BUP.CreateBackups()
		# backup.CreateAllBackups()

		# from functions import Indexes
		# Indexes().creat_db_indexes()
		# htime = time.time()
		# indextime = htime - atime
		# print("Index time %s" % indextime)
		
		# from functions import DbStats
		# DbStats().db_stats()
		# itime = time.time()
		# statstime = itime - atime
		# print("DBStats time is %s" % statstime)
		# from functions import RandomArtDb
		# RandomArtDb().create_random_art_db()
		# jtime = time.time()
		# ranarttime = jtime - atime
		# print("RandomArtDB time is %s" % ranarttime)
		ptime = time.time()
		t = ptime - atime
		print("SETUP HAS BEEN COMPLETED IN %s SECONDS" % t)

if __name__ == "__main__":
	su = SetUp()
	su.main()
	import ampserver as app
	app.main()
