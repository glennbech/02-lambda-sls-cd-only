import os
import json
import boto3
from UnleashClient import UnleashClient

def handler(event, context):

    client = boto3.client('comprehend')

## Process sentiment analysis onlyif the MOCK toggle is ON. Mock returns very Positive sentiment just in case
    body = event["body"]
    sentiment = client.detect_sentiment(LanguageCode = "en", Text = body)

    return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "sentiment ": json.dumps(sentiment)
            })
        }