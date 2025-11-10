from sly import Lexer

class LogiLangLexer(Lexer):
    tokens = {
        KEYWORD, IDENTIFIER, INTEGER, STRING,
        EQ, NEQ, LE, GE, LT, GT, ASSIGN,
        PLUS, MINUS, MULT, DIV, MODULO,
        LPAREN, RPAREN, LBRACE, RBRACE, LBRACKET, RBRACKET,
        COMMA, DOT, SEMICOLON, QUESTION, COLON,
        COMMENT
    }

    # ------------------------
    # الكلمات المفتاحية
    # ------------------------
    KEYWORDS = {
        "this","has","many","only","import","logic",
        "if","elif","else","while","for","print",
        "int","bool","AND","OR","NOT","XOR","mod",
        "out","inp","n_inp","n_out"
    }

    # ------------------------
    # التعبيرات النمطية
    # ------------------------
    IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
    INTEGER    = r'\d+'
    STRING     = r'"([^"\\]|\\.)*"'

    EQ         = r'=='
    NEQ        = r'!='
    LE         = r'<='
    GE         = r'>='
    LT         = r'<'
    GT         = r'>'
    ASSIGN     = r'='
    PLUS       = r'\+'
    MINUS      = r'-'
    MULT       = r'\*'
    DIV        = r'/'
    MODULO     = r'%'

    LPAREN     = r'\('
    RPAREN     = r'\)'
    LBRACE     = r'\{'
    RBRACE     = r'\}'
    LBRACKET   = r'\['
    RBRACKET   = r'\]'
    COMMA      = r','
    DOT        = r'\.'
    SEMICOLON  = r';'
    QUESTION   = r'\?'
    COLON      = r':'

    COMMENT    = r'//[^\n]*|/\*[\s\S]*?\*/'

    # ------------------------
    # تجاهل المسافات البيضاء
    # ------------------------
    ignore = ' \t\r\n'

    # ------------------------
    # تحويل IDENTIFIER إلى KEYWORD عند الحاجة
    # ------------------------
    def IDENTIFIER(self, t):
        if t.value in self.KEYWORDS:
            t.type = 'KEYWORD'
        return t

# اختبار
if __name__ == "__main__":
    lexer = LogiLangLexer()
    code = '''
this Example has many;

import adder;
import comparator.*;

logic half_adder(n_inp=2, n_out=2) {

  out[0] = adder(inp[0], inp[1]);
  out[1] = inp[0] AND inp[1];
}

logic comparator_1bit(n_inp=2, n_out=1) {
  if (inp[0] == inp[1]) {
    out[0] = 1;
  } else {
    out[0] = 0;
  }
}

logic main_circuit(n_inp=4, n_out=2) {
  int i = 0;
  bool active = true;

  if (active) {
    print("Main circuit active...");
  }

  while (i < 2) {
    print("Processing pair " + i);
    out[i] = adder(in[i*2], in[i*2 + 1]);
    i = i + 1;
  }

  bool equal = comparator_1bit(inp[0], inp[1]);
  if (equal) {
    print("Inputs 0 and 1 are equal.");
  } else {
    print("Inputs 0 and 1 are different.");
  }
}

logic arithmetic_unit(n_inp=3, n_out=2) {
  int sum = inp[0] + inp[1];
  int remainder = sum mod inp[2];

  // test

  if (remainder == 0) {
    out[0] = 1;
  } else {
    out[0] = 0;
  }
  if (sum > inp[2]){
  out[1] = 1 ;
  }else {
  out[1] = 0;
  }
}

    '''
    for tok in lexer.tokenize(code):
        print(tok)
