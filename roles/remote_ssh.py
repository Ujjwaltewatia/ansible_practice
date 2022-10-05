#from ipaddress import ip_address
import subprocess


def runCommandOnRemote(ip, user, pemkey, command):
    print(
        f"Running ---> ssh -i {pemkey} {user}@{ip} {command}")
    commands = command.split(' ')
    executable_command = [
        'ssh', '-o', 'StrictHostKeyChecking=no', '-i', f'{pemkey}', f'{user}@{ip}']
    executable_command.extend(commands)
    p = subprocess.run(executable_command, stdout=subprocess.PIPE)
    if p.returncode == 0:
        return p.stdout.decode()
    else:
        raise Exception(f"Error Running {command} command on host {ip}")


while True:
    print("Choose a input", end='\n')
    print("1. Provide the command to be executed on remote servers", end='\n')
    command = input()
    print("2. Provide the path of file that contains comma separated IP Address, User and path of pem key", end='\n')
    file_path = input()
    print("3. Type Y[y] to continue and N[n] to exit ")
    out = input()

    if out == "Y" or out == "y":
        pass
    else:
        break

    with open(file_path, 'r') as file:
        data = file.read().splitlines()
        print(data)
        for line in data:
            content = line.split(',')
            print(content)
            ip_address = content[0]
            user = content[1]
            pemfile_path = content[2]
            print(command)
            try:
                output = runCommandOnRemote(
                    ip_address, user, pemfile_path, command)
                print("Command Successfully ran on host "+ip_address)
                print(output)
            except Exception as e:
                print(e)
