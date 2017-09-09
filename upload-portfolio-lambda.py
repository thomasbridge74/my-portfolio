
import boto3
import zipfile
import StringIO
from botocore.client import Config
import mimetypes

def lambda_handler(event, context):
    sns = boto3.resource('sns')
    topic = sns.Topic('arn:aws:sns:eu-west-1:567418401012:deployPortfolio')
        
    try:
        s3 = boto3.resource("s3")
        s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))
        port_bucket = s3.Bucket("portfolio.aws.wibble.to")
		
        build_bucket = s3.Bucket("portfoliobuild.aws.wibble.to")
		
        portfolio_zip = StringIO.StringIO()
        build_bucket.download_fileobj("portfoliobuild.zip", portfolio_zip)
        		
        with zipfile.ZipFile(portfolio_zip) as myzip:
            for nm in myzip.namelist():
                obj = myzip.open(nm)
                port_bucket.upload_fileobj(obj, nm, ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
        print "Job Done"
        topic.publish(Subject = "Portfolio updated", Message="The portfolio website has been updated from the S3 bucket") 
    except:
		topic.publish(Subject = "Portfolio update failed", Message="The portfolio updatefailed.   Please check the logs")
		raise
    return "Hello from Lambda"
    
    