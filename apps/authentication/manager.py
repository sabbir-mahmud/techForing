from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    # create user
    def create_user(self, email, password=None, confirm_password=None):
        if not email:
            raise ValueError("Enter a valid email")

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    # create staff user
    def create_staffuser(self, email, password=None):
        user = self.create_user(email, password)
        user.staff = True
        user.save(using=self._db)
        return user

    # create super user / admin
    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user
