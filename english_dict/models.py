from django.db import models
from django.contrib.auth.models import User


class WordManager(models.Manager):
    def get_words_by_lemma(self, lemma):
        return self.filter(lemma=lemma)

    def get_dictionary(self, is_frequency, word_type):
        if not (word_type is None):
            filtered_words = WordPartProperty.objects.filter(property=word_type).values('word')
            words = self.filter(word_id__in=filtered_words)
        else:
            words = self
        if is_frequency:
            return words.filter(frequency__isnull=False).order_by('frequency')
        else:
            return words.all().order_by('lemma')


class Word(models.Model):
    word_id = models.BigIntegerField(primary_key=True)
    word = models.CharField(max_length=255)
    lemma = models.CharField(max_length=255)
    transcription = models.CharField(max_length=255, null=True, blank=True)
    frequency = models.BigIntegerField(null=True, blank=True)
    translation = models.TextField(null=True, blank=True)
    objects = WordManager()

    def __str__(self):
        return self.lemma

    class Meta:
        db_table = 'words'


class PartProperty(models.Model):
    prop_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=64, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'parts_properties'


class WordPartProperty(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    property = models.ForeignKey(PartProperty, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.word_id) + ':' + str(self.prop_id)

    class Meta:
        db_table = 'words_parts_properties'


class IrregularVerb(models.Model):
    infinitive_word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name="infinitive")
    simple_past_word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name="simple_past")
    past_particle_word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name="past_particle")
    description = models.TextField()

    def __str__(self):
        return str(self.infinitive_word_id)

    class Meta:
        db_table = 'irregular_verbs'


class WordStatuses(models.Model):
    mane = models.CharField(max_length=255)

    class Meta:
        db_table = 'word_statuses'


class WordsWordStatuses(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    status = models.ForeignKey(WordStatuses, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'words_word_statuses'
