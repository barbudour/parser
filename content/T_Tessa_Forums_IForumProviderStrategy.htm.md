# IForumProviderStrategy - интерфейс
Объект, предоставляющий средства для взаимодействия с обсуждениями на сервере
в дополнение к методам [IForumProvider](T_Tessa_Forums_IForumProvider.htm).
## __Definition
 **Пространство имён:** [Tessa.Forums](N_Tessa_Forums.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IForumProviderStrategy : IForumProvider
VB __Копировать
     Public Interface IForumProviderStrategy
    	Inherits IForumProvider
C++ __Копировать
     public interface class IForumProviderStrategy : IForumProvider
F# __Копировать
     type IForumProviderStrategy = 
        interface
            interface IForumProvider
        end
Implements
    [IForumProvider](T_Tessa_Forums_IForumProvider.htm)
##  __Методы
[AddParticipantsAsync](M_Tessa_Forums_IForumProvider_AddParticipantsAsync.htm)|
Добавляет участников в топик.  
(Унаследован от [IForumProvider](T_Tessa_Forums_IForumProvider.htm))  
---|---  
[AddRolesAsync](M_Tessa_Forums_IForumProvider_AddRolesAsync.htm)|  Добавляет
роли участников в топик.  
(Унаследован от [IForumProvider](T_Tessa_Forums_IForumProvider.htm))  
[AddTopicAsync](M_Tessa_Forums_IForumProvider_AddTopicAsync.htm)|  Создаёт
топик.  
(Унаследован от [IForumProvider](T_Tessa_Forums_IForumProvider.htm))  
[ArchiveTopicAsync](M_Tessa_Forums_IForumProvider_ArchiveTopicAsync.htm)|
Выполняет архивирование или разархивирование топика.  
(Унаследован от [IForumProvider](T_Tessa_Forums_IForumProvider.htm))  
[CheckPermissionByFileAsync](M_Tessa_Forums_IForumProvider_CheckPermissionByFileAsync.htm)|
Проверяет возможность загрузить файл у пользователя в сессии.  
(Унаследован от [IForumProvider](T_Tessa_Forums_IForumProvider.htm))  
[GetMessagesAsync](M_Tessa_Forums_IForumProvider_GetMessagesAsync.htm)|
Загружает сообщения топика.  
(Унаследован от [IForumProvider](T_Tessa_Forums_IForumProvider.htm))  
[GetSatelliteIDAsync](M_Tessa_Forums_IForumProvider_GetSatelliteIDAsync.htm)|
Возвращает идентификатор карточки-сателлита для обсуждений.  
(Унаследован от [IForumProvider](T_Tessa_Forums_IForumProvider.htm))  
[GetSatelliteIDByTopicAsync](M_Tessa_Forums_IForumProviderStrategy_GetSatelliteIDByTopicAsync.htm)|
Возвращает идентификаторы карточки-сателлита обсуждений и основной карточки по
идентификатору топика. Не выполняет проверки доступа для текущего сотрудника.  
[GetTopicAsync](M_Tessa_Forums_IForumProvider_GetTopicAsync.htm)|  Возвращает
информацию по указанному топику.  
(Унаследован от [IForumProvider](T_Tessa_Forums_IForumProvider.htm))  
[GetTopicIDListByCardIDAsync](M_Tessa_Forums_IForumProviderStrategy_GetTopicIDListByCardIDAsync.htm)|
Возвращает идентификаторы всех топиков в указанной карточке. Не выполняет
проверки доступа для текущего сотрудника.  
[GetTopicsWithMessagesAsync](M_Tessa_Forums_IForumProvider_GetTopicsWithMessagesAsync.htm)|
Возвращает список топиков с последними сообщениями в каждом из них.  
(Унаследован от [IForumProvider](T_Tessa_Forums_IForumProvider.htm))  
[HasUnreadMessagesAsync](M_Tessa_Forums_IForumProviderStrategy_HasUnreadMessagesAsync.htm)|
Возвращает признак того, что в указанном топике присутствуют непрочитанные
сообщения для текущего пользователя.
Возвращает HasUnreadMessages = false, если либо все сообщения прочитаны, либо
топик отсутствует.  
[RemoveParticipantsAsync](M_Tessa_Forums_IForumProvider_RemoveParticipantsAsync.htm)|
Удаляет участников топика.  
(Унаследован от [IForumProvider](T_Tessa_Forums_IForumProvider.htm))  
[RemoveRolesAsync](M_Tessa_Forums_IForumProvider_RemoveRolesAsync.htm)|
Удаляет роли участников из топика.  
(Унаследован от [IForumProvider](T_Tessa_Forums_IForumProvider.htm))  
[SendMessageAsync](M_Tessa_Forums_IForumProvider_SendMessageAsync.htm)|
Отправляет сообщение в топике.  
(Унаследован от [IForumProvider](T_Tessa_Forums_IForumProvider.htm))  
[SetForumSettingsAsync](M_Tessa_Forums_IForumProvider_SetForumSettingsAsync.htm)|
Сохраняет глобальные (сейчас визуальные) настройки топика.  
(Унаследован от [IForumProvider](T_Tessa_Forums_IForumProvider.htm))  
[SubscribeAsync](M_Tessa_Forums_IForumProvider_SubscribeAsync.htm)|
Подписывает или отписывает текущего сотрудника как участника топика.  
(Унаследован от [IForumProvider](T_Tessa_Forums_IForumProvider.htm))  
[TryGetMessageInfoAsync](M_Tessa_Forums_IForumProviderStrategy_TryGetMessageInfoAsync.htm)|
Возвращает актуальную информацию по сообщению с указанным идентификатором. Не
загружает содержимое сообщения
[Body](P_Tessa_Forums_Models_MessageModelBase_Body.htm) и приложенные файлы
[Attachments](P_Tessa_Forums_Models_MessageModel_Attachments.htm). Возвращает
null, если указанное сообщение не найдено.  
[UpdateMessageAsync](M_Tessa_Forums_IForumProvider_UpdateMessageAsync.htm)|
Редактирует ранее отправленное сообщение.  
(Унаследован от [IForumProvider](T_Tessa_Forums_IForumProvider.htm))  
[UpdateParticipantsAsync](M_Tessa_Forums_IForumProvider_UpdateParticipantsAsync.htm)|
Изменяет свойства участников в топике.  
(Унаследован от [IForumProvider](T_Tessa_Forums_IForumProvider.htm))  
[UpdateRolesAsync](M_Tessa_Forums_IForumProvider_UpdateRolesAsync.htm)|
Изменяет роли участников в топике.  
(Унаследован от [IForumProvider](T_Tessa_Forums_IForumProvider.htm))  
##  __См. также
#### Ссылки
[Tessa.Forums - пространство имён](N_Tessa_Forums.htm)
