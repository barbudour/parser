# NumberQueuePredicateTypes.ItemIsHandled - поле
Действие с номером обрабатывается, если действие с идентификатором
[TryGetPredicateItemID(NumberQueueItem)](M_Tessa_Cards_Numbers_NumberExtensions_TryGetPredicateItemID.htm)
было отмечено, как успешно обработанное, или было удалено из очереди
(например, при обработке на другом этапе). Это позволяет добавлять в очередь
зависимые друг от друга действия.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static readonly NumberQueuePredicateType ItemIsHandled
VB __Копировать
     Public Shared ReadOnly ItemIsHandled As NumberQueuePredicateType
C++ __Копировать
     public:
    static initonly NumberQueuePredicateType^ ItemIsHandled
F# __Копировать
     static val ItemIsHandled: NumberQueuePredicateType
#### Значение поля
[NumberQueuePredicateType](T_Tessa_Cards_Numbers_NumberQueuePredicateType.htm)
##  __См. также
#### Ссылки
[NumberQueuePredicateTypes -
](T_Tessa_Cards_Numbers_NumberQueuePredicateTypes.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
