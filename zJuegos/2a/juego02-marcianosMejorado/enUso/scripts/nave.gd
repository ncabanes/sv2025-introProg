extends Area2D

var velocidad = 300

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	if Input.is_action_pressed("ui_right"):
		position.x += velocidad * delta
	if Input.is_action_pressed("ui_left"):
		position.x -= velocidad * delta
	if Input.is_action_pressed("ui_up"):
		position.y -= velocidad * delta
	if Input.is_action_pressed("ui_down"):
		position.y += velocidad * delta
