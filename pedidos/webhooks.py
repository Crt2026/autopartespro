import json
import mercadopago
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Orden

@csrf_exempt
def mercadopago_webhook(request):
    if request.method == 'POST':
        try:
            # MP sends notification in query params or body depending on topic
            topic = request.GET.get('topic') or request.GET.get('type')
            payment_id = request.GET.get('id') or request.GET.get('data.id')

            if not payment_id and request.body:
                 data = json.loads(request.body)
                 payment_id = data.get('data', {}).get('id')

            if payment_id:
                sdk = mercadopago.SDK("APP_USR-e72d1962-1a6f-4a72-aa69-479b0c87a62f")
                payment_info = sdk.payment().get(payment_id)
                
                if payment_info['status'] == 200:
                    payment = payment_info['response']
                    orden_id = payment.get('external_reference')
                    
                    if orden_id:
                        orden = Orden.objects.get(id=orden_id)
                        
                        if payment['status'] == 'approved':
                            orden.estado = 'pagado'
                            orden.metodo_pago_id = str(payment_id)
                            orden.save()
                        elif payment['status'] == 'rejected':
                            orden.estado = 'rechazado'
                            orden.save()
            
            return HttpResponse(status=200)
            
        except Exception as e:
            print(f"Error en webhook: {e}")
            return HttpResponse(status=400)
    return HttpResponse(status=200)
