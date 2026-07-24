from django.apps import AppConfig


class ProjectGalleryConfig(AppConfig):
    name = 'project_gallery'

    def ready(self):
        import project_gallery.signals
