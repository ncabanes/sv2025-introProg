extends Area2D

var velocidad = 400

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	position.x += velocidad * delta
	if position.x > get_viewport_rect().size.x:
		queue_free()


func _on_area_entered(otro: Area2D) -> void:
	if otro.is_in_group("enemigos"):
		get_parent().explotar(position)
		otro.queue_free()
		queue_free()
