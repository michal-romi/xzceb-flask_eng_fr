"""
This program holds the Watson IBM translation functions for the final project
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['APIKEY']
URL = os.environ['URL']
VERSION_LT='2018-05-01'

# Creating a watson translator object

authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(version=VERSION_LT,authenticator=authenticator)
language_translator.set_service_url(URL)
language_translator.set_disable_ssl_verification(True)

def english_to_french(english_text):
    """
    This functions takes in an English text and translates it into French
    """
    try:
        translation_response = language_translator.translate(\
        text=english_text, model_id='en-fr')
        translation = translation_response.get_result()
        french_text = translation['translations'][0]['translation']
    except:
        french_text = "Input is null"
    return french_text

def french_to_english(french_text):
    """
    This function takes in French text and translates it into English
    """
    try:
        translation_response = language_translator.translate(\
        text=french_text, model_id='fr-en')
        translation = translation_response.get_result()
        english_text = translation['translations'][0]['translation']
    except:
        english_text = "Input is null"
    return english_text
