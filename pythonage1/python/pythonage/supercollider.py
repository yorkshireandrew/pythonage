import math
from .vector import PVector

# =================== PSuperCollider ====================
# Utility for working out if two bodies have collided

class PSuperCollider:

    @staticmethod
    def how_far_is_point_inside_of_rectangle(x, y, rectangle):
        
        r = rectangle
        
        v1 = PVector(r.p1_x, r.p1_y, r.p2_x, r.p2_y)
        p1 = v1.perpendicular()
        direction_vector1 = v1.get_vector_to(x, y)
        depth1 = -PVector.scalar_multiply(direction_vector1, p1)     
        if depth1 < 0:
            return depth1 # not inside
                  
        v2 = PVector(r.p2_x, r.p2_y, r.p3_x, r.p3_y)
        p2 = v2.perpendicular()
        direction_vector2 = v2.get_vector_to(x, y)
        depth2 = -PVector.scalar_multiply(direction_vector2, p2)     
        if depth2 < 0:
            return depth2 # not inside
        
        v3 = PVector(r.p3_x, r.p3_y, r.p4_x, r.p4_y)
        p3 = v3.perpendicular()
        direction_vector3 = v3.get_vector_to(x, y)
        depth3 = -PVector.scalar_multiply(direction_vector3, p3)     
        if depth3 < 0:
            return depth3 # not inside
        
        v4 = PVector(r.p4_x, r.p4_y, r.p1_x, r.p1_y)
        p4 = v4.perpendicular()
        direction_vector4 = v4.get_vector_to(x, y)

        depth4 = -PVector.scalar_multiply(direction_vector4, p4)     
        if depth4 < 0:
            return depth4 # not inside

        # The point was behind all four sides. Now find which side reported the least penetration
        minimum = depth1
        if depth2 < minimum:
            minimum = depth2
        if depth3 < minimum:
            minimum = depth3
        if depth4 < minimum:
            minimum = depth4

        return minimum

    @staticmethod
    def how_far_is_rectangle_a_inside_rectangle_b(rectangle_a, rectangle_b):
        
        a = rectangle_a
        b = rectangle_b
        
        p1_depth = PSuperCollider.how_far_is_point_inside_of_rectangle(a.p1_x, a.p1_y, b)
        p2_depth = PSuperCollider.how_far_is_point_inside_of_rectangle(a.p2_x, a.p2_y, b)
        p3_depth = PSuperCollider.how_far_is_point_inside_of_rectangle(a.p3_x, a.p3_y, b)
        p4_depth = PSuperCollider.how_far_is_point_inside_of_rectangle(a.p4_x, a.p4_y, b)

        # We want to find the point in rectangle A that gave the deepest penetration
        maximum = p1_depth
        if p2_depth > maximum:
            maximum = p2_depth
        if p3_depth > maximum:
            maximum = p3_depth
        if p4_depth > maximum:
            maximum = p4_depth

        return maximum # Can return negative indicating no penetration

    @staticmethod
    def is_point_inside_rectangle(x, y, rectangle):
        
        r = rectangle
        v1 = PVector(r.p1_x, r.p1_y, r.p2_x, r.p2_y)
        p1 = v1.faster_perpendicular()
        direction_vector1 = v1.get_vector_to(x, y)
        depth1 = -PVector.scalar_multiply(direction_vector1, p1)
        if depth1 < 0:
            return False
  
        v2 = PVector(r.p2_x, r.p2_y, r.p3_x, r.p3_y)
        p2 = v2.faster_perpendicular()
        direction_vector2 = v2.get_vector_to(x, y)
        depth2 = -PVector.scalar_multiply(direction_vector2, p2)     
        if depth2 < 0:
            return False
             
        v3 = PVector(r.p3_x, r.p3_y, r.p4_x, r.p4_y)
        p3 = v3.faster_perpendicular()
        direction_vector3 = v3.get_vector_to(x, y)
        depth3 = -PVector.scalar_multiply(direction_vector3, p3)     
        if depth3 < 0:
            return False
       
        v4 = PVector(r.p4_x, r.p4_y, r.p1_x, r.p1_y)
        p4 = v4.faster_perpendicular()
        direction_vector4 = v4.get_vector_to(x, y)
        depth4 = -PVector.scalar_multiply(direction_vector4, p4)     
        if depth4 < 0:
            return False

        return True

    @staticmethod
    def has_rectangle_a_points_inside_rectangle_b(rectangle_a, rectangle_b):
        
        a = rectangle_a
        b = rectangle_b
        
        if PSuperCollider.is_point_inside_rectangle(a.p1_x, a.p1_y, b):
            return True

        if PSuperCollider.is_point_inside_rectangle(a.p2_x, a.p2_y, b):
            return True

        if PSuperCollider.is_point_inside_rectangle(a.p3_x, a.p3_y, b):
            return True

        if PSuperCollider.is_point_inside_rectangle(a.p4_x, a.p4_y, b):
            return True
      
        return False
