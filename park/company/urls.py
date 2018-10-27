from django.conf.urls import url
from company.views import CompanyView, CompaniesView

urlpatterns = [
    url(r'^company$', CompanyView.as_view()),
    url(r'^companies/(?P<company_name>\w+)$', CompanyView.as_view()),
    url(r'^companies/(?P<company_id>\w+)$', CompaniesView.as_view())
#
]