# NumberQueueProcessor.PredicateByType - свойство
Хеш-таблица, задающая отношение между типом предиката
[NumberQueuePredicateType](T_Tessa_Cards_Numbers_NumberQueuePredicateType.htm)
и функцией, обрабатывающей предикат
[NumberQueuePredicateFuncAsync](T_Tessa_Cards_Numbers_NumberQueuePredicateFuncAsync.htm).
Используется в реализации [CanProcessAsync(INumberObject, INumberContext,
NumberQueue, NumberQueueItem, NumberQueueActionType, NumberQueuePredicateType,
CancellationToken)](M_Tessa_Cards_Numbers_NumberQueueProcessor_CanProcessAsync.htm)
по умолчанию.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected Dictionary<NumberQueuePredicateType, NumberQueuePredicateFuncAsync> PredicateByType { get; }
VB __Копировать
     Protected ReadOnly Property PredicateByType As Dictionary(Of NumberQueuePredicateType, NumberQueuePredicateFuncAsync)
    	Get
C++ __Копировать
     protected:
    property Dictionary<NumberQueuePredicateType^, NumberQueuePredicateFuncAsync^>^ PredicateByType {
    	Dictionary<NumberQueuePredicateType^, NumberQueuePredicateFuncAsync^>^ get ();
    }
F# __Копировать
     member PredicateByType : Dictionary<NumberQueuePredicateType, NumberQueuePredicateFuncAsync> with get
#### Значение свойства
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[NumberQueuePredicateType](T_Tessa_Cards_Numbers_NumberQueuePredicateType.htm),
[NumberQueuePredicateFuncAsync](T_Tessa_Cards_Numbers_NumberQueuePredicateFuncAsync.htm)>
##  __Заметки
Для добавления предиката рекомендуется добавить запись о нём в значение этого
свойства в дочернем классе на момент выполнения конструктора.
## __См. также
#### Ссылки
[NumberQueueProcessor - ](T_Tessa_Cards_Numbers_NumberQueueProcessor.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
