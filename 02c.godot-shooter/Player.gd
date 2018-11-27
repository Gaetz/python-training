extends Sprite

onready var shot = preload("res://Shot.tscn")
export (int) var speed = 500
signal game_over

func _ready():
	pass

func _process(delta):
	# Move
	if Input.is_action_pressed("ui_up"):
		position.y = position.y - speed * delta
	if Input.is_action_pressed("ui_down"):
		position.y = position.y + speed * delta
	var texture_half_size = texture.get_height() / 2
	position.y = clamp(position.y, texture_half_size, 480 - texture_half_size)
	
	# Shoot
	if Input.is_action_just_pressed("fire"):
		var s = shot.instance()
		s.position.y = position.y
		#add_child(s)
		get_tree().get_root().add_child(s)


func _on_Area2D_area_entered(area):
	emit_signal("game_over")
	queue_free()
	

