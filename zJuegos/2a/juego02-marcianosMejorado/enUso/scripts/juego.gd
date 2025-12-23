extends Node2D

var escenaEnemigo: PackedScene
var escenaEnemigo2: PackedScene
var escenaExplosion: PackedScene
var escenaDisparo: PackedScene
var escenaDisparoEnemigos: PackedScene
#var puntos : int = 0
#@export var vidas : int = 3
var posicionInicialNave: Vector2
@export var numero_nivel: int
@export var tiempo_hasta_salto_nivel: float

func _ready() -> void:
	escenaEnemigo = load("res://escenas/enemigo.tscn")
	escenaEnemigo2 = load("res://escenas/enemigo_2.tscn")
	escenaExplosion = load("res://escenas/explosion.tscn")
	escenaDisparo = load("res://escenas/disparo.tscn")
	escenaDisparoEnemigos = load("res://escenas/disparo_enemigo.tscn")
	posicionInicialNave = $Nave.position
	$TextoPuntos .text = "Puntos: " + str(ConfigJuego.puntos)
	$TextoVidas.text = "Vidas: " + str(ConfigJuego.vidas)

func _process(delta: float) -> void:
	tiempo_hasta_salto_nivel -= delta
	if tiempo_hasta_salto_nivel <= 0:
		tiempo_hasta_salto_nivel = 20
		avanzar_nivel()
	if Input.is_action_just_pressed("disparo"):
		var disparo = escenaDisparo.instantiate()
		add_child(disparo)
		disparo.position = $Nave.position
	if Input.is_action_just_pressed("cambiar_nivel"):
		avanzar_nivel()

func mostrarExplosion(donde: Vector2) -> void:
	var explosion = escenaExplosion.instantiate()
	add_child(explosion)
	explosion.position = donde
	explosion.emitting = true

func _on_timer_salida_enemigos_timeout() -> void:
	var enemigo
	if randi_range(1,10) > 3:
		enemigo = escenaEnemigo.instantiate()
	else:
		enemigo = escenaEnemigo2.instantiate()
	enemigo.position.x = 1200
	enemigo.position.y = randi_range(50, get_viewport_rect().size.y-50)
	add_child(enemigo)

func incrementarPuntos(cantidad: int) -> void:
	ConfigJuego.puntos += cantidad
	$TextoPuntos .text = "Puntos: " + str(ConfigJuego.puntos)

func perderVida() -> void:
	ConfigJuego.vidas -= 1
	$TextoVidas.text = "Vidas: " + str(ConfigJuego.vidas)
	$Nave.position = posicionInicialNave
	for hijo in get_children():
		if hijo.is_in_group("enemigos"):
			hijo.queue_free()
	if ConfigJuego.vidas <= 0:
		call_deferred("volver_a_bienvenida")

func volver_a_bienvenida() -> void:
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

func avanzar_nivel():
	tiempo_hasta_salto_nivel = 20
	var nivel_proximo = numero_nivel + 1
	print(nivel_proximo)
	if nivel_proximo > ConfigJuego.nivel_maximo:
		nivel_proximo = 1
	get_tree().change_scene_to_file("res://escenas/nivel" +
		str(nivel_proximo)+".tscn")
