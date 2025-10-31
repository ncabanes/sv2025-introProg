extends Area2D


var velocidad = 300

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	position.x += velocidad * delta
	if position.x > 1280 or position.x < 0:
		velocidad = -velocidad
