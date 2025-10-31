extends Area2D


# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	position.y = 600


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	if Input.is_action_pressed("ui_right") and position.x < 1200:
		position.x += 2
	if Input.is_action_pressed("ui_left") and position.x > 80:
		position.x -= 2
