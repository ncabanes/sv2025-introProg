extends Area2D

func _ready() -> void:
	position.x = 400

func _process(delta: float) -> void:
	if Input.is_action_pressed("ui_right") and position.x < 1200: 
		position.x += 4
	if Input.is_action_pressed("ui_left") and position.x > 80: 
		position.x -= 4
