from django.views import generic


class Index(generic.TemplateView):
    template_name = 'index.html'


class Ability(generic.TemplateView):
    template_name = 'ability.html'
