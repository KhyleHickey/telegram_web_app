from mini_apps.web import WebApp


class StaticFiles(WebApp):
    def __init__(self, settings, name):
        super().__init__(settings, name)
        self.path = settings.paths.root / settings.path

    def prepare_app(self, http, app):
        app.router.add_static("/", self.path)
