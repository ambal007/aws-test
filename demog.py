def male_count_by_zip( zip ):
	lst=open('demog.csv').readlines()
	lst=txt.split('\n')[:-1]
	h=lst[0]
	lst2=h.split()
	tgt='count male'
	tgt=tgt.upper()
	ii=[i for i in range(len(lst2)) if lst2[i].find(tgt.split()[0])!=-1 and 
	lst2[i].find(tgt.split()[1])!=-1]
	print lst2[ii[0]],lst2[ii[1]]
	lst=lst[1:]
	d=[]
	for x in lst:
	  a=x[:-1].split(',')
	  if a[0]!=zip: continue
	  d=d+[(lst2[ii[0]].replace(',','_').lower(),a[ii[0]])]
	  d=d+[(lst2[ii[1]].replace(',','_').lower(),a[ii[1]])]
	d=dict(d)
	return d
########################################################
import requests
url='https://ambal007.s3.us-east-2.amazonaws.com/demog.csv'
r=requests.get(url);
txt= r.content
f=open('demog.csv','w+')
f.write( txt )
f.close()
print male_count_by_zip( '12423'  )


# amazon download example
#import boto3
#boto3.set_stream_logger('botocore', level='DEBUG')
#s3 = boto3.resource('s3')
#s3.Bucket('ambal007').download_file('demog.csv', '/tmp/demog.csv')
#
# botocore.exceptions.NoCredentialsError: Unable to locate credentials

#Overview 	Key 	demog.csv
#	Path    s3://ambal007/demog.csv
#	Size 	26.7 KB
#	Expiration date 	N/A
#	Expiration rule 	N/A
#	ETag 	48b3f3a2a13f1844867febfe1fcd2739
#	Last modified 	Oct 21, 2019 1:25:10 PM GMT-0400
#	Object URL 	https://ambal007.s3.us-east-2.amazonaws.com/demog.csv
#Properties 	Storage class 	Standard
#	Encryption 	None
#	Metadata 	1
#	Tags 	0 Tags
#	Object lock 	Disabled
#Permissions 	Owner 	
#	Object 	
#	Read 	1 Grantees
#	Object permissions 	
#	Read 	1 Grantees
#	Write 	1 Grantees
