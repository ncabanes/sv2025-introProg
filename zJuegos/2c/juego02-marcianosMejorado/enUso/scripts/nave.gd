extends Area2D

var velocidad : int = 500

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	if Input.is_action_pressed("ui_right") \
			and position.x < get_viewport_rect().size.x / 2:
		position.x += velocidad * delta
	if Input.is_action_pressed("ui_left") \
			and position.x > 50:
		position.x -= velocidad * delta
	if Input.is_action_pressed("ui_down") \
			and position.y < get_viewport_rect().size.y - 50:
		position.y += velocidad * delta
	if Input.is_action_pressed("ui_up") \
			and position.y > 50:
		position.y -= velocidad * delta
