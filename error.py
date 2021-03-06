import cgi
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.ext import db
import webapp2
from stream import Stream
from stream import Picture

from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers

from google.appengine.api import images


ERROR_PAGE_TEMPLATE ="""\
<!DOCTYPE html>
<html>
<body>
  <h1>Connex.us</h1>
    <table style="width:50%">
      <tr>
      <td><a href="management">Manage</td>
      <td><a href="createstream">Create</a></td>
      <td><a href="viewallstream">View</a></td>
        <td><a href="search">Search</a></td>
        <td><a href="trending">Trending</a></td>
        <td><a href="social">Social</a></td>
      </tr>
    </table>
    <h3>Error: you tried to create a new stream</h3>
    <h3> whose name is same as an</h3>
    <h3> existing stream; operation did not complete.</h3>
    </body>
</html>
"""
class error(webapp2.RequestHandler):
  def get(self):
    self.response.write(ERROR_PAGE_TEMPLATE)
    self.response.out.write('<td><img src="http://technothlon.techniche.org/error/error.png"></img></td>')


application = webapp2.WSGIApplication([
    ('/error.*', error),
], debug=True)
