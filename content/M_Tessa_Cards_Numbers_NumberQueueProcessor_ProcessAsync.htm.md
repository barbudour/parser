# NumberQueueProcessor.ProcessAsync - метод
Выполняет действия из заданной очереди [Tessa.Cards.Numbers.NumberQueue].
Возвращает признак того, что во всех выполненных действиях отсутствуют ошибки.
Действия, которые были успешно выполнены, удаляются из очереди.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<bool> ProcessAsync(
    	INumberContext context,
    	NumberQueue queue,
    	CancellationToken cancellationToken = default,
    	params NumberQueueEventType[] queueEventTypes
    )
VB __Копировать
     Public Function ProcessAsync ( 
    	context As INumberContext,
    	queue As NumberQueue,
    	Optional cancellationToken As CancellationToken = Nothing,
    	ParamArray queueEventTypes As NumberQueueEventType()
    ) As Task(Of Boolean)
C++ __Копировать
     public:
    virtual Task<bool>^ ProcessAsync(
    	INumberContext^ context, 
    	NumberQueue^ queue, 
    	CancellationToken cancellationToken = CancellationToken(), 
    	... array<NumberQueueEventType^>^ queueEventTypes
    ) sealed
F# __Копировать
     abstract ProcessAsync : 
            context : INumberContext * 
            queue : NumberQueue * 
            ?cancellationToken : CancellationToken * 
            queueEventTypes : NumberQueueEventType[] 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
    override ProcessAsync : 
            context : INumberContext * 
            queue : NumberQueue * 
            ?cancellationToken : CancellationToken * 
            queueEventTypes : NumberQueueEventType[] 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером.
queue [NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm)
    Очередь действий с номерами.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
queueEventTypes
[NumberQueueEventType](T_Tessa_Cards_Numbers_NumberQueueEventType.htm)[]
     Типы обрабатываемых событий по вызову действий в очереди. Используйте null или пустой массив, чтобы обрабатывать все события. 
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если обработаны все действия в очереди для подходящих событий; false,
если хотя бы одно действие не было обработано, потому что обработчик
неизвестен или потому что при обработке возникли ошибки, которые сохранены в
заданном контексте действия context.
#### Реализации
[INumberQueueProcessor.ProcessAsync(INumberContext, NumberQueue,
CancellationToken,
NumberQueueEventType[])](M_Tessa_Cards_Numbers_INumberQueueProcessor_ProcessAsync.htm)  
##  __См. также
#### Ссылки
[NumberQueueProcessor - ](T_Tessa_Cards_Numbers_NumberQueueProcessor.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
