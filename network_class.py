# -*- coding: utf-8 -*-

import time
import paramiko


class NetworkSSH:

    remote_conn = None

    ############################################
    # Configuration
    ############################################

    # hostname = u'<device-id>'
    # username = u'<device-user-name>'
    # password = u'<device-password>'

    hostname = u'187.95.236.107'
    username = u'eduardo'
    password = u'edu@rdo.2020'

    ############################################
    # Functions
    ############################################

    def log(self, message):
        print('>> {}...'.format(message))

    def run_command(self, commands):

        if not isinstance(commands, list):
            commands = [commands]

        for command in commands:
            self.remote_conn.send('{}\n'.format(command))                                   # Wrap the command you want to send in quotes
            time.sleep(2)                                                                   # Wait for device to return the output of the CLI
            output = self.remote_conn.recv(1000)                                            # Save 1000 bytes of the returned output to variable output
            print('>> ' + output.decode("utf-8", errors='replace').replace('', ''))        # Print the variable output

    ############################################
    # Logic
    ############################################

    def connect(self):

        # Connect to switch and build ssh connection
        remote_conn_pre = paramiko.SSHClient()
        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        remote_conn_pre.connect(
            hostname=self.hostname,
            username=self.username,
            password=self.password,
            look_for_keys=False,
            allow_agent=False
        )

        self.log('SSH connection established to ' + self.hostname)
        self.remote_conn = remote_conn_pre.invoke_shell()
        self.log('Interactive SSH session established')

        # Print terminal to screen
        self.run_command('')

        # Username root requires getting into the cli
        if self.username == 'root':
            self.run_command('cli')

        # Show routes
        self.run_command('show route')

    def configure(self, device, vlan, ports):

        self.log('Ajustando confogiração do device: {}'.format(device))

        commands = [
            'configure',
            'set vlans vlan{vlan} vlan-id {vlan}'.format(vlan=vlan),
            'set interfaces ge-0/0/{port} unit 0 family ethernet-switching port-mode trunk'.format(port=ports[0]),
            'set interfaces ge-0/0/{port} unit 0 family ethernet-switching vlan members vlan{vlan}'.format(vlan=vlan, port=ports[0]),
            'set interfaces ge-0/0/{port} unit 0 family ethernet-switching port-mode trunk'.format(port=ports[1]),
            'set interfaces ge-0/0/{port} unit 0 family ethernet-switching vlan members vlan{vlan}'.format(vlan=vlan, port=ports[1]),
            'commit',
        ]
        self.run_command(commands)

        # show configuregion
        self.run_command('run show vlans | find vlan{vlan}'.format(vlan=vlan, port=ports[0]))
