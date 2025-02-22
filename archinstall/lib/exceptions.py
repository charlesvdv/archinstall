class RequirementError(BaseException):
	pass


class DiskError(BaseException):
	pass


class UnknownFilesystemFormat(BaseException):
	pass


class ProfileError(BaseException):
	pass


class SysCallError(BaseException):
	def __init__(self, message, exit_code):
		super(SysCallError, self).__init__(message)
		self.message = message
		self.exit_code = exit_code


class ProfileNotFound(BaseException):
	pass


class HardwareIncompatibilityError(BaseException):
	pass


class PermissionError(BaseException):
	pass


class UserError(BaseException):
	pass


class ServiceException(BaseException):
	pass
