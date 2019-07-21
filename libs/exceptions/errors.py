from libs.exceptions.base_error import ApiHttpException


class InvalidToken(ApiHttpException):
    code = 422
    message = "访问令牌无效"
    errcode = 4010


class ExpirationFailed(ApiHttpException):
    code = 422
    message = "访问令牌过期"
    errcode = 4011


class AuthLoginFailed(ApiHttpException):
    code = 200
    message = "授权失败"
    errcode = 4012


class AuthLoginSuccess(ApiHttpException):
    code = 201
    message = "授权成功"
    errcode = 0

    def __init__(self, token):
        super(AuthLoginSuccess, self).__init__()
        self.token = token

    @property
    def generate_body(self):
        return {
            'message': self.message,
            'errcode': self.errcode,
            'access_token': self.token,
        }


class ApplySuccess(ApiHttpException):
    code = 200
    message = '报名成功'
    errcode = 0


class ApplyFailed(ApiHttpException):
    code = 400
    message = '报名失败'
    errcode = 4014


class UpdateApplySuccess(ApiHttpException):
    code = 200
    message = '更新报名信息成功'
    errcode = 0


class SaveFailed(ApiHttpException):
    code = 400
    message = '数据库操作错误'
    errcode = 4015



