import requestsimport reimport xbmcguiimport xbmcimport xbmcaddondialog = xbmcgui.Dialog()from bs4 import BeautifulSoupHeaders = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36' }class Scraper:	def __init__(self):		self.Base = ('https://series.movie/%sseason-%s-episode-%s')		self.Search = ('search/%s')		self.links = []	def Index(self,type, term,year,imdb,torrents):		year = year.strip()		MovieTitle = term		term = term.lower()		if type == 'TV':			try:				season = re.findall(r'''(s\d+)''',term.lower(),flags=re.I)[0].replace('s0','').replace('e0','').replace('s','')				episode = re.findall(r'''(e\d+)''',term.lower(),flags=re.I)[0].replace('e0','').replace('e0','').replace('e','')				StartUrl = re.findall("(s[0-9][0-9]e[0-9][0-9])",term.lower())[0]				link = requests.get(self.Base % (term.replace(StartUrl,'').replace(' ','-'),season,episode),headers=Headers).text				soup = BeautifulSoup(link,'html.parser')				r = soup.select('li[data-video]')				for i in r:					try:						source = i['data-video']						if not source.startswith('http') : source = ('https:%s' % source)						if not 'load.php' in source and 'hydrax.net' not in source:							qual = 'HD'							quality = '7'							title = ('[COLOR white]WATCHSERIES ( Resolve Url ) | %s | %s[/COLOR]' % (qual,MovieTitle))							self.links.append({'title': title, 'url': source, 'quality': quality, 'Debrid' : False, 'Direct' : False})					except: pass				return self.links			except Exception as c:				xbmc.log("SCRAPER ERROR WatchSeries  ::: %s" %c , level=xbmc.LOGNOTICE)		else: pass