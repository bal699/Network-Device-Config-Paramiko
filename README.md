# Network Device Configuration with Paramiko Lib

## Paramiko

### O que é o Paramiko?

Biblioteca python que implementa o protocolo SSHv2 provendo funcionalidades de cliente e servidor SSH.

### O que é o Flask?

Biblioteca python para criação de aplicações web.

## Configurar ambiente de execução

### Configurar ambiente virtual

Instalar ambiente virtual:

```
pip install virtualenv
virtualenv network_ssh -p c:\\Python\\38\\python.exe
```

Ativar ambiente virtual (Linux):

```
source ./network_ssh/bin/activate
```

Ativar ambiente virtual (Windows):

```
network_ssh/Scripts/activate.bat
```

Instalar pacote Paramiko:

```
pip install paramiko
```

Instalar pacote web Flask:

```
pip install flask
```


### Configurar VSCode

Criar uma pasta para o projeto e abrir no VSCode.

Criar um arquivo chamado `app.py`.

Criar um novo arquivo de execução indicando o `python.exe` do ambiente virtual:

```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Run Network Commands",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/network_script.py",
            "pythonPath": "C:/Python/38/venvs/network_ssh/Scripts/python.exe",
            "console": "internalConsole"
        },
        {
            "name": "Python: Flask",
            "type": "python",
            "request": "launch",
            "module": "app",
            "pythonPath": "C:/Python/38/venvs/network_ssh/Scripts/python.exe",
            "env": {
                "FLASK_APP": "app.py",
                "FLASK_ENV": "development",
                "FLASK_DEBUG": "0"
            },
            "args": [
                "run",
                "--no-debugger",
                "--no-reload"
            ],
            "jinja": true
        }
    ]
}
```

## Configuration Script

O arquivo de configuração pode ser encontrado em `app.py`.

## Referências

* https://www.pycursos.com/python-para-zumbis/
* http://www.paramiko.org/installing.html
* https://encore.tech/network-automation-with-paramiko/
* https://www.reddit.com/r/networking/comments/6wdut7/paramiko_practical_interface_modification_script/
