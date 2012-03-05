"""
Date: 18 February 2012
Description:provides an easy to use interface for communicating with the peoplebrowsr API system.

as of the date of publication of this library, the kred API includes methods of kredscore and kred
kred method parameters in addtion to app_id and app_key
	source*
	term*
	
kredscore method parameters in addtion to app_id and app_key				
	source*
	term*
	
*denotes required parameters
"""
class Kred:

	def __init__(self, app_id, app_key):
		self.app_id = app_id
		self.app_key = app_key
		self.url = "http://api.kred.ly"
		
	def Kred(self, source, term, influence = "", influenceCommunities = "", name = "", outreach = "", outreachCommunities = ""):
		url = self.url + '/kred'
		query = "app_id=" + self.app_id
		query = query + "&app_key=" + self.app_key
		if influence != "":
			query = query + "&influence=" + influence
		if influenceCommunities != "":
			query = query + "&influence_communities=" + influenceCommunities
		if name != "":
			query = query + "&name=" + name
		if outreach != "":
			query = query + "&outreach=" + outreach
		if outreachCommunities != "":
			query = query + "&outreach_communities=" + outreachCommunities
		query = query + "&source=" + source
		query = query + "&term=" + term
		return self.GET(url, query)
		
	def Kredscore(self, source, term, influence = "", name = "", outreach = ""):
		url = self.url + '/kredscore'
		query = "app_id=" + self.app_id
		query = query + "&app_key=" + self.app_key
		if influence != "":
			query = query + "&influence=" + influence
		if name != "":
			query = query + "&name=" + name
		if outreach != "":
			query = query + "&outreach=" + outreach
		query = query + "&source=" + source
		query = query + "&term=" + term
		return self.GET(url, query)
			
	def GET(self, url, query):
		import urllib2
		response = urllib2.urlopen( url + "?" + query ).read()
		return response