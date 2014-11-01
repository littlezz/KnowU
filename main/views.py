from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, UpdateView
from django_ajax.decorators import ajax
from main.algorithmX import AlgorithmX
from .models import Tag, Article, UserProfile, BookArticleMembership


class LoginRequiredMixin:
    @classmethod
    def as_view(cls, **kwargs):
        return login_required(super().as_view(**kwargs))



class Register(View):
    register_form = UserCreationForm
    template = 'register.html'

    def get(self, request, *args, **kwargs):
        form = self.register_form()
        return render(request, self.template, {'form':form})

    def post(self, request, *args, **kwargs):
        form = self.register_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            form.save()
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            else:
                return HttpResponse('None')

            return redirect('manage')

        return render(request, self.template, {'form': form})




@ajax(mandatory=False)
@login_required
def manage(request):

    if request.method == 'GET':
            user_info, created = UserProfile.objects.get_or_create(user=request.user)
            tags_all = Tag.objects.values('label','id')
            tags_user = user_info.tags.values('label','id')
            tags_dict = {'tags_all': tags_all,
                         'tags_user': tags_user,
                        }

            return render(request, 'manage.html', tags_dict)

    elif request.method == 'POST' and request.is_ajax():

        for tag_id in request.POST.getlist('tags'):
            tag = get_object_or_404(Tag,id=tag_id)
            request.user.userprofile.tags.add(tag)

        return redirect('home')
    else:
        return HttpResponseBadRequest()




class Home(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')

    def post(self, request, *args, **kwargs):

       pass


@ajax(mandatory=False)
@login_required
def book_view(request):
    if request.method == 'GET':
        return render(request, 'book_view.html')

    elif request.method == 'POST' and request.is_ajax():
        try:
            times = int(request.POST['times'])
        except ValueError:
            return HttpResponseBadRequest()

        per_time = 5
        userinfo = request.user.userprofile
        books_quries = userinfo.article_books.all()[times:times * per_time]

        # faster!
        if books_quries.exists():
            items = books_quries.values('headline', 'id')

            #items is a list contain dict
            return {'item':items}
        else:
            return {'item':None}




@ajax
@login_required
def book_or_favour_or_dislike_article(request):
    """
    - - = +
    """
    if request.method == 'POST' and request.is_ajax():
        article_id = request.POST['article_id']
        mode = request.POST['mode']
        user = request.user

        article = get_object_or_404(Article, id=article_id)
        if mode == 'book':
            obj, creted = BookArticleMembership.objects.get_or_create(userinfo=user.userprofile, article=article)
            if creted:
                obj.delete()
            else:
                obj.save()
            return {'book_total': article.how_many_booked()}

        elif mode == 'favour':
            try:
                article.favour.get(id=user.id)
                article.favour.remove(user)
            except ObjectDoesNotExist:
                article.favour.add(user)
            return {'favour_total': article.how_many_favour()}

        elif mode == 'dislike':
            user.userprofile.article_dislike.add(article)

        else:
            raise Http404



@login_required
def userlogout(request):
    logout(request)
    return redirect('welcome')


@ajax
@login_required
def ajax_article(request):
    user = request.user

    if request.method == 'GET':
        art = AlgorithmX(user)
    elif request.method == 'POST':
        article_id = request.POST['article_id']
        art = get_object_or_404(Article, id=article_id)

    booked_total = art.how_many_booked()
    favor_total =  art.how_many_favour()
    isbooked = True if user.userprofile.article_books.filter(id=art.id).first() else False
    isfavour = True if art.favour.filter(username = user.username).first() else False

    #return JsonResponse({'content':art.content})
    #return HttpResponse(art.content, {'user':username})
    #return {'article':render(request, 'article.html'), 'user':username}
    return {'content': art.content,
            'headline': art.headline,
            'article_id':art.id,
            'booked_total': booked_total,
            'favour_total': favor_total,
            'isfavour': isfavour,
            'isbooked': isbooked,
            'link': art.link,
            'source_name': art.source_name,
            }