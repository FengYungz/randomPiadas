# Serviço de Piadas de Programação


## Descrição :rotating_light:
Este micro serviço em Flask fornece piadas de programação aleatórias, com suporte para filtragem por nível de humor e seleção de idioma.


---


## Estrutura do Projeto :construction:

  - `app.py`: O arquivo principal da aplicação Flask.
  - `jokes.py`: Lógica para carregar e gerenciar piadas.
  - `data/jokes.json`: Arquivo JSON com as piadas.
  - `templates/index.html`: Front-end da aplicação.
  - `static/style.css`: Arquivo CSS para estilização da página.


  ---


## Endpoint :card_file_box:


#### `GET /joke`
- Retorna uma piada de programação aleatória.
- Parâmetro de consulta opcional:
  - `level`: Define o nível de humor (low, medium, high). Exemplo: `/joke?level=high`.
- Cabeçalho HTTP:
  - `Accept-Language`: Define o idioma da piada (`en` para inglês ou `pt-br` para português do Brasil).


---


# Guia para uso :memo:


## 1 - Preparando Ambiente


1) git clone nesse repositório

2) Navegue até

```bash
/randomPiadas
```


## 2 - Construa a imagem Docker

```bash
docker build -t randompiada .
```

### Agora vamos executar o container:

```bash
docker build -t randompiada .
```
# Agora vamos testar! :rocket:

## Testando no Insomnia
 1) Abra o Insomnia.

 2) Crie uma nova requisição

  - Clique em "New Request" e dê um nome (por exemplo, "Get Joke")
  - Selecione o método GET
3) Configuração da URL

 - Defina a URL como:

```bash
http://localhost:5000/joke
```

 - Passando o Parâmetro `level` na URL

 A API permite que o usuário filtre as piadas por nível de humor diretamente pela URL, utilizando o parâmetro de consulta level. Esse parâmetro é opcional, e, se não for fornecido, a API retorna uma piada de nível médio por padrão.

 Como usar o parâmetro `level` na URL

 Você pode passar o nível de humor (como low, medium, ou high) na URL da seguinte maneira:

- Exemplo de requisição GET:

```bash
http://localhost:5000/joke?level=low
joke
```

Observação:

- Se você omitir o parâmetro level, a API retornará uma piada de nível médio.


## Testando a API via HTML no Navegador

Você também pode testar a API diretamente pelo navegador usando o arquivo HTML que foi criado.

Passos:

1) Abrir o arquivo HTML no navegador:

- Abra o arquivo index.html:

  ![Texto alternativo](/images/telaInicial.png)

2) Selecione o Idioma e Nível da Piada:

  - No formulário da página, você verá uma opção de seleção para o idioma (Português ou Inglês) e o nível da piada (low, medium, high).

  - Selecione suas preferências.

3) Clique no Botão para Obter Piada:

  - Clique em "Obter Piada".

  - O JavaScript fará uma requisição para a API e exibirá a piada na tela

  ![Texto alternativo](/images/telaFinal.png)


# Pronto, espero que tenha se divertido! :zap: