prec_dict =  {'**':7, '*':6, '/':6, '//':6, '%':6, '+':5, '-':5, '==':4, '>=':4, '>':4, '<=':4, '<':4, '!=':4, '&':3, '^':2, '|':1}
assoc_dict = {'**':1, '*':0, '/':0, '//':0, '%':0, '+':0, '-':0, '==':0, '>=':0, '>':0, '<=':0, '<':0, '!=':0, '&':0, '^':0, '|':0}
 
class Node:
    def __init__(self,x,op,y=None):
        self.precedence = prec_dict[op]
        self.assocright = assoc_dict[op]
        self.op = op
        self.x,self.y = x,y
 
    def __str__(self):
        if self.y == None:
            return '%s(%s)'%(self.op,str(self.x))
 
        str_y = str(self.y)
        if  self.y < self or \
            (self.y == self and self.assocright) or \
            (str_y[0] == '-' and self.assocright):
 
            str_y = '(%s)'%str_y
        str_x = str(self.x)
        str_op = self.op
        if self.op == '+' and not isinstance(self.x, Node) and str_x[0] == '-':
            str_x = str_x[1:]
            str_op = '-'
        elif self.op == '-' and not isinstance(self.x, Node) and str_x[0] == '-':
            str_x = str_x[1:]
            str_op = '+'
        elif self.x < self or \
             (self.x == self and not self.assocright and \
              getattr(self.x, 'op', 1) != getattr(self, 'op', 2)):
 
            str_x = '(%s)'%str_x

        if str_op == '**':
            str_op = '^'
            str_x = '{' + str_x + '}'
        elif str_op == '/':
            return '\\frac{'+str_y+'}{'+str_x+'}'
        return ' '.join([str_y, str_op, str_x])
 
    def __repr__(self):
        return 'Node(%s,%s,%s)'%(repr(self.x), repr(self.op), repr(self.y))
 
    def __lt__(self, other):
        if isinstance(other, Node):
            return self.precedence < other.precedence
        return self.precedence < prec_dict.get(other,9)
 
    def __gt__(self, other):
        if isinstance(other, Node):
            return self.precedence > other.precedence
        return self.precedence > prec_dict.get(other,9)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.precedence == other.precedence
        return self.precedence > prec_dict.get(other,9)
 
 
 
def rpn_to_infix(s):
    stack=[]
    for token in s:
        if token in prec_dict:
            stack.append(Node(stack.pop(),token,stack.pop()))
        else:
            stack.append(token)
 
    return str(stack[0])


