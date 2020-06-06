# -*- coding: utf-8 -*-

from flask import Flask
from flask import request

from network_class import NetworkSSH


app = Flask(__name__)

content = '''

    <html>
    <head>
        <title>Network SHH</title>
    </head>
    <body>

        <h1>Network Routers Configuration via SSH</h1>
        <hr />

        <form method="POST" action="/configure">

            <div>
                <div>
                    <label for="routers">Selecione um roteador:</label>
                    <br />
                    <select name="routers" id="routers" multiple>
                        <option value="1">Router 1</option>
                        <option value="2">Router 2</option>
                        <option value="3">Router 3</option>
                        <option value="4">Router 4</option>
                    </select>
                </div>
                <div>
                    <label for="vlans">Selecione uma VLAN:</label>
                    <br />
                    <select name="vlans" id="vlans" multiple>
                        <option value="90">VLAN 90</option>
                        <option value="91">VLAN 91</option>
                        <option value="92">VLAN 92</option>
                        <option value="93">VLAN 93</option>
                    </select>
                </div>
                <div>
                    <label for="ports">Selecione as portas:</label>
                    <br />
                    <select name="ports" id="ports" multiple>
                        <option value="0">Porta 0</option>
                        <option value="1">Porta 1</option>
                        <option value="2">Porta 2</option>
                        <option value="3">Porta 3</option>
                    </select>
                </div>
            </div>

            <button type="submit">Configurar Agora >></button>

        </form>

        <label for="message">Mensagem: @message</label>

    </body>
    </html>

'''


# página principal
@app.route('/')
def index():
    return content 


# página/rota de configuração principal
@app.route('/configure', methods = ['POST'])
def configure():

    routers = request.form.getlist('routers')
    vlans = request.form.getlist('vlans')
    ports = request.form.getlist('ports')

    try:
        for router in routers:
            for vlan in vlans:
                network = NetworkSSH()
                network.connect()
                network.configure(router, vlan, ports)
    except Exception as e:
        return content.replace('@message', str(e))

    return content.replace('@message', 'Configuração aplicadacom sucesso!')

# run server
if __name__ == '__main__':
    app.run(debug=True)
