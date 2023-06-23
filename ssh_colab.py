import sys
import os
import re

def main():
    cloudflared_path =os.environ['USERPROFILE']+r"\.ssh\cloudflared.exe"
    default_open_path = '/code'
    args = sys.argv[1:]

    if len(args) != 1:
        print("Expected 1 argument.")
        print("Usage: python script.py <HostName>")
        sys.exit(1)

    hostname = args[0]
    user = 'root'

    ssh_config = f"""# >>> sshcolab
Host sshcolab
\tHostName {hostname}
\tUser {user}
\tUserKnownHostsFile NUL
\tVisualHostKey yes
\tStrictHostKeyChecking no
\tProxyCommand {cloudflared_path} access ssh --hostname %h
#<<< sshcolab
"""

    config_path = os.path.expanduser('~/.ssh/config')

    with open(config_path, 'r') as f:
        contents = f.read()

    pattern = re.compile(r'# >>> sshcolab.*?#<<< sshcolab', re.DOTALL)
    new_contents = pattern.sub('', contents).strip() + '\n\n' + ssh_config

    with open(config_path, 'w') as f:
        f.write(new_contents)

    os.system(f'code --remote ssh-remote+{user}@sshcolab {default_open_path}')

if __name__ == '__main__':
    main()