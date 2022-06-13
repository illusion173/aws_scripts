import boto3
import pprint
import json
AWS_REGION = "us-west-2"

client = boto3.client("s3", region_name = AWS_REGION)
s3 = boto3.resource('s3')


i = 0
hash_bucket = {}
for bucket in s3.buckets.all():
    #print(bucket.name)    
    hash_bucket[i] = bucket.name
    i = i + 1

print("Table of S3 current Buckets")

print("----------------------------------")


pprint.pprint(hash_bucket)

#print(len(hash_bucket))

def show_bucket(bucket_num_delete):
    j = 1
    s3_bucket_name = hash_bucket[bucket_num_delete]
    s3_bucket = s3.Bucket(s3_bucket_name)
    for s3_object in s3_bucket.objects.all():
        print("    {}     {}".format(j, s3_object.key))
        j = j + 1
    print("")
    print("")

while 1:
    bucket_num_delete = int(input("Which bucket do you want to show all of the contents (Enter integer): "))
    
    if 0 >= bucket_num_delete > len(hash_bucket):
        print("invalid")
        continue

    print("Contents of {}" .format(hash_bucket[bucket_num_delete]))
    print("---------------------------------")
    show_bucket(bucket_num_delete)

    i = 0
    hash_bucket = {}
    for bucket in s3.buckets.all():
        #print(bucket.name)
    
        hash_bucket[i] = bucket.name
        i = i + 1

    print("Table of S3 current Buckets")

    print("----------------------------------")

    pprint.pprint(hash_bucket)

