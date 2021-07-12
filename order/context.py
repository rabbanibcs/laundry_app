from order.models import Orders


def extras(request):
    total_pending = Orders.objects.filter(order_status='pending').count()

    return {'total_pending': total_pending}
