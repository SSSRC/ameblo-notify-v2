import requests
import re
import html

def getTitleFromURL(url):
  html_content = requests.get(url)
  title = re.findall(r'<meta data-react-helmet="true" property="og:title" content="『.*』"/>', html_content.text)[0]
  title = title.split('"/>')[0]
  title = title.split('<meta data-react-helmet="true" property="og:title" content="')[1]
  title = html.unescape(title)
  return title