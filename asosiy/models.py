from django.db import models

JINS = [
    ("Erkak", "Erkak"),
    ("Ayol", "Ayol")
]

JANR = [
    ("Badiy", "Badiy"),
    ("Ilmiy", "Ilmiy")
]


class Talaba(models.Model):
    ism = models.CharField(max_length=30)
    kurs = models.PositiveSmallIntegerField()
    kitob_soni = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.ism}"


class Muallif(models.Model):
    ism = models.CharField(max_length=30)
    jins = models.CharField(max_length=30, blank=True, choices=JINS)
    tugilgan_sana = models.DateField()
    kitoblar_soni = models.PositiveSmallIntegerField()
    tirik = models.BooleanField(blank=True)

    def __str__(self):
        return f"{self.ism}"


class Kitob(models.Model):
    nom = models.CharField(max_length=30)
    janr = models.CharField(max_length=8, blank=True, choices=JANR)
    sahifa = models.PositiveBigIntegerField()
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.nom}"


class Kutubxonachi(models.Model):
    ism = models.CharField(max_length=30)
    ish_vaqti = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.ism}"


class Record(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE,null=True)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE, null=True)
    kutubxonachi = models.ForeignKey(Kutubxonachi, on_delete=models.CASCADE,null=True)
    olingan_sana = models.DateField(auto_now_add=True)
    qaytarish_sana = models.DateField(auto_now_add=True, null=True)
    qaytardi = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.olingan_sana}"
