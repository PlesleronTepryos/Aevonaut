import math


class VectorError(Exception):
    pass


class Vec3:

    def __init__(self, vl):
        if isinstance(vl, list):
            vl += [0] * (3 - len(vl))
            self.x = vl[0]
            self.y = vl[1]
            self.z = vl[2]
        elif isinstance(vl, Vector):
            self.x = vl.x
            self.x = vl.x
            self.x = vl.x
        else:
            raise VectorError("Not a valid vector-like object.")

    def set(self, vl):
        if isinstance(vl, list):
            vl += [0] * (3 - len(vl))
            self.x = vl[0]
            self.y = vl[1]
            self.z = vl[2]
        elif isinstance(vl, Vector):
            self.x = vl.x
            self.x = vl.x
            self.x = vl.x
        else:
            raise VectorError("Not a valid vector-like object.")

    def __mod__(self, vl):
        if isinstance(vl, list):
            vl += [0] * (3 - len(vl))
            return Vec2([self.x % vl[0], self.y % vl[1], self.z % vl[2]])
        elif isinstance(vl, Vec2):
            return Vec2([self.x % vl.x, self.y % vl.y, self.z % vl.z])
        else:
            raise VectorError("Not a valid vector-like object.")

    def __add__(self, vl):
        if isinstance(vl, list):
            vl += [0] * (3 - len(vl))
            return Vec2([self.x + vl[0], self.y + vl[1], self.z + vl[2]])
        elif isinstance(vl, Vec2):
            return Vec2([self.x + vl.x, self.y + vl.y, self.z + vl.z])
        else:
            raise VectorError("Not a valid vector-like object.")

    def __sub__(self, vl):
        if isinstance(vl, list):
            vl += [0] * (3 - len(vl))
            return Vec2([self.x - vl[0], self.y - vl[1], self.z - vl[2]])
        elif isinstance(vl, Vec2):
            return Vec2([self.x - vl.x, self.y - vl.y, self.z - vl.z])
        else:
            raise VectorError("Not a valid vector-like object.")

    def __mul__(self, n):
        return Vec2([self.x * n, self.y * n, self.z * n])

    def __truediv__(self, n):
        return Vec2([self.x / n, self.y / n, self.z / n])

    def __str__(self):
        return 'Vec3([{0}, {1}, {2}])'.format(round(self.x, 2), round(self.y, 2), round(self.z, 2))

    def mag(self):
        return sum([self.x ** 2, self.y ** 2, self.z ** 2]) ** 0.5

    def norm(self):
        self.div(self.mag())

    def setMag(self, n):
        self.norm().mult(n)



class Vec2:

    def __init__(self, vl):
        if isinstance(vl, list):
            vl += [0] * (2 - len(vl))
            self.x = vl[0]
            self.y = vl[1]
        elif isinstance(vl, Vec2):
            self.x = vl.x
            self.y = vl.y
        else:
            raise VectorError("Not a valid vector-like object.")

    def set(self, vl):
        if isinstance(vl, list):
            vl += [0] * (2 - len(vl))
            self.x = vl[0]
            self.y = vl[1]
        elif isinstance(vl, Vec2):
            self.x = vl.x
            self.y = vl.y
        else:
            raise VectorError("Not a valid vector-like object.")

    def __mod__(self, vl):
        if isinstance(vl, list):
            vl += [0] * (2 - len(vl))
            return Vec2([self.x % vl[0], self.y % vl[1]])
        elif isinstance(vl, Vec2):
            return Vec2([self.x % vl.x, self.y % vl.y])
        else:
            raise VectorError("Not a valid vector-like object.")

    def __add__(self, vl):
        if isinstance(vl, list):
            vl += [0] * (2 - len(vl))
            return Vec2([self.x + vl[0], self.y + vl[1]])
        elif isinstance(vl, Vec2):
            return Vec2([self.x + vl.x, self.y + vl.y])
        else:
            raise VectorError("Not a valid vector-like object.")

    def __sub__(self, vl):
        if isinstance(vl, list):
            vl += [0] * (2 - len(vl))
            return Vec2([self.x - vl[0], self.y - vl[1]])
        elif isinstance(vl, Vec2):
            return Vec2([self.x - vl.x, self.y - vl.y])
        else:
            raise VectorError("Not a valid vector-like object.")

    def __mul__(self, n):
        return Vec2([self.x * n, self.y * n])

    def __truediv__(self, n):
        return Vec2([self.x / n, self.y / n])

    def __str__(self):
        return 'Vec2([{0}, {1}])'.format(round(self.x, 2), round(self.y, 2))

    def mag(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def norm(self):
        if self.mag() > 0:
            return self / self.mag()
        else:
            return self

    def withMag(self, n):
        return self.norm() * n

    def head(self):
        return math.atan2(-self.y,-self.x)+math.pi

    def fromAngle(tht):
        return Vec2([math.cos(tht), math.sin(tht)])