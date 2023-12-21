# DefaultNumberQueueProcessor.ProcessAcquireAsync - метод
Функция, выполняющая обработку действия с номером
[Tessa.Cards.Numbers.NumberQueueActionTypes.Reserve] и возвращающая признак
того, что обработка выполнена удачно.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual Task<bool> ProcessAcquireAsync(
    	INumberContext context,
    	NumberQueue queue,
    	NumberQueueItem queueItem,
    	NumberQueueEventType queueEventType,
    	NumberQueueActionType queueActionType,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overridable Function ProcessAcquireAsync ( 
    	context As INumberContext,
    	queue As NumberQueue,
    	queueItem As NumberQueueItem,
    	queueEventType As NumberQueueEventType,
    	queueActionType As NumberQueueActionType,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
     protected:
    virtual Task<bool>^ ProcessAcquireAsync(
    	INumberContext^ context, 
    	NumberQueue^ queue, 
    	NumberQueueItem^ queueItem, 
    	NumberQueueEventType^ queueEventType, 
    	NumberQueueActionType^ queueActionType, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract ProcessAcquireAsync : 
            context : INumberContext * 
            queue : NumberQueue * 
            queueItem : NumberQueueItem * 
            queueEventType : NumberQueueEventType * 
            queueActionType : NumberQueueActionType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
    override ProcessAcquireAsync : 
            context : INumberContext * 
            queue : NumberQueue * 
            queueItem : NumberQueueItem * 
            queueEventType : NumberQueueEventType * 
            queueActionType : NumberQueueActionType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером.
queue [NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm)
    Очередь действий с номерами.
queueItem [NumberQueueItem](T_Tessa_Cards_Numbers_NumberQueueItem.htm)
    Информация по действию с номером.
queueEventType
[NumberQueueEventType](T_Tessa_Cards_Numbers_NumberQueueEventType.htm)
    Тип события по вызову действия.
queueActionType
[NumberQueueActionType](T_Tessa_Cards_Numbers_NumberQueueActionType.htm)
    Тип действия с номером в очереди.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если обработка действия с номером была выполнена удачно; false, если
обработка не была выполнена или была выполнена с ошибками.
## __См. также
#### Ссылки
[DefaultNumberQueueProcessor -
](T_Tessa_Cards_Numbers_DefaultNumberQueueProcessor.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
