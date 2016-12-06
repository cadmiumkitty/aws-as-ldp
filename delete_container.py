# -*- coding: utf-8 -*-
""" 
delete_container.py Semantic Web London Demo - AWS as LDP
"""

import boto3

s3 = boto3.resource('s3')

s3.Object('semantic-web-london', 'events/').delete()