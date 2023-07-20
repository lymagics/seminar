from django.views.generic import RedirectView


class ActionView(RedirectView):
    def perform_action(self):
        raise NotImplementedError

    def get(self, request, *args, **kwargs):
        self.perform_action()
        return super().get(request, *args, **kwargs)
