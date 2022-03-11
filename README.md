# Web-Crawler-de-Noticias-com-Scrapy
Desafio/Projeto do Processo Seletivo para vaga de Estágio em Engenharia de Dados na Oncase.

Instale o Scrapy, caso não tenha, utilizando: $ pip install scrapy

No diretório ...Web-Crawler-de-Noticias-com-Scrapy/noticias, utilize os seguintes comandos para executar as "Spiders" e gerar os arquivos:

$ scrapy crawl [spider] -o dados/[nome do arquivo].json

  ou
  
$ scrapy crawl [spider] -o dados/[nome do arquivo].csv
  
Os nomes das spiders são 'omelete' e 'cinepop'. Os arquivos gerados vão estar na pasta 'dados'.
