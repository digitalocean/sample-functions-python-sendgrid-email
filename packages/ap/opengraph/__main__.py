from http import HTTPStatus
import os
from opengraph_parse import parse_page

def main(args):
    '''
    Takes in the email address, subject, and message to send an email using SendGrid, 
    returns a json response letting the user know if the email sent or failed to send.

        Parameters:
            args: Contains the from email address, to email address, subject and message to send

        Returns:
            json body: Json response if the email sent successfully or if an error happened
    '''
    url = args.get("from")

    parsed_og_tags = parse_page(url, ["og:url", "og:image", "og:title", "og:type", "og:url", "og:description"])

    if response.status_code != 202:
        return {
            "statusCode" : response.status_code,
            "body" : "fail"
        }
    return {
        "statusCode" : HTTPStatus.ACCEPTED,
        "body" : parsed_og_tags
    }