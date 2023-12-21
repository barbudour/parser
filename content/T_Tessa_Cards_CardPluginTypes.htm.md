# CardPluginTypes - класс
Стандартные типы плагинов, выполняющих запросы к сервису карточек с
расширениями. Типы позволяют отработать специфичное поведение при запуске из
плагина.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class CardPluginTypes
VB __Копировать
     Public NotInheritable Class CardPluginTypes
C++ __Копировать
     public ref class CardPluginTypes abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type CardPluginTypes = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardPluginTypes
##  __Поля
[RemoveDeletedCards](F_Tessa_Cards_CardPluginTypes_RemoveDeletedCards.htm)|
Плагин, окончательно удаляющий карточки, которые были удалены достаточно
давно. Плагин выполняет удаление карточки [DeleteAsync(CardDeleteRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_DeleteAsync.htm).  
---|---  
[RemoveErrorCards](F_Tessa_Cards_CardPluginTypes_RemoveErrorCards.htm)|
Плагин, удаляющий карточки ошибок, которые были созданы достаточно давно.
Плагин выполняет удаление карточки [DeleteAsync(CardDeleteRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_DeleteAsync.htm).  
[ReturnTasksFromPostponed](F_Tessa_Cards_CardPluginTypes_ReturnTasksFromPostponed.htm)|
Плагин, возвращающий задания из отложенного состояния, если срок, на который
они были отложены, подошёл к концу. Плагин выполняет удаление карточки
[StoreAsync(CardStoreRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_StoreAsync.htm).  
## __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
