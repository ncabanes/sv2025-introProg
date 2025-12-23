extends Area2D

var velocidad = 400

func _process(delta: float) -> void:
	position.x += velocidad * delta
	if position.x > get_viewport_rect().size.x:
		queue_free()


func _on_area_entered(area: Area2D) -> void:
	if area.is_in_group("enemigos"):
		get_parent().mostrarExplosion(area.position)
		get_parent().incrementarPuntos(10)
		area.queue_free()
		queue_free()
