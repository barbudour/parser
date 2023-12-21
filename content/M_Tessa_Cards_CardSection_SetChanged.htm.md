# CardSection.SetChanged - метод
Устанавливает признак isChanged, определяющий, было ли изменено значение
объекта с ключом key.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardSection SetChanged(
    	string key,
    	bool isChanged = true
    )
VB __Копировать
     Public Function SetChanged ( 
    	key As String,
    	Optional isChanged As Boolean = true
    ) As CardSection
C++ __Копировать
     public:
    CardSection^ SetChanged(
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
    -> CardSection 
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
[CardSection](T_Tessa_Cards_CardSection.htm)  
Текущий объект для цепочки вызовов.
##  __Исключения
[InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception)|
Тип секции [Type](P_Tessa_Cards_CardSection_Type.htm) не равен
[Entry](T_Tessa_Cards_CardSectionType.htm). Метод доступен только для
строковых секций.  
---|---  
## __См. также
#### Ссылки
[CardSection - ](T_Tessa_Cards_CardSection.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
