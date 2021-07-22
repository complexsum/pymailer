# Author : Shubham Sharma
# Contact: shubhamjsharma10@gmail.com

from email.message import Message
from smtplib import SMTP, SMTPException


class EmailService:
    """Email service

    This class serves the purpose of sending the email messages to the clients. 
    Other modules can use this class for sending the email messsages.

    Examples
    --------
    >>> service = EmailService('host', '587', 'John', 'Secret')
    >>> service.sendmail(message)
    """

    def __init__(self,
                 host: str, port: int,
                 user: str, password: str) -> None:
        """Initialize a new instance.

        Parameters
        ----------
        host: str
            The name of remote host

        port: int
            The port to which to connect.

        user: str
            The email address from which to send email messages.

        passwd: str
            The password used for authenticating the email address 
            from which to send the email messages.
        """

        self._host = host
        self._port = port
        self._user = user
        self._password = password


    def sendmail(self, msg: Message) -> None:
        """Sends an email message using a SMTP connection.

        Parameters
        ----------
        msg: Message
            The Message object.

        Returns
        -------
        None
        
        Raises
        ------
        SMTPException
        """

        with SMTP(self._host, self._port) as smtp:
            smtp.ehlo()
            smtp.starttls()
            if self._password:
                smtp.login(self._user, self._password)

            send_errs = smtp.send_message(msg)
            # send_errs is a dictionary, with one entry for each
            # recipient that was refused.  Each entry contains a tuple of the SMTP
            # error code and the accompanying error message sent by the server.
