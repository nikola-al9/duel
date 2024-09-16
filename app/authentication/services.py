import uuid
from app.common.services import DataAbstract
from app.users.models import Account, RegistrationTokenEmail
from app.errors.services import trigger_exception
from app.emails.confirm_registration_email import get_confirm_registration_token, send_confirm_registration_email

def auth_user_get_jwt_secret_key(user: Account) -> str:
    return str(user.jwt_key)


def auth_jwt_response_payload_handler(token, user=None, request=None, issued_at=None):
    """
    Default implementation. Add whatever suits you here.
    """
    return {"token": token}


def auth_logout(user: Account) -> Account:
    user.jwt_key = uuid.uuid4()
    user.full_clean()
    user.save(update_fields=["jwt_key"])

    return user


class UserService(DataAbstract):
    def register_user(self):
        # make sure no user with this email exists
        if Account.objects.filter(email=self.validated_data["email"]).exists():
            return trigger_exception("This e-mail is already in use", 400)

        # create reg token email
        rte = RegistrationTokenEmail.objects.create(
            email=self.validated_data["email"],
            name=self.validated_data["name"]
        )

        # send email with confirmation token
        send_confirm_registration_email.delay(
            self.validated_data['name'],
            self.validated_data['email'],
            get_confirm_registration_token(rte.token)
        )

        return 200

    def set_password(self):
        # if password_1 and password_2 are not the same return error
        if self.validated_data["password_1"] != self.validated_data["password_2"]:
            return trigger_exception("Passwords are not the same", 400)

        try:
            rte = RegistrationTokenEmail.objects.get(token=self.validated_data["token"])
        except RegistrationTokenEmail.DoesNotExist:
            return trigger_exception("Token is invalid", 400)

        if rte.is_expired:
            trigger_exception("Token is expired", 400)

        email = rte.email
        name = rte.name
        rte.is_expired = True
        rte.save()

        # create user
        account = Account.objects.create(
            email=email,
            name=name,
            points=100
        )
        account.set_password(self.validated_data.get('password_1'))
        account.save()

        return account

    def update(self):
        user = self.user
        user.name = self.data.get('name')
        user.save()

        return 200
