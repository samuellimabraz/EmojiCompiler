
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftEQUALNEQUALleftLTLTEGTGTEleftPLUSMINUSleftMULTIPLYDIVMODrightNOTAND ASSIGN BOOL BREAK CHAR CHARACTER COMMA CONTINUE DIV DOT ELSE EQUAL FALSE FLOAT FOR GT GTE IF INT LBRACE LBRACKET LPAREN LT LTE MAIN MINUS MOD MULTIPLY NEQUAL NOME NOT NUMBER OR PLUS PRINTF RBRACE RBRACKET RETURN RPAREN SCANF SEMICOLON SQUOTE TRUE VOID WHILEprogram : INT MAIN LPAREN RPAREN blocosinal : NOT PLUS\n        | NOT MINUS\n        | NOT\n        | PLUS\n        | MINUScomando : declaration\n        | assignment SEMICOLON\n        | if_statement\n        | while_statement\n        | for_statement\n        | bloco\n        | break_statement\n        | continue_statement\n        | return_statement\n        | printf_statement\n        | scanf_statementcomandos : comando comandos\n        | comandobloco : LBRACE comandos RBRACE\n        | LBRACE RBRACEparentheses : LPAREN valor RPARENtype : INT\n        | FLOAT\n        | CHAR\n        | VOID\n        | BOOLoperador : MULTIPLY\n        | DIV\n        | MOD\n        | PLUS\n        | MINUS\n        | EQUAL\n        | NEQUAL\n        | GT\n        | LT\n        | GTE\n        | LTE\n        | AND\n        | OR\n        boolean : TRUE\n        | FALSEvalor : NUMBER\n        | NOME\n        | CHARACTER\n        | boolean\n        | operation\n        | parentheses\n        | sinal valorvalores : valor\n        | valor COMMA valores\n        operation : valor operador valor\n        assignment : NOME ASSIGN valordeclaration_list : NOME\n        | NOME declaration_list\n        | NOME ASSIGN valor\n        | NOME ASSIGN valor COMMA declaration_listdeclaration : type declaration_list SEMICOLONif_statement : IF LPAREN valor RPAREN blocowhile_statement : WHILE LPAREN valor RPAREN blocofor_statement : FOR LPAREN for_init SEMICOLON for_condition SEMICOLON for_update RPAREN comandofor_init : assignment\n        | declaration\n        | valor\n        | empty\n        | assignment for_comma\n        | valor for_comma\n        | declaration for_comma\n        for_comma : COMMA assignment\n        | COMMA valor SEMICOLON\n        | COMMA assignment for_commafor_condition : assignment\n        | valor\n        | valor for_comma\n        | assignment for_comma\n        | emptyfor_update : assignment\n        | valor\n        | valor for_comma\n        | assignment for_comma\n        | emptyscanf_statement : SCANF LPAREN CHARACTER COMMA NOME RPAREN SEMICOLONprintf_statement : PRINTF LPAREN CHARACTER COMMA valores RPAREN SEMICOLON\n        | PRINTF LPAREN CHARACTER RPAREN SEMICOLONbreak_statement : BREAK SEMICOLONcontinue_statement : CONTINUE SEMICOLONreturn_statement : RETURN valor SEMICOLONempty :'
    
