# Author:w8ay
# Name:测试DEMO


def assign(service, arg):
    if service == "www":
        return True, arg


def poc(arg):
    result = {
        "name": "Demo插件",  # 插件名称
        "content": "如果这个插件能显示出来，就说明w12scan框架测试成功了",  # 插件返回内容详情，会造成什么后果。
        "url": arg,  # 漏洞存在url
        "log": {
            "send": "send",
            "response": "response"
        },
        "tag": "demo"  # 漏洞标签
    }
    return result


if __name__ == "__main__":
    pass