from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('unoporuno.views', 
                   url(r'^$','lista_busquedas'),
                   url(r'login/', 'show_login'),
                   url(r'login_cidesal/', 'login_cidesal'),
                   url(r'logout/', 'logout_cidesal'),
                   url(r'registro/', 'registro'),
                   url(r'registra_usuario/', 'registra_usuario'),
                   url(r'busquedas/','lista_busquedas'),
                   url(r'busqueda/(?P<busqueda_id>\d+)/$', 'busqueda'),
                   url(r'busqueda/(?P<busqueda_id>\d+)/persona/(?P<persona_id>\d+)/(?P<pipeline_id>(top|all))/(?P<features>\d+)/$', 'persona'),
                   url(r'busqueda/(?P<busqueda_id>\d+)/persona/(?P<persona_id>\d+)/(?P<pipeline_id>(top|all))/(?P<features>\d+)/options.html$', 'options'),
                   url(r'busqueda/(?P<busqueda_id>\d+)/persona/(?P<persona_id>\d+)/(?P<pipeline_id>(top|all))/(?P<features>\d+)/pipeline.html$', 'pipeline'),
                   url(r'busqueda/(?P<busqueda_id>\d+)/persona/(?P<persona_id>\d+)/evalua/$', 'evalua'),
                   url(r'busqueda/(?P<busqueda_id>\d+)/persona/(?P<persona_id>\d+)/pipeline/(?P<pipeline_id>(top|all))/(?P<features>\d+)/busca/$', 'busca'),
                   url(r'busqueda/(?P<busqueda_id>\d+)/persona/(?P<persona_id>\d+)/vinculos/$', 'vincula'),
                    )
  