_lr_action_items = {'INT':([0,7,9,10,11,13,14,15,16,17,18,19,20,21,37,39,45,46,47,64,76,111,112,121,136,138,139,142,],[2,32,-21,32,-7,-9,-10,-11,-12,-13,-14,-15,-16,-17,-20,-8,32,-85,-86,-58,-87,-59,-60,-84,-83,-82,32,-61,]),'$end':([1,6,9,37,],[0,-1,-21,-20,]),'MAIN':([2,],[3,]),'LPAREN':([3,24,25,26,29,30,31,42,43,44,45,55,58,59,60,61,66,77,78,79,80,81,82,83,84,85,86,87,88,89,90,93,94,100,102,107,124,130,],[4,43,44,45,58,62,63,58,58,58,58,58,58,-4,-5,-6,58,58,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-2,-3,58,58,58,58,58,]),'RPAREN':([4,49,50,51,52,53,54,56,57,67,68,69,75,91,92,95,105,106,117,119,120,122,124,127,128,132,133,134,135,137,140,141,],[5,-43,-44,-45,-46,-47,-48,-41,-42,-53,98,99,-44,-49,106,108,-52,-22,-69,129,-50,131,-88,-71,-70,139,-77,-78,-81,-51,-80,-79,]),'LBRACE':([5,7,9,10,11,13,14,15,16,17,18,19,20,21,37,39,46,47,64,76,98,99,111,112,121,136,138,139,142,],[7,7,-21,7,-7,-9,-10,-11,-12,-13,-14,-15,-16,-17,-20,-8,-85,-86,-58,-87,7,7,-59,-60,-84,-83,-82,7,-61,]),'RBRACE':([7,8,9,10,11,13,14,15,16,17,18,19,20,21,37,38,39,46,47,64,76,111,112,121,136,138,142,],[9,37,-21,-19,-7,-9,-10,-11,-12,-13,-14,-15,-16,-17,-20,-18,-8,-85,-86,-58,-87,-59,-60,-84,-83,-82,-61,]),'NOME':([7,9,10,11,13,14,15,16,17,18,19,20,21,22,29,32,33,34,35,36,37,39,41,42,43,44,45,46,47,55,58,59,60,61,64,66,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,93,94,100,102,107,109,110,111,112,121,124,130,136,138,139,142,],[23,-21,23,-7,-9,-10,-11,-12,-13,-14,-15,-16,-17,41,50,-23,-24,-25,-26,-27,-20,-8,41,50,50,50,75,-85,-86,50,50,-4,-5,-6,-58,50,-87,50,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-2,-3,75,75,50,122,41,-59,-60,-84,75,50,-83,-82,23,-61,]),'IF':([7,9,10,11,13,14,15,16,17,18,19,20,21,37,39,46,47,64,76,111,112,121,136,138,139,142,],[24,-21,24,-7,-9,-10,-11,-12,-13,-14,-15,-16,-17,-20,-8,-85,-86,-58,-87,-59,-60,-84,-83,-82,24,-61,]),'WHILE':([7,9,10,11,13,14,15,16,17,18,19,20,21,37,39,46,47,64,76,111,112,121,136,138,139,142,],[25,-21,25,-7,-9,-10,-11,-12,-13,-14,-15,-16,-17,-20,-8,-85,-86,-58,-87,-59,-60,-84,-83,-82,25,-61,]),'FOR':([7,9,10,11,13,14,15,16,17,18,19,20,21,37,39,46,47,64,76,111,112,121,136,138,139,142,],[26,-21,26,-7,-9,-10,-11,-12,-13,-14,-15,-16,-17,-20,-8,-85,-86,-58,-87,-59,-60,-84,-83,-82,26,-61,]),'BREAK':([7,9,10,11,13,14,15,16,17,18,19,20,21,37,39,46,47,64,76,111,112,121,136,138,139,142,],[27,-21,27,-7,-9,-10,-11,-12,-13,-14,-15,-16,-17,-20,-8,-85,-86,-58,-87,-59,-60,-84,-83,-82,27,-61,]),'CONTINUE':([7,9,10,11,13,14,15,16,17,18,19,20,21,37,39,46,47,64,76,111,112,121,136,138,139,142,],[28,-21,28,-7,-9,-10,-11,-12,-13,-14,-15,-16,-17,-20,-8,-85,-86,-58,-87,-59,-60,-84,-83,-82,28,-61,]),'RETURN':([7,9,10,11,13,14,15,16,17,18,19,20,21,37,39,46,47,64,76,111,112,121,136,138,139,142,],[29,-21,29,-7,-9,-10,-11,-12,-13,-14,-15,-16,-17,-20,-8,-85,-86,-58,-87,-59,-60,-84,-83,-82,29,-61,]),'PRINTF':([7,9,10,11,13,14,15,16,17,18,19,20,21,37,39,46,47,64,76,111,112,121,136,138,139,142,],[30,-21,30,-7,-9,-10,-11,-12,-13,-14,-15,-16,-17,-20,-8,-85,-86,-58,-87,-59,-60,-84,-83,-82,30,-61,]),'SCANF':([7,9,10,11,13,14,15,16,17,18,19,20,21,37,39,46,47,64,76,111,112,121,136,138,139,142,],[31,-21,31,-7,-9,-10,-11,-12,-13,-14,-15,-16,-17,-20,-8,-85,-86,-58,-87,-59,-60,-84,-83,-82,31,-61,]),'FLOAT':([7,9,10,11,13,14,15,16,17,18,19,20,21,37,39,45,46,47,64,76,111,112,121,136,138,139,142,],[33,-21,33,-7,-9,-10,-11,-12,-13,-14,-15,-16,-17,-20,-8,33,-85,-86,-58,-87,-59,-60,-84,-83,-82,33,-61,]),'CHAR':([7,9,10,11,13,14,15,16,17,18,19,20,21,37,39,45,46,47,64,76,111,112,121,136,138,139,142,],[34,-21,34,-7,-9,-10,-11,-12,-13,-14,-15,-16,-17,-20,-8,34,-85,-86,-58,-87,-59,-60,-84,-83,-82,34,-61,]),'VOID':([7,9,10,11,13,14,15,16,17,18,19,20,21,37,39,45,46,47,64,76,111,112,121,136,138,139,142,],[35,-21,35,-7,-9,-10,-11,-12,-13,-14,-15,-16,-17,-20,-8,35,-85,-86,-58,-87,-59,-60,-84,-83,-82,35,-61,]),'BOOL':([7,9,10,11,13,14,15,16,17,18,19,20,21,37,39,45,46,47,64,76,111,112,121,136,138,139,142,],[36,-21,36,-7,-9,-10,-11,-12,-13,-14,-15,-16,-17,-20,-8,36,-85,-86,-58,-87,-59,-60,-84,-83,-82,36,-61,]),'SEMICOLON':([12,27,28,40,41,45,48,49,50,51,52,53,54,56,57,64,65,67,70,71,72,73,74,75,91,97,100,101,103,104,105,106,108,113,114,115,116,117,118,123,125,126,127,128,129,131,],[39,46,47,64,-54,-88,76,-43,-44,-45,-46,-47,-48,-41,-42,-58,-55,-53,100,-62,-63,-64,-65,-44,-49,-56,-88,-66,-68,-67,-52,-22,121,124,-72,-73,-76,-69,128,-57,-75,-74,-71,-70,136,138,]),'ASSIGN':([23,41,75,],[42,66,42,]),'NUMBER':([29,42,43,44,45,55,58,59,60,61,66,77,78,79,80,81,82,83,84,85,86,87,88,89,90,93,94,100,102,107,124,130,],[49,49,49,49,49,49,49,-4,-5,-6,49,49,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-2,-3,49,49,49,49,49,]),'CHARACTER':([29,42,43,44,45,55,58,59,60,61,62,63,66,77,78,79,80,81,82,83,84,85,86,87,88,89,90,93,94,100,102,107,124,130,],[51,51,51,51,51,51,51,-4,-5,-6,95,96,51,51,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-2,-3,51,51,51,51,51,]),'TRUE':([29,42,43,44,45,55,58,59,60,61,66,77,78,79,80,81,82,83,84,85,86,87,88,89,90,93,94,100,102,107,124,130,],[56,56,56,56,56,56,56,-4,-5,-6,56,56,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-2,-3,56,56,56,56,56,]),'FALSE':([29,42,43,44,45,55,58,59,60,61,66,77,78,79,80,81,82,83,84,85,86,87,88,89,90,93,94,100,102,107,124,130,],[57,57,57,57,57,57,57,-4,-5,-6,57,57,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-2,-3,57,57,57,57,57,]),'NOT':([29,42,43,44,45,55,58,59,60,61,66,77,78,79,80,81,82,83,84,85,86,87,88,89,90,93,94,100,102,107,124,130,],[59,59,59,59,59,59,59,-4,-5,-6,59,59,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-2,-3,59,59,59,59,59,]),'PLUS':([29,42,43,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,61,66,67,68,69,73,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,97,100,102,105,106,107,115,118,120,124,130,134,],[60,60,60,60,60,81,-43,-44,-45,-46,-47,-48,60,-41,-42,60,-4,-5,-6,60,81,81,81,81,-44,60,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,81,81,-2,-3,81,60,60,81,-22,60,81,81,81,60,60,81,]),'MINUS':([29,42,43,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,61,66,67,68,69,73,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,97,100,102,105,106,107,115,118,120,124,130,134,],[61,61,61,61,61,82,-43,-44,-45,-46,-47,-48,61,-41,-42,61,-4,-5,-6,61,82,82,82,82,-44,61,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,82,82,-2,-3,82,61,61,82,-22,61,82,82,82,61,61,82,]),'MULTIPLY':([48,49,50,51,52,53,54,56,57,67,68,69,73,75,91,92,97,105,106,115,118,120,134,],[78,-43,-44,-45,-46,-47,-48,-41,-42,78,78,78,78,-44,78,78,78,78,-22,78,78,78,78,]),'DIV':([48,49,50,51,52,53,54,56,57,67,68,69,73,75,91,92,97,105,106,115,118,120,134,],[79,-43,-44,-45,-46,-47,-48,-41,-42,79,79,79,79,-44,79,79,79,79,-22,79,79,79,79,]),'MOD':([48,49,50,51,52,53,54,56,57,67,68,69,73,75,91,92,97,105,106,115,118,120,134,],[80,-43,-44,-45,-46,-47,-48,-41,-42,80,80,80,80,-44,80,80,80,80,-22,80,80,80,80,]),'EQUAL':([48,49,50,51,52,53,54,56,57,67,68,69,73,75,91,92,97,105,106,115,118,120,134,],[83,-43,-44,-45,-46,-47,-48,-41,-42,83,83,83,83,-44,83,83,83,83,-22,83,83,83,83,]),'NEQUAL':([48,49,50,51,52,53,54,56,57,67,68,69,73,75,91,92,97,105,106,115,118,120,134,],[84,-43,-44,-45,-46,-47,-48,-41,-42,84,84,84,84,-44,84,84,84,84,-22,84,84,84,84,]),'GT':([48,49,50,51,52,53,54,56,57,67,68,69,73,75,91,92,97,105,106,115,118,120,134,],[85,-43,-44,-45,-46,-47,-48,-41,-42,85,85,85,85,-44,85,85,85,85,-22,85,85,85,85,]),'LT':([48,49,50,51,52,53,54,56,57,67,68,69,73,75,91,92,97,105,106,115,118,120,134,],[86,-43,-44,-45,-46,-47,-48,-41,-42,86,86,86,86,-44,86,86,86,86,-22,86,86,86,86,]),'GTE':([48,49,50,51,52,53,54,56,57,67,68,69,73,75,91,92,97,105,106,115,118,120,134,],[87,-43,-44,-45,-46,-47,-48,-41,-42,87,87,87,87,-44,87,87,87,87,-22,87,87,87,87,]),'LTE':([48,49,50,51,52,53,54,56,57,67,68,69,73,75,91,92,97,105,106,115,118,120,134,],[88,-43,-44,-45,-46,-47,-48,-41,-42,88,88,88,88,-44,88,88,88,88,-22,88,88,88,88,]),'AND':([48,49,50,51,52,53,54,56,57,67,68,69,73,75,91,92,97,105,106,115,118,120,134,],[89,-43,-44,-45,-46,-47,-48,-41,-42,89,89,89,89,-44,89,89,89,89,-22,89,89,89,89,]),'OR':([48,49,50,51,52,53,54,56,57,67,68,69,73,75,91,92,97,105,106,115,118,120,134,],[90,-43,-44,-45,-46,-47,-48,-41,-42,90,90,90,90,-44,90,90,90,90,-22,90,90,90,90,]),'COMMA':([49,50,51,52,53,54,56,57,64,67,71,72,73,75,91,95,96,97,105,106,114,115,117,120,133,134,],[-43,-44,-45,-46,-47,-48,-41,-42,-58,-53,102,102,102,-44,-49,107,109,110,-52,-22,102,102,102,130,102,102,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'bloco':([5,7,10,98,99,139,],[6,16,16,111,112,16,]),'comandos':([7,10,],[8,38,]),'comando':([7,10,139,],[10,10,142,]),'declaration':([7,10,45,139,],[11,11,72,11,]),'assignment':([7,10,45,100,102,124,139,],[12,12,71,114,117,133,12,]),'if_statement':([7,10,139,],[13,13,13,]),'while_statement':([7,10,139,],[14,14,14,]),'for_statement':([7,10,139,],[15,15,15,]),'break_statement':([7,10,139,],[17,17,17,]),'continue_statement':([7,10,139,],[18,18,18,]),'return_statement':([7,10,139,],[19,19,19,]),'printf_statement':([7,10,139,],[20,20,20,]),'scanf_statement':([7,10,139,],[21,21,21,]),'type':([7,10,45,139,],[22,22,22,22,]),'declaration_list':([22,41,110,],[40,65,123,]),'valor':([29,42,43,44,45,55,58,66,77,100,102,107,124,130,],[48,67,68,69,73,91,92,97,105,115,118,120,134,120,]),'boolean':([29,42,43,44,45,55,58,66,77,100,102,107,124,130,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'operation':([29,42,43,44,45,55,58,66,77,100,102,107,124,130,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'parentheses':([29,42,43,44,45,55,58,66,77,100,102,107,124,130,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'sinal':([29,42,43,44,45,55,58,66,77,100,102,107,124,130,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'for_init':([45,],[70,]),'empty':([45,100,124,],[74,116,135,]),'operador':([48,67,68,69,73,91,92,97,105,115,118,120,134,],[77,77,77,77,77,77,77,77,77,77,77,77,77,]),'for_comma':([71,72,73,114,115,117,133,134,],[101,103,104,125,126,127,140,141,]),'for_condition':([100,],[113,]),'valores':([107,130,],[119,137,]),'for_update':([124,],[132,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> INT MAIN LPAREN RPAREN bloco','program',5,'p_program','emoji_parser.py',76),
  ('sinal -> NOT PLUS','sinal',2,'p_sinal','emoji_parser.py',80),
  ('sinal -> NOT MINUS','sinal',2,'p_sinal','emoji_parser.py',81),
  ('sinal -> NOT','sinal',1,'p_sinal','emoji_parser.py',82),
  ('sinal -> PLUS','sinal',1,'p_sinal','emoji_parser.py',83),
  ('sinal -> MINUS','sinal',1,'p_sinal','emoji_parser.py',84),
  ('comando -> declaration','comando',1,'p_comando','emoji_parser.py',88),
  ('comando -> assignment SEMICOLON','comando',2,'p_comando','emoji_parser.py',89),
  ('comando -> if_statement','comando',1,'p_comando','emoji_parser.py',90),
  ('comando -> while_statement','comando',1,'p_comando','emoji_parser.py',91),
  ('comando -> for_statement','comando',1,'p_comando','emoji_parser.py',92),
  ('comando -> bloco','comando',1,'p_comando','emoji_parser.py',93),
  ('comando -> break_statement','comando',1,'p_comando','emoji_parser.py',94),
  ('comando -> continue_statement','comando',1,'p_comando','emoji_parser.py',95),
  ('comando -> return_statement','comando',1,'p_comando','emoji_parser.py',96),
  ('comando -> printf_statement','comando',1,'p_comando','emoji_parser.py',97),
  ('comando -> scanf_statement','comando',1,'p_comando','emoji_parser.py',98),
  ('comandos -> comando comandos','comandos',2,'p_comandos','emoji_parser.py',102),
  ('comandos -> comando','comandos',1,'p_comandos','emoji_parser.py',103),
  ('bloco -> LBRACE comandos RBRACE','bloco',3,'p_bloco','emoji_parser.py',110),
  ('bloco -> LBRACE RBRACE','bloco',2,'p_bloco','emoji_parser.py',111),
  ('parentheses -> LPAREN valor RPAREN','parentheses',3,'p_parentheses','emoji_parser.py',118),
  ('type -> INT','type',1,'p_type','emoji_parser.py',122),
  ('type -> FLOAT','type',1,'p_type','emoji_parser.py',123),
  ('type -> CHAR','type',1,'p_type','emoji_parser.py',124),
  ('type -> VOID','type',1,'p_type','emoji_parser.py',125),
  ('type -> BOOL','type',1,'p_type','emoji_parser.py',126),
  ('operador -> MULTIPLY','operador',1,'p_operador','emoji_parser.py',132),
  ('operador -> DIV','operador',1,'p_operador','emoji_parser.py',133),
  ('operador -> MOD','operador',1,'p_operador','emoji_parser.py',134),
  ('operador -> PLUS','operador',1,'p_operador','emoji_parser.py',135),
  ('operador -> MINUS','operador',1,'p_operador','emoji_parser.py',136),
  ('operador -> EQUAL','operador',1,'p_operador','emoji_parser.py',137),
  ('operador -> NEQUAL','operador',1,'p_operador','emoji_parser.py',138),
  ('operador -> GT','operador',1,'p_operador','emoji_parser.py',139),
  ('operador -> LT','operador',1,'p_operador','emoji_parser.py',140),
  ('operador -> GTE','operador',1,'p_operador','emoji_parser.py',141),
  ('operador -> LTE','operador',1,'p_operador','emoji_parser.py',142),
  ('operador -> AND','operador',1,'p_operador','emoji_parser.py',143),
  ('operador -> OR','operador',1,'p_operador','emoji_parser.py',144),
  ('boolean -> TRUE','boolean',1,'p_boolean','emoji_parser.py',149),
  ('boolean -> FALSE','boolean',1,'p_boolean','emoji_parser.py',150),
  ('valor -> NUMBER','valor',1,'p_valor','emoji_parser.py',154),
  ('valor -> NOME','valor',1,'p_valor','emoji_parser.py',155),
  ('valor -> CHARACTER','valor',1,'p_valor','emoji_parser.py',156),
  ('valor -> boolean','valor',1,'p_valor','emoji_parser.py',157),
  ('valor -> operation','valor',1,'p_valor','emoji_parser.py',158),
  ('valor -> parentheses','valor',1,'p_valor','emoji_parser.py',159),
  ('valor -> sinal valor','valor',2,'p_valor','emoji_parser.py',160),
  ('valores -> valor','valores',1,'p_valores','emoji_parser.py',164),
  ('valores -> valor COMMA valores','valores',3,'p_valores','emoji_parser.py',165),
  ('operation -> valor operador valor','operation',3,'p_operation','emoji_parser.py',173),
  ('assignment -> NOME ASSIGN valor','assignment',3,'p_assignment','emoji_parser.py',178),
  ('declaration_list -> NOME','declaration_list',1,'p_declaration_list','emoji_parser.py',182),
  ('declaration_list -> NOME declaration_list','declaration_list',2,'p_declaration_list','emoji_parser.py',183),
  ('declaration_list -> NOME ASSIGN valor','declaration_list',3,'p_declaration_list','emoji_parser.py',184),
  ('declaration_list -> NOME ASSIGN valor COMMA declaration_list','declaration_list',5,'p_declaration_list','emoji_parser.py',185),
  ('declaration -> type declaration_list SEMICOLON','declaration',3,'p_declaration','emoji_parser.py',222),
  ('if_statement -> IF LPAREN valor RPAREN bloco','if_statement',5,'p_if_statement','emoji_parser.py',226),
  ('while_statement -> WHILE LPAREN valor RPAREN bloco','while_statement',5,'p_while_statement','emoji_parser.py',230),
  ('for_statement -> FOR LPAREN for_init SEMICOLON for_condition SEMICOLON for_update RPAREN comando','for_statement',9,'p_for_statement','emoji_parser.py',234),
  ('for_init -> assignment','for_init',1,'p_for_init','emoji_parser.py',240),
  ('for_init -> declaration','for_init',1,'p_for_init','emoji_parser.py',241),
  ('for_init -> valor','for_init',1,'p_for_init','emoji_parser.py',242),
  ('for_init -> empty','for_init',1,'p_for_init','emoji_parser.py',243),
  ('for_init -> assignment for_comma','for_init',2,'p_for_init','emoji_parser.py',244),
  ('for_init -> valor for_comma','for_init',2,'p_for_init','emoji_parser.py',245),
  ('for_init -> declaration for_comma','for_init',2,'p_for_init','emoji_parser.py',246),
  ('for_comma -> COMMA assignment','for_comma',2,'p_for_comma','emoji_parser.py',254),
  ('for_comma -> COMMA valor SEMICOLON','for_comma',3,'p_for_comma','emoji_parser.py',255),
  ('for_comma -> COMMA assignment for_comma','for_comma',3,'p_for_comma','emoji_parser.py',256),
  ('for_condition -> assignment','for_condition',1,'p_for_condition','emoji_parser.py',263),
  ('for_condition -> valor','for_condition',1,'p_for_condition','emoji_parser.py',264),
  ('for_condition -> valor for_comma','for_condition',2,'p_for_condition','emoji_parser.py',265),
  ('for_condition -> assignment for_comma','for_condition',2,'p_for_condition','emoji_parser.py',266),
  ('for_condition -> empty','for_condition',1,'p_for_condition','emoji_parser.py',267),
  ('for_update -> assignment','for_update',1,'p_for_update','emoji_parser.py',274),
  ('for_update -> valor','for_update',1,'p_for_update','emoji_parser.py',275),
  ('for_update -> valor for_comma','for_update',2,'p_for_update','emoji_parser.py',276),
  ('for_update -> assignment for_comma','for_update',2,'p_for_update','emoji_parser.py',277),
  ('for_update -> empty','for_update',1,'p_for_update','emoji_parser.py',278),
  ('scanf_statement -> SCANF LPAREN CHARACTER COMMA NOME RPAREN SEMICOLON','scanf_statement',7,'p_scanf_statement','emoji_parser.py',286),
  ('printf_statement -> PRINTF LPAREN CHARACTER COMMA valores RPAREN SEMICOLON','printf_statement',7,'p_printf_statement','emoji_parser.py',291),
  ('printf_statement -> PRINTF LPAREN CHARACTER RPAREN SEMICOLON','printf_statement',5,'p_printf_statement','emoji_parser.py',292),
  ('break_statement -> BREAK SEMICOLON','break_statement',2,'p_break_statement','emoji_parser.py',300),
  ('continue_statement -> CONTINUE SEMICOLON','continue_statement',2,'p_continue_statement','emoji_parser.py',305),
  ('return_statement -> RETURN valor SEMICOLON','return_statement',3,'p_return_statement','emoji_parser.py',310),
  ('empty -> <empty>','empty',0,'p_empty','emoji_parser.py',314),
]
