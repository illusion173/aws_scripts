import boto3
import pprint
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

def delete_bucket(bucket_num_delete):
    s3_bucket_name = hash_bucket[bucket_num_delete]
    s3_bucket = s3.Bucket(s3_bucket_name)
    for s3_object in s3_bucket.objects.all():
        s3_object.delete()
    # Deleting objects versions if S3 versioning enabled
    for s3_object_ver in s3_bucket.object_versions.all():
        s3_object_ver.delete()
    s3_bucket.delete()
    print("Deleted Bucket!")
    print("")
    print("")

while 1:
    bucket_num_delete = int(input("Which bucket do you want to delete (Enter integer): "))
    
    delete_bucket(bucket_num_delete)

    i = 0
    hash_bucket = {}
    for bucket in s3.buckets.all():
        #print(bucket.name)
    
        hash_bucket[i] = bucket.name
        i = i + 1

    print("Table of S3 current Buckets")

    print("----------------------------------")

    pprint.pprint(hash_bucket)





