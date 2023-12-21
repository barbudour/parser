# IForumProvider - интерфейс
Объект, предоставляющий средства для получения объектов форумов с сервера и
отправки с клиента на сервер.
## __Definition
 **Пространство имён:** [Tessa.Forums](N_Tessa_Forums.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IForumProvider
VB __Копировать
     Public Interface IForumProvider
C++ __Копировать
     public interface class IForumProvider
F# __Копировать
     type IForumProvider = interface end
##  __Методы
[AddParticipantsAsync](M_Tessa_Forums_IForumProvider_AddParticipantsAsync.htm)|
Добавляет участников в топик.  
---|---  
[AddRolesAsync](M_Tessa_Forums_IForumProvider_AddRolesAsync.htm)|  Добавляет
роли участников в топик.  
[AddTopicAsync](M_Tessa_Forums_IForumProvider_AddTopicAsync.htm)|  Создаёт
топик.  
[ArchiveTopicAsync](M_Tessa_Forums_IForumProvider_ArchiveTopicAsync.htm)|
Выполняет архивирование или разархивирование топика.  
[CheckPermissionByFileAsync](M_Tessa_Forums_IForumProvider_CheckPermissionByFileAsync.htm)|
Проверяет возможность загрузить файл у пользователя в сессии.  
[GetMessagesAsync](M_Tessa_Forums_IForumProvider_GetMessagesAsync.htm)|
Загружает сообщения топика.  
[GetSatelliteIDAsync](M_Tessa_Forums_IForumProvider_GetSatelliteIDAsync.htm)|
Возвращает идентификатор карточки-сателлита для обсуждений.  
[GetTopicAsync](M_Tessa_Forums_IForumProvider_GetTopicAsync.htm)|  Возвращает
информацию по указанному топику.  
[GetTopicsWithMessagesAsync](M_Tessa_Forums_IForumProvider_GetTopicsWithMessagesAsync.htm)|
Возвращает список топиков с последними сообщениями в каждом из них.  
[RemoveParticipantsAsync](M_Tessa_Forums_IForumProvider_RemoveParticipantsAsync.htm)|
Удаляет участников топика.  
[RemoveRolesAsync](M_Tessa_Forums_IForumProvider_RemoveRolesAsync.htm)|
Удаляет роли участников из топика.  
[SendMessageAsync](M_Tessa_Forums_IForumProvider_SendMessageAsync.htm)|
Отправляет сообщение в топике.  
[SetForumSettingsAsync](M_Tessa_Forums_IForumProvider_SetForumSettingsAsync.htm)|
Сохраняет глобальные (сейчас визуальные) настройки топика.  
[SubscribeAsync](M_Tessa_Forums_IForumProvider_SubscribeAsync.htm)|
Подписывает или отписывает текущего сотрудника как участника топика.  
[UpdateMessageAsync](M_Tessa_Forums_IForumProvider_UpdateMessageAsync.htm)|
Редактирует ранее отправленное сообщение.  
[UpdateParticipantsAsync](M_Tessa_Forums_IForumProvider_UpdateParticipantsAsync.htm)|
Изменяет свойства участников в топике.  
[UpdateRolesAsync](M_Tessa_Forums_IForumProvider_UpdateRolesAsync.htm)|
Изменяет роли участников в топике.  
## __См. также
#### Ссылки
[Tessa.Forums - пространство имён](N_Tessa_Forums.htm)
