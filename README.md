Letters = Dictionaire{<code>"Letter" : LetterNode</code>}

Connectors List(ConnectorNode)

Implication = List(Implication)

## LetterNode (Herite de Node)
| Name | Value |
|---|---|
|Name | Nom de la Letter|


## ConnectorNode (Herite de Node)
| Name | Value |
|---|---|
|type | Type doperateur|
|operand | LetterNode concernés|

## ImplicationNode (Herite de Node)
| Name | Value |
|---|---|
|left | ConnectorNode sinon LetterNode|
|right |ConnectorNode sinon LetterNode|