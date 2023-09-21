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
