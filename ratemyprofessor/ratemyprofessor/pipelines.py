# pipeline spider output to a text file
class FilePipeline(object):

    def __init__(self):
        self.file = open('schools.txt', 'wb')

    def process_item(self, item, spider):
        line = item['name'].strip() + ', ' + item['city'].strip() + ', ' + item['region'].strip() + '\n'
        self.file.write(line)
        return item
