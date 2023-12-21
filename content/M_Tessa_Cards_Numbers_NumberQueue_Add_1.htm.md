# NumberQueue.Add(NumberQueueActionType, NumberQueueEventType,
NumberEventType, NumberTypeDescriptor, NumberQueuePredicateType, Boolean,
INumberLocation, INumberLocation) - метод
Добавляет запись в очередь, которая описывает действие с типом номера.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public NumberQueueItem Add(
    	NumberQueueActionType queueActionType,
    	NumberQueueEventType queueEventType,
    	NumberEventType eventType,
    	NumberTypeDescriptor numberType,
    	NumberQueuePredicateType predicateType = null,
    	bool predicateExpectedValue = true,
    	INumberLocation sourceLocation = null,
    	INumberLocation targetLocation = null
    )
VB __Копировать
     Public Function Add ( 
    	queueActionType As NumberQueueActionType,
    	queueEventType As NumberQueueEventType,
    	eventType As NumberEventType,
    	numberType As NumberTypeDescriptor,
    	Optional predicateType As NumberQueuePredicateType = Nothing,
    	Optional predicateExpectedValue As Boolean = true,
    	Optional sourceLocation As INumberLocation = Nothing,
    	Optional targetLocation As INumberLocation = Nothing
    ) As NumberQueueItem
C++ __Копировать
     public:
    NumberQueueItem^ Add(
    	NumberQueueActionType^ queueActionType, 
    	NumberQueueEventType^ queueEventType, 
    	NumberEventType^ eventType, 
    	NumberTypeDescriptor^ numberType, 
    	NumberQueuePredicateType^ predicateType = nullptr, 
    	bool predicateExpectedValue = true, 
    	INumberLocation^ sourceLocation = nullptr, 
    	INumberLocation^ targetLocation = nullptr
    )
F# __Копировать
     member Add : 
            queueActionType : NumberQueueActionType * 
            queueEventType : NumberQueueEventType * 
            eventType : NumberEventType * 
            numberType : NumberTypeDescriptor * 
            ?predicateType : NumberQueuePredicateType * 
            ?predicateExpectedValue : bool * 
            ?sourceLocation : INumberLocation * 
            ?targetLocation : INumberLocation 
    (* Defaults:
            let _predicateType = defaultArg predicateType null
            let _predicateExpectedValue = defaultArg predicateExpectedValue true
            let _sourceLocation = defaultArg sourceLocation null
            let _targetLocation = defaultArg targetLocation null
    *)
    -> NumberQueueItem 
#### Параметры
queueActionType
[NumberQueueActionType](T_Tessa_Cards_Numbers_NumberQueueActionType.htm)
     Тип события, происходящего с номером, в очереди. Не может быть равен null. 
queueEventType
[NumberQueueEventType](T_Tessa_Cards_Numbers_NumberQueueEventType.htm)
     Тип события по вызову действия с номером, определяет момент времени, в который выполяется действие. Не может быть равен null. 
eventType [NumberEventType](T_Tessa_Cards_Numbers_NumberEventType.htm)
     Тип события, происходящего с номером, в результате которого запись добавлена в очередь. Не может быть равен null. 
numberType
[NumberTypeDescriptor](T_Tessa_Cards_Numbers_NumberTypeDescriptor.htm)
     Тип номера, с которым выполняется действие. Не может быть равен null. 
predicateType
[NumberQueuePredicateType](T_Tessa_Cards_Numbers_NumberQueuePredicateType.htm)
(Optional)
     Тип предиката, который определяет возможность выполнения действия, или null, если действие выполняется всегда, независимо от предиката. 
predicateExpectedValue
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     Ожидаемое значение, которое возвращает предикат. Действие будет выполнено только в том случае, если значение, возвращённое предикатом, и значение этого свойства совпадут. 
sourceLocation [INumberLocation](T_Tessa_Cards_Numbers_INumberLocation.htm)
(Optional)
     Информация по местоположению номера в карточке, по которому номер следует получить для выполнения действия, или null, если используется пустой номер заданного типа numberType. 
targetLocation [INumberLocation](T_Tessa_Cards_Numbers_INumberLocation.htm)
(Optional)
     Информация по местоположению номера в карточке, по которому номер следует сохранить после выполнения действия, или null, если местоположение не указывается. 
#### Возвращаемое значение
[NumberQueueItem](T_Tessa_Cards_Numbers_NumberQueueItem.htm)  
Добавленная в очередь запись.
##  __См. также
#### Ссылки
[NumberQueue - ](T_Tessa_Cards_Numbers_NumberQueue.htm)
[Add - перегрузка](Overload_Tessa_Cards_Numbers_NumberQueue_Add.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
