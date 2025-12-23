extends Area2D

var velocidad = -500
var direccion = Vector2(velocidad, 0)

func _ready() -> void:
	add_to_group("enemigos")

func _process(delta: float) -> void:
	position += direccion * delta
	if position.x < -50:
		queue_free()
