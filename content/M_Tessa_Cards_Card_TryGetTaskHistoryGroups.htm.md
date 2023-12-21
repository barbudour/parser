# Card.TryGetTaskHistoryGroups - метод
Возвращает список с информацией по группам заданий, которые были выданы на
карточку, или null, если список ещё не был задан.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ListStorage<CardTaskHistoryGroup> TryGetTaskHistoryGroups()
VB __Копировать
     Public Function TryGetTaskHistoryGroups As ListStorage(Of CardTaskHistoryGroup)
C++ __Копировать
     public:
    ListStorage<CardTaskHistoryGroup^>^ TryGetTaskHistoryGroups()
F# __Копировать
     member TryGetTaskHistoryGroups : unit -> ListStorage<CardTaskHistoryGroup> 
#### Возвращаемое значение
[ListStorage](T_Tessa_Platform_Storage_ListStorage_1.htm)<[CardTaskHistoryGroup](T_Tessa_Cards_CardTaskHistoryGroup.htm)>  
Список с информацией по группам заданий, которые были выданы на карточку, или
null, если список ещё не был задан.
## __См. также
#### Ссылки
[Card - ](T_Tessa_Cards_Card.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
