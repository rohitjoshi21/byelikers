#!/usr/bin/python3

import requests,json

user_access_token = 'Your Token'

group_id = '105175086826459'

# Getting group posts id from the group
group_feed = json.loads(requests.get('https://graph.facebook.com/'+group_id+'/feed?access_token='+user_access_token).text)

group_post = []
for i in group_feed['data']:
	group_post.append(i['id'])

# Getting the reactors information from each post
for i in group_post:
	group_reaction = json.loads(requests.get('https://graph.facebook.com/'+i+'/reactions?access_token='+user_access_token).text)

	for j in group_reaction['data']:
		print(j['id'])
		print(j['name'])
		print(j['type'])
		print('_'*135)

