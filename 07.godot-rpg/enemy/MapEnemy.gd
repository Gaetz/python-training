extends Area2D

func _on_MapEnemy_area_entered(area):
	queue_free()
	global.switch_scene("res://battle/Fight.tscn")	
