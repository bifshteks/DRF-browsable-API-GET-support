from rest_framework.renderers import BrowsableAPIRenderer


class GETFormBrowsableAPIRenderer(BrowsableAPIRenderer):
    """ Кастомный рендерер, добавляющий в BrowsableAPIRenderer поле для ввода GET параметров """
    template = 'browsable-api-template.html'

    def get_context(self, data, accepted_media_type, renderer_context):
        context = super().get_context(data, accepted_media_type, renderer_context)
        view = renderer_context['view']
        if 'GET' in view.allowed_methods:
            sz_class = view.get_serializer_class() if hasattr(view, 'get_serializer_class') else view.serializer_class
            sz = sz_class(data=view.request.query_params)
            context['get_form'] = self.render_form_for_serializer(sz)
        return context
