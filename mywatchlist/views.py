from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import AttributeWatchList

# Create your views here.
# Counter Function
def watch_counter(query):
    msg = ""
    done_count = 0
    ongoing_count = 0
    queued_count = 0

    for atr in query:
        if atr.watched == "Completed":
            done_count += 1
        else:
            ongoing_count += 1

    if done_count >= (ongoing_count + queued_count):
        msg = "Selamat, kamu sudah banyak menonton!"
    else:
        msg = "Wah, kamu masih sedikit menonton!"

    return msg


# HTML Show Watchlist
def show_watchlist_html(request):
    data_watchlist = AttributeWatchList.objects.all()
    message = watch_counter(data_watchlist)
    context = {
        'list_atr' : data_watchlist,
        'nama' : 'Arya Daniswara Khairan',
        'id' : '2106702781',
        'message' : message
    }
    return render(request, "watchlist.html", context)


# view json/xml
def show_watchlist_xml(request):
    data = AttributeWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_watchlist_json(request):
    data = AttributeWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


# view json/xml + id
def show_xml_by_id(request, id):
    data = AttributeWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = AttributeWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")