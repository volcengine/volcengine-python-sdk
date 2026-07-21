English | [中文](README.md)

# Volcengine SDK for Python

## Index

* Requirements
* Install
* Usage
* FAQ

### Requirements

* Python version **>= 2.7**.
* If you use Ark Runtime (`arkruntime`), Python version **>= 3.6** is required.

### Install

Install via pip:

```sh
pip install volcengine-python-sdk
```

To use Ark Runtime, install the optional Ark dependencies:

```sh
pip install "volcengine-python-sdk[ark]"
```

### Usage

#### Detailed Documentation

For detailed SDK documentation (credentials, endpoint, transport, timeout, retry, error handling, debugging), see: [SDK Integration Guide](./docs/0-Overview.md)

#### Configuration Usage

Step 1: initialize and configure global defaults

```python
import volcenginesdkautoscaling
import volcenginesdkcore

configuration = volcenginesdkcore.Configuration()
configuration.client_side_validation = True  # enable client-side validation
configuration.scheme = "https"  # https or http
configuration.debug = False
configuration.logger_file = "sdk.log"

volcenginesdkcore.Configuration.set_default(configuration)
```

Step 2: get the client

```python
def get_client(ak, sk, region):
    configuration = volcenginesdkcore.Configuration()
    configuration.ak = ak
    configuration.sk = sk
    configuration.region = region
    client = volcenginesdkautoscaling.AUTOSCALINGApi(volcenginesdkcore.ApiClient(configuration))
    return client
```

#### Endpoint Configuration

To customize the endpoint:

```python
configuration = volcenginesdkcore.Configuration()
configuration.host = 'ecs.cn-beijing-autodriving.volcengineapi.com'
```

Standard endpoint rules:

| Regional Service | Global Service |
|---|---|
| `{service}.{region}.volcengineapi.com` <br> e.g. `ecs.cn-beijing-autodriving.volcengineapi.com` | `{service}.volcengineapi.com` <br> e.g. `iam.volcengineapi.com` |

Note:

- If the service name contains `_`, it should be converted to `-` in the endpoint. Use lowercase for all characters.

#### Complete Example

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
    volcenginesdkcore.Configuration.set_default(configuration)

    api_instance = volcenginesdkecs.ECSApi()

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

### FAQ

For common issues when using the SDK, see [FAQ](FAQ.EN.md).

## Security and privacy
This project takes security seriously. 
For vulnerability reporting and supported versions, see [SECURITY.md](SECURITY.md)
