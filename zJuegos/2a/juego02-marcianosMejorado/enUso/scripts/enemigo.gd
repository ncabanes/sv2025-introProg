extends Area2D

var velocidad : int = 400

func _ready() -> void:
	pass

func _process(delta: float) -> void:
	position.x -= velocidad * delta
	if position.x < 0:
		queue_free()
