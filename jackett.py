#!/usr/local/bin/python

# Package Modules
from models.torrent_results import TorrentResults
from structs.filtering_modes import FilteringMode
from structs.categories import Categories
from structs.trackers import Trackers
from models.movie import Movie
from models.tv import TV

# Supporting Modules
from urllib.parse import urlencode as urlencode
from pprint import pprint as pprint
import requests, re

class Jackett:
	API_KEY = ""
	HOST = "127.0.0.1"
	PORT = 9117

	def __init__(self, api_key, host=None, port=None):
		self.API_KEY = api_key
		if host: self.HOST = host
		if port: self.PORT = port

	def search(self, query, trackers=None, categories=None, sort_key=None):
		query = {"apikey": self.API_KEY, "Query": query}
		if trackers: query["Tracker[]"] = [tracker.value for tracker in trackers]
		if categories: query["Category[]"] = [category.value for category in categories]
		search_url = 'http://{}:{}/api/v2.0/indexers/all/results?{}'.format(
						self.HOST, self.PORT, urlencode(query, doseq=True))
		response = requests.get(search_url)
		if response.status_code == 200 and response.json()["Results"]:
			response = response.json()["Results"]
			if sort_key: response = sorted(response, key=lambda i: i[sort_key], reverse=True)
			return TorrentResults(response)
		else:
			return []

	def filter(self, results, mode):
		if mode == FilteringMode.MOVIE:
			return self._filterMovies(results)
		elif mode == FilteringMode.TV:
			return self._filterTV(results)
		return None

	def _filterMovies(self, results):
		matched = []
		for result in results:
			match = re.match("(.*?)(?:\.?\(?\+?)(\d{4}).*(720[pP]|1080[pP]|2160[pP]|4[kK])", result.Title)
			if (match):
				matched.append(Movie(result, match))
		return matched

	def _filterTV(self, results):
		matched = []
		for result in results:
			match = re.match("(.*?)(?:\.?\(?\+?)(?:[sS])(\d{1,2})(?:[eE])(\d{1,2}).*(720[pP]|2160[pP]|4[kK]|1080[pP])", result.Title)
			if (match):
				matched.append(TV(result, match))
		return matched


if __name__ == "__main__":
	jackett = Jackett(" ")

	results = jackett.search(" ",
					trackers=Trackers.public_trackers(),
					categories=Categories.all_tv(),
					sort_key='Seeders')
	results = jackett.filter(results, FilteringMode.TV)

	pprint(results)

	results = jackett.search(" ",
					trackers=Trackers.public_trackers(),
					categories=Categories.all_movies(),
					sort_key='Seeders')

	results = jackett.filter(results, FilteringMode.MOVIE)

	pprint(results)
