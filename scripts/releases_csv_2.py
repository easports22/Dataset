from lib import *
import csv

languages = ['javascript','java','python','php','ruby','c++','c', 'csharp','objective-c','R','go','perl','viml', 'swift','scala','haskell','lua','clojure']

keylist = [u'id',u'created_at',u'published_at',u'name', u'body', 'author_url', 'author_id', 'author_login', u'assets_url',  u'url',  u'target_commitish', u'tarball_url', u'html_url', u'zipball_url', u'tag_name', u'draft', u'prerelease' ]

repos = dict()
count = dict()
for language in languages:
    selected = getpickle('../../Milestones/data/{}/selected2'.format(language))
    print(language,len(selected))
    count[language] = len(selected)
    for repo in selected:
        if repo[0]['full_name'] not in repos:
            repos[repo[0]['full_name']] = repo[1]

print("NUMBER OF REPOS: {}".format(len(repos)))

for repo_name in repos:
    file_name = '|'.join(repo_name.split('/'))+'.csv'
    with open('../Releases/'+file_name,'w+') as f:
        wr = csv.DictWriter(f,fieldnames=keylist)
        wr.writeheader()
        for release in repos[repo_name]:
            author = release['author']
            release.pop('author',None)
            if author is not None:
                release['author_url'] = author['url']
                release['author_id'] = author['id']
                release['author_login'] = author['login']
            release.pop('upload_url',None)
            release.pop('assets',None)
            for key in release:
                release[key] = unicode(release[key]).encode('utf-8')
            wr.writerow(release)

'''
    TEST

selected = getpickle('../../Milestones/data/c++/selected2')

with open('../../temp.csv','w+') as f:

    keylist = selected[0][1][0].keys()
    keylist.remove('author')
    keylist.remove('upload_url')
    keylist.remove('assets')
    keylist.append('author_url')
    keylist.append('author_id')
    keylist.append('author_login')
    print(keylist)
    
    wr = csv.DictWriter(f,fieldnames=keylist)
    wr.writeheader()
    for release in selected[0][1]:
        author = release['author']
        release.pop('author',None)
        release['author_url'] = author['url']
        release['author_id'] = author['id']
        release['author_login'] = author['login']
        release.pop('upload_url',None)
        release.pop('assets',None)
        for key in release:
            release[key] = unicode(release[key]).encode('utf-8')
        wr.writerow(release)

'''
