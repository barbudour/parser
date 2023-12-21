# DefaultNumberQueueProcessor.CanProcessAlwaysAsync - метод
Функция, возвращающая признак того, что обработка действия с номером разрешена
для предиката [Tessa.Cards.Numbers.NumberQueuePredicateTypes.Always].
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual Task<bool> CanProcessAlwaysAsync(
    	INumberObject number,
    	INumberContext context,
    	NumberQueue queue,
    	NumberQueueItem queueItem,
    	NumberQueueActionType queueActionType,
    	NumberQueuePredicateType queuePredicateType,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overridable Function CanProcessAlwaysAsync ( 
    	number As INumberObject,
    	context As INumberContext,
    	queue As NumberQueue,
    	queueItem As NumberQueueItem,
    	queueActionType As NumberQueueActionType,
    	queuePredicateType As NumberQueuePredicateType,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
     protected:
    virtual Task<bool>^ CanProcessAlwaysAsync(
    	INumberObject^ number, 
    	INumberContext^ context, 
    	NumberQueue^ queue, 
    	NumberQueueItem^ queueItem, 
    	NumberQueueActionType^ queueActionType, 
    	NumberQueuePredicateType^ queuePredicateType, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract CanProcessAlwaysAsync : 
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
    override CanProcessAlwaysAsync : 
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
[DefaultNumberQueueProcessor -
](T_Tessa_Cards_Numbers_DefaultNumberQueueProcessor.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
