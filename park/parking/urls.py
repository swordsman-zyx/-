from django.conf.urls import url
from parking.views import ParkingView1,ParkingView2

urlpatterns = [
    url(r'^parking/(?P<company_name>\w+)/(?P<parking_name>\w+)$',ParkingView2.as_view()),
    url(r'^parking/(?P<parking_name>\w+)$',ParkingView2.as_view()),
    url(r'^parking$',ParkingView1.as_view()),

]