from obs import ObsClient
from obs import const

# 配置你的华为云 OBS 访问密钥
access_key_id = 'U4C6ATAN6PEAR09O9JYT'
secret_access_key = 'CC1FWzGIdhtgjV3YYQsfmXD70q8VIoB663sq8mvJ'
server = 'http://obs.cn-north-1.myhuaweicloud.com'

# 创建 OBS 客户端
obs_client = ObsClient(access_key_id, secret_access_key, server)

# 配置桶和对象信息
bucket_name = 'test-pocc'
object_key = 'obs://test-pocc/dtc_demo/json_file_path_v402.json'  # 例如 'folder/subfolder/filename.json'
file_path = 'C:/Users/awosh/OneDrive/Desktop/json_file_path_v402.json'  # 例如 'DTC_20241113.JSON'

# 上传文件
def upload_file(bucket_name, object_key, file_path):
    try:
        with open(file_path, 'rb') as file_data:
            obs_client.put_object(bucket_name, object_key, file_data)
        print(f"文件 {file_path} 上传到 OBS 桶 {bucket_name} 成功")
    except Exception as e:
        print(f"上传文件到 OBS 失败：{e}")

# 调用上传函数
upload_file(bucket_name, object_key, file_path)
