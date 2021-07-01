import urllib.request

#镜像源
url = {
    "Mojang":"http://launchermeta.mojang.com/mc/game/version_manifest.json",
    "bmclapi":"https://bmclapi2.bangbang93.com/mc/game/version_manifest.json",
    "mcbbs":"https://download.mcbbs.net/",
    "mcinal":"https://mcinalgitpor.cn"
}
#mcinal 云计算 ， 全球节点（为 桥粮 所搭建)
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.59"}
use = urllib.request.Request(url['Mojang'],headers=headers)
response = urllib.request.urlopen(use)
print(response.read())