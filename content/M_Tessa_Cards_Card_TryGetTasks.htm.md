# Card.TryGetTasks - метод
Возвращает список заданий, которые были выданы на карточку и ещё не были
завершены, или null, если список ещё не был задан.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ListStorage<CardTask> TryGetTasks()
VB __Копировать
     Public Function TryGetTasks As ListStorage(Of CardTask)
C++ __Копировать
     public:
    ListStorage<CardTask^>^ TryGetTasks()
F# __Копировать
     member TryGetTasks : unit -> ListStorage<CardTask> 
#### Возвращаемое значение
[ListStorage](T_Tessa_Platform_Storage_ListStorage_1.htm)<[CardTask](T_Tessa_Cards_CardTask.htm)>  
Список заданий, которые были выданы на карточку и ещё не были завершены, или
null, если список ещё не был задан.
## __См. также
#### Ссылки
[Card - ](T_Tessa_Cards_Card.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
