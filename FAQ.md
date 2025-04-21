### 1. 获取请求和响应类型

在方法调用前，通过 param 和 return 获取请求和响应对应的结构体  
以 ecs.run_instances 为例

```python
def run_instances(self, body, **kwargs):  # noqa: E501
    """run_instances
    :param RunInstancesRequest body: (required)
    :return: RunInstancesResponse
    """
```

### 2. 获取请求和响应的参数类型

在 Request 或者 Response 请求体中，通过 swagger_types 查看具体的请求参数和类型  
以 volcenginesdkecs.RunInstancesRequest 为例，其参数名称和定义如下所示

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

对应的请求体为

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

### 3. 出现内存溢出

检查 Configuration._default 是否被初始化  
如果没有初始化，每一次创建 Configuration 的时候，会创建新的 logger handler 并加入到全局的 logger 中  
建议通过 Configuration.set_default 方法对 Configuration 进行赋值

```python
configuration = volcenginesdkcore.Configuration()
configuration.client_side_validation = False
configuration.schema = "http"  # https or http
configuration.debug = False  # 是否开启调试

volcenginesdkcore.Configuration.set_default(configuration)
```

### 4. 对象转 Dict

对于请求和响应的对象，可以通过 to_dict() 方法将其转换成 dict 类型

### 5. 查看使用示例

[volcenginesdkexamples](https://github.com/volcengine/volcengine-python-sdk/tree/master/volcenginesdkexamples)

### 6. 响应对象转驼峰风格 Dict

在实际调用 API 后，所接收的响应对象参数通常采用首字母大写的驼峰命名法。而在使用 Python SDK 进行编码时，由于 Python
的整体命名规范为下划线命名法，当使用响应参数并对照文档时，您可能想要在 Python SDK 所采用的下划线命名法与文档中的驼峰命名法之间进行转换。

当然，可通过调用以下代码将响应对象转换为驼峰格式的字典，转换后字典中的字段名与文档中的字段名完全一致

```python
import json
import pprint
from volcenginesdkcore.model import canonical_str

try:
    resp = api_instance.list_users(req)
    pprint(resp)  # 字段为下划线的响应对象
    dict_resp = json.loads(json.dumps(canonical_str(resp)))
    pprint(dict_resp)  # 字段为驼峰的响应字典

except ApiException as e:
    print("Exception when calling IAMApi->ListUsers: %s\n" % e)

```

不过，这种方法并非推荐的使用方式。建议直接使用响应对象中以下划线命名的参数，而非进行上述转换后使用。 