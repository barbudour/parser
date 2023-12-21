# ITopicQueryBuilder - интерфейс
Выполняет построение запроса для получения списка уведомлений по топикам.
## __Definition
 **Пространство имён:**
[Tessa.Forums.Notifications](N_Tessa_Forums_Notifications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ITopicQueryBuilder
VB __Копировать
     Public Interface ITopicQueryBuilder
C++ __Копировать
     public interface class ITopicQueryBuilder
F# __Копировать
     type ITopicQueryBuilder = interface end
##  __Методы
[Append](M_Tessa_Forums_Notifications_ITopicQueryBuilder_Append.htm)|
Добавляет пользовательскую часть в запрос.  
---|---  
[AppendJoins](M_Tessa_Forums_Notifications_ITopicQueryBuilder_AppendJoins.htm)|
Добавляет базовые джойны к запросу.  
[AppendJoinTopicsAndUsers](M_Tessa_Forums_Notifications_ITopicQueryBuilder_AppendJoinTopicsAndUsers.htm)|
Добавляет базовый Inner Join Lateral в запрос для получения списка пар
идентификаторов топика и сотрудника.  
[AppendOrderBy](M_Tessa_Forums_Notifications_ITopicQueryBuilder_AppendOrderBy.htm)|
Добавляет базовую сортировку к запросу.  
[AppendSelect](M_Tessa_Forums_Notifications_ITopicQueryBuilder_AppendSelect.htm)|
Добавляет в запрос базовые колонки.  
[AppendWhere](M_Tessa_Forums_Notifications_ITopicQueryBuilder_AppendWhere.htm)|
Добавляет базовые условия в запрос.  
[Build](M_Tessa_Forums_Notifications_ITopicQueryBuilder_Build.htm)|
Возвращает результат построение запроса.  
## __См. также
#### Ссылки
[Tessa.Forums.Notifications - пространство
имён](N_Tessa_Forums_Notifications.htm)
