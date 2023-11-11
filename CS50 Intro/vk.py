import sys
import json
import requests
import csv


def take_100_posts():

	token = '701191ca701191ca701191ca1c7307d0d477011701191ca155fd77325aacf6af914a00c'
	version = 5.154
	domain = 'ssshhhiiittt'
	count = 10
	offset = 0
	all_posts = []

	while offset < 100:
		response = requests.get("https://api.vk.com/method/wall.get",
								params={
									'access_token': token,
									'v': version,
									'domain' : domain,
									'count': count,
									'offset': offset
								}
								)

		data = response.json()['response']['items']
		offset += 100
		all_posts.extend(data)
	return all_posts



def file_writer(data):
	with open('ssshhhiiittt.csv', 'w') as file:
		a_pen = csv.writer(file)
		a_pen.writerow(('likes', 'body', 'url'))
		for post in data:
			try:
				if post['attachments'][0]['type']:
					img_url = post['attachments'][0]['photo']['sizes'][-1]['url'] 
				else:
					img_url = 'pass'
			except:
				pass
			a_pen.writerow((post['likes']['count'], post['text'], img_url))

all_posts = take_100_posts()
file_writer(all_posts)

