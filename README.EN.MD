English | [中文](README.md)

# Volcengine SDK for Python
## ⚠️ Known Issue (Historical Versions)

In some historical versions of **volcengine-python-sdk** (**4.0.1 – 4.0.42**, inclusive), the SDK’s built-in retry mechanism has a defect.

When a request encounters an exception (such as network instability or API errors), the SDK may trigger its retry logic internally; however, due to this defect, the retry does not take effect as expected. As a result, the client may still experience the exception from the initial request, and the retry mechanism cannot effectively improve request success rates.

### Affected Versions

- **SDK**: volcengine-python-sdk  
- **Versions**: 4.0.1 – 4.0.42 (inclusive)

### Impact

For applications that rely on the SDK’s retry mechanism to handle transient failures or network instability:

- Actual request availability may be lower than expected  
- Retry configurations may not function as intended  

### Resolution and Recommendation

This issue has been fixed in **version 4.0.43 and above**.  
**We strongly recommend all users upgrade to volcengine-python-sdk ≥ 4.0.43** to ensure the retry mechanism functions correctly in exception scenarios.

## Breaking Change Notice

Breaking change notice for Volcengine SDK for Python.

Affected versions: `3.0.1` and later

Change description:

To address installation failures on Windows caused by excessively long package paths, starting from `3.0.1` we shortened some overly long API model filenames under the `transitrouter` service. If you depended on those full model filenames, this change is not backward compatible. Use the shortened model name as follows:

```python
from volcenginesdktransitrouter import TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesOutput

var = TransitRouterBandwidthPackageForDescribeTransitRouterBandwidthPackagesOutput()
```

Impacted service and APIs:

Service: `transitrouter`

Version: `2020-04-01`

APIs:

- DescribeTransitRouterBandwidthPackages
- DescribeTransitRouterRoutePolicyTables
- DescribeTransitRouterRoutePolicyEntries
- DescribeTransitRouterForwardPolicyTables
- DescribeTransitRouterBandwidthPackagesBilling
- DescribeTransitRouterDirectConnectGatewayAttachments
- DescribeTransitRouterRouteTableAssociations
- DescribeTransitRouterRouteTablePropagations
- DescribeTransitRouterTrafficQosQueueEntries
- DescribeTransitRouterTrafficQosQueuePolicies
- DescribeTransitRouterTrafficQosMarkingEntries
- DescribeTransitRouterTrafficQosMarkingPolicies

--------

Affected versions: `2.0.1` and later

Change description:

Starting from `2.0.1`, the default request protocol changes from **HTTP** to **HTTPS**. After upgrading, ensure you test for compatibility risks. If you must continue using HTTP (not recommended), set `scheme` to `http`:

```python
import volcenginesdkcore

configuration = volcenginesdkcore.Configuration()
configuration.scheme = 'http'
```

## Table of Contents

* Requirements
* Install
* Usage
* FAQ

### Requirements

* Python version **>= 2.7**.
* On Windows, installation may fail due to maximum path length limitations. Configure it as follows:

```
1. Press Win+R, type regedit to open Registry Editor.
2. Set LongPathsEnabled to 1 at:
   HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem
```

### Install

Install via pip:

```sh
pip install volcengine-python-sdk
```

Install via [Setuptools](http://pypi.python.org/pypi/setuptools):

```sh
python setup.py install --user
```

(Or `sudo python setup.py install` to install for all users)

### Configuration Usage

Step 1: initialize and configure global defaults

```python
configuration = volcenginesdkcore.Configuration()
configuration.client_side_validation = True  # enable client-side validation
configuration.schema = "http"  # https or http
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

### Endpoint Configuration

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

### SDK Example

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

For more examples, see: [SDK Integration Guide](./SDK_Integration.md)

### FAQ

For common issues when using the SDK, see [FAQ](FAQ.EN.md).

