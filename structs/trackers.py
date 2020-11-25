from enum import Enum

class Trackers(Enum):
	EZTV = "eztv"
	HON3YHD = "hon3yhd"
	ISOHUNT = "isohunt"
	KICKASS = "kickasstorrents"
	MAGNETDL = "magnetdl"
	RARGB = "rargb"
	SHOWRSS = "showrss"
	TORRENTDB = "torrentdb"
	TORRENTLEECH = "torrentleech"
	ONETHREETHREESEVENX = "1337x"

	@classmethod
	def all_trackers(self):
		return [self.EZTV, self.HON3YHD, self.ISOHUNT, self.KICKASS,
				self.MAGNETDL, self.RARGB, self.SHOWRSS, self.TORRENTDB,
				self.TORRENTLEECH, self.ONETHREETHREESEVENX]

	@classmethod
	def public_trackers(self):
		return [self.EZTV, self.ISOHUNT, self.KICKASS, self.MAGNETDL,
				self.RARGB, self.SHOWRSS, self.ONETHREETHREESEVENX]

	@classmethod
	def private_trackers(self):
		return [self.HON3YHD, self.TORRENTDB, self.TORRENTLEECH]
