import platform  # For getting the operating system name
import subprocess  # For executing a shell command
from pythonping import ping
import requests

class PythonPing:
    @staticmethod
    def execute():
        ping("www.baidu.com", verbose=True)

        # ping("smtp.qq.com", verbose=True)

        ping("www.google.com", verbose=True)

    @staticmethod
    def execute_native():
        host1 = "www.baidu.com"
        host2 = "www.google.com"
        host3 = "smtp.qq.com"
        # Option for the number of packets as a function of
        param = '-n' if platform.system().lower() == 'windows' else '-c'

        # Building the command. Ex: "ping -c 1 google.com"
        command1 = ['ping', param, '1', host1]
        command2 = ['ping', param, '1', host2]
        command3 = ['ping', param, '1', host3]

        print(subprocess.call(command1) == 0)
        print(subprocess.call(command2) == 0)
        print(subprocess.call(command3) == 0)

    @staticmethod
    def execute_http():
        # 导入requests包
        url = "http://www.tuling123.com/openapi/api"
        myParams = {"key": "username", "info": "plusroax"}  # 字典格式，推荐使用，它会自动帮你按照k-v拼接url
        res = requests.get(url=url, params=myParams)

        print('url:', res.request.url)  # 查看发送的url
        print("response:", res.text)  # 返回请求结果
        return res.text