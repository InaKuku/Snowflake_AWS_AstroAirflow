class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if not category in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if not topic in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if not document in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name:str):
        cat = [categ for categ in self.categories if categ.id == category_id]
        if len(cat) >  0:
            cat[0].edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        tpc = [tpc for tpc in self.topics if tpc.id == topic_id]
        if len(tpc) > 0:
            tpc[0].edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        dcm = [dcm for dcm in self.documents if dcm.id == document_id]
        if len(dcm) > 0:
            dcm[0].edit(new_file_name)


    def delete_category(self, category_id):
        ctg = [ctg for ctg in self.categories if ctg.id == category_id]
        if len(ctg) > 0:
            self.categories.remove(ctg[0])

    def delete_topic(self, topic_id):
        tpc = [tpc for tpc in self.topics if tpc.id == topic_id]
        if len(tpc) > 0:
            self.topics.remove(tpc[0])


    def delete_document(self, document_id):
        dcm = [dcm for dcm in self.documents if dcm.id == document_id]
        if len(dcm) > 0:
            self.documents.remove(dcm[0])

    def get_document(self, document_id):
        doc = [dcm for dcm in self.documents if dcm.id==document_id]
        if len(doc) > 0:
            return doc[0]

    def __repr__(self):
        result = ""
        result += '\n'.join([dc.__repr__() for dc in self.documents])
        return result