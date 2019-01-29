extends Node2D

#func _ready():
#	if global.is_position_stored:
#		print(global.restore_player_position())
#		$Hero.position = global.restore_player_position()
	
func launch_battle():
	global.store_player_position($Hero.position.x, $Hero.position.y)
	print($Hero.position.x, " ", $Hero.position.y)
	get_tree().change_scene("res://battle/Fight.tscn")

