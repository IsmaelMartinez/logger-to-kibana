from requests_aws4auth import AWS4Auth
import boto3

region = 'eu-west-1'
service = 'es'


def get_credentials() -> dict:
    credentials = boto3.Session().get_credentials()
    return AWS4Auth(
        credentials.access_key,
        credentials.secret_key,
        region,
        service,
        session_token=credentials.token
    )
