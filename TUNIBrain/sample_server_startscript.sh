cd ~/UTAbotti/rosie-y/scripts/xnix
screen -S rosie -d -m ~/UTAbotti/rosie-y/scripts/xnix/flask-rosie.sh &
cd ~/UTAbotti-deps/starter-pack-rasa-nlu
screen -S rasa -d -m ~/UTAbotti-deps/starter-pack-rasa-nlu/run.sh &
cd ~/UTAbotti-deps/ChatScript/BINARIES
screen -S chatscript -d -m ~/UTAbotti-deps/ChatScript/BINARIES/ChatScript &
cd ~/UTAbotti/TUNIBrain
screen -S tunibrain -d -m python3 ~/UTAbotti/TUNIBrain/app.py &
