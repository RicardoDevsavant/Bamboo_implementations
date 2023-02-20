# Bamboo_implementations
On this repo, you will find the POC implementation to update the table Employee into the DevSavant database, and you will find the codes and the documentation about the reports and Jupyter codes to understand how the Bamboo open API works. 

## How to run POC bamboo WebHook
1. Install python 3.9 
2. Create an environment could be direct in python or anaconda
    > c:\>python -m venv c:\path\to\myenv
    > C:\> <venv>\Scripts\activate.bat
3. install the requirements.txt
    > pip install -r requirements.txt 
4. Run your favorite localhost exposer (Ngox) 
    > ngox http 80
5. Copy the forwarding URL (your localhost exposed on Internet)
6. Open Webhooks.py and replace the TOKEN variable for the value and run that script. You must get an update message from bamboo for webhook 7 and 8.
7. Run in console main.py
8. Go to the internal.testing account and make some modification to any employee on the fields realted with DCP.Emoployees DevSavant database. 



