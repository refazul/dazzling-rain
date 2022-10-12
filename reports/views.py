from .models import Police
from wkhtmltopdf.views import PDFTemplateView
from django.views.generic import TemplateView

class MyPDF(PDFTemplateView):
    filename = 'pdf.pdf'
    template_name = 'pdf.html'
    model = Police
    cmd_options = {
        'margin-top': 3
    }
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        police_id = self.kwargs['police_id']
        police = Police.objects.get(pk=police_id)
        
        context['fields'] = Police._meta.get_fields()
        context['object'] = police
        
        return context