# Volcengine SDK for Python

## Table of Contents

* Requirements
* Install
* Usage
* FAQ

### Requirements ###

Python版本需要不低于2.7。

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

### Basic Usage ###

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
### FAQ ###
关于 SDK 使用时碰到的常见问题，请查看 [FAQ](FAQ.md)