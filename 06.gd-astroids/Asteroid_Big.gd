extends Area2D

var direction
var speed = 50

func _ready():
	direction = randi() % 360

func _process(delta):
	var dir = Vector2(cos(deg2rad(direction)), sin(deg2rad(direction)))
	position = position + dir * speed * delta
	
	if position.x > get_viewport_rect().size.x:
		position.x = 0
	if position.x < 0:
		position.x = get_viewport_rect().size.x
		
	if position.y > get_viewport_rect().size.y:
		position.y = 0
	if position.y < 0:
		position.y = get_viewport_rect().size.y

func _on_Asteroid_Big_area_entered(area):
	queue_free()
