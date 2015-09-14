# Manila Traffic Monitor
Fetches MMDA data and saves results into a JSON file.

## Setup
```
sudo touch /var/log/manila-traffic.log
sudo -H chmod 775 /var/log/manila-traffic.log 
sudo chown ubuntu:ubuntu manila-traffic.log
```

## To use:
```
python run.py /home/ubuntu/manila-traffic.json
```