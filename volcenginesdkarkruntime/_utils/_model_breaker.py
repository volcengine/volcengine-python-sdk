from datetime import datetime, timedelta


class ModelBreaker:
    def __init__(self):
        # 初始化 allow_time 为当前时间
        self.allow_time = datetime.now()

    def allow(self):
        # 检查当前时间是否在 allow_time 之后
        return datetime.now() > self.allow_time

    def reset(self, duration):
        # 将 allow_time 重置为当前时间加上指定的持续时间
        self.allow_time = datetime.now() + timedelta(seconds=duration.total_seconds())

    def get_allowed_duration(self):
        # 计算当前时间与 allow_time 之间的持续时间
        allow_duration = self.allow_time - datetime.now()
        # 如果持续时间为负，则返回一个零时长的 timedelta 对象
        if allow_duration.total_seconds() < 0:
            return timedelta(0)
        return allow_duration