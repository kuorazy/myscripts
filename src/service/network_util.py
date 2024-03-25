from pythonping import ping


class PythonPing:
    @staticmethod
    def execute():
        ping("www.baidu.com", verbose=True)

        ping("smtp.qq.com", verbose=True)

        ping("www.google.com", verbose=True)

