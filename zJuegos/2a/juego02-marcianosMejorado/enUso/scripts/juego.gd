extends Node2D

var escenaEnemigo: PackedScene
var escenaExplosion: PackedScene
var escenaDisparo: PackedScene
var escenaDisparoEnemigos: PackedScene
var puntos : int = 0
@export var vidas : int = 3
var posicionInicialNave: Vector2

func _ready() -> void:
	escenaEnemigo = load("res://escenas/enemigo.tscn")
	escenaExplosion = load("res://escenas/explosion.tscn")
	escenaDisparo = load("res://escenas/disparo.tscn")
	escenaDisparoEnemigos = load("res://escenas/disparo_enemigo.tscn")
	posicionInicialNave = $Nave.position

func _process(delta: float) -> void:
	if Input.is_action_just_pressed("disparo"):
		var disparo = escenaDisparo.instantiate()
		add_child(disparo)
		disparo.position = $Nave.position

func mostrarExplosion(position: Vector2) -> void:
	var explosion = escenaExplosion.instantiate()
	add_child(explosion)
	explosion.position = position
	explosion.emitting = true

func _on_timer_salida_enemigos_timeout() -> void:
	var enemigo = escenaEnemigo.instantiate()
	enemigo.position.x = 1200
	enemigo.position.y = randi_range(50, get_viewport_rect().size.y-50)
	add_child(enemigo)

func incrementarPuntos(cantidad: int) -> void:
	puntos += cantidad
	$TextoPuntos.text = "Puntos: " + str(puntos)

func perderVida() -> void:
	vidas -= 1
	$TextoVidas.text = "Vidas: " + str(vidas)
	$Nave.position = posicionInicialNave
	for hijo in get_children():
		if hijo.is_in_group("enemigos"):
			hijo.queue_free()
	if vidas <= 0:
		get_tree().change_scene_to_file("res://escenas/bienvenida.tscn")


func _on_timer_disparo_enemigos_timeout() -> void:
	var disparoEnemigo = escenaDisparoEnemigos.instantiate()
	# Memorizamos los enemigos activos
	var enemigos = []
	for hijo in get_children():
		if hijo.is_in_group("enemigos"):
			enemigos.append(hijo)
	# Escogemos uno de ellos
	var numeroEnemigo = randi_range(0,len(enemigos)-1)
	# Y creamos el disparo en su posición
	if numeroEnemigo >= 0 and numeroEnemigo < len(enemigos):
		disparoEnemigo.position = enemigos[numeroEnemigo].position
		var direccionDisparo = (disparoEnemigo.position - $Nave.position).normalized()
		disparoEnemigo.direccion = direccionDisparo * disparoEnemigo.velocidad
		add_child(disparoEnemigo)
	# Y preparamos la pausa para el siguientes disparo
	$TimerDisparoEnemigos.wait_time = randf_range(2, 3)
