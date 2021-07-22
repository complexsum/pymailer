# Author : Shubham Sharma
# Contact: shubhamjsharma10@gmail.com

"""Messaging utilities

Provides basic messaging utility functions.
"""

import mimetypes
from pathlib import Path
from typing import List, Optional, Union

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage, Message


def build_message(fr_addr: str,
                  to_addrs: List[str],
                  cc_addrs: List[str],
                  subject: str,
                  content: str,
                  htmlcontent: Optional[str] = None,
                  attachments: Optional[List[str]] = None) -> Message:
    """Creates a new email message.

    Parameters
    ----------
    fr_addr: str
        The sender's email address.

    to_addrs: list of str
        The primary recipient's email addresses.

    cc_addrs: list of str
        The secondary recipient's email addresses.
        If you don't want to specify the secondary recipients just pass in the empty list.

    subject: str
        The subject of message.

    content: str
        The body of email message in plain text format.

    htmlcontent: str, optional
        The body of email message in html format.

    attachments: list of str, optional
        The list of absolute filepaths associated with the files that are present 
        on the filesystem which you wish to attach to the email message.

    Returns
    -------
    Message
    """

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = fr_addr
    msg['To'] = ', '.join(to_addrs)

    if cc_addrs:
        msg['CC'] = ', '.join(cc_addrs)

    if content is not None:
        msg.set_content(content)
    
    if htmlcontent is not None:
        msg.add_alternative(htmlcontent, subtype='html')

    if attachments is not None:
        for filepath in attachments:
            # Guess the content type.
            ctype, encoding = mimetypes.guess_type(filepath)

            if ctype is None:
                # unknown file type
                # skip the attachment
                continue

            # for example,
            # if ctype is image/png
            # then maintype will be image
            # and subtype will be png
            maintype, subtype = ctype.split('/', maxsplit=1)

            with open(filepath, 'rb') as file:
                msg.add_attachment(file.read(),
                                   maintype=maintype,
                                   subtype=subtype,
                                   filename=Path(filepath).name)

    # Save email message?
    # For now its not required.
    # In general its good practice to save the messages

    return msg