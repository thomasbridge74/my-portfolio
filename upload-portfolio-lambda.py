
import boto3
import zipfile
import StringIO
from botocore.client import Config
import mimetypes

def lambda_handler(event, context):
    
    sns = boto3.resource('sns')
    topic = sns.Topic('arn:aws:sns:eu-west-1:567418401012:deployPortfolio')
    initMessage = "Not yet set"
    
    try:
        s3 = boto3.resource("s3")
        s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))
        port_bucket = s3.Bucket("portfolio.aws.wibble.to")
        
        job = event.get("CodePipeline.job")
    
        if job:
            for artifact in job["data"]["inputArtifacts"]:
                if artifact["name"] == "MyAppBuild":
                    location = artifact["location"]["s3Location"]
            initMessage = "\n\nThis was initiated by codebuild"
        else:
            location = {
                "bucketName": "portfoliobuild.aws.wibble.to",
                "objectKey": "portfoliobuild.zip"
            }
            initMessage = "\n\nThis was initiated manually"

        print "Building Location from " + str(location)
		
        build_bucket = s3.Bucket(location["bucketName"])
		
        portfolio_zip = StringIO.StringIO()
        build_bucket.download_fileobj(location["objectKey"], portfolio_zip)
        		
        with zipfile.ZipFile(portfolio_zip) as myzip:
            for nm in myzip.namelist():
                obj = myzip.open(nm)
                port_bucket.upload_fileobj(obj, nm, ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
        print "Job Done"
        topic.publish(Subject = "Portfolio updated", Message="The portfolio website has been updated from the S3 bucket"+initMessage) 
        if job:
            codepipeline = boto3.client('codepipeline')
            codepipeline.put_job_success_result(jobId=job["id"])
    except:
		topic.publish(Subject = "Portfolio update failed", Message="The portfolio updatefailed.   Please check the logs"+initMessage)
		raise
    return "Hello from Lambda"