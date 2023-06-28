from flask import Flask, render_template, request

app = Flask(__name__)

def index():
    return render_template("index.html")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        codec = request.form['codec'].upper()

        if codec == 'C':
            mensagem = request.form['mensagem']
            val = int(request.form['deslocamento'])

            cifrada = ""

            for caracter in mensagem:
                if caracter.isalpha():
                    if caracter.isupper():
                        base = ord('A')
                    else:
                        base = ord('a')
                    ind = ord(caracter) - base
                    nova_letra = chr((ind + val) % 26 + base)
                    cifrada += nova_letra
                else:
                    cifrada += caracter

            return render_template('index.html', mensagem_original=mensagem, resultado=cifrada, codec=codec)
        elif codec == 'D':
            mensagem = request.form['mensagem']
            val = int(request.form['deslocamento'])

            cifrada = ""

            for caracter in mensagem:
                if caracter.isalpha():
                    if caracter.isupper():
                        base = ord('A')
                    else:
                        base = ord('a')
                    ind = ord(caracter) - base
                    nova_letra = chr((ind - val) % 26 + base)
                    cifrada += nova_letra
                else:
                    cifrada += caracter

            return render_template('index.html', mensagem_original=mensagem, resultado=cifrada, codec=codec)
        else:
            return render_template('index.html', mensagem_original=None, resultado=None, codec=None)
    else:
        return render_template('index.html', mensagem_original=None, resultado=None, codec=None)

if __name__ == '__main__':
    app.run()
