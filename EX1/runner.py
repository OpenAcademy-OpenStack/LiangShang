import keystoneclient.v2_0.client as ksclient
import novaclient.v1_1.client as nvclient
import glanceclient
import os
import time

def get_keystone_creds():
    d = {}
    d['username'] = 'admin'
    d['password'] = 'password'
    d['auth_url'] = 'http://10.0.2.15:5000/v2.0/'
    d['tenant_name'] = 'demo'
    return d

def get_nova_creds():
    d = {}
    d['username'] = 'admin'
    d['api_key'] = 'password'
    d['auth_url'] = 'http://10.0.2.15:5000/v2.0/'
    d['project_id'] = 'demo'
    return d

def create_instance_for(image):
    flavor = nova.flavors.find(name="m1.micro")
    instance = nova.servers.create(name="test", image=image, flavor=flavor)

if __name__== "__main__":
    keystone_creds = get_keystone_creds()
    keystone = ksclient.Client(**keystone_creds)
    nova_creds = get_nova_creds()
    nova = nvclient.Client(**nova_creds)

    glance_endpoint = keystone.service_catalog.url_for(service_type='image',
                                                       endpoint_type='publicURL')
    glance = glanceclient.Client('1',glance_endpoint, token=keystone.auth_token)
    #print glance
    images = glance.images.list()
   # print images
    for one_image in images:
    	if one_image.name.find('ubuntu') > -1: 
    	    create_instance_for(one_image)


   