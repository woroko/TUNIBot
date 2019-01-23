@echo off

CLS

mkdir .\temp

SET PYTHONPATH=..\programy\src;..\programy\libs\MetOffer-1.3.2;.

python -m programy.clients.events.console.client --config .\config.windows.yaml --cformat yaml --logging .\logging.windows.yaml

