# -*- coding: utf-8 -*-
import logging
import json

logger = logging.getLogger(__name__)

import firebase_admin
from firebase_admin import credentials, messaging

cred = credentials.Certificate({
  # YOUR CREDENTIALS
}
)
firebase_admin.initialize_app(cred)

def sendPush(notification, registration_token, dataObject=None):
    # Testing Data set.
    alert = {}
    message = {}
    alert['title']= 'notification.title'
    alert['text']= 'notification.text'
    alert['kind'] = 4
    alert['scholarship'] = {
        'id': 1,
        'name': 'Test Name',
    }
    alert['tip'] = {
        'id': 2,
        'title': 'notification.tip.title',
        'created_at': '08. 12,2021'
    }
    message['message'] = json.dumps(alert)
    dataObject = message
    try:
        message = messaging.Message(
            data=dataObject,
            token=registration_token
        )
        # Send a message to devices subscribed to the combination of topics
        # specified by the provided condition.
        response = messaging.send(message)
        # Response is a message ID string.
        print('Successfully sent message:', response)
    except Exception:
        logger.exception('Seding Push to Android')