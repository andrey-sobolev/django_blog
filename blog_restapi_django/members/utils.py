import logging

from django.conf import settings
from pyhunter import PyHunter
import clearbit
from requests.exceptions import ConnectionError, Timeout, HTTPError


logger = logging.getLogger()


def check_email_hunter(email):
    try:
        # we could also use hunter.email_finder for get email list from domain and check is it include our email or not,
        # but I see that we don't get all emails using this function and I decide dont't use it
        verified = False
        hunter = PyHunter(settings.HUNTERIO_API_KEY)
        result = hunter.email_verifier(email)
        
        if isinstance(result, dict) and result.get('webmail', False) and not result.get('block', True):
            verified = True
    except (ConnectionError, Timeout, HTTPError) as ex:
        logger.error(f'Email hunter connection error {ex}')
    return verified


def get_clearbit_user_info(email):
    try:
        person = None
        clearbit.key = settings.CLEARBIT_SECRET_KEY
        person = clearbit.Person.find(email=email, stream=True)
    except (ConnectionError, Timeout, HTTPError) as ex:
        logger.error(f'Clearbit hunter connection error {ex}')
    except (clearbit.ClearbitError, clearbit.ParamsInvalidError):
        logger.exception(f'Clearbit error')
    return person
