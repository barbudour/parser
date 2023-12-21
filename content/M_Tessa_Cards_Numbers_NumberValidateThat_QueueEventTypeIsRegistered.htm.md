# NumberValidateThat.QueueEventTypeIsRegistered - метод
Возвращает признак того, что тип события
[NumberQueueEventType](T_Tessa_Cards_Numbers_NumberQueueEventType.htm) с
заданным идентификатором зарегистрирован в реестре типов, который используется
в стандартном API. Если параметр равен null, то возвращает true.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool QueueEventTypeIsRegistered(
    	Guid? typeID
    )
VB __Копировать
     Public Shared Function QueueEventTypeIsRegistered ( 
    	typeID As Guid?
    ) As Boolean
C++ __Копировать
     public:
    static bool QueueEventTypeIsRegistered(
    	Nullable<Guid> typeID
    )
F# __Копировать
     static member QueueEventTypeIsRegistered : 
            typeID : Nullable<Guid> -> bool 
#### Параметры
typeID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Идентификатор типа события [NumberQueueEventType](T_Tessa_Cards_Numbers_NumberQueueEventType.htm).
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Признак того, что тип события
[NumberQueueEventType](T_Tessa_Cards_Numbers_NumberQueueEventType.htm) с
заданным идентификатором зарегистрирован в реестре типов, который используется
в стандартном API.
## __См. также
#### Ссылки
[NumberValidateThat - ](T_Tessa_Cards_Numbers_NumberValidateThat.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
