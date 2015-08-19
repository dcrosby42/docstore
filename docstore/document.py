class Document(object):
  """docstring for Document"""
  def __init__(self, doc_id, content=None):
    super(Document, self).__init__()
    self._id = doc_id
    self._content = content
     
  def id():
    doc = "The id property."
    def fget(self):
      return self._id
    return locals()
  id = property(**id())
  
  def content():
    doc = "The content property."
    def fget(self):
      return self._content
    def fset(self, value):
      self._content = value
    def fdel(self):
      del self._content
    return locals()
  content = property(**content())

