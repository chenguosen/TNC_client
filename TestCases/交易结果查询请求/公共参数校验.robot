*** Test Cases ***
pubInfo节点不存在，校验失败，返回错误码

appId节点不存在，校验失败，返回错误码

appId数据类型不正确，校验失败，返回错误码

appId值是空串，校验失败，返回错误码

appId值为空，校验失败，返回错误码

appId值长度大于32，校验失败，返回错误码

reqTime节点不存在，校验失败，返回错误码

reqTime数据类型不正确，校验失败，返回错误码

reqTime值是空串，校验失败，返回错误码

reqTime值为空，校验失败，返回错误码

reqTime值格式不是YYYYMMDDHHMMSS，校验失败，返回错误码

ver节点不存在，校验失败，返回错误码

ver数据类型不正确，校验失败，返回错误码

ver值是空串，校验失败，返回错误码

ver值为空，校验失败，返回错误码

ver值长度大于6，校验失败，返回错误码

tid节点不存在，校验失败，返回错误码

tid数据类型不正确，校验失败，返回错误码

tid值是空串，校验失败，返回错误码

tid值为空，校验失败，返回错误码

tid值已存在，校验失败，返回错误码

sign节点不存在，校验失败，返回错误码

sign数据类型不正确，校验失败，返回错误码

sign值是空串，校验失败，返回错误码

sign值为空，校验失败，返回错误码

sign值已存在，校验失败，返回错误码

sign值不等于MD5(appId+reqTime+tid+appSecret)，校验失败，返回错误码

cbUrl值长度大于256，校验失败，返回错误码
