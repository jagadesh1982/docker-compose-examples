import logging
import os
import json
import tornado.ioloop
import tornado.web
import random
import time
import socket
import platform
from tornado.escape import json_encode


def getSName():
  try:
    hostSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    hostSocket.connect(("8.8.8.8", 80))
    return (hostSocket.getsockname()[0])
    hostSocket.close()
  except Exception, e:
     print e  

class Info(tornado.web.RequestHandler):
  def get(self):
    """
    Handles `/info` resource.
    """
    try:
     hostname = platform.node()
     IPAddr = getSName()
     logging.info("/info serving from %s has been invoked from %s \n", hostname, IPAddr)
     self.set_header("Content-Type", "application/json")
     self.write(json_encode(
        {
          "ip Address": IPAddr,
          "hostname": hostname, 
          "host" : self.request.host,
          "from" : self.request.remote_ip
        }
      ))
     self.finish()
    except Exception, e:
     logging.debug(e)
     self.set_status(404)

class Version(tornado.web.RequestHandler):
  def get(self):
    """
    Handles `/version` resource.
    """
    try:
      hostname = platform.node()
      IPAddr = getSName()
      logging.info("/version serving from %s has been invoked from %s \n", self.request.host, self.request.remote_ip)
      self.set_header("Content-Type", "application/json")
      self.write(json_encode(
        { 
          "Fruit Version" : "banana",
          "VERSION": VERSION,
          "ip Address": IPAddr,
          "hostname": hostname
        }
      ))
      self.finish()
    except Exception, e:
      logging.debug(e)
      print e
      self.set_status(404)

class Environment(tornado.web.RequestHandler):
  def get(self):
    """
    Handles `/env` resource.
    """
    try:
      logging.info("/env serving from %s has been invoked from %s \n", self.request.host, self.request.remote_ip)
      self.set_header("Content-Type", "application/json")
      self.write(json_encode(
        {
          "version" : VERSION,
          "env" : str(os.environ),
        }
      ))
      self.finish()
    except Exception, e:
      logging.debug(e)
      self.set_status(404)



if __name__ == "__main__":
  app = tornado.web.Application([
        (r"/info", Info),
        (r"/ver", Version),
        (r"/env", Environment)
  ])
 
 
  PORT = os.getenv('PORT0', 9876)
  VERSION = os.getenv('VERSION', "0.5.0")

  app.listen(PORT, address='0.0.0.0')
  logging.info("This is simple service in version v%s listening on port %s", VERSION, PORT)
  tornado.ioloop.IOLoop.current().start()

