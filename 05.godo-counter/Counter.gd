extends Label

var counter

func _ready():
	counter = 0
	
func _process(delta):
	counter = counter + delta
	text = str(counter)