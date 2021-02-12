from django.db import models
from django.utils import timezone


class PartnerLog(models.Model):
    create_at = models.DateTimeField("Дата создания")
    partner_id = models.PositiveBigIntegerField("ID партнера")

    class Meta:
        db_table = 'partner_log'
        verbose_name = 'Лог партнера'
        verbose_name_plural = 'Логи партнеров'

    def __str__(self):
        return f"ID logs: {self.id} => дата создания: {self.create_at}"

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        super(PartnerLog, self).save(*args, **kwargs)
        return self