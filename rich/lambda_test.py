# unit testfor rich lambda
import unittest


class TestLambda(unittest.TestCase):
    def test_add(self):
        num = (lambda x, y: x + y)(1, 2)
        self.assertEqual(num, 3)

    def test_add_curry(self):
        num = (lambda x: lambda y: x + y)(1)(2)
        self.assertEqual(num, 3)

    def test_add_curry2(self):
        fun = (lambda x: (lambda y: x + y))
        num = fun(1)(2)
        self.assertEqual(num, 3)

    def test_true_false_curry(self):
        # A function that returns a function whose result is the first argument
        ltrue = (lambda x: (lambda y: x))
        lfalse = (lambda x: (lambda y: y))
        lif = (lambda b: (lambda x: (lambda y: b(x)(y))))
        num = lif(ltrue)(1)(2)
        self.assertEqual(num, 1)
        num = lif(lfalse)(1)(2)
        self.assertEqual(num, 2)

    def test_true_false_nocurry(self):
        ltrue = (lambda x, y: x)
        lfalse = (lambda x, y: y)
        lif = (lambda b, x, y: b(x,y))
        num = lif(ltrue,5,8)
        self.assertEqual(num, 5)
        num = lif(lfalse,5,8)
        self.assertEqual(num, 8)

    def test_not(self):
        # A function that returns a function that negates the first argument
        ltrue = (lambda x, y: x)
        lfalse = (lambda x, y: y)
        lnot = (lambda x: x(lfalse,ltrue))
        self.assertEqual(ltrue,lnot(lfalse))
        self.assertEqual(lfalse,lnot(ltrue))
        num = lnot(ltrue)(5, 8)
        self.assertEqual(num, 8)
        num = lnot(lfalse)(3, 7)
        self.assertEqual(num, 3)

    def test_and(self):
        # A function that returns a function that negates the first argument
        ltrue = (lambda x, y: x)
        lfalse = (lambda x, y: y)
        land = (lambda p, q: p(q,p))

        self.assertEqual(ltrue,land(ltrue,ltrue))
        self.assertEqual(lfalse,land(ltrue,lfalse))
        self.assertEqual(lfalse,land(lfalse,ltrue))
        self.assertEqual(lfalse,land(lfalse,lfalse))

    def test_or(self):
        # A function that returns a function that negates the first argument
        ltrue = (lambda x, y: x)
        lfalse = (lambda x, y: y)
        lor = (lambda p, q: p(p,q))

        self.assertEqual(ltrue,lor(ltrue,ltrue))
        self.assertEqual(ltrue,lor(ltrue,lfalse))
        self.assertEqual(ltrue,lor(lfalse,ltrue))
        self.assertEqual(lfalse,lor(lfalse,lfalse))

    def test_numbers(self):
        lzero = (lambda f, x: x)
        lone = (lambda f, x: f(x))
        ltwo = (lambda f, x: f(f(x)))   
        lthree = (lambda f, x: f(f(f(x))))
        lfour = (lambda f, x: f(f(f(f(x)))))

        lsucc = (lambda n: (lambda f, x: f(n(f,x))))
        inc = (lambda n: n+1)
        self.assertEqual(lsucc(lzero)(inc,5), lone(inc,5))
        #self.assertEqual(lsucc(lzero), lone)
        #self.assertEqual(lone(lsucc)(0), 1)
        #self.assertEqual(ltwo(lsucc)(0), 2)
        #self.assertEqual(lthree(lsucc)(0), 3)
        #self.assertEqual(lfour(lsucc)(0), 4)

        #self.assertEqual(lsucc(lzero)(lzero)(0), 1)
        #self.assertEqual(lsucc(lone)(lzero)(0), 2)
        #self.assertEqual(lsucc(ltwo)(lzero)(0), 3)
        #self.assertEqual(lsucc(lthree)(lzero)(0), 4)
        #self.assertEqual(lsucc(lfour)(lzero)(0), 5)