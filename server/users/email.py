from decouple import config
from djoser.email import ActivationEmail


class CustomActivationEmail(ActivationEmail):
    template_name = 'email/activation_new.html'

    def get_context_data(self):
        context = super().get_context_data()

        context['site_name'] = 'Envelope Budget'
        context['url'] = f'{config("DOMAIN_NAME")}/{context["url"]}'
        return context
