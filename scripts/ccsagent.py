import time
import logging
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("ccs.log"),
        logging.StreamHandler()
    ]
)

SERVER_URL = "https://10.120.0.111/update"

def main():
    while True:
        try:
            response = requests.post(SERVER_URL, verify=False)
            logging.info("Agent hit successful.")

        except requests.RequestException as e:
            logging.error("Error connecting to server: %s", e)

        time.sleep(120)

if __name__ == "__main__":
    main()
