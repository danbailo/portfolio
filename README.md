# Tutorial to deploy Flask application to AWS (Free)

Can works fine in others clouds, but I've test only in AWS.

Tested in EC2, Ubuntu 18.04

## Sending project to your server
    scp -i "{your_key.pem}" -r {project_folder} {your_user}@{your_public_server_ip}

## Connecting in your server

    ssh -i "{your_key.pem}" {your_user}@{your_public_server_ip}    

## Preparing enviroment
    sudo apt install update
    sudo apt install full-upgrade
    sudo apt install python3-pip

    cd project_folder
    python3 -m virtualenv venv -p=PYTHON_VERSION

    source venv/bin/activate

    pip3 install -r requirements.txt
    pip3 install gunicorn

## Configuring AWS

After prepare env, we need to add firewall rules to your server accept connections.

Go to `Instances` page in your account in AWS.

* Select your Instance
* In `Description` tab, select `launch-wizard-2`
* Select `Inbound rules`, then click in the button `Edit inbound rules`

Create the rules:

* `HTTP` - add IP `0.0.0.0/0`
* `HTTPS` - add IP `0.0.0.0/0`
* `SSH` - add IP `0.0.0.0/0`
* `Custom TCP` - Port: 5000, add IP `0.0.0.0/0`

and then, click in `Save rules`.

Now, your server can receive connections.

## Setting Nginx

    sudo apt install nginx

    sudo rm /etc/nginx/sites-enabled/default

    sudo touch /etc/nginx/sites-available/{app_name}_settings
    sudo ln -s /etc/nginx/sites-available/{app_name}_settings /etc/nginx/sites-enabled/{app_name}_settings

    sudo nano /etc/nginx/sites-enabled/{app_name}_settings

Put the following settings inside `/etc/nginx/sites-enabled/{app_name}_settings`

    server {
        location / {
            proxy_pass http://127.0.0.1:8000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }
    }


And then, restart nginx

    sudo /etc/init.d/nginx restart

## Setting Supervisor


    sudo apt install supervisor

    sudo nano /etc/supervisor/conf.d/{app_name}.conf

Put the following settings inside `/etc/supervisor/conf.d/{app_name}.conf`

    [program:{app_name}]
    directory=/home/{your_user}/{project_folder}/src
    command=/home/{your_user}/{project_folder}/venv/bin/gunicorn -w {no_workers} wsgi
    user={your_user}
    autostart=true
    autorestart=true
    killasgroup=true
    stderr_logfile=/var/log/{app_name}/{app_name}.err.log
    stdout_logfile=/var/log/{app_name}/{app_name}.out.log

Create the log files

    sudo mkdir -p /var/log/{app_name}/

    sudo touch /var/log/{app_name}/{app_name}.err.log
    sudo touch /var/log/{app_name}/{app_name}.out.log

And then, reload supervisor

    sudo supervisorctl reload

### ALL DONE

Your server should be online and you can access it using the public IP in any internet browser.