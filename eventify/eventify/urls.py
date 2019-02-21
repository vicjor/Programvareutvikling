"""eventify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from event import views as event_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name="register"),
    path('profile/', user_views.profile, name="profile"),
    path('createEvent/', event_views.HtmlRender.createEventPage, name='create-event'),
    path('allEvents/', event_views.HtmlRender.allEvents, name='all-events'),
    path('myEvents/', event_views.HtmlRender.myEvents, name='my-events'),
    path('editEvent/', event_views.HtmlRender.editEvent, name='edit-event'),
    path('event/update/<int:post_id>/', event_views.EventViews.updateEvent, name='update-event'),
    path('event/remove/', event_views.EventViews.removeEvent, name='remove-event'),
    path('createEvent/event/create/', event_views.EventViews.createEvent, name='createEvent'),
    path('event/search/', event_views.EventViews.searchEvents, name='searchEvents'),
    path('event/details/', event_views.EventViews.eventDetails, name='eventDetails'),
    path('event/join/', event_views.EventViews.eventJoin, name='eventJoin'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('', include('event.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)