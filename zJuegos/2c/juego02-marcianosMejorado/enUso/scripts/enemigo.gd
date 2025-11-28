extends Area2D

var velocidad = 400

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	add_to_group("enemigos")

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	position.x -= velocidad * delta
	if position.x < -50:
		queue_free()
