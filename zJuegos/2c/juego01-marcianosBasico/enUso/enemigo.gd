extends Area2D

var velocidad = 400

func _process(delta: float) -> void:
	position.x += velocidad * delta
	if position.x > 1200:
		velocidad = -velocidad
	if position.x < 80:
		velocidad = -velocidad
