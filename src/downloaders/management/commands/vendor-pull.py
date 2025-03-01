import helpers
from typing import Any
from django.core.management.base import BaseCommand
from django.conf import settings

STATICFILES_VENDOR_DIR= getattr(settings, 'STATICFILES_VENDOR_DIR')

VENDOR_STATICFILES = {
    "flowbite.min.js": "https://cdn.jsdelivr.net/npm/flowbite@2.4.1/dist/flowbite.min.js",
    "flowbite.min.css" : "https://cdn.jsdelivr.net/npm/flowbite@2.4.1/dist/flowbite.min.css"
}

class Command (BaseCommand):

    def handle(self, *args: Any, **options: Any) -> str | None:
       self.stdout.write("Downloading vendor static files")

       completed_urls = []

       
       for name, url in VENDOR_STATICFILES.items():
           out_path = STATICFILES_VENDOR_DIR / name
           print(name, url, out_path)
           dl_success = helpers.download_to_local(url, out_path)
           
           if dl_success:
               completed_urls.append(url) 
           
           else:
               self.stdout.write(
                   self.style.ERROR(f'failed to download {url}')
               )

           if set(completed_urls) == set(VENDOR_STATICFILES.values()):
               self.stdout.write(
                   self.style.SUCCESS(f'Successfully updated all vendor static files')
               )
           else: 
               self.stdout.write(
                   self.style.WARNING(f'Some files were not downloaded')
               )
                      
               
    