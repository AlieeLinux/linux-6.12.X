import os

class myclass:
    @staticmethod
    def myself():
        print()

myclass.myself()

class Version:
    @staticmethod
    def linuxrc():
        linuxversion = "linux-6.15"
        rclink = f"https://cdn.kernel.org/pub/linux/kernel/x6.x/{linuxversion}.tar.xz"
        if os.path.exists("linux-6.15.tar.gz") == False:
            os.system(f"wget {rclink}")
            os.system(f"tar -xvf {linuxversion}.tar.xz")
        return linuxversion

    @staticmethod
    def linux613():
        linuxversion = "linux-6.14.9"
        if os.path.exists(linuxversion) == False:
            os.system(f"wget 'https://cdn.kernel.org/pub/linux/kernel/v6.x/{linuxversion}.tar.xz'")
            os.system(f"tar -xvf {linuxversion}.tar.xz")

        return linuxversion

    @staticmethod
    def linux612():
        linuxversion = "linux-6.12.31"
        if os.path.exists(linuxversion) == False:
            os.system(f"wget 'https://cdn.kernel.org/pub/linux/kernel/v6.x/{linuxversion}.tar.xz'")
            os.system(f"tar -xvf {linuxversion}.tar.xz")
        return linuxversion
'''
    @staticmethod
    def linux66():
        linuxversion = "6.6.80"
        if os.path.exists(linuxversion) == False:
            os.system(f"wget 'https://cdn.kernel.org/pub/linux/kernel/v6.x/{linuxversion}.tar.xz'")
            os.system(f"tar -xvf {linuxversion}.tar.xz")
        return linuxversion

    @staticmethod
    def linux61():
        linuxversion = "linux-6.1.129"
        if os.path.exists(linuxversion) == False:
            os.system(f"wget 'https://cdn.kernel.org/pub/linux/kernel/v6.x/{linuxversion}.tar.xz'")
            os.system(f"tar -xvf {linuxversion}.tar.xz")
        return linuxversion

    @staticmethod
    def linux515():
        linuxversion = "linux-5.15.178"
        if os.path.exists(linuxversion) == False:
            os.system(f"wget 'https://cdn.kernel.org/pub/linux/kernel/v6.x/{linuxversion}.tar.xz'")
            os.system(f"tar -xvf {linuxversion}.tar.xz")
        return linuxversion

'''
