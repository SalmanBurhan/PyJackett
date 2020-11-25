from enum import Enum

class Categories(Enum):
	MOVIES = 2000
	MOVIES_FOREIGN = 2010
	MOVIES_OTHER = 2020
	MOVIES_SD = 2030
	MOVIES_HD = 2040
	MOVIES_UHD = 2045
	MOVIES_BLURAY = 2050
	MOVIES_3D = 2060
	MOVIES_DVD = 2070
	MOVIES_WEBDL = 2080

	@classmethod
	def all_movies(self):
		return [self.MOVIES, self.MOVIES_FOREIGN,
				self.MOVIES_OTHER, self.MOVIES_SD,
				self.MOVIES_HD, self.MOVIES_UHD,
				self.MOVIES_BLURAY, self.MOVIES_3D,
				self.MOVIES_DVD, self.MOVIES_WEBDL]

	TV = 5000
	TV_WEBDL = 5010
	TV_FOREIGN = 5020
	TV_SD = 5030
	TV_HD = 5040
	TV_UHD = 5045
	TV_OTHER = 5050
	TV_SPORT = 5060
	TV_ANIME = 5070
	TV_DOCUMENTARY = 5080

	@classmethod
	def all_tv(self):
		return [self.TV, self.TV_WEBDL, self.TV_FOREIGN,
				self.TV_SD, self.TV_HD, self.TV_UHD, self.TV_OTHER,
				self.TV_SPORT, self.TV_ANIME, self.TV_DOCUMENTARY]
