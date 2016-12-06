# -*- coding: utf-8 -*-
""" 
import_and_deploy_ldp.py Semantic Web London Demo - AWS as LDP
"""

import boto3

client = boto3.client('apigateway')

api = client.import_rest_api(
    failOnWarnings = True,
    body = open('ldp.json', 'rb'))
    
client.create_deployment(
    restApiId = api['id'],
    stageName = 'prod',
    stageDescription = 'Production',
    description = 'Production',
    cacheClusterEnabled = False
)        