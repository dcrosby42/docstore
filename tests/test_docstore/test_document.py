from docstore.document import Document

class TestDocument:
  def setup(self):
    self.doc = Document("docId1", "initial content")

  def test_id(self):
    assert self.doc.id == "docId1"

  def test_content(self):
    assert self.doc.content == "initial content"

    c2 = { "new": [ "content", "strings" ] }
    self.doc.content = c2
    assert self.doc.content == c2


    
