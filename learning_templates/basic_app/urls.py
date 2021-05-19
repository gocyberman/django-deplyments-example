from django.conf.urls import url
from basic_app import views

# esto es una variable para Template Tagging, lo que significa es que
# django busca en la aplicación basica y busca las urls
app_name = 'basic_app'

urlpatterns = [
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
]
