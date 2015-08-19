from docstore.document import Document
from docstore.repo import Repo, DocumentNotFound
import types
import uuid

from nose.tools import assert_raises

class TestRepo:
  def setup(self):
    self.repo = Repo()

  def test_create_empty(self):
    doc = self.repo.create()
    assert doc != None
    assert doc.id != None
    assert isinstance(doc.id, uuid.UUID)
    assert doc.content == None

  def test_create_with_content(self):
    data = {"some":"data"}
    doc = self.repo.create(data)
    assert doc.content == data

  def test_fetch(self):
    content = {"more":"info"}
    doc = self.repo.create(content)
    doc2 = self.repo.fetch(doc.id)
    assert doc2.id == doc.id
    assert doc2.content == content

  def test_fetch_miss(self):
    random_id = uuid.uuid4()
    assert_raises(DocumentNotFound, lambda: self.repo.fetch(random_id))

  def test_fetch_string_id(self):
    content = {"more":"info"}
    doc = self.repo.create(content)
    assert isinstance(doc.id, uuid.UUID) # sanity check
    string_id = str(doc.id)

    doc2 = self.repo.fetch(string_id)
    assert isinstance(doc2.id, uuid.UUID) # sanity check 2
    assert doc2.id == doc.id
    assert doc2.content == content
    




    
