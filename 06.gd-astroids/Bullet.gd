extends Area2D

var speed = 1000

func _process(delta):
	var direction = Vector2(cos(deg2rad(rotation_degrees)), sin(deg2rad(rotation_degrees)))
	position = position + direction * speed * delta
	