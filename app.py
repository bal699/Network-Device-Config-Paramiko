# -*- coding: utf-8 -*-

import paramiko

import time

############################################
# Configuration
############################################

hostname = u'<device-id>'
username = u'<device-user-name>'
password = u'<device-password>'

############################################
# Functions
############################################

def log(message):
    print('>> {}...'.format(message))

def run_command(commands):

    if not isinstance(commands, list):
        commands = [commands]

    for command in commands:
        remote_conn.send('{}\n'.format(command))                                         # Wrap the command you want to send in quotes
        time.sleep(2)                                                                    # Wait for device to return the output of the CLI
        output = remote_conn.recv(1000)                                                  # Save 1000 bytes of the returned output to variable output
        print('>> ' + output.decode("utf-8", errors='replace').replace('', ''))         # Print the variable output

############################################
# Logic
############################################

# Connect to switch and build ssh connection
remote_conn_pre = paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(
    hostname=hostname,
    username=username,
    password=password,
    look_for_keys=False,
    allow_agent=False
)

log('SSH connection established to ' + hostname)
remote_conn = remote_conn_pre.invoke_shell()
log('Interactive SSH session established')

# Print terminal to screen
run_command('')

# Username root requires getting into the cli
if username == 'root':
    run_command('cli')

# Show routes
run_command('show route')

# Set configuration on devices

devices = [
    {
        'id': 1,
        'name': 'Torre Natal',
        'vlan': 90,
        'ports': [0, 1]
    },
    {
        'id': 2,
        'name': 'Torre Guarabira',
        'vlan': 91,
        'ports': [2, 3]
    },
    {
        'id': 3,
        'vlan': 92,
        'name': 'Torre Rio de Janeiro',
        'ports': [4, 5]
    },
]

# para cada device selecionado
for device in devices:

    log('Ajustando confogiração do device: {}'.format(device.get('name')))

    vlan = device.get('vlan')
    ports = device.get('ports')

    commands = [
        'configure',
        'set vlans vlan{vlan} vlan-id {vlan}'.format(vlan=vlan),
        'set interfaces ge-0/0/{port} unit 0 family ethernet-switching port-mode trunk'.format(port=ports[0]),
        'set interfaces ge-0/0/{port} unit 0 family ethernet-switching vlan members vlan{vlan}'.format(vlan=vlan, port=ports[0]),
        'set interfaces ge-0/0/{port} unit 0 family ethernet-switching port-mode trunk'.format(port=ports[1]),
        'set interfaces ge-0/0/{port} unit 0 family ethernet-switching vlan members vlan{vlan}'.format(vlan=vlan, port=ports[1]),
        'commit',
    ]
    run_command(commands)

    # show configuregion
    run_command('run show vlans | find vlan{vlan}'.format(vlan=vlan, port=ports[0]))
