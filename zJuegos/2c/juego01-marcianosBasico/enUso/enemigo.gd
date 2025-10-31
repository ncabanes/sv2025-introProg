extends Area2D

var velocidadX = 400
var velocidadY = 300

func _process(delta: float) -> void:
	position.x += velocidadX * delta
	if position.x > 1200 or position.x < 80:
		velocidadX = -velocidadX
	
	position.y += velocidadY * delta
	if position.y > 640 or position.y < 80:
		velocidadY = -velocidadY


func _on_area_entered(area: Area2D) -> void:
	print("Boom")
