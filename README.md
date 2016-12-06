# Amazon Web Services as Linked Data Platform

## Semantic Web London October 2016

This code is from the third [Semantic Web London](https://www.meetup.com/semantic-web-london/events/234237999/) meetup in October 2016.

We talked about implementing [Linked Data Platform](https://www.w3.org/TR/ldp/) spec using [Amazon Web Servcices](https://aws.amazon.com/) tools.

## Intro

The talk focuses on the premise that you don't need complex and expensive infrastructure to host linked data.
Linked Data Platform (LDP) is a standard for exposing RDF resources and resource containers and AWS provides a set of tools that you can configure to expose
LDP interface to your data.  

Tools used in the demo are [S3](https://aws.amazon.com/documentation/s3/), [APIgateway](https://aws.amazon.com/api-gateway/) and [AIM](https://aws.amazon.com/iam/), 
but in the ideal world you would also mix in [Cognito](https://aws.amazon.com/cognito/), [Route53](https://aws.amazon.com/route53/), 
[CloudFront](https://aws.amazon.com/cloudfront/) and [CloudFormation](https://aws.amazon.com/cloudformation/).

## Future work

 1. Would be great to add Route53, Cognito and CDN
 1. Would be good to have fully conformant LDP definition in Swagger, not just part of the spec (I think this is doable)
 1. Perhaps going for a templated container in APIGateway is a good idea, so we don’t need to explicitly flatten the container content
 1. Add billing into LDP API, perhaps via S3 caller pays feature or log analysis (let's say you want to build a Bloomberg competitor on the cheap)
 1. LDP-in-a-box approach with CloudFormation

## References and inspiration

 1. MarkLogic case study https://d0.awsstatic.com/whitepapers/marklogic-on-aws.pdf
 1. RDF Data Management in Amazon Cloud http://dl.acm.org/citation.cfm?id=2320790
 1. Automatic mapping of web APIs http://datalegend.net/assets/paper7.pdf
 
## Demo

### Data

Sample RDF resources are individual meetup events (232354771.ttl), (233037799.ttl) and (234237999.ttl). Sample container is (events.ttl).

### Pre-requisites

You need to configure AWS credentials for boto3 to use; there are [many different ways](http://boto3.readthedocs.io/en/latest/guide/configuration.html), 
I've picked shared credentials file `~/.aws/credentials` and shared config `~/.aws/config` for this demo. 

Credentials file:

```
[default]
aws_access_key_id=foo
aws_secret_access_key=bar
aws_session_token=baz
```

Config file:

```
[default]
region=eu-west-1
```

### How to run

You'll need your own AWS account, bucket and key. I'm using Python and AWS Python client, [boto3](https://boto3.readthedocs.io/en/latest/reference/services/s3.html).

First get your environment and dependencies ready.

```
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
```

Then use the tools to upload flattened data into S3:

```
python3 post_container.py
python3 post_resources.py
```

Then create the API (I have cut out real identifiers from `ldp.json`, so you will need to create your own buckets, etc.):

```
python3 import_and_deploy_ldp.py
```