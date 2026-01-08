### 1. Get Request and Response Types

Before calling a method, you can obtain the corresponding request and response structures via `param` and `return`.
Taking `ecs.run_instances` as an example:

```python
def run_instances(self, body, **kwargs):  # noqa: E501
    """run_instances
    :param RunInstancesRequest body: (required)
    :return: RunInstancesResponse
    """
```

### 2. Get Parameter Types for Requests and Responses

In the Request or Response body, you can check specific request parameters and their types via `swagger_types`.
Taking `volcenginesdkecs.RunInstancesRequest` as an example, its parameter names and definitions are as follows:

```python
swagger_types = {
    'auto_renew': 'bool',
    'auto_renew_period': 'int',
    'client_token': 'str',
    'count': 'int',
    'network_interfaces': 'list[NetworkInterfaceForRunInstancesInput]',
    'security_enhancement_strategy': 'str',
    'volumes': 'list[VolumeForRunInstancesInput]',
    ......
}
```

The corresponding request body is:

```python
volcenginesdkecs.RunInstancesRequest(
    instance_name="insname",
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
)
```

### 3. Memory Overflow Occurs

Check whether `Configuration._default` has been initialized.
If not, each time you create a `Configuration` instance, a new logger handler will be created and added to the global logger.
It is recommended to set the default configuration via `Configuration.set_default`.

```python
configuration = volcenginesdkcore.Configuration()
configuration.client_side_validation = False
configuration.schema = "http"  # https or http
configuration.debug = False  # Whether to enable debugging

volcenginesdkcore.Configuration.set_default(configuration)
```

### 4. Convert Object to Dict

For request and response objects, you can convert them to `dict` using the `to_dict()` method.

### 5. View Usage Examples

[volcenginesdkexamples](https://github.com/volcengine/volcengine-python-sdk/tree/master/volcenginesdkexamples)

### 6. Convert Response Object to CamelCase Dict

After calling an API, the parameters in the received response object typically use PascalCase (CamelCase with the first letter capitalized). When coding with the Python SDK, since Python generally uses snake_case, you may want to convert between the SDK's snake_case fields and the documentation's CamelCase fields.

You can convert the response object into a CamelCase dictionary with the following code. After conversion, the field names in the dictionary will be exactly the same as those in the documentation.

```python
import json
import pprint
from volcenginesdkcore.model import canonical_str

try:
    resp = api_instance.list_users(req)
    pprint(resp)  # Response object with snake_case fields
    dict_resp = json.loads(json.dumps(canonical_str(resp)))
    pprint(dict_resp)  # Response dict with CamelCase fields

except ApiException as e:
    print("Exception when calling IAMApi->ListUsers: %s\n" % e)

```

However, this is not the recommended approach. It is suggested to directly use the snake_case parameters in the response object instead of converting.
