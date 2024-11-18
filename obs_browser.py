from obs import ObsClient
import os
import traceback

# 配置你的华为云 OBS 访问密钥
access_key_id = 'U4C6ATAN6PEAR09O9JYT'
secret_access_key = 'CC1FWzGIdhtgjV3YYQsfmXD70q8VIoB663sq8mvJ'
server = 'https://obs.cn-north-1.myhuaweicloud.com'  # 确保没有HTML实体

# 创建 OBS 客户端
print("Server URL:", server)
obsClient = ObsClient(access_key_id, secret_access_key, server=server)

# 配置桶和对象信息
try:
    bucketName = 'test-pocc'
    objectKey = 'dtc_demo/json_file_path_v402.json'  # 例如 'folder/subfolder/filename.json'
    file_path = 'C:/Users/awosh/OneDrive/Desktop/json_file_path_v402.json'  # 例如 'DTC_20241113.JSON'

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
