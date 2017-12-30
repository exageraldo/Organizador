# Organizador

Script de organização de arquivos.

Criado inicialmente para organização de arquivos baixados pelo Telegram.


## Instalação
A instalação é simples, basta entrar no diretório do projeto e digitar o comando:

`$ pip install -r requirements.txt`

## Configuração
O script foi testado em maquinas com Windows e Linux.
O arquivo de configuração é o `config.json`.
Para configurar, altere os seguintes campos:
+ `formatos`: é para selecionar os arquivos que serão movidos;
+ `origem` : é o caminho do diretório onde ele irá buscar os arquivos;
+ `mover` : é o caminho para onde os arquivos dos formatos selecionados serão movidos.

> Em diretórios do Windows, é preciso que coloque duas barras (\\) ao digitar os caminhos.

### Exemplo de `config.json`
```javascript
{
  "config":{
    "formatos": ["mp3", "ogg", "acc", "wma"],
    "windows":{
      "origem": "C:\\Users\\{0}\\Downloads\\Telegram Desktop",
      "mover": "C:\\Users\\{0}\\Music"
    },
    "linux": {
      "origem": "/home/{0}/Downloads/Telegram Desktop",
      "mover": "/home/{0}/Music"
    }
  }
}

```
Os caminhos colocados são caminhos padrões de downloads do Telegram tanto no Windows, quanto no Linux. Eles podem ser alterados para qualquer diretórios do computador.

> O script ~~ainda~~ não cria pastas/diretórios não existentes. Ele pressupõe que os caminhos selecionados já existem no sistema.

O arquivo serve tanto para sistemas Windows, como para Linux. Caso queira usar em apenas um sistema especifico, pode remover as configurações do outro. Por exemplo, para sistemas Linux:
```javascript
{
  "config":{
    "formatos": ["mp3", "ogg", "acc", "wma"],
    "linux": {
      "origem": "/home/{0}/Downloads/Telegram Desktop",
      "mover": "/home/{0}/Music"
    }
  }
}

```


> O caminho do diretório deve ser absoluto, ou seja, o caminho completo.
>
> Substitua o nome de usuário pelo marcador `{0}` para que o script funcione adequadamente.
