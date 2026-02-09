from django.db import migrations
from django.conf import settings

def update_site_name(apps, schema_editor):
    Site = apps.get_model('sites', 'Site')
    # ID=1 is default
    site, created = Site.objects.get_or_create(id=1)
    site.domain = 'autopartespro.pythonanywhere.com'
    site.name = 'AutoPartes Pro'
    site.save()

class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'), 
        ('web', '0001_initial_site'), 
    ]

    operations = [
        migrations.RunPython(update_site_name),
    ]
