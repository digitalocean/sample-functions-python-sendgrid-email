from http import HTTPStatus
from nis import match
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def translateCode(code):
    '''
    Takes in the sendgrid status code, 
    returns a http status code.

        Parameters:
            args: Contains the sendgrid error status code

        Returns:
            json statusCode: Json http error status code
    '''
    match code:
        case "60000":
            return HTTPStatus.BAD_REQUEST
        case "60001":
            return HTTPStatus.UNAUTHORIZED
        case "60002":
            return HTTPStatus.BAD_REQUEST
        case "60003":
            return HTTPStatus.TOO_MANY_REQUESTS
        case "60004":
            return HTTPStatus.BAD_REQUEST
        case "60005":
            return HTTPStatus.BAD_REQUEST
        case "60021":
            return HTTPStatus.FORBIDDEN
        case "60022":
            return HTTPStatus.UNAUTHORIZED
        case "60023":
            return HTTPStatus.NOT_FOUND
        case "60032":
            return HTTPStatus.BAD_REQUEST
        case "60033":
            return HTTPStatus.BAD_REQUEST
        case "60042":
            return HTTPStatus.BAD_REQUEST
        case "60046":
            return HTTPStatus.BAD_REQUEST
        case "60060":
            return HTTPStatus.SERVICE_UNAVAILABLE
        case "60064":
            return HTTPStatus.FORBIDDEN
        case "60065":
            return HTTPStatus.FORBIDDEN
        case "60066":
            return HTTPStatus.FORBIDDEN
        case "60069":
            return HTTPStatus.BAD_REQUEST
        case "60070":
            return HTTPStatus.BAD_REQUEST
        case "60071":
            return HTTPStatus.NOT_FOUND
        case "60072":
            return HTTPStatus.NOT_FOUND
        case "60073":
            return HTTPStatus.BAD_REQUEST
        case "60074":
            return HTTPStatus.BAD_REQUEST
        case "60075":
            return HTTPStatus.BAD_REQUEST
        case "60078":
            return HTTPStatus.FORBIDDEN
        case "60082":
            return HTTPStatus.FORBIDDEN
        case "60083":
            return HTTPStatus.FORBIDDEN
        case _ :
            return HTTPStatus.INTERNAL_SERVER_ERROR

def main(args):
    '''
    Takes in the email address, subject, and message to send an email using SendGrid, 
    returns a json response letting the user know if the email sent or failed to send.

        Parameters:
            args: Contains the from email address, to email address, subject and message to send

        Returns:
            json body: Json response if the email sent successfully or if an error happened
    '''
    key = os.getenv('API_KEY')
    user_from = args.get("from")
    user_to = args.get("to")
    user_subject = args.get("subject")
    content = args.get("content", "this message was sent from the sendgrid API")

    if not user_from:
        return {
            "statusCode" : HTTPStatus.BAD_REQUEST,
            "body" : "no user email provided"
        }
    if not user_to:
        return {
            "statusCode" : HTTPStatus.BAD_REQUEST,
            "body" : "no receiver email provided"
        }
    if not user_subject:
        return {
            "statusCode" : HTTPStatus.BAD_REQUEST,
            "body" : "no subject provided"
        }
    if not content:
        return {
            "statusCode" : HTTPStatus.BAD_REQUEST,
            "body" : "no content provided"
        }

    sg = SendGridAPIClient(key)
    message = Mail(
        from_email = user_from,
        to_emails = user_to,
        subject = user_subject,
        html_content = content)
    response = sg.send(message)

    if response.status_code != 202:
        code = translateCode(response.status_code)
        return {
            "statusCode" : code,
            "body" : "email failed to send"
        }
    return {
        "statusCode" : HTTPStatus.ACCEPTED,
        "body" : "success"
    }