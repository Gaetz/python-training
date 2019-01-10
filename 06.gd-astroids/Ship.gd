extends Area2D

export (PackedScene) var bullet

var acceleration = 10
var speed = 0
var deceleration = 0.98
var rotation_speed = 2

func _process(delta):
	# Move
	if Input.is_action_pressed("ui_up"):
		speed = speed + acceleration
	if Input.is_action_pressed("ui_left"):
		rotation_degrees -= rotation_speed
	if Input.is_action_pressed("ui_right"):
		rotation_degrees += rotation_speed
	
	speed = speed * deceleration
	var direction = Vector2(cos(deg2rad(rotation_degrees)), sin(deg2rad(rotation_degrees)))
	position = position + direction * speed * delta
	
	# Shoot
	if Input.is_action_just_pressed("fire"):
		var b = bullet.instance()
		b.rotation_degrees = rotation_degrees
		b.position = position
		get_tree().root.get_node("Main").add_child(b)
		

	