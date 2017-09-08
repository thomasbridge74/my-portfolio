#!/usr/bin/python

import boto3
import zipfile
import StringIO
from botocore.client import Config
import mimetypes

s3 = boto3.resource("s3")
s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))

port_bucket = s3.Bucket("portfolio.aws.wibble.to")

build_bucket = s3.Bucket("portfoliobuild.aws.wibble.to")
# build_bucket.download_file("portfoliobuild.zip", "/tmp/portfolio.zip")

portfolio_zip = StringIO.StringIO()
build_bucket.download_fileobj("portfoliobuild.zip", portfolio_zip)

with zipfile.ZipFile(portfolio_zip) as myzip:
	for nm in myzip.namelist():
		obj = myzip.open(nm)
		port_bucket.upload_fileobj(obj, nm, 
			ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
		port_bucket.Object(nm).Acl().put(ACL='public-read')
		