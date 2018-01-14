from lib import *
import csv

reader = csv.DictReader(open('../repos.csv','r'))
repo_list = []
for line in reader:
    repo_list.append(line)

stat_keys = ['full_name','id','distinct_releases','releases_mean_time','releases_median_time','first_release_date','last_release_date','total_time_days']
stats = []

def median(arr):
    m_ind = int(len(arr)/2)
    arr = sorted(arr)
    if m_ind == len(arr)/2:
        return arr[m_ind]
    return (arr[m_ind]+arr[m_ind+1])/2

for repo in repo_list:
    name = '|'.join(repo['full_name'].split('/'))
    reader = csv.DictReader(open('../Releases/{}.csv'.format(name)))
    releases = []
    for line in reader:
        releases.append(line)

    pub_dates = []
    for release in releases:
        pub_date = getdate(release['published_at'])
        if pub_date is not None:
            pub_dates.append(pub_date)

    pub_dates = sorted(pub_dates)
    ind = 0
    #print pub_dates
    while(ind<len(pub_dates)-1):
        if timedif(pub_dates[ind],pub_dates[ind+1])<3:
            pub_dates.pop(ind+1)
            ind -= 1
        ind += 1
    #print sorted(pub_dates)
    pub_dif = []
    for i in range(len(pub_dates)-1):
        pub_dif.append(timedif(pub_dates[i],pub_dates[i+1]))
    #print pub_dif

    mean_time = None
    median_time = None
    if len(pub_dif)>0:
        mean_time = sum(pub_dif)/len(pub_dif)
        median_time = median(pub_dif)
    else:
        print('[NOTE]',pub_dates)
    stats.append({
        'full_name': repo['full_name'],
        'id': repo['id'],
        'distinct_releases': len(pub_dates),
         'releases_mean_time': mean_time,
         'releases_median_time': median_time,
         'first_release_date': '-'.join(map(str,pub_dates[0])),
         'last_release_date': '-'.join(map(str,pub_dates[-1])),
         'total_time_days': timedif(pub_dates[0],pub_dates[-1])
    })

    print repo['full_name']

with open('../repo_stats_1.csv','w+') as f:
    writer = csv.DictWriter(f,fieldnames=stat_keys)
    writer.writeheader()
    for record in stats:
        for key in record:
            record[key] = unicode(record[key]).encode('utf-8')
        writer.writerow(record)
