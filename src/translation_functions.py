from doc_handling import *
from google.cloud import translate_v3
from dotenv import load_dotenv
import os
import json

load_dotenv()
PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")
CREDENTIALS = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")

def translate(
        text, 
        source_language_code: str = "en-US", 
        target_language_code: str = "fr"
        ) -> translate_v3.TranslationServiceClient:
    """
    Translate Text from a Source language to a Target language.
    Args:
        text: The content to translate.
        source_language_code: The code of the source language.
        target_language_code: The code of the target language.
            For example: "fr" for French, "es" for Spanish, etc.
            Find available languages and codes here:
            https://cloud.google.com/translate/docs/languages#neural_machine_translation_model
    """
    
    #Initialize Translation Client
    client = translate_v3.TranslationServiceClient()
    parent = f"projects/{PROJECT_ID}/locations/global"

    #MIME type of the content to translate.
    #Supported MIME types:
    #https://cloud.google.com/translate/docs/supported-formats
    mime_type = "text/plain"

    #Translate text from the source to the target language.
    response = client.translate_text(
        contents=[text],
        parent=parent,
        mime_type=mime_type,
        source_language_code=source_language_code,
        target_language_code=target_language_code,
    )

    return response

def detect_language(
        text: str,
        #project_id: str = {PROJECT_ID},
) -> dict:
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    response = translate_client.detect_language(text)

    return response

def detect_language_advanced(
        text: str,
) -> translate_v3.TranslationServiceClient:
    '''
    Detecting the language of a text string.

    Args: project_id: The GCP project ID.

    Returns: The detected language of the text.
    '''
    client = translate_v3.TranslationServiceClient()
    location = "global"
    parent = f"projects/{PROJECT_ID}/locations/{location}"

     #Detail on supported types can be found here:
     #https://cloud.google.com/translate/docs/supported-formats
    response = client.detect_language(
       content=text,
        parent=parent,
        mime_type="text/plain", # mime types: text/plain, text/html
    )

    return response

def get_supported_languages() -> translate_v3.types.SupportedLanguages:
     client = translate_v3.TranslationServiceClient()
     parent = f"projects/{PROJECT_ID}"

     response = client.get_supported_languages(parent=parent, display_language_code="en")

     langs = []
     for lang in response.languages:
         langs.append(lang.display_name)
     
     return langs