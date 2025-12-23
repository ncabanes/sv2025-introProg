extends Area2D

var velocidad = 300

func _process(delta: float) -> void:
	if Input.is_action_pressed("arriba") and position.y > 20:
		position.y -= velocidad * delta
	if Input.is_action_pressed("abajo") \
			and position.y < get_viewport_rect().size.y - 100:
		position.y += velocidad * delta
	if Input.is_action_pressed("izquierda") and position.x > 50:
		position.x -= velocidad * delta
	if Input.is_action_pressed("derecha") \
			and position.x < get_viewport_rect().size.x / 2:
		position.x += velocidad * delta

func _on_area_entered(area: Area2D) -> void:
	get_parent().mostrarExplosion(area.position)
	get_parent().perderVida()
	area.queue_free()
