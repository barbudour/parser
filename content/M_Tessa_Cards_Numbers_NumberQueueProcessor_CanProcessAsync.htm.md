# NumberQueueProcessor.CanProcessAsync - метод
Возвращает признак того, что предикат queuePredicateType по действию с номером
number разрешает выполнить это действие. Возвращает null, если для заданного
типа предиката получить действие не удалось.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual Task<bool?> CanProcessAsync(
    	INumberObject number,
    	INumberContext context,
    	NumberQueue queue,
    	NumberQueueItem queueItem,
    	NumberQueueActionType queueActionType,
    	NumberQueuePredicateType queuePredicateType,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overridable Function CanProcessAsync ( 
    	number As INumberObject,
    	context As INumberContext,
    	queue As NumberQueue,
    	queueItem As NumberQueueItem,
    	queueActionType As NumberQueueActionType,
    	queuePredicateType As NumberQueuePredicateType,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean?)
C++ __Копировать
     protected:
    virtual Task<Nullable<bool>>^ CanProcessAsync(
    	INumberObject^ number, 
    	INumberContext^ context, 
    	NumberQueue^ queue, 
    	NumberQueueItem^ queueItem, 
    	NumberQueueActionType^ queueActionType, 
    	NumberQueuePredicateType^ queuePredicateType, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract CanProcessAsync : 
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
    -> Task<Nullable<bool>> 
    override CanProcessAsync : 
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
    -> Task<Nullable<bool>> 
#### Параметры
number [INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm)
     Номер, действие с которым выполняется. Может быть пустым номером, если для действия актуален только тип. 
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст, в котором выполняется действие с номером.
queue [NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm)
    Очередь действий с номерами.
queueItem [NumberQueueItem](T_Tessa_Cards_Numbers_NumberQueueItem.htm)
    Информация по действию с номером.
queueActionType
[NumberQueueActionType](T_Tessa_Cards_Numbers_NumberQueueActionType.htm)
    Тип действия с номером в очереди.
queuePredicateType
[NumberQueuePredicateType](T_Tessa_Cards_Numbers_NumberQueuePredicateType.htm)
    Тип обрабатываемого предиката.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>>  
true, если можно продолжить выполнение действия; false, если выполнение
действия с таким номером запрещено; null, если получить действие не удалось.
## __См. также
#### Ссылки
[NumberQueueProcessor - ](T_Tessa_Cards_Numbers_NumberQueueProcessor.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
