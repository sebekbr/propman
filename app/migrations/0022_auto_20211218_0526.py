# Generated by Django 3.2.8 on 2021-12-18 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20211216_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bills',
            name='bill_vendor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='app.billvendors'),
        ),
        migrations.AlterField(
            model_name='bills',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.property'),
        ),
        migrations.AlterField(
            model_name='leaseagreement',
            name='landlords',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.landlords'),
        ),
        migrations.AlterField(
            model_name='leaseagreement',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.property'),
        ),
        migrations.AlterField(
            model_name='leaseagreement',
            name='tenants',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.tenants'),
        ),
        migrations.AlterField(
            model_name='leaseagreement',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.leaseagreement_type'),
        ),
        migrations.AlterField(
            model_name='property',
            name='house_association',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.housingassociation'),
        ),
    ]
