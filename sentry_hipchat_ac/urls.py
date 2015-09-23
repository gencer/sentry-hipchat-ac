from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
    url('^$', views.DescriptorView.as_view()),
    url('^addon/descriptor$', views.DescriptorView.as_view(),
        name='sentry-hipchat-ac-descriptor'),
    url('^addon/installable$', views.InstallableView.as_view(),
        name='sentry-hipchat-ac-installable'),
    url('^addon/installable/(?P<oauth_id>[^/]+)$',
        views.InstallableView.as_view()),
    url('^configuration/$', views.configure,
        name='sentry-hipchat-ac-config'),
    url('^configuration/signout$', views.sign_out,
        name='sentry-hipchat-ac-sign-out'),

    url('^sidebar/event-details$', views.event_details,
        name='sentry-hipchat-ac-event-details'),
    url('^sidebar/recent-events$', views.recent_events,
        name='sentry-hipchat-ac-recent-events'),

    url('^glance/recent-events$', views.recent_events_glance,
        name='sentry-hipchat-ac-recent-events-glance'),

    url('^event/link-message$', views.on_link_message,
        name='sentry-hipchat-ac-link-message')
)
