# Awesomobot - custom audio bot for Discord app

Update Instructions:
  - Add new commands with the same name as the audio file its gonna play;
  - All audios must be in the 'audio' folder;
  - No need to add the new entries to the .help command. It's automated now;
  - Keep it clean;
  - If there is updates to the bot, its automatically uploaded to the server. So don't break it;
 
WIP:
   - [x]  Automatic server updates/upload;
   - [ ]  Export some en variables;
   - [ ]  Reduce repetitive code (on command functions);

--------------------------
## Setup:

### Python e dependencias
`yum install git python36  python36-pip python36-setuptools python-devel libevent-devel  -y && mkdir ./awesomobot && cd ./awesomobot`

### Instalar ffmpeg

`rpm --import http://li.nux.ro/download/nux/RPM-GPG-KEY-nux.ro`
`rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm`
`yum install ffmpeg ffmpeg-devel -y`

### Clona repo
`git clone https://github.com/lariskovski/audio-bot.git && cd ./awesomobot/audio-bot`

### Dependencias
`pip3 install -r requirements.txt`


### Arquivos do serviços
`touch /etc/init.d/awesomobot.conf && touch /usr/lib/systemd/system/awesomobot.service`

~~~~
tee -a /etc/init.d/awesomobot.conf <<EOF
chdir /home/$USER/awesomobot
exec python3.6 awesomobot.py
respawn
EOF
~~~~

~~~~
tee -a /usr/lib/systemd/system/awesomobot.service <<EOF
[Unit]
Description=Discord Bot
After=auditd.service systemd-user-sessions.service time-sync.target

[Service]
User=root
TimeoutStartSec=0
Type=simple
KillMode=process
export BOT_HOME=/home/$USER/awesomobot/
export PATH=$PATH:$BOT_HOME
WorkingDirectory=/home/$USER/awesomobot
ExecStart=/usr/bin/python3.6 /home/$USER/awesomobot/awesomobot.py
Restart=always
RestartSec=2
LimitNOFILE=5555

[Install]
WantedBy=multi-user.target
EOF
~~~~

### Start the service
`service awesomobot start`


--------------
### Jenkins build option

With Github-webhook active
~~~~
ssh root@dockerhost -p port "cp -r /var/lib/docker/volumes/[codigo do volume do container]/_data/workspace/audio-bot/* /root/audio-bot/ && service awesomobot restart"
~~~~
