# Card.TryGetTaskHistory - метод
Возвращает список с информацией по завершённым заданиям, которые были выданы
на карточку, или null, если список ещё не был задан.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ListStorage<CardTaskHistoryItem> TryGetTaskHistory()
VB __Копировать
     Public Function TryGetTaskHistory As ListStorage(Of CardTaskHistoryItem)
C++ __Копировать
     public:
    ListStorage<CardTaskHistoryItem^>^ TryGetTaskHistory()
F# __Копировать
     member TryGetTaskHistory : unit -> ListStorage<CardTaskHistoryItem> 
#### Возвращаемое значение
[ListStorage](T_Tessa_Platform_Storage_ListStorage_1.htm)<[CardTaskHistoryItem](T_Tessa_Cards_CardTaskHistoryItem.htm)>  
Список с информацией по завершённым заданиям, которые были выданы на карточку,
или null, если список ещё не был задан.
## __См. также
#### Ссылки
[Card - ](T_Tessa_Cards_Card.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
