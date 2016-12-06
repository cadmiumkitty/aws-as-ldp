# -*- coding: utf-8 -*-
""" 
delete_resources.py Semantic Web London Demo - AWS as LDP
"""

import boto3

s3 = boto3.resource('s3')

s3.Object('semantic-web-london', 'events/232354771').delete()

s3.Object('semantic-web-london', 'events/233037799').delete()

s3.Object('semantic-web-london', 'events/234237999').delete()