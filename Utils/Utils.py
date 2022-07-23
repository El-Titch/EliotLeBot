import config


def custom_id(view:str, id: int) -> str:
	"""Return the View and the ID"""
	return f"{config.CLIENT_NAME}:{view}:{id}"