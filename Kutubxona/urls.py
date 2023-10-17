from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('salom/', salomlash),
    path('', homepage),
    path('kitoblar/', hamma_kitoblar),
    path('book/<int:son>/', kitob),
    path('mualliflar/', muallif),
    path('tanlanganlar/<str:nomlar>', tanlangan),
    path('recordlar/', hamma_record),
    path('tiriklar/', tirik),
    path('sahifalar/', eng_kop_sahifa),
    path('kitob_muallif/', kitob_eng_kop_muallif),
    path('record/', olingan_sana),
    path('tirik/', tiriklar),
    path('janrlar/', janr),
    path('kichiklar/', kitob_kichik),
    path('tanlangan_record/<str:name>', tanlangan_record),
    path('talabalar/', talabalar),
    path('talaba_ochir/<int:son>', talaba_ochir),
    path('muallif_ochir/<int:son1>/', muallif_ochir),
    path('record_ochir/<int:son>/', record_ochir),
]
