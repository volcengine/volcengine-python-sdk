"""
密钥管理服务 (TKS) 定义的数据类型.
"""

from dataclasses import dataclass

from typing_extensions import Generic, Literal, NotRequired, Optional, TypedDict, TypeVar


class TksAuthHeaders(TypedDict):
    AppID: str
    """请求TKS的客户端的身份ID"""

    Timestamp: str
    """
    Unix时间戳（UTC+8）
    Example: 1722253648
    """

    Signature: NotRequired[str]
    """
    对请求Body的签名，仅当账号注册时的认证方式带有cert时（cert | cert+zti）
    """

    Token: NotRequired[str]
    """
    认证Token，仅当账号注册时的认证方式带有zti时（zti | cert+zti）
    """


class ResponseError(TypedDict):
    Code: int
    """
    错误码
    Example: 69905
    """

    Message: str
    """
    请求处理错误原因，正常请求为空
    Example: error occured while processing your request
    """


class ResponseMeta(TypedDict):
    Method: str
    """
    请求方法
    Example: KeyGet
    """

    Error: NotRequired[ResponseError]
    """错误信息，在请求正常响应情况下为空"""


T = TypeVar("T")


class TksResponse(Generic[T], TypedDict):
    ResponseMetadata: ResponseMeta
    """描述响应状态的元信息"""

    Result: NotRequired[T]
    """返回结果，当请求出错时为空"""


class ClientChallenge(TypedDict):
    NonceDown: str
    """
    经过hex编码后，长度为256 bits的随机挑战值
    Example: 5779d18b2b8718cef025282df2a313f154ad4f7b862b2948ecf6cf401de17634
    """

    RxpirationTime: int
    """
    时区为UTC+8的Unix时间戳，表示随机挑战的过期时间
    Example: 1721972547
    """

    ChallSig: int
    """
    经过Based64编码后的，TKS针对challenge自身的签名。使用TKS RA阶段提供的cert对应的私钥签名（ECDSA-SECP384R1）
    Example: yk63SiKLaBB7E0OVQs3Flw8NsTRNEYJIUos8s9F14sg=
    """


class SecurityAttestation(TypedDict):
    NonceUp: str
    """
    随机字符串，针对TSK进行远程证明的挑战值（32随机bytes，经过Hex编码）
    Example: a314b43502077cd89d21378b29954207aaf5b3848d4d7fa9f16682ba1f6f3317
    """

    BiAuth: NotRequired[bool]
    """
    是否要求TKS挑战请求方
    Example: true
    """


class AttestationResult(TypedDict):
    RAType: str
    """
    TKS提供的远程证明报告的类型
    Example: sgx | tdx
    """

    Report: str
    """
    经过base64编码后的远程证明报告，需要根据raType来进行验证
    Example: MTIzNA==
    """

    Cert: str
    """
    经过base64编码后的，PEM形式的证书（ECDH-SECP384R1-SHA256）
    Example: LS0tLS1CRUdJTiBQVU==
    """

    DHParam: str
    """
    经过base64编码后的，密钥协商公共参数（ECDH-SECP384R1-SHA256）
    Example: LS0tLS1CRUdJTiBQVUJMSUMg
    """

    Challenge: NotRequired[ClientChallenge]
    """当biAuth参数为true时，返回的针对请求方的挑战内容"""


class KMSInfo(TypedDict):
    Type: Literal["tks"]
    """托管密钥服务的类型，当前仅支持tks"""


class RAEvidence(TypedDict):
    TEEType: str
    """指定请求方的TEE类型"""

    Report: str
    """
    经过Base64编码的，请求方TEE生成的远程证明报告，需要包含clientChall中提供的随机挑战nonceDown
    Example: OUeRWgdMoQahtmzTA0/36qA5Lh8wp8nIK/ySOe0wQeA=
    """


class ZTIEvidence(TypedDict):
    Token: str
    """
    请求方的ZTI JWT Token
    """


class CertEvidence(TypedDict):
    Signature: str
    """
    经过Base64编码的，请求方的私钥签名的nonceDown
    Example: RZeo3OjJM/Gam+aiun+hNzD1mMnnJmpiWckLnVfqqBE=
    """


class KeyIndex(TypedDict):
    AppID: str
    """
    指定要获取的密钥Owner的AppID （PSM）
    Example: security.research.tks_owner
    """

    RingID: str
    """
    密钥环ID
    Example: 640a7c2a-c061-4964-b7d8-951e9272da21
    """

    KeyID: str
    """
    指定要获取的密钥的ID
    Example: d880cf63-7c3e-45e1-83e5-ab62ba3d3441
    """


class KeyIndexWithVersion(KeyIndex):
    Version: int
    """
    返回Key的版本，从1开始
    Example: 1
    """


