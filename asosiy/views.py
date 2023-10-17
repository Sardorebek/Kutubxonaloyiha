from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect

from .models import *

def salomlash(request):
    return HttpResponse("<h1>Salom, Dunyo</h1>")

def homepage(request):
    return render(request, "home.html")

def hamma_kitoblar(request):
    content = {
        "kitoblar": Kitob.objects.all()

    }
    return render(request, "kitoblar.html", content)

def kitob(request, son):
    content = {
        "book": Kitob.objects.get(id=son)
    }
    return render(request, "mashq_uchun/kitob.html", content)

def muallif(request):
    sozlar = request.GET.get("qidirish_so'zi")
    javob = Muallif.objects.all()
    if sozlar:
        javob = javob.filter(ism__contains=sozlar)
    content = {
        "mualliflar": javob
    }
    return render(request,"muallif.html", content)

def muallif_ochir(request, son1):
    Muallif.objects.get(id=son1).delete()
    return redirect("/mualliflar/")

def tanlangan(request,nomlar):
    content = {
        "tanlanganlar": Muallif.objects.get(ism=nomlar)
    }
    return render(request, "tanlangan.html", content)

def hamma_record(request):
    soz = request.GET.get("qidirish_sozi")
    natija1 = Record.objects.all()
    if soz:
        natija1 = natija1.filter(ism__contains=soz)
    content = {
        "recordlar": natija1
    }
    return render(request, "hamma_record.html", content)

def record_ochir(request, son):
    Record.objects.get(id=son)
    return redirect("/recordlar/")
def tirik(request):
    content = {
        "tiriklar": Muallif.objects.filter(tirik=True)
    }
    return render(request, "tiriklar.html", content)

def eng_kop_sahifa(request):
    content = {
        "sahifalar": Kitob.objects.order_by("-sahifa")[:3]
    }
    return render(request, "eng_kop_sahifa.html", content)

def kitob_eng_kop_muallif(request):
    content = {
        "kitob_muallif": Kitob.objects.order_by("-muallif")[:3]
    }
    return render(request, "eng_kop_kitob_muallif.html", content)

def olingan_sana(request):
    content = {
        "record": Record.objects.order_by("olingan_sana")[:3]
    }
    return render(request, "record_sana.html", content)


def tiriklar(request):
    content = {
        "tirik": Muallif.objects.filter(tirik=True,kitoblar_soni=15)
    }
    return render(request, "tirik.html", content)

def janr(request):
    content = {
        "janrlar": Kitob.objects.filter(janr="Badiy")
    }
    return render(request, "janr.html", content)

def kitob_kichik(request):
    content = {
        "kichiklar": Muallif.objects.filter(kitoblar_soni__lt=10)
    }
    return render(request, "kichik_kitoblar.html", content)

def tanlangan_record(request,name):
    content = {
        "tanlangan_record": Record.objects.get(id=name)
    }
    return render(request, "tanlangan_recordlar.html", content)

def talabalar(request):
    soz = request.GET.get("qidirish_so'zi")
    natija = Talaba.objects.all()
    if soz:
        natija = natija.filter(ism__contains=soz)
    content = {
        "talabalar": natija
    }
    return render(request, "bitiruvchi_talabalar.html", content)

def talaba_ochir(request,son):
    Talaba.objects.get(id=son).delete()
    return redirect("/talabalar/")
