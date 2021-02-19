from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .factories.form import FormFactory
from .services.url import UrlService
from .exceptions.not_valid import NotValidException
from .exceptions.hash_exists import HashExists
from django.conf import settings

def url_view(request):
    if request.method == 'POST':
        form = FormFactory.get_form(request.POST)

        if form.is_valid():
            try:
                shortened_url = UrlService().generate_short_from_url(form)
            except NotValidException:
                return render(request, 'url_not_valid.html')
            except HashExists:
                return render(request, 'form.html', { 'is_custom': True, 'hash_exists': True })

            return render(request, 'submit_response.html', { 'shortened_url': shortened_url, 'scheme': settings.SCHEME })

    return HttpResponseNotFound()

def form_custom(request):
    return render(request, 'form.html', { 'is_custom': True })

def form(request):
    return render(request, 'form.html', { 'is_custom': False })

def redirect(request):
    if request.method == 'GET':
        short_url = request.build_absolute_uri()
        url = UrlService().get_url_from_short(short_url)

        if url is None:
            return render(request, 'url_not_found.html')
        else:
            return HttpResponseRedirect(url)
    else:
        return HttpResponseNotFound()