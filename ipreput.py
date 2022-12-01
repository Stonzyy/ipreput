from ast import main
import json
import csv
from unicodedata import name
import requests
import sys
import argparse
import datetime
import time

#Twitter:@r00t_nasser


def abuseipdb():
	parser = argparse.ArgumentParser(description = 'description')
	parser.add_argument("-i", "--ips", required=True)
	parser.add_argument("-k", "--apikey", required=True)
	args = parser.parse_args()
	temp = 0
	#print(args.key)
	keys = open(f'{args.apikey}', 'r')
	for value in keys:
		api = value
	
	ips = open(f'{args.ips}', 'r')
	csv_file = "temp/spaces.csv"
	for ip in ips:
		url = 'https://api.abuseipdb.com/api/v2/check'
		querystring = {
		'ipAddress': ip,
		'maxAgeInDays': '90'
		}
		headers = {
        'Accept': 'application/json',
        'Key': api
        }
		try:
			handle_err = 0 
			
			response = requests.request(method='GET', url=url, headers=headers, params=querystring)
			while not response.ok:
				print('Error')
				time.sleep(5)
				response = requests.request(method='GET', url=url, headers=headers, params=querystring)


			decodedResponse = json.loads(response.text)
			print(json.dumps(decodedResponse, sort_keys=True, indent=4),file=open('result/result.json', 'a'))
			print(json.dumps(decodedResponse, sort_keys=True, indent=4),file=open('temp/temp.json', 'w'))
			f = open('temp/temp.json')

			data = json.load(f)
		
			for key, value in data.items():
				dic = [value]
				csv_columns = ['abuseConfidenceScore','countryCode','domain','hostnames','ipAddress','ipVersion','isPublic','isWhitelisted','isp','lastReportedAt','numDistinctUsers','totalReports','usageType']
				print(dic)
		except:
			raise
		try:
			with open(csv_file, 'a') as csvfile:
				
				writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
				if temp == 0:
					writer.writeheader()
				temp += 1
				for data in dic:
					
					writer.writerow(data)
		
		except IOError:
			print("I/O error")




def whitespace():
	date = datetime.datetime.now()
	print(f'\n\nResult saved successfully :  result/{date.year}-{date.day}-{date.month}-{date.hour}-{date.minute}-{date.second}.csv')
	with open('temp/spaces.csv','r') as f:
		content = f.readlines()
		cleaned = ''
		for line in content:
			if line != '\n':
				cleaned += line
		print(cleaned.replace(" ",""),file=open(f'result/{date.year}-{date.day}-{date.month}-{date.hour}-{date.minute}-{date.second}.csv', 'w'))




def clear():
	json = open("result/result.json","w")
	json.close()
	excel = open("temp/spaces.csv","w")



	excel.close()
def temp():
	temp = open("temp/temp.json","w")
	temp.close()




def main():
	abuseipdb()
	clear()
	temp()
	whitespace()




main()