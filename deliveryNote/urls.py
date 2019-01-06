from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CustomerDetailView, CustomerListView, DeliveryListView, DeliveryDetailView, AddressListView, AddressDetailView


urlpatterns = [
    url(r'customers/$', CustomerListView.as_view() ),
    url(r'customers/(?P<pk>\d+)/$', CustomerDetailView.as_view() ),
    url(r'delivery/$', DeliveryListView.as_view() ),
    url(r'delivery/(?P<pk>\d+)/$', DeliveryDetailView.as_view() ),
    url(r'address/$', AddressListView.as_view() ),
    url(r'address/(?P<pk>\d+)/$', AddressDetailView.as_view() ),
]

urlpatterns = format_suffix_patterns(urlpatterns)