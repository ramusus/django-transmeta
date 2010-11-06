# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils import translation
from transmeta import get_real_fieldname
from djcelery.decorators import respect_to_language

class SetTransMetaAttribute(object):

    def __setattr__(self, name, get_field_callback):
        '''
        Method tried to set full bunch of translatable field using get_field_callback method inside respect_to_language statement
        '''
        if callable(get_field_callback) and hasattr(self._meta, 'translatable_fields') and name in self._meta.translatable_fields:
            for lang in settings.LANGUAGES:
                with respect_to_language(lang[0]):
                    setattr(self, get_real_fieldname(name, lang[0]), get_field_callback())
        else:
            return super(SetTransMetaAttribute, self).__setattr__(name, get_field_callback)

class respect_to_language:
    '''
    Class for 'with' statement. Change current language environment for code inside statement
    You can use it inside this way:

        with respect_to_language(language):
            pass
    '''
    language = None
    language_prev = None

    def __init__(self, language):
        self.language = language

    def __enter__(self):
        self.language_prev = translation.get_language()
        self.language and translation.activate(self.language)

    def __exit__(self, type, value, traceback):
        translation.activate(self.language_prev)