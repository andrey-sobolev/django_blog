import logging

from config import celery_app

from members.models import User
from members.utils import get_clearbit_user_info
from members.serializers import ClearbitUserSerializer


logger = logging.getLogger()


@celery_app.task
def save_clearbit_user_info(user_id):
    try:
        user = User.objects.get(id=user_id)
        person = get_clearbit_user_info(user.email)
        if person:
            user_serializer = ClearbitUserSerializer(user, person['name'])
            if user_serializer.is_valid():
                user_serializer.save()
                logger.debug(f'{user_id} - clearbit get new information for user')
    except User.DoesNotExist:
        logger.error(f'{user_id} - user not found')
