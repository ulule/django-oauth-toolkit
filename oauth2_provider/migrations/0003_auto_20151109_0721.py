# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import separatedvaluesfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth2_provider', '0002_08_updates'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='authorization_grant_type',
        ),
        migrations.AddField(
            model_name='application',
            name='grant_types',
            field=separatedvaluesfield.models.SeparatedValuesField(default=[b'password'], max_length=150, verbose_name='grant types', choices=[(b'authorization-code', 'Authorization code'), (b'implicit', 'Implicit'), (b'password', 'Resource owner password-based'), (b'client-credentials', 'Client credentials')]),
        ),
    ]
