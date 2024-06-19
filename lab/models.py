from django.db import models
from user.models import LabAppointment

# Create your models here.

class LabResult(models.Model):
    lab_res_id = models.BigAutoField(primary_key=True)
    lab_appointment = models.ForeignKey(LabAppointment, on_delete=models.CASCADE)
    result = models.TextField(max_length=1000, verbose_name="Result Description")
    file = models.FileField(upload_to='lab_result', verbose_name="File", null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.result
