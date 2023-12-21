# CardRow.SetChanged - метод
Устанавливает признак isChanged, определяющий, было ли изменено значение
объекта с ключом key.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardRow SetChanged(
    	string key,
    	bool isChanged = true
    )
VB __Копировать
     Public Function SetChanged ( 
    	key As String,
    	Optional isChanged As Boolean = true
    ) As CardRow
C++ __Копировать
     public:
    CardRow^ SetChanged(
    	String^ key, 
    	bool isChanged = true
    )
F# __Копировать
     member SetChanged : 
            key : string * 
            ?isChanged : bool 
    (* Defaults:
            let _isChanged = defaultArg isChanged true
    *)
    -> CardRow 
#### Параметры
key [String](https://learn.microsoft.com/dotnet/api/system.string)
    Ключ, по которому необходимо установить признак наличия изменений в значении объекта.
isChanged [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
Устанавливаемый признак наличия изменений в значении объекта с заданным
ключом.
Равен true, если значение объекта считается изменённым, или false, если
значение объекта считается неизменным.
#### Возвращаемое значение
[CardRow](T_Tessa_Cards_CardRow.htm)  
Текущий объект для цепочки вызовов.
##  __См. также
#### Ссылки
[CardRow - ](T_Tessa_Cards_CardRow.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
