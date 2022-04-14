# Generated by Django 4.0.1 on 2022-03-07 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'admin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Adminlogin',
            fields=[
                ('firstname', models.CharField(db_column='FirstName', max_length=255)),
                ('lastname', models.CharField(db_column='LastName', max_length=255)),
                ('emailid', models.CharField(db_column='EmailId', max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(db_column='Password', max_length=20)),
                ('type', models.CharField(db_column='Type', max_length=255)),
            ],
            options={
                'db_table': 'adminlogin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AllCities',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('city', models.CharField(db_column='City', max_length=255)),
            ],
            options={
                'db_table': 'all_cities',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AllInstitute',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('institute', models.CharField(db_column='Institute', max_length=255)),
            ],
            options={
                'db_table': 'all_institute',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BlogsDisplay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.CharField(max_length=255)),
                ('heading', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('category', models.CharField(max_length=255)),
                ('view', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'blogs_display',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=255)),
                ('job_type', models.CharField(max_length=255)),
                ('job_role', models.CharField(max_length=255)),
                ('qualification', models.CharField(max_length=255)),
                ('key_skills', models.CharField(max_length=255)),
                ('exp', models.CharField(max_length=255)),
                ('required_language', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('job_description', models.TextField()),
                ('image', models.CharField(max_length=255)),
                ('created_datetime', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'career',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CareerApplicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('qualification', models.CharField(max_length=255)),
                ('hq_per', models.CharField(max_length=255)),
                ('high_school', models.CharField(max_length=255)),
                ('higher_sec', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('about', models.TextField()),
                ('resume', models.CharField(max_length=255)),
                ('created_datetime', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'career_applicant',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CareerApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('age', models.CharField(max_length=10)),
                ('qualification', models.CharField(max_length=255)),
                ('hq_per', models.CharField(max_length=255)),
                ('high_school', models.CharField(max_length=255)),
                ('higher_sec', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('about', models.TextField()),
                ('resume', models.CharField(max_length=255)),
                ('created_datetime', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'career_application',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
                ('category_for', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Complains',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('orderid', models.CharField(db_column='OrderId', max_length=255)),
                ('complaintype', models.CharField(db_column='ComplainType', max_length=20)),
                ('description', models.CharField(db_column='Description', max_length=100)),
                ('date', models.CharField(db_column='Date', max_length=255)),
                ('status', models.CharField(db_column='Status', max_length=10)),
                ('cmpby', models.CharField(db_column='CmpBy', max_length=20)),
                ('cmpsolveby', models.CharField(db_column='CmpSolveBy', max_length=20)),
            ],
            options={
                'db_table': 'complains',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ComplainType',
            fields=[
                ('cmptypeid', models.AutoField(db_column='CmpTypeId', primary_key=True, serialize=False)),
                ('cmptype', models.CharField(db_column='CmpType', max_length=50)),
            ],
            options={
                'db_table': 'complain_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=255)),
                ('syllabus', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'course',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CourseQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('course', models.CharField(max_length=255)),
                ('query_date', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'course_query',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Createcertificate',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('empid', models.CharField(db_column='EmpId', max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
                ('signature', models.CharField(max_length=255)),
                ('datetime', models.DateTimeField()),
            ],
            options={
                'db_table': 'createcertificate',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cusid', models.AutoField(db_column='CusId', primary_key=True, serialize=False)),
                ('firstname', models.CharField(db_column='FirstName', max_length=255)),
                ('lastname', models.CharField(db_column='LastName', max_length=255)),
                ('emailid', models.CharField(db_column='EmailId', max_length=255)),
                ('contact', models.CharField(db_column='Contact', max_length=13)),
                ('address', models.TextField(db_column='Address')),
                ('pincode', models.CharField(db_column='Pincode', max_length=6)),
                ('aadhaar', models.CharField(db_column='Aadhaar', max_length=12)),
                ('empid', models.CharField(db_column='EmpId', max_length=255)),
            ],
            options={
                'db_table': 'customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DayWiseTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.IntegerField(blank=True, null=True)),
                ('task_title', models.CharField(blank=True, max_length=255, null=True)),
                ('task_desc', models.TextField(blank=True, null=True)),
                ('task_file', models.CharField(blank=True, max_length=255, null=True)),
                ('task_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'day_wise_task',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DayWiseTask1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.IntegerField()),
                ('task_title', models.CharField(max_length=255)),
                ('task_desc', models.TextField()),
                ('task_file', models.CharField(max_length=255)),
                ('task_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'day_wise_task1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('empid', models.CharField(db_column='EmpId', max_length=50)),
                ('firstname', models.CharField(db_column='FirstName', max_length=20)),
                ('lastname', models.CharField(db_column='LastName', max_length=20)),
                ('emailid', models.CharField(db_column='EmailId', max_length=50)),
                ('password', models.CharField(db_column='Password', max_length=225)),
                ('contact', models.CharField(db_column='Contact', max_length=10)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=100, null=True)),
                ('pincode', models.IntegerField(blank=True, db_column='Pincode', null=True)),
                ('city', models.CharField(blank=True, db_column='City', max_length=255, null=True)),
                ('institute', models.CharField(blank=True, db_column='Institute', max_length=255, null=True)),
                ('photograph', models.CharField(blank=True, db_column='Photograph', max_length=255, null=True)),
                ('description', models.TextField(blank=True, db_column='Description', null=True)),
                ('aadhaar', models.CharField(blank=True, db_column='Aadhaar', max_length=12, null=True)),
                ('emptype', models.CharField(blank=True, db_column='EmpType', max_length=255, null=True)),
                ('teamhead', models.CharField(db_column='TeamHead', max_length=255)),
                ('joiningdate', models.DateField(blank=True, db_column='JoiningDate', null=True)),
                ('start_date', models.CharField(blank=True, max_length=255, null=True)),
                ('end_date', models.CharField(blank=True, max_length=255, null=True)),
                ('log_in_time', models.CharField(blank=True, max_length=255, null=True)),
                ('log_out_time', models.CharField(blank=True, max_length=255, null=True)),
                ('hr', models.IntegerField(blank=True, null=True)),
                ('certificate', models.CharField(blank=True, max_length=10, null=True)),
                ('ac_status', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'employee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Galary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'galary',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LoginDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.CharField(db_column='EmpId', max_length=255)),
                ('login_time', models.CharField(max_length=255)),
                ('logout_time', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'login_details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MailSystem',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('file', models.TextField()),
                ('empid', models.CharField(db_column='EmpId', max_length=255)),
                ('forward_to', models.CharField(max_length=255)),
                ('status', models.IntegerField()),
                ('created_date', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'mail_system',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MailSystemHead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_iden', models.CharField(max_length=255)),
                ('mail_by', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('file', models.TextField()),
                ('created_date', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'mail_system_head',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Meetings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=255)),
                ('org_email', models.CharField(max_length=255)),
                ('org_contact', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('image', models.CharField(max_length=255)),
                ('empid', models.CharField(db_column='EmpId', max_length=255)),
                ('datetime', models.DateTimeField()),
                ('status', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'meetings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.CharField(db_column='EmpId', max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('datetime', models.DateTimeField()),
                ('status', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'message',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Occasion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('status', models.CharField(max_length=255)),
                ('datetime', models.DateTimeField()),
            ],
            options={
                'db_table': 'occasion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OurProducts',
            fields=[
                ('productid', models.AutoField(db_column='ProductId', primary_key=True, serialize=False)),
                ('productname', models.CharField(db_column='ProductName', max_length=255)),
                ('productvalidity', models.CharField(db_column='ProductValidity', max_length=20)),
                ('productprice', models.IntegerField(db_column='ProductPrice')),
            ],
            options={
                'db_table': 'our_products',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PgrQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('query_date', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('display', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'pgr_query',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductComplains',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('product_id', models.CharField(max_length=255)),
                ('cusid', models.CharField(db_column='CusId', max_length=255)),
                ('description', models.CharField(db_column='Description', max_length=255)),
                ('empid', models.CharField(db_column='EmpId', max_length=255)),
                ('datetime', models.DateTimeField()),
            ],
            options={
                'db_table': 'product_complains',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductPpt',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('productname', models.CharField(db_column='ProductName', max_length=255)),
                ('file', models.CharField(db_column='File', max_length=255)),
                ('datetime', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'product_ppt',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RenewProduct',
            fields=[
                ('renewproductid', models.AutoField(db_column='RenewProductId', primary_key=True, serialize=False)),
                ('productid', models.IntegerField(db_column='ProductId')),
                ('orderid', models.CharField(db_column='OrderId', max_length=50)),
                ('productname', models.CharField(db_column='ProductName', max_length=20)),
                ('productvalidity', models.CharField(db_column='ProductValidity', max_length=10)),
                ('productprice', models.IntegerField(db_column='ProductPrice')),
                ('sellingprice', models.CharField(db_column='SellingPrice', max_length=50)),
                ('renewdate', models.CharField(db_column='RenewDate', max_length=255)),
                ('renewby', models.CharField(db_column='RenewBy', max_length=20)),
                ('cusid', models.CharField(db_column='CusId', max_length=20)),
            ],
            options={
                'db_table': 'renew_product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SoldProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.IntegerField(db_column='ProductId')),
                ('orderid', models.CharField(db_column='OrderId', max_length=255)),
                ('productname', models.CharField(db_column='ProductName', max_length=255)),
                ('productprice', models.CharField(db_column='ProductPrice', max_length=255)),
                ('sellingprice', models.CharField(db_column='SellingPrice', max_length=50)),
                ('solddate', models.CharField(db_column='SoldDate', max_length=255)),
                ('empid', models.CharField(db_column='EmpId', max_length=255)),
                ('cusid', models.CharField(db_column='CusId', max_length=255)),
            ],
            options={
                'db_table': 'sold_product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('task_title', models.CharField(max_length=255)),
                ('task_desc', models.CharField(max_length=255)),
                ('task_filename', models.CharField(max_length=255)),
                ('task_date', models.DateTimeField()),
                ('task_s_title', models.CharField(max_length=255)),
                ('task_s_desc', models.CharField(max_length=255)),
                ('task_s_file', models.CharField(max_length=255)),
                ('task_s_date', models.DateTimeField()),
                ('empid', models.CharField(db_column='EmpId', max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('result', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'task',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=255)),
                ('designation', models.TextField(db_column='Designation')),
                ('image', models.TextField(db_column='Image')),
                ('category', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'team',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='XEmployee',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('empid', models.CharField(db_column='EmpId', max_length=50)),
                ('firstname', models.CharField(db_column='FirstName', max_length=20)),
                ('lastname', models.CharField(db_column='LastName', max_length=20)),
                ('emailid', models.CharField(db_column='EmailId', max_length=50)),
                ('password', models.CharField(db_column='Password', max_length=20)),
                ('contact', models.CharField(db_column='Contact', max_length=10)),
                ('address', models.CharField(db_column='Address', max_length=100)),
                ('pincode', models.IntegerField(db_column='Pincode')),
                ('photograph', models.CharField(db_column='Photograph', max_length=255)),
                ('description', models.CharField(db_column='Description', max_length=255)),
                ('aadhaar', models.CharField(db_column='Aadhaar', max_length=12)),
                ('emptype', models.CharField(db_column='EmpType', max_length=255)),
                ('teamhead', models.CharField(db_column='TeamHead', max_length=255)),
                ('status', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'x_employee',
                'managed': False,
            },
        ),
    ]