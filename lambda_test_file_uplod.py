
import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    
    SOURCE_BUCKET='source-test-sachin'
    DESTINATION_BUCKET='destiation-test-sachin'

    s3_resource = boto3.resource('s3')
    s3_client = boto3.client('s3')

    #This is the lambda fuction for
    # Check if there is are files source S3 Bucket
    # Upload thos file to Destination S3 bucket
    # IF no file is there in Source S3 Bucket print "No FIles"
    
    bucket = s3_resource.Bucket(SOURCE_BUCKET)
    dest_bucket = s3_resource.Bucket(DESTINATION_BUCKET)

    #count = bucket.objects.filter(Prefix=SOURCE_BUCKET)
    count = bucket.objects.all()
    
    #count total files in bucket
    
    totalCount = 0
    
    print('result :',len(list(count)))

    length = len(list(count))
    
    if (length==0):
    
        print('result :',len(list(count)))
        print("bucket is empety")
    
    else:
        
        print("bucket is not empety")
        
        for object in bucket.objects.all():
            print("print :",object.key)
            key1 = object.key
            sourceObject = { 'Bucket' : 'source-test-sachin', 'Key': object.key}
            destObject = { 'Bucket' : 'destiation-test-sachin', 'Key': object.key}
            s3_resource.meta.client.copy(sourceObject, 'destiation-test-sachin',key1)
        
            
        totalCount += 1
    
        print("file copied")
