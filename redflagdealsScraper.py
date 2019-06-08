import requests
from bs4 import BeautifulSoup
import re
from operator import itemgetter
import pprint 
from urllib.parse import unquote
from textAnalyzer import hashtags


def getRFDThreads():
		regex_pattern = r"(https.*)"
		content = []
		r = requests.get("https://forums.redflagdeals.com/hot-deals-f9/")
		c = r.content

		soup = BeautifulSoup(c, "html.parser")
		threads = soup.find_all("div", "thread_info_title")

		for thread in threads:
			if (thread.find("a", "topictitle_retailer") == None):
				topic = ""
			else:
				topic = thread.find("a", "topictitle_retailer").text.strip()
			
			thread_link = str("https://forums.redflagdeals.com/" + thread.find("a", "topic_title_link")["href"])
			r_thread_content = requests.get(thread_link).content
			soup_thread = BeautifulSoup(r_thread_content, "html.parser")

			if (soup_thread.find("a", "autolinker_link") == None):
				link = ""
			else: 
				link = soup_thread.find("a", "autolinker_link")["href"]
				link = unquote(link)
				if (re.search(regex_pattern, link) !=None):
					link = re.search(regex_pattern, link).group(0)
			title = thread.find("a", "topic_title_link").text.strip()
			title = title.replace("/", "")
			if (thread.find("dd", "total_count") == None):
				points = 0
			else:
				points = int(thread.find("dd", "total_count").text.strip())
			if (points > 10 and title != ""):
				thread_env = hashtags(title)
				thread_hashtags = [a for a, b in thread_env]
				if (topic == ""):
					topic = [a for a, b in thread_env if b == 'ORG']

				content.append({"topic": topic, "link": link,  "title": title, "points": points, "hashtags": thread_hashtags})

		content = sorted(content, key=itemgetter('points'), reverse=True)
		return content

