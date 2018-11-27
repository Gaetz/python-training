extends Sprite

export (int) var speed = 2000

func _ready():
	position.x = 120
	
func _process(delta):
	position.x = position.x + speed * delta
	if position.x > 1400:
		queue_free()

func _on_Area2D_area_entered(area):
	queue_free()
