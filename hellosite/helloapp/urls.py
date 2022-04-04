from django.urls import path
from helloapp.views import HelloWorldView, HelloView, GoodbyeView

urlpatterns = [
    # helloapp/
    path('', HelloWorldView.as_view(), name='hello_world'),
    # for some reason, it only works when I put it 2nd here...? 
    # it wouldn't work when I put the goodbye view last? 
    path('<name>', GoodbyeView.as_view(), name='goodbye'), 
    path('<name>', HelloView.as_view(), name='hello_name'),
    

]