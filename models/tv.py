from utilities import human_readable_size
from structs.qualities import Qualities
from enum import Enum

class TV:
	def __init__(self, result, match):
		self.show = match.group(1)
		self.season = match.group(2)
		self.episode = match.group(3)
		self.formatted_episode = 'S{}E{}'.format(self.season.zfill(2), self.episode.zfill(2))
		self.torrent_title = result.Title
		self.seeders = result.Seeders
		self.peers = result.Peers
		self.size = human_readable_size(result.Size)
		self.category = result.CategoryDesc
		self.tracker = result.Tracker
		self.published = result.PublishDate
		self.link = result.Guid

		if match.group(3).lower() == "2160p" or match.group(3).lower() == "4k":
			self.quality = Qualities.UltraHD
		elif match.group(3).lower() == "1080p":
			self.quality = Qualities.FullHD
		elif match.group(3).lower() == "720p":
			self.quality = Qualities.HD
		else:
			self.quality = None

		if result.Link:
			self.download = result.Link
		elif result.MagnetUri:
			self.download = result.MagnetUri
		else:
			self.download = None

	def __str__(self):
		return 'TV(show='+self.show+', season='+str(self.season)+', episode='+str(self.episode)+', seeders='+str(self.seeders)+')'

	def __repr__(self):
		return 'TV(show='+self.show+', season='+str(self.season)+', episode='+str(self.episode)+', seeders='+str(self.seeders)+')'
