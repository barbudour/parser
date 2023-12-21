# NumberControlResponse.CopyNumberQueueTo - метод
Копирует информацию из очереди действий с номерами
[NumberQueue](P_Tessa_Cards_Numbers_NumberControlResponse_NumberQueue.htm) в
очередь действий указанной карточки. Возвращает список объектов, добавленных в
очередь действий в карточку, или null, если действий с номером не было
добавлено.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public List<NumberQueueItem> CopyNumberQueueTo(
    	Card card
    )
VB __Копировать
     Public Function CopyNumberQueueTo ( 
    	card As Card
    ) As List(Of NumberQueueItem)
C++ __Копировать
     public:
    List<NumberQueueItem^>^ CopyNumberQueueTo(
    	Card^ card
    )
F# __Копировать
     member CopyNumberQueueTo : 
            card : Card -> List<NumberQueueItem> 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, в очередь действий с номерами в которой надо скопировать действия.
#### Возвращаемое значение
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[NumberQueueItem](T_Tessa_Cards_Numbers_NumberQueueItem.htm)>  
Список объектов, добавленных в очередь действий в карточку, или null, если
действий с номером не было добавлено.
## __См. также
#### Ссылки
[NumberControlResponse - ](T_Tessa_Cards_Numbers_NumberControlResponse.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
