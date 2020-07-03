from decouple import config
from djoser.email import (ActivationEmail, ConfirmationEmail,
                          PasswordResetEmail, PasswordChangedConfirmationEmail,
                          UsernameChangedConfirmationEmail, UsernameResetEmail)


class CustomActivationEmail(ActivationEmail):
    template_name = 'email/activation_new.html'

    def get_context_data(self):
        context = super().get_context_data()

        context['site_name'] = config('SITE_NAME')
        context['url'] = f'{config("DOMAIN_NAME")}/{context["url"]}'
        return context


class CustomConfirmationEmail(ConfirmationEmail):
    template_name = "email/confirmation_new.html"


class CustomPasswordResetEmail(PasswordResetEmail):
    template_name = "email/password_reset_new.html"

    def get_context_data(self):
        # PasswordResetEmail can be deleted
        context = super().get_context_data()

        context['site_name'] = config('SITE_NAME')
        context['url'] = f'{config("DOMAIN_NAME")}/{context["url"]}'
        return context


class CustomPasswordChangedConfirmationEmail(PasswordChangedConfirmationEmail):
    template_name = "email/password_changed_confirmation_new.html"


class CustomUsernameChangedConfirmationEmail(UsernameChangedConfirmationEmail):
    template_name = "email/username_changed_confirmation_new.html"


class CustomUsernameResetEmail(UsernameResetEmail):
    template_name = "email/username_reset_new.html"

    def get_context_data(self):
        context = super().get_context_data()

        context['site_name'] = config('SITE_NAME')
        context['url'] = f'{config("DOMAIN_NAME")}/{context["url"]}'
        return context
