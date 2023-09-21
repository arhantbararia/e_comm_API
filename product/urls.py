
from django.urls import path, include



urlpatterns = [
   
    path('api/' , include('product.api.urls')),
    #path('account/', include('e_comm.user_account.urls')),

    
]