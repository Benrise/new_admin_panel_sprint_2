import os
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

User = get_user_model()


class Command(BaseCommand):
    help = 'Init superuser creation if none exists.'

    def handle(self, *args, **options):
        username = os.environ.get("DJANGO_ADMIN_USERNAME", "admin")
        email = os.environ.get("DJANGO_ADMIN_EMAIL", 'admin@example.ru')
        password = os.environ.get("DJANGO_ADMIN_PASSWORD", get_random_string(10))

        try:
            user, created = User.objects.get_or_create(
                username=username,
                defaults={'email': email, 'is_superuser': True}
            )

            if created:
                user.set_password(password)
                user.save()

                self.stdout.write(self.style.SUCCESS("==================================="))
                self.stdout.write(self.style.SUCCESS(f"A superuser '{username}' was created with "
                                                      f"email = '{email}' and password = '{password}'"))
                self.stdout.write(self.style.SUCCESS("==================================="))
            else:
                self.stdout.write(self.style.SUCCESS("Admin user found. Skipping superuser creation"))
                self.stdout.write(self.style.SUCCESS(f"Existing superuser: {user}"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"There was an error: {e}"))
