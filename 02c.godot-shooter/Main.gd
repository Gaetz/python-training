extends Node2D

onready var enemy = preload("res://Enemy.tscn")

func _on_Timer_timeout():
	var e = enemy.instance()
	var e_height = e.texture.get_height()
	e.position.y = randi() % (480 - e_height) + e_height / 2
	add_child(e)

func _on_Player_game_over():
	$UIGameOver.visible = true
	$Timer.stop()
