from gtts import gTTS #biblioteca de voz do google
from flask import Flask, render_template, request

# Criando o objeto flask
app = Flask(__name__)
# Criando uma rota
@app.route('/', methods=['GET','POST'])
def index():
    audio_path = None
    if request.method == 'POST':
        #pegar valor do html <textfield>
        texto = request.form["texto"]

        #configurar idioma
        lingua = 'pt-br'

        # criação do objeto
        tts = gTTS(text=texto, lang=lingua)

        # Nome do arquivo de audio.
        audio_path = "static/audio_exemplo.mp3"

        # salvar o arquivo
        tts.save(audio_path)
    return render_template('index.html', audio_path=audio_path)

if __name__ == '__main__':
    app.run(debug=True)