extends Node2D

var velocidadEnemigos = 500

func _ready() -> void:
	ConfigJuego.vidas = 3
	ConfigJuego.puntos = 0

func _process(delta: float) -> void:
	$Enemigo.position.x -= velocidadEnemigos * delta
	if $Enemigo.position.x < 0:
		$Enemigo.position.x = 1300
	$Enemigo2.position.x -= velocidadEnemigos * delta
	if $Enemigo2.position.x < 0:
		$Enemigo2.position.x = 1300
	if Input.is_action_just_pressed("jugar"):
		get_tree().change_scene_to_file("res://escenas/nivel1.tscn")

func _on_boton_jugar_pressed() -> void:
	get_tree().change_scene_to_file("res://escenas/nivel1.tscn")
