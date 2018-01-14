from lib import *
import csv

languages = ['javascript','java','python','php','ruby','c++','c', 'csharp','objective-c','R','go','perl','viml', 'swift','scala','haskell','lua','clojure']

repos = dict()
count = dict()
for language in languages:
    selected = getpickle('./data/{}/selected2'.format(language))
    print(language,len(selected))
    count[language] = len(selected)
    for repo in selected:
        if repo[0]['full_name'] not in repos:
            repos[repo[0]['full_name']] = repo[0]

print("NUMBER OF REPOS: {}".format(len(repos)))

with open('../repos.csv','w+') as f:
    keylist = []
    for rep_name in repos:
        keylist = repos[rep_name].keys()
        break
    wr = csv.DictWriter(f,fieldnames=keylist)
    wr.writeheader()
    for repo_name in repos:
        for key in repos[repo_name]:
            repos[repo_name][key] = unicode(repos[repo_name][key]).encode("utf-8")
        wr.writerow(repos[repo_name])


'''
with open('../repos.csv','w+') as f:
        wr = csv.DictWriter(f,fieldnames=selected[0][0].keys())
        wr.writeheader()
        for repo in selected:
            for key in repo[0].keys():
                repo[0][key] = unicode(repo[0][key]).encode("utf-8")
            wr.writerow(repo[0])
    f.close()
'''
