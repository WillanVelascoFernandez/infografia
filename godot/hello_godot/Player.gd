extends KinematicBody2D

export (int) var speed = 100

var target
var velocity = Vector2()

func _ready():
	target = position
func _input(event):
	if event.is_action_pressed("click"):
		target = get_global_mouse_position()
		print(target)
	
# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pas
func _physics_process(delta):
	velocity = position.direction_to(target) * speed
	
	if position.distance_to(target)>5:
		velocity = move_and_slide(velocity)
