# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import separatedvaluesfield.models


def add_grant_types(apps, schema_editor):
    Application = apps.get_model('oauth2_provider', 'Application')
    applications = Application.objects.using(schema_editor.connection.alias).all()
    for app in applications:
        app.grant_types = [app.authorization_grant_type]
        app.save()


class Migration(migrations.Migration):

    operations = [
        migrations.AddField(
            model_name='application',
            name='grant_types',
            field=separatedvaluesfield.models.SeparatedValuesField(default=[b'password'], max_length=150, verbose_name='grant types', choices=[(b'authorization-code', 'Authorization code'), (b'implicit', 'Implicit'), (b'password', 'Resource owner password-based'), (b'client-credentials', 'Client credentials')]),
        ),
        migrations.RunPython(add_grant_types),
    ]
