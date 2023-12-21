# NumberBuilder.TryGetNumberQueueAsync - метод
Возвращает очередь действий с номерами для заданного контекста или null, если
очередь недоступна.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<NumberQueue> TryGetNumberQueueAsync(
    	INumberContext context,
    	bool createIfNotExists = false,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function TryGetNumberQueueAsync ( 
    	context As INumberContext,
    	Optional createIfNotExists As Boolean = false,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of NumberQueue)
C++ __Копировать
     public:
    virtual ValueTask<NumberQueue^> TryGetNumberQueueAsync(
    	INumberContext^ context, 
    	bool createIfNotExists = false, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract TryGetNumberQueueAsync : 
            context : INumberContext * 
            ?createIfNotExists : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _createIfNotExists = defaultArg createIfNotExists false
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<NumberQueue> 
    override TryGetNumberQueueAsync : 
            context : INumberContext * 
            ?createIfNotExists : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _createIfNotExists = defaultArg createIfNotExists false
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<NumberQueue> 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
     Контекст события, происходящего с номером, для которого возвращается очередь. 
createIfNotExists
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     Признак того, что если очередь допустима для карточки, но ещё не создана, то следует создать и вернуть пустую очередь, чтобы в неё можно было добавить действия. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm)>  
Очередь действий с номерами для заданного контекста или null, если очередь
недоступна.
#### Реализации
[INumberQueueContainer.TryGetNumberQueueAsync(INumberContext, Boolean,
CancellationToken)](M_Tessa_Cards_Numbers_INumberQueueContainer_TryGetNumberQueueAsync.htm)  
##  __См. также
#### Ссылки
[NumberBuilder - ](T_Tessa_Cards_Numbers_NumberBuilder.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
