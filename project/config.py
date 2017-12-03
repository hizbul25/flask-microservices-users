class BaseConfig:
	"""Base Configuration"""
	DEBUG = False 
	TESTING = False


class DevelopmentConfig(BaseConfig):
	""" Development Configuration"""
	DEBUG = True 


class TestingConfig(BaseConfig):
	""" Testing Configuration"""
	DEBUG = True 
	TESTING = True


class ProductionConfig(BaseConfig):
	""" Development Configuration"""
	DEBUG = False 

