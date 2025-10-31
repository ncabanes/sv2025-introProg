extends Area2D

var velocidad = 250

func _ready() -> void:
	position.x = 400

func _process(delta: float) -> void:
	if Input.is_action_pressed("ui_right") and position.x < 1200: 
		position.x += velocidad * delta
	if Input.is_action_pressed("ui_left") and position.x > 80: 
		position.x -= velocidad * delta
