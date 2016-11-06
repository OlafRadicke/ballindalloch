import bottle
import json
import logging
import os.path
import datetime
import simplejson


import controls.home
import docker.rest

class Ballindalloch:

	def __init__(self):
		'''Constructor do some preparations for app environment'''
		self.app = bottle.Bottle()
		self.read_config()
		self.config_docker_connect()
		self.init_controler()
		self.set_routs()

	def read_config(self):
		'''Reade config file '''
		if os.path.isfile("ballindalloch.conf"):
		    with open("ballindalloch.conf") as json_file:
		        self.configData = json.load(json_file)
		else:
		    print("No local configuraton found. go continus with /etc/ballindalloch.conf...")
		    with open("/etc/ballindalloch.conf") as json_file:
		        self.configData = json.load(json_file)

	def config_docker_connect(self):
		'''Prepare database connect parameters for configuration'''
		self.dockerRest = docker.rest.RestWrapper()
		self.dockerRest.setHost( self.configData["docker_host"] )
		self.dockerRest.setPort( self.configData["docker_port"] )


	def init_controler(self):
		# init controler
		self.home_page  = controls.home.Home( self.dockerRest, self.configData )


	def set_routs(self):
		'''set routs'''
		self.app.route('/', ['GET'], self.home_page.start_get)
		self.app.route('/info', ['GET'], self.home_page.start_get)
		self.app.route('/containers', ['GET'], self.home_page.containers_get)
		self.app.route('/images', ['GET'], self.home_page.images_get)
		self.app.route('/version', ['GET'], self.home_page.version_get)
		self.app.route('/volumes', ['GET'], self.home_page.volumes_get)
		self.app.route('/networks', ['GET'], self.home_page.networks_get)
		self.app.route('/plugins', ['GET'], self.home_page.plugins_get)
		self.app.route('/nodes', ['GET'], self.home_page.nodes_get)
		self.app.route('/swarm', ['GET'], self.home_page.swarm_get)
		self.app.route('/services', ['GET'], self.home_page.services_get)
		self.app.route('/services_create', ['GET'], self.home_page.services_create_get)
		self.app.route('/services_create', ['POST'], self.home_page.services_create_post)
		self.app.route('/tasks', ['GET'], self.home_page.tasks_get)

		#/services/create

	def run(self):
		'''Start listening'''
		bottle.run(
			self.app,
			host=self.configData["webservice_host"],
			port=self.configData["webservice_port"],
			server='cherrypy'
	    )

ballindalloch = Ballindalloch()
ballindalloch.run()
