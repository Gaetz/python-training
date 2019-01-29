extends Node

# Position memory
var player_position
var is_position_stored

func store_player_position(x, y):
	player_position = Vector2(x, y)
	is_position_stored = true

func restore_player_position():
	is_position_stored = false
	return player_position


# Enemy killed memory
var killed_enemies

func _ready():
	killed_enemies = []
	
func fill_enemies(enemies):
	for enemy in enemies:
		killed_enemies.push(false)
		
func kill_enemy(index):
	killed_enemies[index] = true
	
func restore_enemies():
	pass

