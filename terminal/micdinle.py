import speech_recognition as sr
from gtts import gTTS
import os

def mikrofon_dinle_ve_cevir(dosya_adi="cikti.mp3"):
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Mikrofon dinleniyor, bir şeyler söyleyin...")
        audio = r.listen(source)
        print("Dinleme tamamlandı, metin çıkartılıyor...")
    
    try:
        metin = r.recognize_google(audio, language="tr-TR")  
        print("Söylenen metin: " + metin)
        
        tts = gTTS(text=metin, lang="tr") 
        tts.save(dosya_adi)
        print(f"Metin ses dosyasına dönüştürüldü: {dosya_adi}")
        
        return metin
    except sr.UnknownValueError:
        print("Anlaşılamadı")
    except sr.RequestError as e:
        print("Google Web Speech API hatası; {0}".format(e))
    return None

if __name__ == "__main__":
    mikrofon_dinle_ve_cevir()
