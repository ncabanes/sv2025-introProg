extends Area2D

var velocidad = 300

func _ready() -> void:
	add_to_group("enemigos")

func _process(delta: float) -> void:
	position.x -= velocidad * delta
	if position.x < -50:
		queue_free()
