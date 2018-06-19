# importing flask modules
# encoding: utf-8
from flask import Flask, render_template, request

# initializing a variable of Flask
app = Flask(__name__)

# decorating index function with the app.route with url as /MTChallenge4
@app.route('/MTChallenge4')
def index():
   return render_template('MTChallenge4.html')

@app.route('/MTChallenge4',  methods=['POST'])
def Translated():
   if request.method == 'POST':
       texto_2_trad = request.form['texto_2_trad']
       texto_translated = translate(texto_2_trad)
       return render_template('MTChallenge4.html', texto_2_trad=texto_2_trad, texto_translated=texto_translated)
   else:
       pass
def translate (text_2_translate):        
    import json, ast
    from watson_developer_cloud import LanguageTranslatorV2 as LanguageTranslator
    language_translator = LanguageTranslator(username='80a4fe15-b198-4ffa-b807-1fa85897ce1d',password='NdJMu1O5NNnY')
#define a língua
    #text_2_translate = text_2_translate.encode('utf-8') #converte o texto a ser traduzido em utf-8
    language = language_translator.identify(text_2_translate)
    lang = json.loads(json.dumps(language, indent=2))
    lang = lang['languages']
    lang = lang[0]
    lang = lang['language']
#faz a traducao
    traducao = json.dumps(language_translator.translate( text_2_translate ,source = lang, target = 'en'), ensure_ascii = False)
    traducao = ast.literal_eval(traducao)
    return traducao

if __name__ == "__main__":
   app.run()
