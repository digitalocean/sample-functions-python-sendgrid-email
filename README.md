# Sample Function: Python "Sendgrid Emails"

## Introduction

This repository contains a sample Sendgrid Emails function written in Python. You are able to send an email using Sendgrid's API to email addresses with or without DMARCS. You can deploy it on DigitalOcean's App Platform as a Serverless Function component.
Documentation is available at https://docs.digitalocean.com/products/functions.

### Requirements

* You need a DigitalOcean account. If you don't already have one, you can sign up at [https://cloud.digitalocean.com/registrations/new](https://cloud.digitalocean.com/registrations/new).
* You need to create a SendGrid API key with Full Access to connect to your sendgrid account. You can learn more about it at https://docs.sendgrid.com/ui/account-and-settings/api-keys.
* You need to add your `API_KEY` to the `.env` file to connect to the SendGrid API.
* To send emails with valid email addresses, you have to set up sender authentication. You can learn more at https://docs.sendgrid.com/glossary/sender-authentication.
* To send emails to email address with DMARCS, you have to set up domain authentication. You can learn more at https://docs.sendgrid.com/ui/account-and-settings/how-to-set-up-domain-authentication.
* To deploy from the command line, you will need the [DigitalOcean `doctl` CLI](https://github.com/digitalocean/doctl/releases).


## Deploying the Function

```bash
# clone this repo
git clone git@github.com:digitalocean/sample-functions-python-emails.git
```

```
# deploy the project, using a remote build so that compiled executable matched runtime environment
> doctl serverless deploy sample-functions-python-emails --remote-build
Deploying 'sample-functions-python-emails'
  to namespace 'fn-...'
  on host 'https://faas-...'
Submitted action 'emails' for remote building and deployment in runtime python:default (id: ...)

Deployed functions ('doctl sls fn get <funcName> --url' for URL):
  - sample/emails
```

## Using the Function

```bash
doctl serverless functions invoke presign/url -p from:user@do.com to:user@gmail.com subject:Sammy content:Good Morning from Sammy!
```
```json
{
  "body": "email sent"
}
```

### To send an email using curl:
```
curl -X PUT -H 'Content-Type: application/json' {your-DO-app-url} -d '{"from":"user@do.com", "to":"user@gmail.com", "subject": "Sammy", "content":"Good Morning from Sammy!"}' 
```

### Learn More

You can learn more about Functions and App Platform integration in [the official App Platform Documentation](https://www.digitalocean.com/docs/app-platform/).