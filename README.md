# Volcengine SDK for Python

## Table of Contents

* Requirements
* Install
* Usage

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

### Usage ###

```python
from __future__ import print_function
import volcenginesdkautoscaling
import volcenginesdkcore
from pprint import pprint
from volcenginesdkcore.rest import ApiException

if __name__ == '__main__':
    configuration = volcenginesdkcore.Configuration()
    configuration.ak = "Your AK"
    configuration.sk = "Your SK"
    configuration.region = "cn-beijing"

    try:
        api_instance = volcenginesdkautoscaling.AUTOSCALINGApi(volcenginesdkcore.ApiClient(configuration))
        resp = api_instance.describe_scaling_groups(volcenginesdkautoscaling.DescribeScalingGroupsRequest(

        ))
        pprint(resp)
    except ApiException as e:
        print("Exception when calling AUTOSCALINGApi->describe_scaling_groups: %s\n" % e)

```
