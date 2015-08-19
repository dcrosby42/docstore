from docstore.document import Document
import uuid   # https://docs.python.org/2/library/uuid.html 

class DocumentNotFound:
  def __init__(self,doc_id=None):
    self._doc_id = doc_id

  def __repr__(self):
    return "DocumentNotFound(%r)" % self._doc_id
    
  pass

class Repo(object):
  def __init__(self):
    super(Repo, self).__init__()
    self._docs_by_id = {}

  def create(self, content=None):
    """Create, store and return a new Document.  Content optional."""
    doc = Document(self._next_doc_id_str(), content=content)
    self._docs_by_id[doc.id] = doc
    return doc

  def fetch(self, doc_id):
    if isinstance(doc_id,basestring):
      doc_id = uuid.UUID(doc_id)
    try:
      doc = self._docs_by_id[doc_id]
      return doc
    except KeyError:
      raise DocumentNotFound(doc_id)


  # PRIVATE:
   
  def _next_doc_id_str(self):
    u = uuid.uuid4() # random UUID
    # return str(u)
    return u

