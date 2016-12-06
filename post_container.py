# -*- coding: utf-8 -*-
""" 
post_container.py Semantic Web London Demo - AWS as LDP
"""

import boto3

s3 = boto3.resource('s3')

s3.Object('semantic-web-london', 'events/').put(
    ACL = 'private',
    Body = open('events.ttl', 'rb'),
    ContentType = 'text/turtle',
    Metadata = {'Link': '<http://www.w3.org/ns/ldp#BasicContainer>; rel="type", <http://www.w3.org/ns/ldp#Resource>; rel="type"'})