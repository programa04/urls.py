# """mysite URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/dev/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

# """

from django.urls import path
from django.conf.urls import include, re_path
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
	path('busca/<str:busca>/', AjaxBusca.as_view(), name='AjaxBusca'),
	path('idioma/<str:langcode>/', AjaxIdioma.as_view(), name='AjaxIdioma'),
	path('idioma/cadastro/<str:langcode>/', AjaxIdiomaCadastro.as_view(), name='AjaxIdiomaCadastro'),
	path('aprentacao/download/<str:langcode>/', AjaLinkDownload.as_view(), name='AjaxApresentaDownload'),
	path('idioma/cpf/<str:langcode>/', AjaxIdiomaCPF.as_view(), name='AjaxCPF'),
	path('idioma/code/<str:langcode>/', AjaxIdiomaCode.as_view(), name='AjaxCode'),
	path('idioma/codigopais/<str:langcode>/', AjaxCodigoPais.as_view(), name='AjaxCodigoPais'),

]
urlpatterns += staticfiles_urlpatterns()
