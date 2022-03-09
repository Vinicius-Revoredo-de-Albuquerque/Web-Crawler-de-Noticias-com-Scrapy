# from itemadapter import ItemAdapter


class NoticiasPipeline(object):

    def process_item(self, item, spider):

        # Tratamento do Texto: retirando os caracteres '\n' e os espaços em branco!
        item['text'] = item['text'].replace('\n', '')
        item['text'] = item['text'].replace('  ', '')

        # Tratamento do Time: retirando os caracteres '\n' e os espaços em branco!
        item['time'] = item['time'].replace('\n', '')
        item['time'] = item['time'].replace('  ', '')

        return item
