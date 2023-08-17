from .admin import admin
from .arts import arts
from .images import images
from .other import other

routers = [
	admin, arts, images,
	other
]