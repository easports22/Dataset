import json
import os, pickle
import requests
import codecs
import time
import datetime

head1 = {
	'Accept': 'application/vnd.github.v3+json'
}
perm = ('anonymoussaketjoshi','GitHubPass071')
perm2 = ('saketrule','GitHubPass071')
perm3 = ('saket0071','GitHubPass071')

#######  JSON
def jsontotext(itm):
	return json.dumps(itm,indent=4,sort_keys=True)

def gresp(itm):
	itm = json.loads(itm)
	return json.dumps(itm,indent=4,sort_keys=True)

######## FILE HANDLING
def makefold(path):
	if not os.path.exists(path):
		os.mkdir(path)

def send(filename,data):
	f = codecs.open(filename,'w+',encoding='utf-8')
	assert(f)
	f.write(data)
	f.close()

def getjson(filename):
	f = open(filename)
	itm = json.loads(f.read())
	f.close()
	return itm

######## pickle
def getpickle(filename):
	print("* Getting data *\n")
	with open(filename+'.pickle') as f:
		data = pickle.load(f)
	return data

def savepickle(data,filename):
	print("* Saving Data *\n")
	with open(filename+'.pickle','w') as f:
		pickle.dump(data,f)


######### REQUESTS
def req2(url,params={},head=head1):
	resp = requests.get(url,auth=perm3,params=params,headers=head)
	if resp.status_code == 200:
		return resp
	else:
		print("Error getting url: ",url)
		print(resp.text)
		return -1

######### time
def getdate(string):
	date = map(int,string[:10].split('-'))
	return date

def timedif(created,closed):
	return (closed[0]-created[0])*365 + (closed[1]-created[1])*30 + (closed[2]-created[2])

def getstamp(dt):
	s = str(dt[2]) +'/'+ str(dt[1]) +'/'+ str(dt[0])
	return time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple())
'''
parallel 2 brances:
1. Agile developemenet
2. Working from yt

1. process flow is -
SR(problem) => deadline 1, unsure

2. Don't know
Must push (must)

pln 11 - 14:
cls, almost timedif ! Sem 5 is icpc

(DBS??? - CD??? - still haven't submitted test and proect papers )
'''
