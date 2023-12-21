# NumberQueueEventTypes - класс
Стандартные типы событий по вызову действия с номером в очереди
[NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class NumberQueueEventTypes
VB __Копировать
     Public NotInheritable Class NumberQueueEventTypes
C++ __Копировать
     public ref class NumberQueueEventTypes abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type NumberQueueEventTypes = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ NumberQueueEventTypes
##  __Методы
[IsKnown](M_Tessa_Cards_Numbers_NumberQueueEventTypes_IsKnown.htm)|
Возвращает признак того, что тип события является известным для стандартного
API.  
---|---  
## __Поля
[AfterStore](F_Tessa_Cards_Numbers_NumberQueueEventTypes_AfterStore.htm)|
Действие выполняется после того, как сохранение карточки было выполнено
успешно.  
---|---  
[AfterStoreUnsuccessful](F_Tessa_Cards_Numbers_NumberQueueEventTypes_AfterStoreUnsuccessful.htm)|
Действие выполняется после того, как сохранение карточки было выполнено
неудачно.  
[All](F_Tessa_Cards_Numbers_NumberQueueEventTypes_All.htm)|  Список всех типов
событий, которые являются частью стандартного API.  
[BeforeStore](F_Tessa_Cards_Numbers_NumberQueueEventTypes_BeforeStore.htm)|
Действие выполняется перед сохранением карточки, т.е. оно может изменять
карточку таким образом, что изменения попадут в историю действий.  
[ClosingOrRefreshingCard](F_Tessa_Cards_Numbers_NumberQueueEventTypes_ClosingOrRefreshingCard.htm)|
Действие выполняется перед тем, как будет закрыта вкладка с текущей карточкой
или карточка будет обновлена, в т.ч. после успешного сохранения. Действие
актуально только со стороны клиента.  
[InsideStoreTransaction](F_Tessa_Cards_Numbers_NumberQueueEventTypes_InsideStoreTransaction.htm)|
Действие выполняется внутри транзакции на сохранение карточки после того, как
все изменения с карточкой были выполнены в базе данных, но перед тем, как
транзакция будет закрыта.  
## __См. также
#### Ссылки
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
