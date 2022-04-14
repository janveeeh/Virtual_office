from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models




class Admin(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'admin'
        unique_together = (('id', 'email'),)


class Adminlogin(models.Model):
    firstname = models.CharField(db_column='FirstName', max_length=255)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255)  # Field name made lowercase.
    emailid = models.CharField(db_column='EmailId', primary_key=True, max_length=20)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=20)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminlogin'


class AllCities(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'all_cities'


class AllInstitute(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    institute = models.CharField(db_column='Institute', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'all_institute'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BlogsDisplay(models.Model):
    images = models.CharField(max_length=255)
    heading = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(max_length=255)
    view = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'blogs_display'


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
    resume = models.CharField(max_length=255)
    created_datetime = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'career_applicant'


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


class Category(models.Model):
    category = models.CharField(max_length=255)
    category_for = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'category'


class ComplainType(models.Model):
    cmptypeid = models.AutoField(db_column='CmpTypeId', primary_key=True)  # Field name made lowercase.
    cmptype = models.CharField(db_column='CmpType', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'complain_type'


class Complains(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    orderid = models.CharField(db_column='OrderId', max_length=255)  # Field name made lowercase.
    complaintype = models.CharField(db_column='ComplainType', max_length=20)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=255)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10)  # Field name made lowercase.
    cmpby = models.CharField(db_column='CmpBy', max_length=20)  # Field name made lowercase.
    cmpsolveby = models.CharField(db_column='CmpSolveBy', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'complains'


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255)
    syllabus = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'course'


class CourseQuery(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    query_date = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'course_query'


class Createcertificate(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    empid = models.CharField(db_column='EmpId', max_length=255)  # Field name made lowercase.
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    signature = models.CharField(max_length=255)
    datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'createcertificate'

class Customer(models.Model):
    cusid = models.AutoField(db_column='CusId', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255)  # Field name made lowercase.
    emailid = models.CharField(db_column='EmailId', max_length=255)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=13)  # Field name made lowercase.
    address = models.TextField(db_column='Address')  # Field name made lowercase.
    pincode = models.CharField(db_column='Pincode', max_length=6)  # Field name made lowercase.
    aadhaar = models.CharField(db_column='Aadhaar', max_length=12)  # Field name made lowercase.
    empid = models.CharField(db_column='EmpId', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'


class DayWiseTask(models.Model):
    task_id = models.IntegerField(blank=True, null=True)
    task_title = models.CharField(max_length=255, blank=True, null=True)
    task_desc = models.TextField(blank=True, null=True)
    task_file = models.CharField(max_length=255, blank=True, null=True)
    task_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'day_wise_task'


class DayWiseTask1(models.Model):
    task_id = models.IntegerField()
    task_title = models.CharField(max_length=255)
    task_desc = models.TextField()
    task_file = models.CharField(max_length=255)
    task_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'day_wise_task1'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employee(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    empid = models.CharField(db_column='EmpId', max_length=50)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=20)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=20)  # Field name made lowercase.
    emailid = models.CharField(db_column='EmailId', max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=225)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=10)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pincode = models.IntegerField(db_column='Pincode', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)  # Field name made lowercase.
    institute = models.CharField(db_column='Institute', max_length=255, blank=True, null=True)  # Field name made lowercase.
    photograph = models.CharField(db_column='Photograph', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    aadhaar = models.CharField(db_column='Aadhaar', max_length=12, blank=True, null=True)  # Field name made lowercase.
    emptype = models.CharField(db_column='EmpType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    teamhead = models.CharField(db_column='TeamHead', max_length=255)  # Field name made lowercase.
    joiningdate = models.DateField(db_column='JoiningDate', blank=True, null=True)  # Field name made lowercase.
    start_date = models.CharField(max_length=255, blank=True, null=True)
    end_date = models.CharField(max_length=255, blank=True, null=True)
    log_in_time = models.CharField(max_length=255, blank=True, null=True)
    log_out_time = models.CharField(max_length=255, blank=True, null=True)
    hr = models.IntegerField(blank=True, null=True)
    certificate = models.CharField(max_length=10, blank=True, null=True)
    ac_status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'
        unique_together = (('id', 'empid'),)


class Galary(models.Model):
    title = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    category = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'galary'


class LoginDetails(models.Model):
    empid = models.CharField(db_column='EmpId', max_length=255)  # Field name made lowercase.
    login_time = models.CharField(max_length=255)
    logout_time = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'login_details'


class MailSystem(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.TextField()
    empid = models.CharField(db_column='EmpId', max_length=255)  # Field name made lowercase.
    forward_to = models.CharField(max_length=255)
    status = models.IntegerField()
    created_date = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mail_system'


class MailSystemHead(models.Model):
    mail_iden = models.CharField(max_length=255)
    mail_by = models.CharField(max_length=255)
    description = models.TextField()
    file = models.TextField()
    created_date = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mail_system_head'


class Meetings(models.Model):
    org_name = models.CharField(max_length=255)
    org_email = models.CharField(max_length=255)
    org_contact = models.CharField(max_length=255)
    desc = models.TextField()
    image = models.CharField(max_length=255)
    empid = models.CharField(db_column='EmpId', max_length=255)  # Field name made lowercase.
    datetime = models.DateTimeField()
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'meetings'


class Message(models.Model):
    empid = models.CharField(db_column='EmpId', max_length=255)  # Field name made lowercase.
    title = models.CharField(max_length=255)
    message = models.TextField()
    datetime = models.DateTimeField()
    status = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'message'


class Occasion(models.Model):
    message = models.TextField()
    status = models.CharField(max_length=255)
    datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'occasion'


class OurProducts(models.Model):
    productid = models.AutoField(db_column='ProductId', primary_key=True)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=255)  # Field name made lowercase.
    productvalidity = models.CharField(db_column='ProductValidity', max_length=20)  # Field name made lowercase.
    productprice = models.IntegerField(db_column='ProductPrice')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'our_products'


class PgrQuery(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    query_date = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    display = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'pgr_query'


class ProductComplains(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    product_id = models.CharField(max_length=255)
    cusid = models.CharField(db_column='CusId', max_length=255)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255)  # Field name made lowercase.
    empid = models.CharField(db_column='EmpId', max_length=255)  # Field name made lowercase.
    datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'product_complains'


class ProductPpt(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=255)  # Field name made lowercase.
    file = models.CharField(db_column='File', max_length=255)  # Field name made lowercase.
    datetime = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'product_ppt'


class RenewProduct(models.Model):
    renewproductid = models.AutoField(db_column='RenewProductId', primary_key=True)  # Field name made lowercase.
    productid = models.IntegerField(db_column='ProductId')  # Field name made lowercase.
    orderid = models.CharField(db_column='OrderId', max_length=50)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=20)  # Field name made lowercase.
    productvalidity = models.CharField(db_column='ProductValidity', max_length=10)  # Field name made lowercase.
    productprice = models.IntegerField(db_column='ProductPrice')  # Field name made lowercase.
    sellingprice = models.CharField(db_column='SellingPrice', max_length=50)  # Field name made lowercase.
    renewdate = models.CharField(db_column='RenewDate', max_length=255)  # Field name made lowercase.
    renewby = models.CharField(db_column='RenewBy', max_length=20)  # Field name made lowercase.
    cusid = models.CharField(db_column='CusId', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'renew_product'


class SoldProduct(models.Model):
    productid = models.IntegerField(db_column='ProductId')  # Field name made lowercase.
    orderid = models.CharField(db_column='OrderId', max_length=255)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=255)  # Field name made lowercase.
    productprice = models.CharField(db_column='ProductPrice', max_length=255)  # Field name made lowercase.
    sellingprice = models.CharField(db_column='SellingPrice', max_length=50)  # Field name made lowercase.
    solddate = models.CharField(db_column='SoldDate', max_length=255)  # Field name made lowercase.
    empid = models.CharField(db_column='EmpId', max_length=255)  # Field name made lowercase.
    cusid = models.CharField(db_column='CusId', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sold_product'


class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_title = models.CharField(max_length=255)
    task_desc = models.CharField(max_length=255)
    task_filename = models.CharField(max_length=255)
    task_date = models.DateTimeField()
    task_s_title = models.CharField(max_length=255)
    task_s_desc = models.CharField(max_length=255)
    task_s_file = models.CharField(max_length=255)
    task_s_date = models.DateTimeField()
    empid = models.CharField(db_column='EmpId', max_length=255)  # Field name made lowercase.
    status = models.CharField(max_length=255)
    result = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'task'


class Team(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    designation = models.TextField(db_column='Designation')  # Field name made lowercase.
    image = models.TextField(db_column='Image')  # Field name made lowercase.
    category = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'team'


class XEmployee(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    empid = models.CharField(db_column='EmpId', max_length=50)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=20)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=20)  # Field name made lowercase.
    emailid = models.CharField(db_column='EmailId', max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=20)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=10)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100)  # Field name made lowercase.
    pincode = models.IntegerField(db_column='Pincode')  # Field name made lowercase.
    photograph = models.CharField(db_column='Photograph', max_length=255)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255)  # Field name made lowercase.
    aadhaar = models.CharField(db_column='Aadhaar', max_length=12)  # Field name made lowercase.
    emptype = models.CharField(db_column='EmpType', max_length=255)  # Field name made lowercase.
    teamhead = models.CharField(db_column='TeamHead', max_length=255)  # Field name made lowercase.
    status = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'x_employee'