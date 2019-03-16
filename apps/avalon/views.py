from django.views import generic


class Index(generic.TemplateView):
    template_name = 'index.html'


class Role(generic.FormView):
    template_name = 'role.html'


class Ability(generic.TemplateView):
    template_name = 'ability.html'

    extra_context = dict(player_name='kyon')

    def get_context_data(self, **kwargs):
        kwargs['room_id'] = self.kwargs['room_id']
        return super().get_context_data(**kwargs)
