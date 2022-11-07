import json
import csv
import requests
import sys
import argparse


#Twitter:@r00t_nasser
def whitespace():
	with open('temp/spaces.csv','r') as f:
		content = f.readlines()
		cleaned = ''
		for line in content:
			if line != '\n':
				cleaned += line
		print(cleaned.replace(" ",""),file=open('result/result.csv', 'w'))


def clear():
	json = open("result/result.json","w")
	json.close()
	excel = open("temp/spaces.csv","w")

	excel.close()
def temp():
	temp = open("temp/temp.json","w")
	temp.close()

def neutrinoapi():
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--input", required=True)
	args = parser.parse_args()
	temp = 0
	ips = open('ips.txt', 'r')
	csv_file = "temp/spaces.csv"
	for ip in ips:
		url = 'https://api.abuseipdb.com/api/v2/check'
		querystring = {
		'ipAddress': ip,
		'maxAgeInDays': '90'
		}
		headers = {
        'Accept': 'application/json',
        'Key': '<api-key>'
        }
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
		try:
			with open(csv_file, 'a') as csvfile:
				
				writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
				if temp == 0:
					writer.writeheader()
				temp += 1
				for data in dic:
					print(data)
					writer.writerow(data)
		
		except IOError:
			print("I/O error")
clear()
neutrinoapi()
temp()
whitespace()
