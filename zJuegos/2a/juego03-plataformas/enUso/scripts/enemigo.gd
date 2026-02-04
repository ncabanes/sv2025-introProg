extends Area2D

@export var origen : Vector2
@export var destino : Vector2
@export var velocidad : int

func _ready() -> void:
	position = origen

func _process(delta: float) -> void:
	position = position.move_toward(destino, velocidad*delta)
	if position.distance_to(destino) < 5:
		var temporal = origen
		origen = destino
		destino = temporal
