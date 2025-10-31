extends Area2D

func _ready() -> void:
	position.x = 400

func _process(delta: float) -> void:
	if Input.is_action_pressed("ui_right"):
		position.x += 2
