import os
import sys

c = c  # pylint:disable=undefined-variable

# c.JupyterHub.spawner_class = 'dockerspawner.SystemUserSpawner'
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_IMAGE']
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
c.JupyterHub.hub_ip = os.environ['HUB_IP']

# c.JupyterHub.tornado_settings = {'slow_spawn_timeout': 30}
c.Spawner.args = ['--NotebookApp.allow_origin=*']
#c.NotebookApp.allow_remote_access = True
# c.JupyterHub.tornado_settings = {
#     'headers': {
#         'Access-Control-Allow-Origin': '*'
#     },
# }

# user data persistence
# see https://github.com/jupyterhub/dockerspawner#data-persistence-and-dockerspawner
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan/work'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }


# For Google OAuth Authentication
from oauthenticator.google import LocalGoogleOAuthenticator
c.JupyterHub.authenticator_class = LocalGoogleOAuthenticator

c.LocalGoogleOAuthenticator.create_system_users = True
c.Authenticator.add_user_cmd = ['adduser', '-q', '--gecos', '""', '--disabled-password', '--force-badname']

"""
c.Authenticator.username_map = {
    'javieranorgab@gmail.com': 'jabenito'
}
"""

c.Authenticator.allowed_users = allowed_users = set()
c.Authenticator.admin_users = admin = set()

join = os.path.join

here = os.path.dirname(__file__)
root = os.environ.get('OAUTHENTICATOR_DIR', here)
sys.path.insert(0, root)

with open(join(root, 'userlist')) as f:
    for line in f:
        if not line:
            continue
        parts = line.split(',')
        name = parts[0].strip()
        service_name = parts[2].strip()
        c.Authenticator.username_map.update({service_name : name})
        allowed_users.add(name)
        #allowed_users.add(service_name)
        if len(parts) > 1 and parts[1].strip() == 'admin':
            admin.add(name)
            #admin.add(service_name)

c.GoogleOAuthenticator.oauth_callback_url = os.environ['OAUTH_CALLBACK_URL']

# c.JupyterHub.services = [
#     {
#         'name': 'cull_idle',
#         'admin': True,
#         'command': 'python /srv/jupyterhub/cull_idle_servers.py --timeout=3600'.split(),
#     },
# ]