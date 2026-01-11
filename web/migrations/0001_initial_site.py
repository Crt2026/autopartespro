
from django.db import migrations
from django.conf import settings

def update_site_domain(apps, schema_editor):
    Site = apps.get_model('sites', 'Site')
    # Update the default example.com site (ID=1)
    Site.objects.update_or_create(
        id=settings.SITE_ID,
        defaults={
            'domain': 'autopartespro.up.railway.app',
            'name': 'AutoPartes Pro'
        }
    )

class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.RunPython(update_site_domain),
    ]