class ChallengeResponse(TypedDict):
    ClientChall: NotRequired[ClientChallenge]
    """
    在远程阶段获取到的，由TKS返回的挑战信息。
    """

    RAEvidence: NotRequired[RAEvidence]
    """
    提供基于TEE远程证明相关的证明信息，当访问控制策略中包含RA类型时需要提供
    """

    ZTIEvidence: NotRequired[ZTIEvidence]
    """
    提供基于ZTI相关的证明信息，当访问控制策略中包含ZTI类型时需要提供
    """

    CertEvidence: NotRequired[CertEvidence]
    """
    提供基于证书相关的证明信息，当访问控制策略中包含Cert类型时需要提供
    """


class KeyExportation(KeyIndex, ChallengeResponse):
    DHParam: str
    """
    经过Base64编码的，请求方的DH公共参数
    Example: KGIW9H8TCIi+ZNwikN8cc4V2cTNzOi/VfLNF7oYBwvE=
    """

    KMSInfo: NotRequired[KMSInfo]
    """
    描述密钥所在的KMS位置，当前仅支持TKS
    """

    Passport: NotRequired[str]
    """
    JWT Token。由TKS签发的访问Token，获取Token的参与方在验证通过可以直接获取密钥。
    """


class ExportationResult(KeyIndexWithVersion):
    Key: str
    """
    经过Base64编码后的Key的密文，通过请求参数密钥协商出来的密钥加密（AES-256-GCM）
    Example: aq1xcWeuyyKTDY8kXqgqk9TmBjhqFhwZB7+p0GgK60I=
    """


class KeyCreation(TypedDict):
    RingID: str
    """
    密钥环ID（为空情况下，放置到用户的一个default密钥环下）
    Example: 640a7c2a-c061-4964-b7d8-951e9272da21
    """

    KeyID: NotRequired[str]
    """
    密钥ID，置空则由TKS随机分配一个UUID
    Example: d880cf63-7c3e-45e1-83e5-ab62ba3d3441
    """

    KeyName: str
    """
    密钥名称
    Example: test-demo-key
    """

    KeyAlgo: str
    """
    密钥算法（当前仅支持基于对称加密算法）
    Example: SYMMTRIC_128 | SYMMTRIC_256
    """

    Source: Literal["external", "internal"]
    """
    密钥来源
    - external: 外部导入
    - internal: 由TKS生成
    Example: internal
    """

    Description: NotRequired[str]
    """
    密钥描述信息
    Example: Key for test
    """

    Lifetime: NotRequired[int]
    """
    密钥生命周期，Unix时间戳（UTC+8）。默认情况为-1，表示无限期
    Example: 1722254231
    """

    KMSInfo: NotRequired[KMSInfo]
    """
    描述密钥托管位置
    """

    ACLRules: NotRequired[str]
    """
    描述密钥的访问控制策略，JSON字符串，默认情况下允许所有人访问，即
    {"default": "accept","rules": [],"range": "keyID","issue tkn": "false"}
    Example: {"type": "RA", "tee": "tdx", "measurements":
              {"tdx.rtmr0": "561bf3eee22f", "tdx.rtmr1": "d4247b6bd6eb"}}
    """


class KeyImportation(TypedDict):
    RingID: str
    """
    密钥环ID（为空情况下，放置到用户的一个default密钥环下
    Example: 640a7c2a-c061-4964-b7d8-951e9272da21
    """

    KeyID: str
    """
    密钥ID，置空则由TKS随机分配一个UUID
    Example: d880cf63-7c3e-45e1-83e5-ab62ba3d3441
    """

    Key: str
    """
    密钥密文。经过Base64编码后的密钥密文，加密密钥应通过AES-GCM-256加密，
    AES密钥基于TKS公共参数协商得出（ECDH-SECP384R1-SHA256）。可为空，置空后密钥状态为empty
    Example: wjBXVnzCFOc/NhQ6vXZhllGa1Kirs9VvE+GVSuYCEZM=
    """

    DHParam: str
    """
    经过Base64编码后的请求方侧的密钥协商参数，帮助TKS派生出通信密钥（ECDH-SECP384R1-SHA256）
    Example: wjBXVnzCFOc/NhQ6vXZhllGa1Kirs9VvE+GVSuYCEZM=
    """


@dataclass
class AppOptions:
    """特定于 App 的认证选项."""

    id: str
    """App ID."""

    signing_key: Optional[str] = None
    """PEM 格式的 App 私钥. 当 TKS 中 authType 设置为 cert 时使用."""

    zti_token: Optional[str] = None
    """ZTI 令牌. 当 TKS 中 authType 设置为 zti 时使用."""
