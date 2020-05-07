from django.shortcuts import render
from english_dict.forms import SelectWordForm, TranslateForm
from english_dict.models import IrregularVerb, Word
from english_dict.business_logic import Translator


def index(request):
    return render(request, 'english_dict/index.html')


def dictionary(request):
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


def sounds(request):
    return render(request, 'english_dict/sounds.html')


def irregular_verbs(request):
    return render(request, 'english_dict/irregular_verbs.html', {
        'result': IrregularVerb.objects.select_related().order_by('infinitive_word__lemma')
    })


def translate(request):
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
