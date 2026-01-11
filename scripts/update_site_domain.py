
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "autopartespro.settings")
django.setup()

from django.contrib.sites.models import Site

def update_site():
    domain = "autopartespro.up.railway.app"
    name = "AutoPartes Pro"
    
    try:
        site = Site.objects.get(pk=1)
        site.domain = domain
        site.name = name
        site.save()
        print(f"Successfully updated Site ID 1 to {domain}")
    except Site.DoesNotExist:
        Site.objects.create(pk=1, domain=domain, name=name)
        print(f"Created new Site ID 1: {domain}")
    except Exception as e:
        print(f"Error updating site: {e}")

if __name__ == "__main__":
    update_site()
