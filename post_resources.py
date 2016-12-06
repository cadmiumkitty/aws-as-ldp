# -*- coding: utf-8 -*-
""" 
post_resources.py Semantic Web London Demo - AWS as LDP
"""

import boto3

s3 = boto3.resource('s3')

s3.Object('semantic-web-london', 'events/232354771').put(
    ACL = 'private',
    Body = open('232354771.ttl', 'rb'),
    ContentType = 'text/turtle',
    Metadata = {'Link': '<http://www.w3.org/ns/ldp#Resource>; rel="type"'})
    
s3.Object('semantic-web-london', 'events/233037799').put(
    ACL = 'private',
    Body = open('233037799.ttl', 'rb'),
    ContentType = 'text/turtle',
    Metadata = {'Link': '<http://www.w3.org/ns/ldp#Resource>; rel="type"'})

s3.Object('semantic-web-london', 'events/234237999').put(
    ACL = 'private',
    Body = open('234237999.ttl', 'rb'),
    ContentType = 'text/turtle',
    Metadata = {'Link': '<http://www.w3.org/ns/ldp#Resource>; rel="type"'})        