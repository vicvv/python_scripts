


class Rectangle:
    """ example of class and static methods/functions """

    # class ("static") intended constants
    ORIGINAL_DEFAULT_DIMENSION = 1.
    ORIGINAL_DEFAULT_LABEL = "(no label)"
    MIN_DIM = 0.
    MAX_DIM = 1000000.
    MIN_STRING_LENGTH = 2

    # class attributes that will change over time
    default_dimension = ORIGINAL_DEFAULT_DIMENSION
    default_label = ORIGINAL_DEFAULT_LABEL

    # initializer ("constructor") method -------------------------------
    def __init__(self,
                 label=None,
                 width=None,
                 height=None):

        # repair mutable defaults
        if (width == None):
            width = self.default_dimension
        if (height == None):
            height = self.default_dimension
        if (label == None):
            label = self.default_dimension

        # instance attributes
        if (not self.set_width(width)):
            self.width = self.default_dimension
        if (not self.set_height(height)):
            self.height = self.default_dimension
        if (not self.set_label(label)):
            self.label = self.default_label

    # mutators -----------------------------------------------
    def set_width(self, width):
        if not self.valid_dimension(width):
            return False
        # else
        self.width = width
        return True

    def set_height(self, height):
        if not self.valid_dimension(height):
            return False
        # else
        self.height = height
        return True

    def set_width_height(self, width, height):
        if not (self.valid_dimension(width)
                and
                self.valid_dimension(height)):
            return False
        # else
        self.width = width
        self.height = height
        return True

    def set_label(self, label):
        if not self.valid_string(label):
            return False
        # else
        self.label = label
        return True

    # accessors -----------------------------------------------
    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_label(self):
        return self.label

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    # output method  ----------------------------------------
    def show_me(self, client_intro_str="RECTANGLE DATA:"):
        print(self.to_string(client_intro_str))

    # instance helpers -------------------------------
    def to_string(self, optional_title=""):
        if not self.valid_string(optional_title):
            optional_title = ""
        ret_str = ((optional_title
                    + "\n    label: {}"
                    + "\n    dimensions: {}(w) x {}(h).").
                   format(self.label, self.width, self.height))
        return ret_str

    #  static and class helpers -------------------------------
    @classmethod
    def valid_dimension(cls, dim_to_test):
        if ((type(dim_to_test) != float and
             type(dim_to_test) != int) or
                not (cls.MIN_DIM <= dim_to_test <= cls.MAX_DIM)
        ):
            return False
        # else
        return True

    @classmethod
    def valid_string(cls, string_to_test):
        if (type(string_to_test) != str or
                len(string_to_test) < cls.MIN_STRING_LENGTH):
            return False
            # else
            return True

    @staticmethod
    def which_is_bigger_ref(rect_1, rect_2):
        if (rect_1.get_area() > rect_2.get_area()):
            return rect_1
        else:
            return rect_2

    @classmethod
    def which_is_bigger_clone(cls, rect_1, rect_2):
        if (rect_1.get_area() > rect_2.get_area()):
            larger_ref = rect_1
        else:
            larger_ref = rect_2
        ret_obj = cls(larger_ref.label,
                      larger_ref.width, larger_ref.height)
        return ret_obj

    # class mutators and accessors ----------------------------
    @classmethod
    def set_default_dim(cls, new_dimension):
        if not cls.valid_dimension(new_dimension):
            return False
        # else
        cls.default_dimension = new_dimension
        return True

    @classmethod
    def set_default_lab(cls, new_label):
        if not cls.valid_string(new_label):
            return False
        # else
        cls.default_label = new_label
        return True

    @classmethod
    def get_default_dim(cls):
        return cls.default_dimension

    @classmethod
    def get_default_lab(cls):
        return cls.default_label


# client --------------------------------------------

# instantiate two default Rectangle objects
r1 = Rectangle()
r2 = Rectangle()

# show original data
print("\n*** After default constructors:")
r1.show_me()
r2.show_me()

# mutate, r1, with dimensions 5 x 8
r1.label = 'Rect A'
r1.set_width_height(5, 8)
# mutate, r2, with dimensions 6 x 6
# ... for practice with accessors, base it on r1's dimensions:
r2.label = 'Rect B'
r2.set_width_height(r1.get_width() + 1, r1.get_height() - 2)

print("\n*** After mutators:")
r1.show_me()
r2.show_me()

print()
print("Rectangle with label " + r1.get_label()
      + " has area " + str(r1.get_area())
      + " and perimeter " + str(r1.get_perimeter()))

print("Rectangle with label " + r2.get_label()
      + " has area " + str(r2.get_area())
      + " and perimeter " + str(r2.get_perimeter()))

# find out which is bigger - result (reference) is r3:
r3 = Rectangle.which_is_bigger_ref(r1, r2)

# at this point r3 and r1 (because r1 was bigger) point
# to the same object.  If we changed r1, we would also be
# changing r3.  How can you verify this? (informal hwk)
print()
print("Rectangle with label " + r3.get_label()
      + " is larger, having area " + str(r3.get_area()))

# find out which is bigger - result (object) is r3:
r3 = Rectangle.which_is_bigger_clone(r1, r2)

# now r3 is decoupled from r1 and r2.  It is its own
# object.  However the output looks identical to above.
print("Rectangle with label " + r3.get_label()
      + " is larger, having area " + str(r3.get_area()))

# demonstrate mutation and access of static class members
print()
if (Rectangle.set_default_lab("-UNLABELED RECTANGLE -")):
    print("Successfully changed default label to",
          Rectangle.get_default_lab())
if (Rectangle.set_default_dim(2.5)):
    print("Successfully changed default dim to",
          Rectangle.get_default_dim())

print()
r4 = Rectangle()
r4.show_me("r4 - All DEFAULT Parameters:")

r5 = Rectangle("x", -2, -5)
r5.show_me("r5 - All BAD Parameters:")

# a demonstration of how to use the Boolean return value
print()
if (not r3.set_width_height(-3, 40)):
    print("ERROR in set_width_height() AS EXPECTED")
else:
    print("OK Return set_width_height()")

if (not r3.set_width_height(21, 40)):
    print("ERROR in set_width_height()")
else:
    print("OK Return set_width_height() AS EXPECTED")

# demonstrate which_is_bigger_ref()
print()
print("which_is_bigger_ref() in action:")
r1 = Rectangle("first", 1, 1)
r2 = Rectangle("second", 2, 2)
r3 = Rectangle.which_is_bigger_ref(r1, r2)
r3.show_me("R3:")
r3.set_width_height(20, 20)
r1.show_me("R1 after changing R3")
r2.show_me("R2 after changing R3")

print()
# demonstrate which_is_bigger_clone()
print()
print("which_is_bigger_clone() in action:")
r1 = Rectangle("first", 1, 1)
r2 = Rectangle("second", 2, 2)
r3 = Rectangle.which_is_bigger_clone(r1, r2)
r3.show_me("R3:")
r3.set_width_height(20, 20)
r1.show_me("R1 after changing R3")
r2.show_me("R2 after changing R3")