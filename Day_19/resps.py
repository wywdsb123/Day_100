"""wang

这个不会这个好像是通过这个接口链接,然后获取信息得到的`
"""
import requests

url = 'https://apis.tianapi.com/guonei/index?key=60ee0c4d7e097edeff6e23a8529a0401&num=10'
try:
    resp = requests.get(url)
    resp.raise_for_status()  # 自动处理HTTP错误（如404、500）
    data_model = resp.json()

    # 检查响应是否包含'newslist'
    if 'newslist' not in data_model:
        print("错误：响应缺少'newslist'字段，完整响应如下：")
        print(data_model)  # 打印完整响应以便调试
        exit(1)

    for news in data_model['newslist']:
        print(news['title'])
        print(news['url'])
        print('-' * 60)

except requests.exceptions.RequestException as e:
    print(f"请求失败: {e}")
except KeyError as e:
    print(f"键错误: {e}（请检查API文档确认字段名）")
except Exception as e:
    print(f"其他错误: {e}")