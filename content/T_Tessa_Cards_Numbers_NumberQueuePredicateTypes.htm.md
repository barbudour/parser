# NumberQueuePredicateTypes - класс
Стандартные типы предикатов, применимых к действиям с номерами
[NumberQueueActionType](T_Tessa_Cards_Numbers_NumberQueueActionType.htm) в
очереди [NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class NumberQueuePredicateTypes
VB __Копировать
     Public NotInheritable Class NumberQueuePredicateTypes
C++ __Копировать
     public ref class NumberQueuePredicateTypes abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type NumberQueuePredicateTypes = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ NumberQueuePredicateTypes
##  __Методы
[IsKnown](M_Tessa_Cards_Numbers_NumberQueuePredicateTypes_IsKnown.htm)|
Возвращает признак того, что тип предиката является известным для стандартного
API.  
---|---  
## __Поля
[All](F_Tessa_Cards_Numbers_NumberQueuePredicateTypes_All.htm)|  Список всех
типов предикатов, которые являются частью стандартного API.  
---|---  
[Always](F_Tessa_Cards_Numbers_NumberQueuePredicateTypes_Always.htm)|
Действие с номером всегда обрабатывается.  
[ItemIsHandled](F_Tessa_Cards_Numbers_NumberQueuePredicateTypes_ItemIsHandled.htm)|
Действие с номером обрабатывается, если действие с идентификатором
[TryGetPredicateItemID(NumberQueueItem)](M_Tessa_Cards_Numbers_NumberExtensions_TryGetPredicateItemID.htm)
было отмечено, как успешно обработанное, или было удалено из очереди
(например, при обработке на другом этапе). Это позволяет добавлять в очередь
зависимые друг от друга действия.  
[NumberIsEmpty](F_Tessa_Cards_Numbers_NumberQueuePredicateTypes_NumberIsEmpty.htm)|
Действие с номером обрабатывается, если номер, для которого оно выполняется,
является пустым.  
[NumberIsSequential](F_Tessa_Cards_Numbers_NumberQueuePredicateTypes_NumberIsSequential.htm)|
Действие с номером обрабатывается, если номер, для которого оно выполняется,
является номером последовательности.  
## __См. также
#### Ссылки
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
