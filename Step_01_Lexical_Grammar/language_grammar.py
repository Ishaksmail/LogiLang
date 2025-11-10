import json
from sly import Lexer

class LogiLangLexer(Lexer):
    # ------------------------
    # تعريف التوكنات العامة
    # ------------------------
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


# ------------------------
# DFA مع نوع كل final state
# ------------------------
class DFA:
    def __init__(self):
        self.states = set()
        self.alphabet = set()
        self.transitions = {}
        self.start_state = 'Q0'
        self.accepting_states = {}  # final state: token type
        self.current_state_id = 1

    def new_state(self):
        state = f"Q{self.current_state_id}"
        self.current_state_id += 1
        self.states.add(state)
        return state

    def add_transition(self, from_state, symbol, to_state):
        self.alphabet.add(symbol)
        self.transitions.setdefault(from_state, {})[symbol] = to_state

    def add_accepting(self, state, token_type):
        self.accepting_states[state] = token_type

    def to_dict(self):
        return {
            "states": list(self.states),
            "alphabet": list(self.alphabet),
            "start_state": self.start_state,
            "accepting_states": self.accepting_states,
            "transitions": self.transitions
        }


# ------------------------
# بناء DFA من Lexer
# ------------------------
def build_dfa_from_lexer():
    lexer = LogiLangLexer()
    dfa = DFA()

    token_examples = {
        'KEYWORD': list(LogiLangLexer.KEYWORDS),
        'IDENTIFIER': ['x1', 'var_name', 'myVar'],
        'INTEGER': ['123', '456'],
        'STRING': ['"hello"', '"world"'],
        'EQ': ['=='], 'NEQ': ['!='], 'LE': ['<='], 'GE': ['>='],
        'LT': ['<'], 'GT': ['>'], 'ASSIGN': ['='],
        'PLUS': ['+'], 'MINUS': ['-'], 'MULT': ['*'], 'DIV': ['/'], 'MODULO': ['%'],
        'LPAREN': ['('], 'RPAREN': [')'], 'LBRACE': ['{'], 'RBRACE': ['}'],
        'LBRACKET': ['['], 'RBRACKET': [']'], 'COMMA': [','], 'DOT': ['.'],
        'SEMICOLON': [';'], 'QUESTION': ['?'], 'COLON': [':'],
        'COMMENT': ['/* comment */', '// comment']
    }

    for token_type, examples in token_examples.items():
        for s in examples:
            current = dfa.start_state
            for c in s:
                if current in dfa.transitions and c in dfa.transitions[current]:
                    current = dfa.transitions[current][c]
                else:
                    next_state = dfa.new_state()
                    dfa.add_transition(current, c, next_state)
                    current = next_state
            dfa.add_accepting(current, token_type)

    return dfa


# ------------------------
# تشغيل وحفظ DFA في JSON
# ------------------------
if __name__ == "__main__":
    dfa = build_dfa_from_lexer()
    dfa_dict = dfa.to_dict()

    with open("final_dfa_grammar.json", "w", encoding="utf-8") as f:
        json.dump(dfa_dict, f, ensure_ascii=False, indent=4)

    print("✅ DFA النهائي محفوظ في ملف final_dfa_grammar.json")
