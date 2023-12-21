# NumberQueueProcessor.TryGetProcessFuncAsync - метод
Возвращает функцию, выполняющую обработку действия с номером в очереди, или
null, если такая функция неизвестна.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual NumberQueueProcessFuncAsync TryGetProcessFuncAsync(
    	NumberQueueActionType queueActionType,
    	INumberContext context,
    	NumberQueue queue,
    	NumberQueueItem queueItem,
    	NumberQueueEventType queueEventType
    )
VB __Копировать
     Protected Overridable Function TryGetProcessFuncAsync ( 
    	queueActionType As NumberQueueActionType,
    	context As INumberContext,
    	queue As NumberQueue,
    	queueItem As NumberQueueItem,
    	queueEventType As NumberQueueEventType
    ) As NumberQueueProcessFuncAsync
C++ __Копировать
     protected:
    virtual NumberQueueProcessFuncAsync^ TryGetProcessFuncAsync(
    	NumberQueueActionType^ queueActionType, 
    	INumberContext^ context, 
    	NumberQueue^ queue, 
    	NumberQueueItem^ queueItem, 
    	NumberQueueEventType^ queueEventType
    )
F# __Копировать
     abstract TryGetProcessFuncAsync : 
            queueActionType : NumberQueueActionType * 
            context : INumberContext * 
            queue : NumberQueue * 
            queueItem : NumberQueueItem * 
            queueEventType : NumberQueueEventType -> NumberQueueProcessFuncAsync 
    override TryGetProcessFuncAsync : 
            queueActionType : NumberQueueActionType * 
            context : INumberContext * 
            queue : NumberQueue * 
            queueItem : NumberQueueItem * 
            queueEventType : NumberQueueEventType -> NumberQueueProcessFuncAsync 
#### Параметры
queueActionType
[NumberQueueActionType](T_Tessa_Cards_Numbers_NumberQueueActionType.htm)
    Тип действия с номером в очереди.
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером.
queue [NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm)
    Очередь действий с номерами.
queueItem [NumberQueueItem](T_Tessa_Cards_Numbers_NumberQueueItem.htm)
    Информация по действию с номером в очереди.
queueEventType
[NumberQueueEventType](T_Tessa_Cards_Numbers_NumberQueueEventType.htm)
    Тип события по вызову действия.
#### Возвращаемое значение
[NumberQueueProcessFuncAsync](T_Tessa_Cards_Numbers_NumberQueueProcessFuncAsync.htm)  
Функция, выполняющая обработку действия с номером в очереди, или null, если
такая функция неизвестна.
## __См. также
#### Ссылки
[NumberQueueProcessor - ](T_Tessa_Cards_Numbers_NumberQueueProcessor.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
