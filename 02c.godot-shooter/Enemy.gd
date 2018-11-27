extends Sprite

export (int) var speed = -500
var life = 3

func _ready():
	position.x = 1280
	
func _process(delta):
	position.x = position.x + speed * delta
	if position.x < -200:
		queue_free()

func _on_Area2D_area_entered(area):
	life = life - 1
	if life <= 0:
		queue_free()
