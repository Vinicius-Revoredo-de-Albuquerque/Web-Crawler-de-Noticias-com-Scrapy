# Log de Trabalho

**1º e 2º dia:** Estudei o framework, entendi a estrutura padrão de arquivos e como esses se relacionam. Através da documentação scrapy, medium.com e alguns vídeos.

Utilizei o scrapy shell para visualizar o funcionamento dos 'CSS Selectors' e entender como obter os dados das páginas web.             

**3º dia:** Implementei o código principal das spiders, a estruturação dos dados no arquivo items.py, o tratamento do texto nos arquivos pipelines.py e settings.py.

Pesquisei sobre métricas em web crawling e, com o que entendi, tentei pensar em como poderia usar os dados obtidos para gerar as métricas.

Então adicionei a primeira métrica. Do dado 'text' coletado é possível saber a quantidade de palavras no artigo.
A partir de alguma métrica de tempo de leitura por palavra é possível obter o tempo de leitura total do artigo.
Assim como da quantidade de palavras no título é possível prever a quantidade de tags que o artigo poderia ter.

**4º dia:** Corrigi e refatorei alguns trechos de código, como o trecho sobre a primeira métrica.

Implementei mais uma métrica. 
Forward Link Count, a partir da quantidade de links referenciando outras páginas, em cada artigo, é possível fazer um ranking de importância para os artigos.

Escrevi o README.md.


# Escalando a Solução

crawling em mais paginas

uso de banco de dados para guardar os dados

exemplo de analises que poderiam ser feitas, se tiver
