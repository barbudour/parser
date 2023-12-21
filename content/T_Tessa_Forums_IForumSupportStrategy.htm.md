# IForumSupportStrategy - интерфейс
Объект, обеспечивающий вспомогательные средства для действий, связанных с
обсуждениями, например: обновление таблицы UserStat, добавление служебных
сообщений в таблицу FmMessages.
## __Definition
 **Пространство имён:** [Tessa.Forums](N_Tessa_Forums.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IForumSupportStrategy
VB __Копировать
     Public Interface IForumSupportStrategy
C++ __Копировать
     public interface class IForumSupportStrategy
F# __Копировать
     type IForumSupportStrategy = interface end
##  __Методы
[UpdateLastMessageTimeInTopicAsync](M_Tessa_Forums_IForumSupportStrategy_UpdateLastMessageTimeInTopicAsync.htm)|
Обновляет дату и время последнего сообщения в топике.  
---|---  
[UpdateUserListStatAsync](M_Tessa_Forums_IForumSupportStrategy_UpdateUserListStatAsync.htm)|
Обновляет дату последнего прочитанного сообщения (посещения пользователем
топика). Возвращает актуальный идентификатор сателлита satelliteID.  
## __См. также
#### Ссылки
[Tessa.Forums - пространство имён](N_Tessa_Forums.htm)
