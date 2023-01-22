from django.urls import path
from Post import views
from Reactions.views import like,love,funny,sad,wow,angry

urlpatterns = [
    path('explore/', views.index, name='home'),
    path('createpost/', views.NewPost, name='NewPost'),
    path('p/<uuid:post_id>/', views.PostDetails, name='post-details'),
    
    path('p/<uuid:post_id>/like', like, name="like"),
    path('p/<uuid:post_id>/love', love, name="love"),
    path('p/<uuid:post_id>/funny', funny, name="funny"),
    path('p/<uuid:post_id>/sad', sad, name="sad"),
    path('p/<uuid:post_id>/wow', wow, name="wow"),
    path('p/<uuid:post_id>/angry', angry, name="angry"),
    # path('<uuid:post_id>/favourite', views.favourite, name="favourite"),
]
