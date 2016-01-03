# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JobJarApplication', '0002_auto_20150328_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='state',
            field=models.IntegerField(choices=[(1, b'Uninitialized'), (2, b'Busy'), (3, b'Available'), (4, b'Idle'), (5, b'Completed'), (6, b'Unknown')]),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='JobState',
        ),
    ]
