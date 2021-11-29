import paramiko
import paramiko
import os


class TargetConfig():
    
    def __init__(self):
        self.Host = os.getenv('CRAWLAB_TARGET_HOST')
        self.Port = os.getenv('CRAWLAB_TARGET_PORT')
        self.Username = os.getenv('CRAWLAB_TARGET_USERNAME')
        self.Password = os.getenv('CRAWLAB_TARGET_PASSWORD')
        self.Path = os.getenv('CRAWLAB_TARGET_PATH')
        self.Notify = os.getenv('CRAWLAB_TARGET_NOTIFY')


def get_target_config():
    return TargetConfig()



# 上传文件
def save_file(name, data):
    # 获取配置
    target = get_target_config()
    local = 'tmp/{}'.format(name)
    remote = os.path.join(target.Path, name)
    # 将图片写到本地
    with open(local, 'wb+') as img:
        img.write(data)
    sf = paramiko.Transport((target.Host, int(target.Port)))
    sf.connect(username=target.Username, password=target.Password)
    sftp = paramiko.SFTPClient.from_transport(sf)
    try:
        if os.path.isdir(local):
            for f in os.listdir(local):
                sftp.put(os.path.join(local + f), os.path.join(remote + f))
        else:
            sftp.put(local, remote)
    except Exception:
        print('upload error:')
    sf.close()
    os.unlink(local)

