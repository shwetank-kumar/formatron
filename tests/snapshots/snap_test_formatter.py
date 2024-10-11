# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_formatter 1'] = '''__choice_0_0_food ::= 'railroad' | 'orange' | 'banana';
__regex_1_0 ::= #'[0-9]+';
__regex_2_0 ::= #'[a-z]+';
__choice_3_0_ID ::= __regex_1_0 | __regex_2_0;
integer ::= #"-?(0|[1-9][0-9]*)";
number ::= #"-?(0|[1-9][0-9]*)(\\\\.[0-9]+)?([eE][+-]?[0-9]+)?";
string ::= #\'"([^\\\\\\\\"\\u0000-\\u001f]|\\\\\\\\["\\\\\\\\bfnrt/]|\\\\\\\\u[0-9A-Fa-f]{4})*"\';
boolean ::= "true"|"false";
null ::= "null";
array ::= array_begin (json_value (comma json_value)*)? array_end;
object ::= object_begin (string colon json_value (comma string colon json_value)*)? object_end;
json_value ::= number|string|boolean|null|array|object;
comma ::= #"[ \t
\r]*,[ \t
\r]*";
colon ::= #"[ \t
\r]*:[ \t
\r]*";
object_begin ::= #"\\\\{[ \t
\r]*";
object_end ::= #"[ \t
\r]*\\\\}";
array_begin ::= #"\\\\[[ \t
\r]*";
array_end ::= #"[ \t
\r]*\\\\]";
__json_4_0_json ::= object_begin \'"name"\' colon __json_4_0_json_name comma \'"weight"\' colon __json_4_0_json_weight comma \'"color"\' colon __json_4_0_json_color object_end;
__json_4_0_json_color ::= string;
__json_4_0_json_weight ::= number;
__json_4_0_json_name ::= string;

start ::= \'Today, I want to eat \' __choice_0_0_food \'\\n\' "My food\'s ID is " __choice_3_0_ID \'.\\n\' "\\nWhat\'s more, indentations\\nare handled\\nappropriately." \'My weight is 14.4kg and my color is pink. This is my personal info json: \' __json_4_0_json \'\\n\';'''

snapshots['test_formatter 2'] = '''Today, I want to eat banana
My food's ID is not.

What's more, indentations
are handled
appropriately.My weight is 14.4kg and my color is pink. This is my personal info json: {"name":"Van","weight":1.4,"color":"pink"}
'''

snapshots['test_formatter 3'] = {
    'ID': GenericRepr("<re.Match object; span=(0, 3), match='not'>"),
    'food': 'banana',
    'json': GenericRepr("Test(name='Van', weight=1.4, color='pink')")
}

snapshots['test_formatter_alternate_accept 1'] = {
    'age': GenericRepr("<re.Match object; span=(0, 2), match='30'>"),
    'name': GenericRepr("<re.Match object; span=(0, 5), match='John,'>")
}

snapshots['test_formatter_callable_schema 1'] = '''integer ::= #"-?(0|[1-9][0-9]*)";
number ::= #"-?(0|[1-9][0-9]*)(\\\\.[0-9]+)?([eE][+-]?[0-9]+)?";
string ::= #\'"([^\\\\\\\\"\\u0000-\\u001f]|\\\\\\\\["\\\\\\\\bfnrt/]|\\\\\\\\u[0-9A-Fa-f]{4})*"\';
boolean ::= "true"|"false";
null ::= "null";
array ::= array_begin (json_value (comma json_value)*)? array_end;
object ::= object_begin (string colon json_value (comma string colon json_value)*)? object_end;
json_value ::= number|string|boolean|null|array|object;
comma ::= #"[ \t
\r]*,[ \t
\r]*";
colon ::= #"[ \t
\r]*:[ \t
\r]*";
object_begin ::= #"\\\\{[ \t
\r]*";
object_end ::= #"[ \t
\r]*\\\\}";
array_begin ::= #"\\\\[[ \t
\r]*";
array_end ::= #"[ \t
\r]*\\\\]";
__json_0_0_json ::= object_begin \'"a"\' colon __json_0_0_json_a comma \'"b"\' colon __json_0_0_json_b comma \'"c"\' colon __json_0_0_json_c object_end;
__json_0_0_json_c ::= integer;
__json_0_0_json_b ::= integer;
__json_0_0_json_a ::= integer;

start ::= __json_0_0_json '\\n';'''

