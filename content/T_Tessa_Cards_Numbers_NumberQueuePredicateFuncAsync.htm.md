# NumberQueuePredicateFuncAsync - делегат
Функция, возвращающая признак того, что обработка действия с номером в очереди
[NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm) разрешена.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate Task<bool> NumberQueuePredicateFuncAsync(
    	INumberObject number,
    	INumberContext context,
    	NumberQueue queue,
    	NumberQueueItem queueItem,
    	NumberQueueActionType queueActionType,
    	NumberQueuePredicateType queuePredicateType,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Delegate Function NumberQueuePredicateFuncAsync ( 
    	number As INumberObject,
    	context As INumberContext,
    	queue As NumberQueue,
    	queueItem As NumberQueueItem,
    	queueActionType As NumberQueueActionType,
    	queuePredicateType As NumberQueuePredicateType,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
     public delegate Task<bool>^ NumberQueuePredicateFuncAsync(
    	INumberObject^ number, 
    	INumberContext^ context, 
    	NumberQueue^ queue, 
    	NumberQueueItem^ queueItem, 
    	NumberQueueActionType^ queueActionType, 
    	NumberQueuePredicateType^ queuePredicateType, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     type NumberQueuePredicateFuncAsync = 
        delegate of 
            number : INumberObject * 
            context : INumberContext * 
            queue : NumberQueue * 
            queueItem : NumberQueueItem * 
            queueActionType : NumberQueueActionType * 
            queuePredicateType : NumberQueuePredicateType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool>
#### Параметры
number [INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm)
    Номер, для которого должно быть выполнено действие.
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером.
queue [NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm)
    Очередь действий с номерами.
queueItem [NumberQueueItem](T_Tessa_Cards_Numbers_NumberQueueItem.htm)
    Информация по действию с номером.
queueActionType
[NumberQueueActionType](T_Tessa_Cards_Numbers_NumberQueueActionType.htm)
    Тип действия с номером в очереди.
queuePredicateType
[NumberQueuePredicateType](T_Tessa_Cards_Numbers_NumberQueuePredicateType.htm)
    Тип предиката.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если обработка действия с номером разрешена; false, если обработка
действия с номером запрещена.
## __См. также
#### Ссылки
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
