from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from order.admin import order_site
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('order/', include('order.urls')),
    path('customer/', include('customer.urls')),
    path('verification/', include('verify_email.urls')),
    path('admin/', admin.site.urls),
    path('order-admin/', order_site.urls),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = [
#     path('admin/', admin.site.urls, {'extra_context': {'mycontext': '123'}}),
# ]
