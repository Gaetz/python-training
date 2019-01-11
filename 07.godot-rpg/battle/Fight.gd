extends Node2D

enum BattlePhase {
	PLAYER_PHASE, ENEMY_PHASE, VICTORY, LOSS
}

enum TurnPhase {
	TARGETING, MOVING, HIT, MOVING_BACK
}	

var phase
var turn_phase

func _ready():
	$ItemList.visible = false
	phase = BattlePhase.PLAYER_PHASE
	turn_phase = TurnPhase.TARGETING

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
	$ItemList.visible = true
	var action = yield($ItemList, "item_selected")
	$ItemList.visible = false
	if(action == 0):
		$AnimationPlayer.play("hero_move_forward")
		yield($AnimationPlayer, "animation_finished")
		$AnimationPlayer.play("hero_hit")
		yield($AnimationPlayer, "animation_finished")
		$AnimationPlayer.play("hero_move_backward")
		yield($AnimationPlayer, "animation_finished")
	else:
		print("defense")
	phase = BattlePhase.ENEMY_PHASE
	
func update_enemy_phase(delta):
	pass
	
func update_victory(delta):
	pass
	
func update_loss(delta):
	pass

func _on_ItemList_item_selected(index):
	return index

