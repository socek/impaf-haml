from implugin.jinja2 import Jinja2Application


class HamlApplication(Jinja2Application):

    def _create_config(self):
        extensions = self.settings.get('jinja2.extensions', [])
        extensions.append('hamlish_jinja.HamlishExtension')
        self.settings['jinja2.extensions'] = extensions
        super()._create_config()

    def _generate_registry(self, registry):
        super()._generate_registry(registry)
        self.config.add_jinja2_renderer('.haml')
