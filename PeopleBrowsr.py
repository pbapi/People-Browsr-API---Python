"""
Date: 18 February 2012
Description:provides an easy to use interface for communicating with the peoplebrowsr API system.

peoplebrowsr API method parameters in addtion to app_id and app_key
	source*
	term*
	first**
	last**
	count**
	period (Day, Hour)
	limit
	number
	reverse
	
*denotes required parameters
**denotes requires precisely two of these parameters passed in
"""
class PeopleBrowsr:

	def __init__(self, app_id, app_key):
		self.app_id = app_id
		self.app_key = app_key
		self.url = "http://api.peoplebrowsr.com"
		
	def atnamecloud(self, source, term, first = "", last = "", count = "", period = "", limit = "", number = "", reverse = ""):
		url = self.url + '/atnamecloud'
		query = "app_id=" + self.app_id
		query = query + "&app_key=" + self.app_key
		if last != "":
			query = query + "&last=" + last
		if first != "":
			query = query + "&first=" + first
		if count != "":
			query = query + "&count=" + count
		if period != "":
			query = query + "&period=" + period
		if limit != "":
			query = query + "&limit=" + limit
		if number != "":
			query = query + "&number=" + number
		if reverse != "":
			query = query + "&reverse=" + reverse
		query = query + "&source=" + source
		query = query + "&term=" + term
		return self.GET(url, query)
		
	def mentions(self, source, term, first = "", last = "", count = "", period = "", limit = "", number = "", reverse = ""):
		url = self.url + '/mentions'
		query = "app_id=" + self.app_id
		query = query + "&app_key=" + self.app_key
		if last != "":
			query = query + "&last=" + last
		if first != "":
			query = query + "&first=" + first
		if count != "":
			query = query + "&count=" + count
		if period != "":
			query = query + "&period=" + period
		if limit != "":
			query = query + "&limit=" + limit
		if number != "":
			query = query + "&number=" + number
		if reverse != "":
			query = query + "&reverse=" + reverse
		query = query + "&source=" + source
		query = query + "&term=" + term
		return self.GET(url, query)
		
	def density(self, source, term, first = "", last = "", count = "", period = "", limit = "", number = "", reverse = ""):
		url = self.url + '/density'
		query = "app_id=" + self.app_id
		query = query + "&app_key=" + self.app_key
		if last != "":
			query = query + "&last=" + last
		if first != "":
			query = query + "&first=" + first
		if count != "":
			query = query + "&count=" + count
		if period != "":
			query = query + "&period=" + period
		if limit != "":
			query = query + "&limit=" + limit
		if number != "":
			query = query + "&number=" + number
		if reverse != "":
			query = query + "&reverse=" + reverse
		query = query + "&source=" + source
		query = query + "&term=" + term
		return self.GET(url, query)
		
	def wordcloud(self, source, term, first = "", last = "", count = "", period = "", limit = "", number = "", reverse = ""):
		url = self.url + '/wordcloud'
		query = "app_id=" + self.app_id
		query = query + "&app_key=" + self.app_key
		if last != "":
			query = query + "&last=" + last
		if first != "":
			query = query + "&first=" + first
		if count != "":
			query = query + "&count=" + count
		if period != "":
			query = query + "&period=" + period
		if limit != "":
			query = query + "&limit=" + limit
		if number != "":
			query = query + "&number=" + number
		if reverse != "":
			query = query + "&reverse=" + reverse
		query = query + "&source=" + source
		query = query + "&term=" + term
		return self.GET(url, query)
		
	def hashtagcloud(self, source, term, first = "", last = "", count = "", period = "", limit = "", number = "", reverse = ""):
		url = self.url + '/hashtagcloud'
		query = "app_id=" + self.app_id
		query = query + "&app_key=" + self.app_key
		if last != "":
			query = query + "&last=" + last
		if first != "":
			query = query + "&first=" + first
		if count != "":
			query = query + "&count=" + count
		if period != "":
			query = query + "&period=" + period
		if limit != "":
			query = query + "&limit=" + limit
		if number != "":
			query = query + "&number=" + number
		if reverse != "":
			query = query + "&reverse=" + reverse
		query = query + "&source=" + source
		query = query + "&term=" + term
		return self.GET(url, query)
		
	def mentionsRetweets(self, source, term, first = "", last = "", count = "", period = "", limit = "", number = "", reverse = ""):
		url = self.url + '/mentions-retweets'
		query = "app_id=" + self.app_id
		query = query + "&app_key=" + self.app_key
		if last != "":
			query = query + "&last=" + last
		if first != "":
			query = query + "&first=" + first
		if count != "":
			query = query + "&count=" + count
		if period != "":
			query = query + "&period=" + period
		if limit != "":
			query = query + "&limit=" + limit
		if number != "":
			query = query + "&number=" + number
		if reverse != "":
			query = query + "&reverse=" + reverse
		query = query + "&source=" + source
		query = query + "&term=" + term
		return self.GET(url, query)	
		
	def friendsandfollowers(self, source, term, first = "", last = "", count = "", period = "", limit = "", number = "", reverse = ""):
		url = self.url + '/friendsandfollowers'
		query = "app_id=" + self.app_id
		query = query + "&app_key=" + self.app_key
		if last != "":
			query = query + "&last=" + last
		if first != "":
			query = query + "&first=" + first
		if count != "":
			query = query + "&count=" + count
		if period != "":
			query = query + "&period=" + period
		if limit != "":
			query = query + "&limit=" + limit
		if number != "":
			query = query + "&number=" + number
		if reverse != "":
			query = query + "&reverse=" + reverse
		query = query + "&source=" + source
		query = query + "&term=" + term
		return self.GET(url, query)
		
	def topFollowers(self, source, term, first = "", last = "", count = "", period = "", limit = "", number = "", reverse = ""):
		url = self.url + '/top-followers'
		query = "app_id=" + self.app_id
		query = query + "&app_key=" + self.app_key
		if last != "":
			query = query + "&last=" + last
		if first != "":
			query = query + "&first=" + first
		if count != "":
			query = query + "&count=" + count
		if period != "":
			query = query + "&period=" + period
		if limit != "":
			query = query + "&limit=" + limit
		if number != "":
			query = query + "&number=" + number
		if reverse != "":
			query = query + "&reverse=" + reverse
		query = query + "&source=" + source
		query = query + "&term=" + term
		return self.GET(url, query)
		
	def topPositiveFollowers(self, source, term, first = "", last = "", count = "", period = "", limit = "", number = "", reverse = ""):
		url = self.url + '/top-positive-followers'
		query = "app_id=" + self.app_id
		query = query + "&app_key=" + self.app_key
		if last != "":
			query = query + "&last=" + last
		if first != "":
			query = query + "&first=" + first
		if count != "":
			query = query + "&count=" + count
		if period != "":
			query = query + "&period=" + period
		if limit != "":
			query = query + "&limit=" + limit
		if number != "":
			query = query + "&number=" + number
		if reverse != "":
			query = query + "&reverse=" + reverse
		query = query + "&source=" + source
		query = query + "&term=" + term
		return self.GET(url, query)
		
	def topNegativeFollowers(self, source, term, first = "", last = "", count = "", period = "", limit = "", number = "", reverse = ""):
		url = self.url + '/top-negative-followers'
		query = "app_id=" + self.app_id
		query = query + "&app_key=" + self.app_key
		if last != "":
			query = query + "&last=" + last
		if first != "":
			query = query + "&first=" + first
		if count != "":
			query = query + "&count=" + count
		if period != "":
			query = query + "&period=" + period
		if limit != "":
			query = query + "&limit=" + limit
		if number != "":
			query = query + "&number=" + number
		if reverse != "":
			query = query + "&reverse=" + reverse
		query = query + "&source=" + source
		query = query + "&term=" + term
		return self.GET(url, query)							
		
	def popularity(self, source, term, first = "", last = "", count = "", period = "", limit = "", number = "", reverse = ""):
		url = self.url + '/popularity'
		query = "app_id=" + self.app_id
		query = query + "&app_key=" + self.app_key
		if last != "":
			query = query + "&last=" + last
		if first != "":
			query = query + "&first=" + first
		if count != "":
			query = query + "&count=" + count
		if period != "":
			query = query + "&period=" + period
		if limit != "":
			query = query + "&limit=" + limit
		if number != "":
			query = query + "&number=" + number
		if reverse != "":
			query = query + "&reverse=" + reverse
		query = query + "&source=" + source
		query = query + "&term=" + term
		return self.GET(url, query)
		
	def sentiment(self, source, term, first = "", last = "", count = "", period = "", limit = "", number = "", reverse = ""):
		url = self.url + '/sentiment'
		query = "app_id=" + self.app_id
		query = query + "&app_key=" + self.app_key
		if last != "":
			query = query + "&last=" + last
		if first != "":
			query = query + "&first=" + first
		if count != "":
			query = query + "&count=" + count
		if period != "":
			query = query + "&period=" + period
		if limit != "":
			query = query + "&limit=" + limit
		if number != "":
			query = query + "&number=" + number
		if reverse != "":
			query = query + "&reverse=" + reverse
		query = query + "&source=" + source
		query = query + "&term=" + term
		return self.GET(url, query)
		
	def topUsarea(self, source, term, first = "", last = "", count = "", period = "", limit = "", number = "", reverse = ""):
		url = self.url + '/top-usarea'
		query = "app_id=" + self.app_id
		query = query + "&app_key=" + self.app_key
		if last != "":
			query = query + "&last=" + last
		if first != "":
			query = query + "&first=" + first
		if count != "":
			query = query + "&count=" + count
		if period != "":
			query = query + "&period=" + period
		if limit != "":
			query = query + "&limit=" + limit
		if number != "":
			query = query + "&number=" + number
		if reverse != "":
			query = query + "&reverse=" + reverse
		query = query + "&source=" + source
		query = query + "&term=" + term
		return self.GET(url, query)
		
	def topcountries(self, source, term, first = "", last = "", count = "", period = "", limit = "", number = "", reverse = ""):
		url = self.url + '/topcountries'
		query = "app_id=" + self.app_id
		query = query + "&app_key=" + self.app_key
		if last != "":
			query = query + "&last=" + last
		if first != "":
			query = query + "&first=" + first
		if count != "":
			query = query + "&count=" + count
		if period != "":
			query = query + "&period=" + period
		if limit != "":
			query = query + "&limit=" + limit
		if number != "":
			query = query + "&number=" + number
		if reverse != "":
			query = query + "&reverse=" + reverse
		query = query + "&source=" + source
		query = query + "&term=" + term
		return self.GET(url, query)															
			
	def topurls(self, source, term, first = "", last = "", count = "", period = "", limit = "", number = "", reverse = ""):
		url = self.url + '/topurls'
		query = "app_id=" + self.app_id
		query = query + "&app_key=" + self.app_key
		if last != "":
			query = query + "&last=" + last
		if first != "":
			query = query + "&first=" + first
		if count != "":
			query = query + "&count=" + count
		if period != "":
			query = query + "&period=" + period
		if limit != "":
			query = query + "&limit=" + limit
		if number != "":
			query = query + "&number=" + number
		if reverse != "":
			query = query + "&reverse=" + reverse
		query = query + "&source=" + source
		query = query + "&term=" + term
		return self.GET(url, query)	
		
	def toppictures(self, source, term, first = "", last = "", count = "", period = "", limit = "", number = "", reverse = ""):
		url = self.url + '/toppictures'
		query = "app_id=" + self.app_id
		query = query + "&app_key=" + self.app_key
		if last != "":
			query = query + "&last=" + last
		if first != "":
			query = query + "&first=" + first
		if count != "":
			query = query + "&count=" + count
		if period != "":
			query = query + "&period=" + period
		if limit != "":
			query = query + "&limit=" + limit
		if number != "":
			query = query + "&number=" + number
		if reverse != "":
			query = query + "&reverse=" + reverse
		query = query + "&source=" + source
		query = query + "&term=" + term
		return self.GET(url, query)	
		
	def topvideos(self, source, term, first = "", last = "", count = "", period = "", limit = "", number = "", reverse = ""):
		url = self.url + '/topvideos'
		query = "app_id=" + self.app_id
		query = query + "&app_key=" + self.app_key
		if last != "":
			query = query + "&last=" + last
		if first != "":
			query = query + "&first=" + first
		if count != "":
			query = query + "&count=" + count
		if period != "":
			query = query + "&period=" + period
		if limit != "":
			query = query + "&limit=" + limit
		if number != "":
			query = query + "&number=" + number
		if reverse != "":
			query = query + "&reverse=" + reverse
		query = query + "&source=" + source
		query = query + "&term=" + term
		return self.GET(url, query)							
		
	def GET(self, url, query):
		import urllib2
		response = urllib2.urlopen( url + "?" + query ).read()
		return response