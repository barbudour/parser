# NumberLocationType - конструктор
Создаёт тип местоположения номера с заданными идентификатором и именем.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public NumberLocationType(
    	Guid id,
    	string name,
    	bool hasInfo = false
    )
VB __Копировать
     Public Sub New ( 
    	id As Guid,
    	name As String,
    	Optional hasInfo As Boolean = false
    )
C++ __Копировать
     public:
    NumberLocationType(
    	Guid id, 
    	String^ name, 
    	bool hasInfo = false
    )
F# __Копировать
     new : 
            id : Guid * 
            name : string * 
            ?hasInfo : bool 
    (* Defaults:
            let _hasInfo = defaultArg hasInfo false
    *)
    -> NumberLocationType
#### Параметры
id [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор типа местоположения номера.
name [String](https://learn.microsoft.com/dotnet/api/system.string)
    Отображаемое имя типа местоположения номера.
hasInfo [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
Признак того, что местоположение является универсальным и определяется
настройками экземпляра местоположения
[INumberLocation](T_Tessa_Cards_Numbers_INumberLocation.htm).
Например, значение true возвращается для типа местоположения в карточке
[Card](F_Tessa_Cards_Numbers_NumberLocationTypes_Card.htm), т.к. оно может
быть связано с произвольным местом в карточке.
##  __См. также
#### Ссылки
[NumberLocationType - ](T_Tessa_Cards_Numbers_NumberLocationType.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