snapshots['test_formatter_callable_schema 2'] = '''{"a":1,"b":2,"c":3}
'''

snapshots['test_formatter_callable_schema 3'] = {
    'json': 6
}

snapshots['test_formatter_dict_inference 1'] = '''integer ::= #"-?(0|[1-9][0-9]*)";
number ::= #"-?(0|[1-9][0-9]*)(\\\\.[0-9]+)?([eE][+-]?[0-9]+)?";
string ::= #\'"([^\\\\\\\\"\\u0000-\\u001f]|\\\\\\\\["\\\\\\\\bfnrt/]|\\\\\\\\u[0-9A-Fa-f]{4})*"\';
boolean ::= "true"|"false";
null ::= "null";
array ::= array_begin (json_value (comma json_value)*)? array_end;
object ::= object_begin (string colon json_value (comma string colon json_value)*)? object_end;
json_value ::= number|string|boolean|null|array|object;
comma ::= #"[ \t
\r]*,[ \t
\r]*";
colon ::= #"[ \t
\r]*:[ \t
\r]*";
object_begin ::= #"\\\\{[ \t
\r]*";
object_end ::= #"[ \t
\r]*\\\\}";
array_begin ::= #"\\\\[[ \t
\r]*";
array_end ::= #"[ \t
\r]*\\\\]";
__json_0_0_json ::= object_begin \'"name"\' colon __json_0_0_json_name comma \'"gender"\' colon __json_0_0_json_gender object_end;
__json_0_0_json_gender ::= string;
__json_0_0_json_name ::= string;

start ::= __json_0_0_json '\\n';'''

snapshots['test_formatter_dict_inference 2'] = '''{"name":"MyName","gender":"male"}
'''

snapshots['test_formatter_dict_inference 3'] = {
    'json': {
        'gender': 'male',
        'name': 'MyName'
    }
}

snapshots['test_formatter_json_schema 1'] = '''{"name":"peter","age":30}
'''

snapshots['test_formatter_json_schema 2'] = {
    'json': {
        'age': 30,
        'name': 'peter'
    }
}

snapshots['test_formatter_json_schema 3'] = '''integer ::= #"-?(0|[1-9][0-9]*)";
number ::= #"-?(0|[1-9][0-9]*)(\\\\.[0-9]+)?([eE][+-]?[0-9]+)?";
string ::= #\'"([^\\\\\\\\"\\u0000-\\u001f]|\\\\\\\\["\\\\\\\\bfnrt/]|\\\\\\\\u[0-9A-Fa-f]{4})*"\';
boolean ::= "true"|"false";
null ::= "null";
array ::= array_begin (json_value (comma json_value)*)? array_end;
object ::= object_begin (string colon json_value (comma string colon json_value)*)? object_end;
json_value ::= number|string|boolean|null|array|object;
comma ::= #"[ \t
\r]*,[ \t
\r]*";
colon ::= #"[ \t
\r]*:[ \t
\r]*";
object_begin ::= #"\\\\{[ \t
\r]*";
object_end ::= #"[ \t
\r]*\\\\}";
array_begin ::= #"\\\\[[ \t
\r]*";
array_end ::= #"[ \t
\r]*\\\\]";
__json_0_0_json ::= object_begin \'"name"\' colon __json_0_0_json_name comma \'"age"\' colon __json_0_0_json_age object_end;
__json_0_0_json_age ::= integer;
__json_0_0_json_name ::= string;

start ::= __json_0_0_json '\\n';'''

snapshots['test_formatter_str 1'] = '''__str_0_0 ::= #'.*?(?:\\\\.)';
start ::= __str_0_0 '\\n';'''

snapshots['test_formatter_str 2'] = '˝ she said. "I\'m from the International Union of Mine, Metal and Air-craft Workers. I\'m here to ask you for a place to stay for a while. I can\'t pay you, but I\'ll pay you back in installments. You\'ll be living with me and my family." I was about to protest, but she had already pulled out a business card. "I\'m sorry, but you have to come with me. My name is Angela, and I\'ll be your maid." She handed me the card and I thanked her. I walked over to her car and got in. She drove off. I looked at the address on the card. It was a town called Pleasant Valley. I knew that the building was the old prison camp. I wondered what happened to them all. The rest of the day was spent driving around looking for any sign of the men who were imprisoned there. After what seemed like an eternity, we arrived at the old prison camp. It was a long walk to the prison itself, but it was worth it. I looked around and saw that it was a very beautiful place. There were many trees and flowers everywhere. I looked around for a sign of the guards, but they weren\'t there. I started'

