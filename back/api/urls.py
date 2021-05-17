from django.conf.urls import url
from api import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^department/$', views.DepartmentAPIClassView.departmentApi),
    url(r'^department/([0-9]+)$', views.DepartmentAPIClassView.departmentApi),
    url(r'^employee/$', views.EmployeeAPIClassView.employeeApi),
    url(r'^employee/([0-9]+)$', views.EmployeeAPIClassView.employeeApi),
    url(r'^SaveFile$', views.SaveFile),
    url(r'^login/$', obtain_jwt_token),
    url(r'^student/$', views.studentApi),
    url(r'^student/([0-9]+)$', views.studentApi),
    url(r'^course/$', views.courseApi),
    url(r'^course/([0-9]+)$', views.courseApi)
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)