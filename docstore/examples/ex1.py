from docstore.repo import Repo

repo = Repo()
print repo

doc = repo.create({"title":"Some Doc Content", "body":"This is an arbitrary piece of content"})
print doc

print "The doc id is", doc.id
print "The doc content is", doc.content