snapshots['test_formatter_str 3'] = {
}

snapshots['test_formatter_substr 1'] = '''__substr_0_0_substr ::= #substrs'Name: Umbrella; Price: 114.514 dollars;';
start ::= __substr_0_0_substr '<eos>';'''

snapshots['test_formatter_substr 2'] = ' 114.514 dollars;<eos>'

snapshots['test_formatter_substr 3'] = {
    'substr': ' 114.514 dollars;'
}

snapshots['test_formatter_top_level_array_json_schema 1'] = '''integer ::= #"-?(0|[1-9][0-9]*)";
number ::= #"-?(0|[1-9][0-9]*)(\\\\.[0-9]+)?([eE][+-]?[0-9]+)?";
string ::= #\'"([^\\\\\\\\"\\u0000-\\u001f]|\\\\\\\\["\\\\\\\\bfnrt/]|\\\\\\\\u[0-9A-Fa-f]{4})*"\';
boolean ::= "true"|"false";
null ::= "null";
array ::= array_begin (json_value (comma json_value)*)? array_end;
object ::= object_begin (string colon json_value (comma string colon json_value)*)? object_end;
json_value ::= number|string|boolean|null|array|object;
comma ::= #"[ \t
\r]*,[ \t
\r]*";
colon ::= #"[ \t
\r]*:[ \t
\r]*";
object_begin ::= #"\\\\{[ \t
\r]*";
object_end ::= #"[ \t
\r]*\\\\}";
array_begin ::= #"\\\\[[ \t
\r]*";
array_end ::= #"[ \t
\r]*\\\\]";
__json_0_0_json ::= array_begin (__json_0_0_json_value (comma __json_0_0_json_value)*)? array_end;
__json_0_0_json_value ::= object_begin \'"id"\' colon __json_0_0_json_value_id comma \'"name"\' colon __json_0_0_json_value_name comma \'"active"\' colon __json_0_0_json_value_active object_end;
__json_0_0_json_value_active ::= __json_0_0_json_value_active_required?;
__json_0_0_json_value_active_required ::= boolean;
__json_0_0_json_value_name ::= string;
__json_0_0_json_value_id ::= integer;

start ::= __json_0_0_json '\\n';'''

snapshots['test_formatter_top_level_array_json_schema 2'] = '''[{"id": 1, "name": "John", "active": true}, {"id": 2, "name": "Bob", "active": true}, {"id": 3, "name": "Charlie", "active": true}]
'''

snapshots['test_formatter_top_level_array_json_schema 3'] = {
    'json': [
        {
            'active': True,
            'id': 1,
            'name': 'John'
        },
        {
            'active': True,
            'id': 2,
            'name': 'Bob'
        },
        {
            'active': True,
            'id': 3,
            'name': 'Charlie'
        }
    ]
}

snapshots['test_grammar_literal 1'] = '''integer ::= #"-?(0|[1-9][0-9]*)";
number ::= #"-?(0|[1-9][0-9]*)(\\\\.[0-9]+)?([eE][+-]?[0-9]+)?";
string ::= #\'"([^\\\\\\\\"\\u0000-\\u001f]|\\\\\\\\["\\\\\\\\bfnrt/]|\\\\\\\\u[0-9A-Fa-f]{4})*"\';
boolean ::= "true"|"false";
null ::= "null";
array ::= array_begin (json_value (comma json_value)*)? array_end;
object ::= object_begin (string colon json_value (comma string colon json_value)*)? object_end;
json_value ::= number|string|boolean|null|array|object;
comma ::= #"[ \t
\r]*,[ \t
\r]*";
colon ::= #"[ \t
\r]*:[ \t
\r]*";
object_begin ::= #"\\\\{[ \t
\r]*";
object_end ::= #"[ \t
\r]*\\\\}";
array_begin ::= #"\\\\[[ \t
\r]*";
array_end ::= #"[ \t
\r]*\\\\]";
__json_0_0_json ::= object_begin \'"a"\' colon __json_0_0_json_a object_end;
__json_0_0_json_a ::= "\\"114\\"" | "\\"514\\"";

start ::= __json_0_0_json '\\n';'''

snapshots['test_grammar_literal 2'] = '''{"a":"114"}
'''

snapshots['test_grammar_literal 3'] = {
    'json': GenericRepr("A(a='114')")
}
