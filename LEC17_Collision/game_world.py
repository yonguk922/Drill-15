world = [[], [], []]  # 0: 배경, 1: 오브젝트, 2: UI

def add_oject(o, depth=1):
    world[depth].append(o)

def add_objects(ol, depth=1):
    world[depth] += ol

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o) # 충돌 쌍에서 제거
            return

def update():
    for layer in world:
        for o in layer[:]:
            o.update()

def render():
    for layer in world:
        for o in layer[:]:
            o.draw()


def clear():
    for layer in world:
        layer.clear()

def collide(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

collision_pairs ={} # 충돌 쌍을 저장하는 딕셔너리

def add_collision_pair(group, a, b):
    if group not in collision_pairs:
        collision_pairs[group] = [[], []] # a와 b를 저장할 빈 리스트 생성
    if a:
        collision_pairs[group][0].append(a)
    if b:
        collision_pairs[group][1].append(b)

def handle_collisions():
    # 충돌 쌍을 순회하며 충돌 처리
    for group, pairs in collision_pairs.items():
        for a in pairs[0]:
            for b in pairs[1]:
                if collide(a, b):
                    # 충돌 시 처리할 로직을 여기에 작성
                    a.handle_collision(group, b)
                    b.handle_collision(group, a)

def remove_collision_object(o):
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)

def remobe_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o)  # 충돌 쌍에서 제거
            return
    raise ValueError("Cannot delete non existing object.")
