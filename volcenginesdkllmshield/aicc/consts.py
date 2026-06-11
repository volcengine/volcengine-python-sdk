class ClientConst:
    MIN_ATTEST_INTERVAL = 3600  # 内置最小的attest间隔，单位秒
    INACTIVE_ATTEST_INTERVAL = 3600 * 3  # 非活跃客户端的attest时间间隔，单位秒

    INACTIVE_THRESHOLD = 3600  # 超过一定阈值被认为是不活跃的客户端，单位秒
