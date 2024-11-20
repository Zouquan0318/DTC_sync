# obs_browser.py
from obs import ObsClient
import traceback

# 配置你的华为云 OBS 访问密钥
access_key_id = 'U4C6ATAN6PEAR09O9JYT'
secret_access_key = 'CC1FWzGIdhtgjV3YYQsfmXD70q8VIoB663sq8mvJ'
server = 'https://obs.cn-north-1.myhuaweicloud.com'

# 创建 OBS 客户端
print("Server URL:", server)
obsClient = ObsClient(access_key_id, secret_access_key, server=server)

# 配置桶信息
bucketName = 'test-pocc'

def upload_to_obs(file_path, filename):
    objectKey = f'dtc_demo/{filename}'  # 更新objectKey
    try:
        # 上传文件
        resp = obsClient.putFile(bucketName, objectKey, file_path)
        # 返回码为2xx时，接口调用成功，否则接口调用失败
        if resp.status < 300:
            print('Put File Succeeded')
            print('requestId:', resp.requestId)
            print('etag:', resp.body.etag)
            print('versionId:', resp.body.versionId)
            print('storageClass:', resp.body.storageClass)
        else:
            print('Put File Failed')
            print('requestId:', resp.requestId)
            print('errorCode:', resp.errorCode)
            print('errorMessage:', resp.errorMessage)
    except:
        print('Put File Failed')
        print(traceback.format_exc())
