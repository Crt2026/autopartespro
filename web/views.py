from django.views.generic import TemplateView
from django.conf import settings

class ReactAppView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Ensure we strip any accidental whitespace from the key
        mp_key = getattr(settings, 'MERCADOPAGO_PUBLIC_KEY', '')
        context['MERCADOPAGO_PUBLIC_KEY'] = str(mp_key).strip() if mp_key else ''
        return context
