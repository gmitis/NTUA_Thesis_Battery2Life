from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Create an admin user if non exists'

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='giannismitis@gmail.com',
                password='admin'
            )
            logger.info(f'Superuser named admin created')
        else:    
            logger.info('Superuser named admin already exists')
