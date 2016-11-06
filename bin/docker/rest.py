
import requests
import json


class RestWrapper:
	## A wrapper class for the rest api of couchdb

	uri_host = "localhost"
	uri_port = "5984"
	user = ""
	password = ""
	database = ""

	def setHost(self, hostname):
	    self.uri_host = hostname

	def setPort(self, portnumber):
	    self.uri_port = portnumber

	def doGET(self, uri_path):
	    ## A GET-Request
	    # @param uri_path the uri path
	    request_uri = "http://" + self.uri_host + ":" + self.uri_port + uri_path
	    print( request_uri )
	    headers = {'content-type': 'application/json'}
	    return requests.get(request_uri, auth=(self.user, self.password), headers=headers)

	def doPUT(self, uri_path):
	    ## A PUT-Request
	    # @param uri_path the uri path
	    request_uri = "http://" + self.uri_host + ":" + self.uri_port + uri_path
	    print(request_uri)
	    return requests.put(request_uri, auth=(self.user, self.password))

	def doPUT2(self, uri_path, json_doc):
	    ## A PUT-Request
	    # @param uri_path the uri path
	    # @param json_doc a json document
	    request_uri = "http://" + self.uri_host + ":" + self.uri_port + uri_path
	    return requests.put(request_uri, auth=(self.user, self.password), json=json.loads(json_doc))

	def doDELETE(self, uri_path):
	    ## A DELETE-Request
	    # @param uri_path the uri path
	    request_uri = "http://" + self.uri_host + ":" + self.uri_port + uri_path
	    return requests.delete(request_uri, auth=(self.user, self.password))

	def doPOST(self, uri_path, json_doc):
		## A Post-Request
		# @param uri_path the uri path
		# @param json_doc a json document
		request_uri = "http://" + self.uri_host + ":" + self.uri_port + uri_path
		headers = {'content-type': 'application/json'}
		json_bin=json.loads(json_doc)
		return requests.post(request_uri, json=json_bin, headers=headers)
