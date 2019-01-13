extends KinematicBody2D

export (int) var speed = 500

var velocity = Vector2()

func get_input():
    velocity = Vector2()
    if Input.is_action_pressed('ui_right'):
        velocity.x += speed
    if Input.is_action_pressed('ui_left'):
        velocity.x -= speed
    if Input.is_action_pressed('ui_down'):
        velocity.y += speed
    if Input.is_action_pressed('ui_up'):
        velocity.y -= speed
    velocity = velocity.normalized() * speed

func _physics_process(delta):
    get_input()
    move_and_slide(velocity)

func _on_MapEnemy_area_entered(area):
	get_tree().change_scene("res://battle/Fight.tscn")
