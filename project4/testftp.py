import os
from ftplib import FTP, error_perm
import shutil
import schedule
import time
import logging

INTERN_DIRECTORY = './internal_network/'
PUBLIC_DIR = './public/ftp'

logging.basicConfig(filename='logging.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')


class MyFtp():
    host = 'ftp.example.com'
    user = 'important_username'
    password = 'password'

    def __init__(self):
        try:
            self.ftp = FTP(self.host)
            self.ftp.login(user=self.user, passwd=self.password)
            logging.info(f"Connected to FTP server: {self.host}")
        except (error_perm, Exception) as e:
            logging.error(f"Failed to connect to FTP server: {self.host}, error: {e}")


def download_files(files, my_ftp):
    for file in files:
        local_file_path = os.path.join(INTERN_DIRECTORY, file)
    try:
        with open(local_file_path, 'wb') as local_file:
            my_ftp.ftp.retrbinary(f"RETR {file}", local_file.write)
        logging.info(f"File transferred: {file}")
    except Exception as e_transfer:
        logging.error(f"Failed to transfer file {file}: {str(e_transfer)}")



def upload_files(files):
    if not os.path.exists(INTERN_DIRECTORY):
        os.makedirs(INTERN_DIRECTORY)
        logging.info(f"Internal directory was missing... Now created: {INTERN_DIRECTORY}")

    for file in files:
        local_file_path = os.path.join(INTERN_DIRECTORY, file)
        try:
            shutil.move(local_file_path, os.path.join(PUBLIC_DIR, file))
            logging.info(f"File moved to internal network: {file}")
        except Exception as e_move:
            logging.error(f"Failed to move file {file} to internal network: {str(e_move)}")


def init_transfer_files():
    ftp_instance = MyFtp()

    try:
        ftp_instance.ftp.cwd('ftp/server')
        file_list = ftp_instance.ftp.nlst()
    except error_perm as e_perm:
        logging.error(
            f"Permission error while accessing FTP server: {str(e_perm)}")
        ftp_instance.ftp.quit()
        return
    except Exception as e_list:
        logging.error(f"Failed to list files on FTP server: {str(e_list)}")
        ftp_instance.ftp.quit()
        return

    download_files(file_list, ftp_instance)

    ftp_instance.ftp.quit()
    logging.info("Disconnected from FTP server successfully")

    upload_files(file_list)


if __name__ == "__main__":
    schedule.every().day.at("12:00").do(init_transfer_files)

    while True:
        schedule.run_pending()
        time.sleep(1)
