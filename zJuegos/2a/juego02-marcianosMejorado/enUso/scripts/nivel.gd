extends Node2D

var escenaEnemigo : PackedScene
var escenaDisparo : PackedScene
var tiempoParaDisparo: float = 1
var tiempoTranscurrido: float = 0

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	escenaEnemigo = load("res://escenas/enemigo.tscn")
	escenaDisparo = load("res://escenas/disparo.tscn")


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	tiempoTranscurrido += delta
	if Input.is_action_just_pressed("ui_accept"):
		var disparo = escenaDisparo.instantiate()
		disparo.position = $Nave.position
		add_child(disparo)
		
	if tiempoTranscurrido >= tiempoParaDisparo:
		var enemigo = escenaEnemigo.instantiate()
		enemigo.position.x = 1200
		enemigo.position.y = randi_range(100, 600)
		add_child(enemigo)
		tiempoTranscurrido = 0
