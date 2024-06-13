import os

# add extra files to watch for changes
extra_dirs = ['DashboardApp',]
extra_files = extra_dirs[:]
for extra_dir in extra_dirs:
    for dirname, dirs, files in os.walk(extra_dir):
        for filename in files:
            filename = os.path.join(dirname, filename)
            if os.path.isfile(filename):
                extra_files.append(filename)

# load ssl
ssl_path = os.path.join(os.path.dirname(__file__), 'ssl')
if os.path.exists(ssl_path):
    # load key and cert
    ssl_key_path = os.path.join(ssl_path, 'key.pem')
    ssl_cert_path = os.path.join(ssl_path, 'cert.pem')

    with open(ssl_key_path, 'rb') as ssl_key_file:
        ssl_key = ssl_key_file.read()
    
    with open(ssl_cert_path, 'rb') as ssl_cert_file:
        ssl_cert = ssl_cert_file.read()
    
    ssl_context = (ssl_cert, ssl_key)
else:
    ssl_context = 'adhoc'
