extends Area2D


var velocidadX = 300
var velocidadY = 300

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	position.x += velocidadX * delta
	if position.x > 1280 or position.x < 0:
		velocidadX = -velocidadX
	
	position.y += velocidadY * delta
	if position.y > 720 or position.y < 0:
		velocidadY = -velocidadY


func _on_area_entered(area: Area2D) -> void:
	print("Boom") # Replace with function body.
