import requestsimport xbmcguiimport xbmcimport xbmcaddonfrom bs4 import BeautifulSoupimport StorageServerimport recache = StorageServer.StorageServer("seehd", 0.2)dialog = xbmcgui.Dialog()#Headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36' }GoodFiles = ['.mp4', '.mkv']class Scraper:	def __init__(self):		self.Base = 'https://seehd.pl'		self.TvBase = 'http://www.seehd.pl/%s-season-%s-episode-%s'		self.Search = ('/%s-watch-online')		self.links = []	def Index(self,type,term,year,imdb,torrents):		def GetTokens():			from cloudscraper2 import CloudScraper			scraper = CloudScraper.create_scraper()			ua = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'			scraper.headers.update({'User-Agent': ua})			try: cookies = scraper.get('http://www.seehd.pl/wp-content/themes/kickass-mediaspace/favicon.png').cookies.get_dict()			except Exception as e : xbmc.log("SCRAPER ERROR SEEHD  ::: %s" %e , level=xbmc.LOGNOTICE)			return (cookies, ua)		if type == 'MOVIE':			try:				term = term.replace(' ','-').replace(':','%3A')				cookies, ua = cache.cacheFunction(GetTokens)				headers = {'User-Agent': ua}				link = requests.get(self.Base+self.Search % term, cookies=cookies, headers=headers).text				dialog.ok("LINK",str(link))				filmname = term.title()				pattern = r'''(?i)<iframe.+?src="(.*?)"'''				findlinks = re.findall(pattern,link,flags=re.DOTALL)				dialog.ok("SEEHD",str(findlinks))				for links in findlinks:					if '24hd.be' in links:						key = links.rsplit('/',1)[1]						ref = links						headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',									'X-Requested-With' : 'XMLHttpRequest',									'Referer' : ref}						link = requests.post('https://24hd.be/api/source/%s' % key, headers=headers).json()						for i in link['data']:							source = i['file']							qual = i['label']							source = source+'|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'							if '1080' in qual:								title = ('SEEHD ( DIRECT ) | FHD | %s' % filmname)								quality = '2'							elif '720' in qual:								title = ('SEEHD ( DIRECT ) | HD | %s' % filmname)								quality = '3'							else:								title = ('SEEHD ( DIRECT ) | SD | %s' % filmname)								quality = '4'							self.links.append({'title': title, 'url': source, 'quality': quality, 'Debrid' : False, 'Direct' : True})					else:						title = ('SEEHD ( ResolveUrl ) | HD | %s' % filmname)						quality = '3'						self.links.append({'title': title, 'url': links, 'quality': quality, 'Debrid' : False, 'Direct' : False})				return self.links			except Exception as c:				xbmc.log("SCRAPER ERROR SEEHD  ::: %s" %c , level=xbmc.LOGNOTICE)		else: pass			try:				term = term.lower()
				season = re.findall(r'''(s\d+)''',term.lower(),flags=re.I)[0].replace('s0','').replace('e0','').replace('s','')				episode = re.findall(r'''(e\d+)''',term.lower(),flags=re.I)[0].replace('e0','').replace('e0','').replace('e','')				StartUrl = re.findall("(s[0-9][0-9]e[0-9][0-9])",term.lower())[0]				cookies, ua = cache.cacheFunction(GetTokens)				headers = {'User-Agent': ua}				link = requests.get(self.TvBase % (term.replace(StartUrl,'').replace(' ','-'),season,episode),cookies=cookies,headers=headers).text				filmname = term.title()				pattern = r'''(?i)<iframe.+?src="(.*?)"'''				findlinks = re.findall(pattern,link,flags=re.DOTALL)				for links in findlinks:					if '24hd.be' in links:						key = links.rsplit('/',1)[1]						ref = links						headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',									'X-Requested-With' : 'XMLHttpRequest',									'Referer' : ref}						link = requests.post('https://24hd.be/api/source/%s' % key, headers=headers).json()						for i in link['data']:							source = i['file']							qual = i['label']							source = source+'|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'							if '1080' in qual:								title = ('SEEHD ( DIRECT ) | FHD | %s' % filmname)								quality = '2'							elif '720' in qual:								title = ('SEEHD ( DIRECT ) | HD | %s' % filmname)								quality = '3'							else:								title = ('SEEHD ( DIRECT ) | SD | %s' % filmname)								quality = '4'							self.links.append({'title': title, 'url': source, 'quality': quality, 'Debrid' : False, 'Direct' : True})					else:						title = ('SEEHD ( ResolveUrl ) | HD | %s' % filmname)						quality = '3'						self.links.append({'title': title, 'url': links, 'quality': quality, 'Debrid' : False, 'Direct' : False})				return self.links			except Exception as c:				xbmc.log("SCRAPER ERROR SEEHD  ::: %s" %c , level=xbmc.LOGNOTICE)