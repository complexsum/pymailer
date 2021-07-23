## About
A simple and convinient way to send emails in python

## Installation

## Usage guide

1. ### Importing the module

    ```py
    from messaging import EmailService, build_message
    ```

2. ### Build an email message
   * Simple `EmailMessage`

      ```python3
      message = build_message(fr_addr='john@company.com', # Sender
                              to_addrs=['peter@abc.com'], # List of recipients
                              cc_addrs=['emma@abc.com' ], # List of secondary recipents
                              subject='Subject of Email',
                              content="Plain text contents of the email")
      ```

   * Extended `EmailMessage` with html body and attachments

      ```py
      message = build_message(fr_addr='john@company.com', # Sender
                              to_addrs=['peter@abc.com'], # List of recipients
                              cc_addrs=['emma@abc.com' ], # List of secondary recipents
                              subject='Subject of Email',
                              content="Plain text contents of the email",
                              htmlcontent="<h1>Fancy</h1> html content of the email",
                              attachments=['absolute path to the attachment'])
      ```

3. ### Instantiate `EmailSevice` and send the `message`

    ```py
    service = EmailService(host='smtp.gmail.com',
                           port=587,
                           user='john@company.com',
                           password='This is super secret')

    service.sendmail(message)
    ```


### Additional notes:

- While creating `EmailService` its optional to specify the `password`. If the `password` is not specified it is assumed that the smtp email server does not require authentication.
