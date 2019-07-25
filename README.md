# Awesomobot - custom audio bot for Discord app

Update Instructions:
  - Add new commands with the same name as the audio file its gonna play;
  - All audios must be in the 'audio' folder;
  - No need to add the new entries to the .help command. It's automated now;
  - Keep it clean;
  - If there is updates to the bot, its manually uploaded to the server (for now);
 
WIP:
  - Automatic server updates/upload;
  - Reduce repetitive code (on command functions);


Setup:
###piton e dependencias
#yum install git python36  python36-pip python36-setuptools python-devel libevent-devel  -y && mkdir ./awesomobot && cd ./awesomobot

###instalar ffmpeg

#rpm --import http://li.nux.ro/download/nux/RPM-GPG-KEY-nux.ro
#rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm
#yum install ffmpeg ffmpeg-devel -y

###clona repo
#git clone https://github.com/lariskovski/audio-bot.git && cd ./awesomobot/audio-bot

###dependencias
#pip3 install -r requirements.txt


###arquivos do serviços
#touch /etc/init.d/awesomobot.conf && touch /usr/lib/systemd/system/awesomobot.service

#tee -a /etc/init.d/awesomobot.conf <<EOF
chdir /home/$USER/awesomobot
exec python3.6 awesomobot.py
respawn
EOF

#tee -a /usr/lib/systemd/system/awesomobot.service <<EOF
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


#service awesomobot start
