extends Node2D

var escenaEnemigo : PackedScene

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	escenaEnemigo = load("res://escenas/enemigo.tscn")


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	if Input.is_action_just_pressed("ui_accept"):
		var enemigo = escenaEnemigo.instantiate()
		enemigo.position.x = 1200
		enemigo.position.y = 360
		add_child(enemigo)
