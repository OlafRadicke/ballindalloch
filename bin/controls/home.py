import bottle
import json
import simplejson
import logging
import yaml

class Home:

	def __init__(self, dockerRest, configData):
		self.dockerRest = dockerRest
		self.configData = configData

	def start_get(self):
		'''Controller of the start page. Get info'''

		response = self.dockerRest.doGET("/info")
		info_list = json.loads(response.text)
		print( json.dumps(info_list, sort_keys=True, indent=4, separators=(',', ': ')) )

		html_sources = bottle.template(
		    'home',
			uri_prefix=self.configData[ "webservice_pub_host" ],
		    title="Info site",
		    main_area=json.dumps(info_list, sort_keys=True, indent=4, separators=(',', ': '))
		)
		return html_sources

	def containers_get(self):
		'''Controller list containers'''

		response = self.dockerRest.doGET("/containers/json")
		info_list = json.loads(response.text)
		print( json.dumps(info_list, sort_keys=True, indent=4, separators=(',', ': ')) )

		html_sources = bottle.template(
		    'home',
			uri_prefix=self.configData[ "webservice_pub_host" ],
		    title="All containers",
		    main_area=json.dumps(info_list, sort_keys=True, indent=4, separators=(',', ': '))
		)
		return html_sources

	def images_get(self):
		'''Controller list images'''

		response = self.dockerRest.doGET("/images/json")
		info_list = json.loads(response.text)
		print( json.dumps(info_list, sort_keys=True, indent=4, separators=(',', ': ')) )

		html_sources = bottle.template(
		    'home',
			uri_prefix=self.configData[ "webservice_pub_host" ],
		    title="All images",
		    main_area=json.dumps(info_list, sort_keys=True, indent=4, separators=(',', ': '))
		)
		return html_sources

	def version_get(self):
		'''Controller get version info'''

		response = self.dockerRest.doGET("/version")
		info_list = json.loads(response.text)
		print( json.dumps(info_list, sort_keys=True, indent=4, separators=(',', ': ')) )

		html_sources = bottle.template(
		    'home',
			uri_prefix=self.configData[ "webservice_pub_host" ],
		    title="Version",
		    main_area=json.dumps(info_list, sort_keys=True, indent=4, separators=(',', ': '))
		)
		return html_sources


	def volumes_get(self):
		'''Controller list of volumes'''

		response = self.dockerRest.doGET("/volumes")
		info_list = json.loads(response.text)
		print( json.dumps(info_list, sort_keys=True, indent=4, separators=(',', ': ')) )

		html_sources = bottle.template(
		    'home',
			uri_prefix=self.configData[ "webservice_pub_host" ],
		    title="Volumes",
		    main_area=json.dumps(info_list, sort_keys=True, indent=4, separators=(',', ': '))
		)
		return html_sources

	def networks_get(self):
		'''Controller list ofnetworks'''

		response = self.dockerRest.doGET("/networks")
		info_list = json.loads(response.text)
		print( json.dumps(info_list, sort_keys=True, indent=4, separators=(',', ': ')) )

		html_sources = bottle.template(
		    'home',
			uri_prefix=self.configData[ "webservice_pub_host" ],
		    title="Networks",
		    main_area=json.dumps(info_list, sort_keys=True, indent=4, separators=(',', ': '))
		)
		return html_sources


	def plugins_get(self):
		'''Controller list of plugins'''

		response = self.dockerRest.doGET("/plugins")
		info_list = json.loads(response.text)
		print( json.dumps(info_list, sort_keys=True, indent=4, separators=(',', ': ')) )

		html_sources = bottle.template(
		    'home',
			uri_prefix=self.configData[ "webservice_pub_host" ],
		    title="Plugins",
		    main_area=json.dumps(info_list, sort_keys=True, indent=4, separators=(',', ': '))
		)
		return html_sources

	def nodes_get(self):
		'''Controller list of nodes'''

		response = self.dockerRest.doGET("/nodes")
		info_list = json.loads(response.text)
		print( json.dumps(info_list, sort_keys=True, indent=4, separators=(',', ': ')) )

		html_sources = bottle.template(
		    'home',
			uri_prefix=self.configData[ "webservice_pub_host" ],
		    title="Nodes",
		    main_area=json.dumps(info_list, sort_keys=True, indent=4, separators=(',', ': '))
		)
		return html_sources

	def swarm_get(self):
		'''Controller info of swarm'''

		response = self.dockerRest.doGET("/swarm")
		info_list = json.loads(response.text)
		print( json.dumps(info_list, sort_keys=True, indent=4, separators=(',', ': ')) )

		html_sources = bottle.template(
		    'home',
			uri_prefix=self.configData[ "webservice_pub_host" ],
		    title="Swarm",
		    main_area=json.dumps(info_list, sort_keys=True, indent=4, separators=(',', ': '))
		)
		return html_sources

	def services_get(self):
		'''Controller list of services'''

		response = self.dockerRest.doGET("/services")
		info_list = json.loads(response.text)
		print( json.dumps(info_list, sort_keys=True, indent=4, separators=(',', ': ')) )

		html_sources = bottle.template(
		    'home',
			uri_prefix=self.configData[ "webservice_pub_host" ],
		    title="Services",
		    main_area=json.dumps(info_list, sort_keys=True, indent=4, separators=(',', ': '))
		)
		return html_sources

	def services_create_get(self):
		'''Create service form'''

		block_create_service = bottle.template('block_create_service')

		html_sources = bottle.template(
		    'skeleton',
			uri_prefix=self.configData[ "webservice_pub_host" ],
		    title="Create ervices",
		    main_area=block_create_service
		)
		return html_sources

	def services_create_post(self):
		'''The POST controller for creating new service'''

		json_doc = bottle.request.forms.getunicode('description_text')
		print( "I will send: \n \n" + json_doc)
		response = self.dockerRest.doPOST( "/services/create", json_doc )
		print( "response: \n \n " + response.text )
		print( response )
		bottle.redirect("/services")


	def tasks_get(self):
		'''Controller list of tasks'''

		response = self.dockerRest.doGET("/tasks")
		info_list = json.loads(response.text)
		print( json.dumps(info_list, sort_keys=True, indent=4, separators=(',', ': ')) )

		html_sources = bottle.template(
		    'home',
			uri_prefix=self.configData[ "webservice_pub_host" ],
		    title="Tasks",
		    main_area=json.dumps(info_list, sort_keys=True, indent=4, separators=(',', ': '))
		)
		return html_sources
