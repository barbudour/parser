# NumberQueueProcessor.ProcessFuncByActionType - свойство
Хеш-таблица, задающая отношение между типом действия в очереди
[NumberQueueActionType](T_Tessa_Cards_Numbers_NumberQueueActionType.htm) и
функцией, обрабатывающей действие
[NumberQueueProcessFuncAsync](T_Tessa_Cards_Numbers_NumberQueueProcessFuncAsync.htm).
Используется в реализации [TryGetProcessFuncAsync(NumberQueueActionType,
INumberContext, NumberQueue, NumberQueueItem,
NumberQueueEventType)](M_Tessa_Cards_Numbers_NumberQueueProcessor_TryGetProcessFuncAsync.htm)
по умолчанию.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected Dictionary<NumberQueueActionType, NumberQueueProcessFuncAsync> ProcessFuncByActionType { get; }
VB __Копировать
     Protected ReadOnly Property ProcessFuncByActionType As Dictionary(Of NumberQueueActionType, NumberQueueProcessFuncAsync)
    	Get
C++ __Копировать
     protected:
    property Dictionary<NumberQueueActionType^, NumberQueueProcessFuncAsync^>^ ProcessFuncByActionType {
    	Dictionary<NumberQueueActionType^, NumberQueueProcessFuncAsync^>^ get ();
    }
F# __Копировать
     member ProcessFuncByActionType : Dictionary<NumberQueueActionType, NumberQueueProcessFuncAsync> with get
#### Значение свойства
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[NumberQueueActionType](T_Tessa_Cards_Numbers_NumberQueueActionType.htm),
[NumberQueueProcessFuncAsync](T_Tessa_Cards_Numbers_NumberQueueProcessFuncAsync.htm)>
##  __Заметки
Для добавления обработчика действия рекомендуется добавить запись о нём в
значение этого свойства в дочернем классе на момент выполнения конструктора.
## __См. также
#### Ссылки
[NumberQueueProcessor - ](T_Tessa_Cards_Numbers_NumberQueueProcessor.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
