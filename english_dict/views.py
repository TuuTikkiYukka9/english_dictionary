from django.shortcuts import render
from english_dict.forms import SelectWordForm, TranslateForm, LoginForm, SignUpForm
from english_dict.models import IrregularVerb, Word
from english_dict.business_logic import Translator
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


def index_view(request):
    return render(request, 'english_dict/index.html')


def dictionary_view(request):
    form = SelectWordForm()
    if request.method == "POST":
        frequency = bool(request.POST.get("frequency"))
        word_type = (lambda x: int(x) if x != "" else None)(request.POST.get("word_type"))
        form.initial = {"frequency": frequency, "word_type": word_type}
        return render(request, 'english_dict/dictionary.html', {
            "form": form,
            'result': Word.objects.get_dictionary(frequency, word_type)
        })
    else:
        return render(request, 'english_dict/dictionary.html', {"form": form})


def sounds_view(request):
    return render(request, 'english_dict/sounds.html')


def irregular_verbs_view(request):
    return render(request, 'english_dict/irregular_verbs.html', {
        'result': IrregularVerb.objects.select_related().order_by('infinitive_word__lemma')
    })


def translate_view(request):
    form = TranslateForm()
    if request.method == "POST":
        input_text = str(request.POST.get("input_text"))
        form.initial = {"input_text": input_text}
        return render(request, 'english_dict/translate.html', {
            "form": form,
            'result': Translator.translate(input_text)
        })
    else:
        return render(request, 'english_dict/translate.html', {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(get_continue_url(request))


def login_view(request):
    error = ''
    url = get_continue_url(request)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(
                username=cleaned_data['username'],
                password=cleaned_data['password']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(url)
            error = u'Неверный логин/пароль'
        else:
            error = u'Не заполнена форма.'
    return render(request, 'english_dict/login.html', {"form": LoginForm(), "error": error, "continue": url})


def signup_view(request):
    url = get_continue_url(request)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(url)
    else:
        form = SignUpForm()
    return render(request, 'english_dict/signup.html', {'form': form, "continue": url})


def get_continue_url(request):
    return request.POST.get("continue", "/") if request.method == 'POST' else request.GET.get("continue", "/")
