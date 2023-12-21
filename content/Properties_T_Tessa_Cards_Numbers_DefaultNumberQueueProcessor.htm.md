# DefaultNumberQueueProcessor - свойства
##  __Свойства
[PredicateByType](P_Tessa_Cards_Numbers_NumberQueueProcessor_PredicateByType.htm)|
Хеш-таблица, задающая отношение между типом предиката
[NumberQueuePredicateType](T_Tessa_Cards_Numbers_NumberQueuePredicateType.htm)
и функцией, обрабатывающей предикат
[NumberQueuePredicateFuncAsync](T_Tessa_Cards_Numbers_NumberQueuePredicateFuncAsync.htm).
Используется в реализации [CanProcessAsync(INumberObject, INumberContext,
NumberQueue, NumberQueueItem, NumberQueueActionType, NumberQueuePredicateType,
CancellationToken)](M_Tessa_Cards_Numbers_NumberQueueProcessor_CanProcessAsync.htm)
по умолчанию.  
(Унаследован от
[NumberQueueProcessor](T_Tessa_Cards_Numbers_NumberQueueProcessor.htm))  
---|---  
[ProcessFuncByActionType](P_Tessa_Cards_Numbers_NumberQueueProcessor_ProcessFuncByActionType.htm)|
Хеш-таблица, задающая отношение между типом действия в очереди
[NumberQueueActionType](T_Tessa_Cards_Numbers_NumberQueueActionType.htm) и
функцией, обрабатывающей действие
[NumberQueueProcessFuncAsync](T_Tessa_Cards_Numbers_NumberQueueProcessFuncAsync.htm).
Используется в реализации [TryGetProcessFuncAsync(NumberQueueActionType,
INumberContext, NumberQueue, NumberQueueItem,
NumberQueueEventType)](M_Tessa_Cards_Numbers_NumberQueueProcessor_TryGetProcessFuncAsync.htm)
по умолчанию.  
(Унаследован от
[NumberQueueProcessor](T_Tessa_Cards_Numbers_NumberQueueProcessor.htm))  
##  __См. также
#### Ссылки
[DefaultNumberQueueProcessor -
](T_Tessa_Cards_Numbers_DefaultNumberQueueProcessor.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
