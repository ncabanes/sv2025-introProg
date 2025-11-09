extends Node2D

var escenaEnemigo : PackedScene
var escenaDisparo : PackedScene
var tiempoRestanteEnemigo : float = 3

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	escenaEnemigo = load("res://escenas/enemigo.tscn")
	escenaDisparo = load("res://escenas/disparo.tscn")


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	tiempoRestanteEnemigo -= delta
	if tiempoRestanteEnemigo <= 0:
		var enemigo = escenaEnemigo.instantiate()
		enemigo.position.x = 1300
		enemigo.position.y = randi_range(50,600)
		add_child(enemigo)
		tiempoRestanteEnemigo = 0.5
	if Input.is_action_just_pressed("ui_accept"	):
		var disparo = escenaDisparo.instantiate()
		disparo.position = get_node("Nave").position
		add_child(disparo)
