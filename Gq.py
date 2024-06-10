import os



import requests



from threading import Thread, active_count



from os import name, system



from datetime import datetime



import time







class DAKAR():



    def __init__(self):



        self.work = 0



        self.bad = 0



        self.error = 0



        self.proxy_type = None



        self.TIMEOUT = 5



        self.admin()







    def clear(self):



        if name == 'nt':



            _ = system('cls')



        else:



            _ = system('clear')







    def set_proxy_type(self):



        ask = input("[/] اختار نوع البروكسي  : \n[1] http-https\n[2] socks5\n[3] socks4\n[?] :")



        if ask.lower() == "1":



            self.proxy_type = "https"



        elif ask.lower() == "2":



            self.proxy_type = "socks5"



        elif ask.lower() == "3":



            self.proxy_type = "socks4"



        else:



            input("[❌] خطا :  اختار رقم صحيح")



            exit()







    def admin(self):



        self.set_proxy_type()



        self.clear()







        ask2 = input("[/]اختار الفحص على نوع المنصه  :  \n[1] Google\n[2] Instagram\n[3] Twitter\n[4] Youtube\n[5] Tiktok\n[?] :")







        self.clear()



        now = datetime.now()







        self.write_good_proxy(f'[ start time  {now.strftime("%H:%M:%S")}]\n')



        f = self.read_proxy('proxy.txt', 'r')



        for p in f:



            a = True



            Thread(target=self.output).start()



            while a:



                if active_count() <= 200:



                    Thread(target=self.check, args=(ask2, p,)).start()



                    a = False



        print("\n\n")



        print("[+] Done Sir .")



        print(f"[ All proxys check ] : {self.bad + self.error + self.work}")



        print(f"[ work proxys ] : {self.work}")



        print(f"[ Done Save All work proxy in ] : {os.getcwd() + '/proxys✅.text'}")



        input('')



        exit()







    def build_proxy(self,proxy, type):



        if type == "https":



            proxies = {



                'http': f'http://{proxy}',



                'https': f'http://{proxy}',



            }



            return proxies



        elif type == "socks5":



            proxies = {



                'http': f"socks5://{proxy}",



                'https': f"socks5://{proxy}"



            }



            return proxies



        elif type == "socks4":



            proxies = {



                'http': f"socks4://{proxy}",



                'https': f"socks4://{proxy}"



            }



            return proxies



        else:



            return 0







    def read_proxy(self, file, method):



        with open(file, method) as file:



            a = [line.strip('\n') for line in file]



            return a







    def write_good_proxy(self, proxy):



        with open("proxys✅.text", "a") as F:



            F.write(proxy + "\n")



            F.close()







    def output(self):



        print(f"\r [ work proxy ] : {self.work}  | [ Bad ] : {self.bad}  | [ Errors ] : {self.error}", flush=True, end='')







    def check(self, method, proxy):



        if method == "1":



            self.check_google(proxy)



        elif method == "2":



            self.check_instagram_api(proxy)



        elif method == "3":



            self.check_twitter(proxy)



        elif method == "4":



            self.check_youtube(proxy)



        elif method == "5":



            self.check_tiktok(proxy)



        else:



            input("[X] Error : Please Chose Number !")



            exit()







    def check_google(self, proxy):



        try:



            url = "https://www.google.com/search?q=givt"



            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/124432 Firefox/11111.0"}



            try:



                r = requests.get(url, headers=headers, proxies=self.build_proxy(proxy, self.proxy_type), timeout=self.TIMEOUT)



                if r.status_code == 200:



                    self.work +=1



                    self.write_good_proxy(proxy)



                else:



                    self.bad +=1



            except requests.exceptions.ConnectionError or requests.exceptions.ConnectTimeout:



                self.bad +=1



            except:



                self.error +=1



        except IndexError:



            self.error+=1







    def check_instagram_api(self, proxy):



        url = "https://i.instagram.com/api/v1/accounts/login/"



        headers = {



            'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',



            "Accept": "*/*",



            "Accept-Encoding": "gzip, deflate",



            "Accept-Language": "en-US",



            "X-IG-Capabilities": "3brTvw==",



            "X-IG-Connection-Type": "WIFI",



            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",



            'Host': 'i.instagram.com'



        }



        data = {



            '_uuid': "00000000000000",



            'password': "givt",



            'username': "instagram",



            'device_id': "00000000000000",



            'from_reg': 'false',



            '_csrftoken': 'missing',



            'login_attempt_count': '0'



        }



        try:



            r = requests.get(url, headers=headers, data=data, proxies=self.build_proxy(proxy, self.proxy_type), timeout=self.TIMEOUT)



            if 'The password you entered is incorrect. Please try again.' in r.text:



                self.work +=1



                self.write_good_proxy(proxy)



            else:



                self.bad +=1



        except requests.exceptions.ConnectionError or requests.exceptions.ConnectTimeout:



            self.bad +=1



        except:



            self.error +=1







    def check_twitter(self, proxy):



        try:



            url = "https://twitter.com/givt"



            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/124432 Firefox/11111.0"}



            try:



                r = requests.get(url, headers=headers, proxies=self.build_proxy(proxy, self.proxy_type), timeout=self.TIMEOUT)



                if r.status_code == 200:



                    self.work +=1



                    self.write_good_proxy(proxy)



                else:



                    self.bad +=1



            except requests.exceptions.ConnectionError or requests.exceptions.ConnectTimeout:



                self.bad +=1



            except:



                self.error +=1



        except IndexError:



            self.error+=1







    def check_youtube(self, proxy):



        
        Instagram - YouTube



        try:



            url = "https://www.youtube.com/@instagram"



            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/124432 Firefox/11111.0"}



            try:



                r = requests.get(url, headers=headers, proxies=self.build_proxy(proxy, self.proxy_type), timeout=self.TIMEOUT)



                if r.status_code == 200:



                    self.work +=1



                    self.write_good_proxy(proxy)



                else:



                    self.bad +=1



            except requests.exceptions.ConnectionError or requests.exceptions.ConnectTimeout:



                self.bad +=1



            except:



                self.error +=1



        except IndexError:



            self.error+=1







    def check_tiktok(self, proxy):



        try:



            url = "https://www.tiktok.com/@tiktok"



            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/124432 Firefox/11111.0"}



            try:



                r = requests.get(url, headers=headers, proxies=self.build_proxy(proxy, self.proxy_type), timeout=self.TIMEOUT)



                if '"uniqueId":"tiktok"' in r.text:



                    self.work +=1



                    self.write_good_proxy(proxy)



                else:



                    self.bad +=1



            except requests.exceptions.ConnectionError or requests.exceptions.ConnectTimeout:



                self.bad +=1



            except:



                self.error +=1



        except IndexError:



            self.error+=1
























DAKAR()
