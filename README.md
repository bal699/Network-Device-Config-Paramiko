# Network Device Configuration with Paramiko Lib

## Paramiko

### O que é o Paramiko?

Biblioteca python que implementa o protocolo SSHv2 provendo funcionalidades de cliente e servidor SSH.

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

### Configurar VSCode

Criar uma pasta para o projeto e abrir no VSCode.

Criar um arquivo chamado `app.py`.

Criar um novo arquivo de execução indicando o `python.exe` do ambiente virtual:

```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Run Network Scripts",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}\\app.py",
            "pythonPath": "<folder>\\network_ssh\\Scripts\\python.exe",
            "console": "integratedTerminal"
        }
    ]
}
```

## Configuration Script

O arquivo de configuração pode ser encontrado em `app.py`.

## Referências

* http://www.paramiko.org/installing.html
* https://encore.tech/network-automation-with-paramiko/
* https://www.reddit.com/r/networking/comments/6wdut7/paramiko_practical_interface_modification_script/
