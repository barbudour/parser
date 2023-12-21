# Card.TryGetTopics - метод
Возвращает список моделей с информацией по сообщениям в обсуждениях или null,
если информация ещё не была задана.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ListStorage<TopicModel> TryGetTopics()
VB __Копировать
     Public Function TryGetTopics As ListStorage(Of TopicModel)
C++ __Копировать
     public:
    ListStorage<TopicModel^>^ TryGetTopics()
F# __Копировать
     member TryGetTopics : unit -> ListStorage<TopicModel> 
#### Возвращаемое значение
[ListStorage](T_Tessa_Platform_Storage_ListStorage_1.htm)<[TopicModel](T_Tessa_Forums_Models_TopicModel.htm)>  
Список моделей с информацией по сообщениям в обсуждениях или null, если
информация ещё не была задана.
## __См. также
#### Ссылки
[Card - ](T_Tessa_Cards_Card.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
