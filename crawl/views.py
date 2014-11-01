from django.contrib.auth.decorators import permission_required
from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import CheckCommitForm
# Create your views here.
from django.views.decorators.http import require_POST
from django.views.generic import ListView
from .models import TemArticle
from main.models import Article, Tag

class List(ListView):
    template_name = 'crawl/list.html'
    model = TemArticle
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CheckCommitForm()
        return context


@require_POST
@permission_required('is_staff')
def every_article_commit_and_clear(request):
    form = CheckCommitForm(request.POST)
    if form.is_valid():
        tem_arts_queries = TemArticle.objects.all()
        for tem_art in tem_arts_queries:
            art, created = Article.objects.get_or_create(headline=tem_art.headline,
                                                         content=tem_art.content,
                                                         source_name=tem_art.source_name,
                                                         link=tem_art.link,
                                                         )
            art.save()

            tem_tags_queries = tem_art.tags.all()
            for tem_tag in tem_tags_queries:
                tag, created = Tag.objects.get_or_create(label=tem_tag.label)
                tag.save()

                art.tags.add(tag)

            tem_art.delete()

        return HttpResponse('ok!')
    else:
        raise Http404





