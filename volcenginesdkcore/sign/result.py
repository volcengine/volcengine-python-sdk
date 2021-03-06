# coding: utf-8

# Copy from https://github.com/volcengine/volc-sdk-python

class SignResult(object):
    def __init__(self):
        self.xdate = ''
        self.xCredential = ''
        self.xAlgorithm = ''
        self.xSignedHeaders = ''
        self.xSignedQueries = ''
        self.xSignature = ''

        self.authorization = ''

    def __str__(self):
        return '\n'.join(['%s:%s' % item for item in self.__dict__.items()])