# Generated by Django 2.2.4 on 2019-10-09 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy_app', '0002_auto_20190925_1816'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComponentDocuments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('required', models.BooleanField()),
                ('validFrom', models.DateField()),
                ('validTo', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CredentialRequirements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('componentDocuments', models.ManyToManyField(to='deploy_app.ComponentDocuments')),
            ],
        ),
        migrations.CreateModel(
            name='Doctype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('complete', models.BooleanField()),
                ('requirements', models.ManyToManyField(to='deploy_app.CredentialRequirements')),
            ],
        ),
        migrations.RemoveField(
            model_name='enterprise_employees',
            name='enterprise_id',
        ),
        migrations.RemoveField(
            model_name='enterprise_employees',
            name='person_id',
        ),
        migrations.RemoveField(
            model_name='government_citizens',
            name='government_id',
        ),
        migrations.RemoveField(
            model_name='government_citizens',
            name='person_id',
        ),
        migrations.DeleteModel(
            name='Enterprise_Customers',
        ),
        migrations.DeleteModel(
            name='Enterprise_Employees',
        ),
        migrations.DeleteModel(
            name='Government_Citizens',
        ),
    ]