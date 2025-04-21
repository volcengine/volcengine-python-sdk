# Volcengine SDK for Python

## Table of Contents

* Requirements
* Install
* Usage
* FAQ

### Requirements ###

* Python版本需要不低于2.7。
* 由于 Windows 系统有最长路径限制，可能会导致安装失败，请按照以下方式设置：

```
1. 按下 Win+R ，输入 regedit 打开注册表编辑器。
2. 设置 \HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem 路径下的变量 LongPathsEnabled 为 1 即可。
```

### Install ###

Install via pip

```sh
pip install volcengine-python-sdk
```

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```

(or `sudo python setup.py install` to install the package for all users)

### Configuration Usage ###

步骤一：启动时初始化，配置 Configuration 全局默认参数

```python
configuration = volcenginesdkcore.Configuration()
configuration.client_side_validation = True  # 客户端是否进行参数校验
configuration.schema = "http"  # https or http
configuration.debug = False  # 是否开启调试
configuration.logger_file = "sdk.log"

volcenginesdkcore.Configuration.set_default(configuration)
```

步骤二：获取 Client

```python
def get_client(ak, sk, region):
    # 包含默认属性
    configuration = volcenginesdkcore.Configuration()
    configuration.ak = ak
    configuration.sk = sk
    configuration.region = region
    client = volcenginesdkautoscaling.AUTOSCALINGApi(volcenginesdkcore.ApiClient(configuration))
    return client
```

### Endpoint 设置 ###

如果您要自定义SDK的Endpoint，可以按照以下示例代码设置：

```python
configuration = volcenginesdkcore.Configuration()
configuration.host = 'ecs.cn-beijing-autodriving.volcengineapi.com'
```

火山引擎标准的Endpoint规则说明：

| Regional 服务                                                                                                                            | Global 服务                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| `{service}.{region}.volcengineapi.com` <br> 例如：云服务ecs在cn-beijing-autodriving Region域名为： `ecs.cn-beijing-autodriving.volcengineapi.com` | `{service}.volcengineapi.com` <br> 例如：访问控制iam为Global服务，域名为：`iam.volcengineapi.com` |

注：

- Service中存在_符号时，Endpoint时需转为-符号。存在大写字母时需转成小写。
- 并非所有云产品和Region都支持标准域名，具体请前往您所使用的产品-API参考中查看。

### SDK 示例 ###

```python
from __future__ import print_function
import volcenginesdkecs
import volcenginesdkcore
from pprint import pprint
from volcenginesdkcore.rest import ApiException

if __name__ == '__main__':
    configuration = volcenginesdkcore.Configuration()
    configuration.ak = "Your AK"
    configuration.sk = "Your SK"
    configuration.region = "cn-beijing"
    configuration.client_side_validation = True
    # set default configuration
    volcenginesdkcore.Configuration.set_default(configuration)

    # use global default configuration
    api_instance = volcenginesdkecs.ECSApi()
    # use custom configuration
    # api_instance = volcenginesdkecs.ECSApi(volcenginesdkcore.ApiClient(configuration))

    try:
        resp = api_instance.run_instances(
            volcenginesdkecs.RunInstancesRequest(
                instance_name="insname",
                instance_type="ecs.g1.large",
                zone_id="cn-beijing-a",
                network_interfaces=[volcenginesdkecs.NetworkInterfaceForRunInstancesInput(
                    subnet_id="subnet-2d68bh73d858ozfekrm8fj",
                    security_group_ids=["sg-2b3dq7v0ha0w2dx0eg0nhljv"],
                )],
                image_id="image-ybvz29l3da4ox5h0m9",
                volumes=[volcenginesdkecs.VolumeForRunInstancesInput(
                    volume_type="ESSD",
                    size=40,
                )],
                key_pair_name="vtable",
                instance_charge_type="PostPaid"
            ))
        pprint(resp)
    except ApiException as e:
        print("Exception when calling ECSApi->run_instances: %s\n" % e)

```

### FAQ ###

关于 SDK 使用时碰到的常见问题，请查看 [FAQ](FAQ.md)