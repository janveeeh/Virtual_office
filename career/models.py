from django.db import models

class Career(models.Model):
    job_title = models.CharField(max_length=255)
    job_type = models.CharField(max_length=255)
    job_role = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    key_skills = models.CharField(max_length=255)
    exp = models.CharField(max_length=255)
    required_language = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    job_description = models.TextField()
    image = models.CharField(max_length=255)
    created_datetime = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'career'

    def __str__(self):
        return self.job_title


class CareerApplicant(models.Model):
    job_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    age = models.IntegerField()
    qualification = models.CharField(max_length=255)
    hq_per = models.CharField(max_length=255)
    high_school = models.CharField(max_length=255)
    higher_sec = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    about = models.TextField()
    resume = models.FileField(upload_to="career/resume", default='')
    created_datetime = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'career_applicant'

    def __str__(self):
        return self.job_id


class CareerApplication(models.Model):
    job_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    age = models.CharField(max_length=10)
    qualification = models.CharField(max_length=255)
    hq_per = models.CharField(max_length=255)
    high_school = models.CharField(max_length=255)
    higher_sec = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    about = models.TextField()
    resume = models.CharField(max_length=255)
    created_datetime = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'career_application'

    def __str__(self):
        return self.job_id

# Create your models here.
