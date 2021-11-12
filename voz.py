import azure.cognitiveservices.speech as speechsdk


def from_mic():

    speech_config = speechsdk.SpeechConfig(subscription="be4302873f0e45fe9a1e2de23b29b3b2", region="southcentralus")
    speech_config.speech_recognition_language="es-MX"
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    
    print("Habla al microfono")
    result = speech_recognizer.recognize_once_async().get()
    
    return result.text

#from_mic()