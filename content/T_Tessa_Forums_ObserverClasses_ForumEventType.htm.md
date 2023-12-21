# ForumEventType - перечисление
##  __Definition
 **Пространство имён:**
[Tessa.Forums.ObserverClasses](N_Tessa_Forums_ObserverClasses.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public enum ForumEventType
VB __Копировать
     Public Enumeration ForumEventType
C++ __Копировать
     public enum class ForumEventType
F# __Копировать
     type ForumEventType
##  __Члены
UpdateForumControl| 0|  Обновляем данные с сервера если вкладка с "обсуждения"
выбрана  
---|---|---  
UpdateTopicItem| 1|  Так как мы загрузили топик во вкладке "обсуждения",
обновляем и в области задания  
UpdateTopicsItemFromServer| 2|  Обновляем топики в области задания с сервера,
значит у нас не открыта вкладка "обсуждения" и в ForumControl мы не обновляем
данные  
UpdateTopicsItemFromForumControl| 3|  Обновляем топики в области задания с
сервера, у нас открыта вкладка "обсуждения" и в топики в области заданий
обновляем из ForumControl  
## __См. также
#### Ссылки
[Tessa.Forums.ObserverClasses - пространство
имён](N_Tessa_Forums_ObserverClasses.htm)
