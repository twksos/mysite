from datetime import datetime
from django.db import models

# Create your models here.
class Programmer(models.Model):
    name = models.CharField(max_length=200)

    def pair_time(self):
        return Pair.objects.filter(programmer_0=self.id).__len__() + Pair.objects.filter(programmer_1=self.id).__len__()

    def pair_time_with(self, pair):
        return Pair.objects.filter(programmer_0=self.id,programmer_1=pair.id).__len__() + Pair.objects.filter(programmer_1=self.id,programmer_0=pair.id).__len__()

    def pair_with(self, programmer):
        Pair(programmer_0 = self,programmer_1 = programmer,date = datetime.now()).save()


class Pair(models.Model):

    programmer_0 = models.ForeignKey(Programmer, related_name='programmer_0')
    programmer_1 = models.ForeignKey(Programmer, related_name='programmer_1')
    date = models.DateTimeField()

    def natural_key(self):
        return self.programmer_0, self.programmer_1, self.date

    class Meta:
        unique_together = (('programmer_0', 'programmer_1', 'date'),)