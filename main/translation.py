from modeltranslation.translator import register, TranslationOptions, translator
from .models import *



class ProgramTranslationOptions(TranslationOptions):
    fields = ('title','description',)

translator.register(Programms, ProgramTranslationOptions)