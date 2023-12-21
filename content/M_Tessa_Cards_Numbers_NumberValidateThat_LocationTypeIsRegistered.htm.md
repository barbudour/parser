# NumberValidateThat.LocationTypeIsRegistered - метод
Возвращает признак того, что тип местоположения номера
[NumberLocationType](T_Tessa_Cards_Numbers_NumberLocationType.htm) с заданным
идентификатором зарегистрирован в реестре типов, который используется в
стандартном API. Если параметр равен null, то возвращает true.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool LocationTypeIsRegistered(
    	Guid? typeID
    )
VB __Копировать
     Public Shared Function LocationTypeIsRegistered ( 
    	typeID As Guid?
    ) As Boolean
C++ __Копировать
     public:
    static bool LocationTypeIsRegistered(
    	Nullable<Guid> typeID
    )
F# __Копировать
     static member LocationTypeIsRegistered : 
            typeID : Nullable<Guid> -> bool 
#### Параметры
typeID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Идентификатор типа местоположения номера [NumberLocationType](T_Tessa_Cards_Numbers_NumberLocationType.htm).
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Признак того, что тип местоположения номера
[NumberLocationType](T_Tessa_Cards_Numbers_NumberLocationType.htm) с заданным
идентификатором зарегистрирован в реестре типов, который используется в
стандартном API.
## __См. также
#### Ссылки
[NumberValidateThat - ](T_Tessa_Cards_Numbers_NumberValidateThat.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
