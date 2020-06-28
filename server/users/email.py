from djoser.email import ActivationEmail


class CustomActivationEmail(ActivationEmail):
    template_name = 'email/activation_new.html'

    def get_context_data(self):
        context = super().get_context_data()

        context['site_name'] = 'Envelope Budget'
        return context
