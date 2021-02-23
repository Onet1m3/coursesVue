from django.db import models
from django.utils import timezone
from django.urls import reverse


class CourseCategory(models.Model):
    translation_lang = models.CharField(max_length=10, blank=True, null=True)
    parent_id = models.ForeignKey(to='self', on_delete=models.CASCADE, blank=True, null=True, verbose_name="Название родительской категории", related_name="children")
    name = models.CharField(max_length=150, verbose_name="Название категории")
    slug = models.CharField(max_length=150, blank=True, null=True, verbose_name="Ссылка категории")
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание категории")
    icon_class = models.CharField(max_length=100, blank=True, null=True)
    lft = models.PositiveIntegerField(blank=True, null=True)
    rgt = models.PositiveIntegerField(blank=True, null=True)
    depth = models.PositiveIntegerField(blank=True, null=True)
    type = models.CharField(max_length=11, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True, verbose_name="Активная ли категория")
    is_custom = models.BooleanField(blank=True, null=True)

    class Meta:
        db_table = 'course_category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f"{self.name}"


# class CoursePartner(models.Model):
#     course_id = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, related_name="partner_category", verbose_name="Отношение к категории")
#     partner_link = models.CharField(max_length=255, blank=True, null=True, verbose_name="Партнерская ссылка")
#     create_at = models.DateTimeField(verbose_name="Дата создания")
#     update_at = models.DateTimeField(verbose_name="Дата последнего изменения")

#     class Meta:
#         db_table = 'course_partner'
#         verbose_name = 'Партнер'
#         verbose_name_plural = 'Партнеры'

#     def __str__(self):
#         return f"ID: {self.id} => {self.course_id}"


#     def save(self, *args, **kwargs):
#         if not self.id:
#             self.created_at = timezone.now()
#         self.updated_at = timezone.now()
#         super(CoursePartner, self).save(*args, **kwargs)
#         return self


class School(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название школы")
    discription = models.TextField(default="")
    partner_link = models.CharField(max_length=255, blank=True, null=True, verbose_name="Партнерская ссылка")
    url = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ссылка на школу(внешняя)")
    picture = models.ImageField(upload_to='img/school/logo', verbose_name="Лого школы", blank=True, null=True)
    slug = models.CharField("Ссылка на школу(внутренняя)", max_length=250, unique=True, default="")

    class Meta:
        db_table = 'scholl'
        verbose_name = 'Школа'
        verbose_name_plural = 'Школы'

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("targetSchool", kwargs={"slug": self.slug})
    

class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, related_name="course_category", blank=True, null=True, verbose_name="Категория курса")
    school_name = models.ForeignKey(School, on_delete=models.CASCADE, related_name="course_school", blank=True, null=True, verbose_name="Онлайн школа курса")
    title = models.CharField(max_length=250, verbose_name="Название курса")
    description = models.TextField(blank=True, null=True, verbose_name="Описание курса")
    slug = models.CharField(max_length=150, blank=True, null=True, verbose_name="Ссылка на курс", unique=True)
    # from_to = models.CharField(max_length=250, blank=True, null=True) Вроде лишняя 
    date_start = models.DateField(blank=True, null=True, verbose_name="Дата начала курса")
    date_end = models.DateField(blank=True, null=True, verbose_name="Дата окончания курса")
    amount = models.DecimalField(max_digits=11, decimal_places=2, verbose_name="Стоимость курса")
    installment = models.BooleanField(default=False, verbose_name="Есть ли рассрочка платежа")
    raiting = models.PositiveIntegerField(default=0, verbose_name="Рэйтинг курса")
    create_at = models.DateTimeField(verbose_name="Дата создания курса")

    class Meta:
        db_table = 'course'
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        super(Course, self).save(*args, **kwargs)
        return self


