extends Node2D

enum BattlePhase {
	PLAYER_PHASE, ENEMY_PHASE, VICTORY, LOSS
}

var phase
var action_executed

export (int) var player_hp = 5
export (int) var player_damage = 1
export (int) var enemy_hp = 2
export (int) var enemy_damage = 1

func _ready():
	$VictoryPanel.visible = false
	$LossPanel.visible = false
	phase = BattlePhase.PLAYER_PHASE
	$ItemList.visible = true
	action_executed = false
	
func _process(delta):
	match(phase):
		BattlePhase.PLAYER_PHASE:
			update_player_phase(delta)
		BattlePhase.ENEMY_PHASE:
			update_enemy_phase(delta)
		BattlePhase.VICTORY:
			update_victory(delta)
		BattlePhase.LOSS:
			update_loss(delta)
	
func update_player_phase(delta):
	var action = yield($ItemList, "item_selected")
	$ItemList.visible = false
	if(action == 0):
		$AnimationPlayer.play("hero_move_forward")
		yield($AnimationPlayer, "animation_finished")
		$AnimationPlayer.play("hero_hit")
		yield($AnimationPlayer, "animation_finished")
		if not action_executed:
			action_executed = true
			enemy_hp = enemy_hp - player_damage
			if(enemy_hp <= 0):
				$Enemy.visible = false
		$AnimationPlayer.play("hero_move_backward")
		yield($AnimationPlayer, "animation_finished")
		$ItemList.unselect(0)
		if(enemy_hp <= 0):
			phase = BattlePhase.VICTORY
		else:
			action_executed = false
			phase = BattlePhase.ENEMY_PHASE
	else:
		player_hp = player_hp + 1
		$ItemList.unselect(1)
		phase = BattlePhase.ENEMY_PHASE

	
func update_enemy_phase(delta):
	$ItemList.visible = true
	phase = BattlePhase.PLAYER_PHASE
	
func update_victory(delta):
	$VictoryPanel.visible = true
	yield($VictoryPanel/Button, "pressed")
	get_tree().change_scene("res://Map.tscn")
	
func update_loss(delta):
	pass

func _on_ItemList_item_selected(index):
	return index

