# IForumUserNamingStrategy - интерфейс
Объект для изменения имен в обсуждениях.
## __Definition
 **Пространство имён:** [Tessa.Forums](N_Tessa_Forums.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IForumUserNamingStrategy
VB __Копировать
     Public Interface IForumUserNamingStrategy
C++ __Копировать
     public interface class IForumUserNamingStrategy
F# __Копировать
     type IForumUserNamingStrategy = interface end
##  __Методы
[PrepareForReplaceAsync(Guid, MessageModel,
CancellationToken)](M_Tessa_Forums_IForumUserNamingStrategy_PrepareForReplaceAsync_1.htm)|
Используется в [SendMessageAsync(Guid, MessageModel, Boolean,
CancellationToken)](M_Tessa_Forums_IForumProvider_SendMessageAsync.htm) для
проставления признака необходимости замены имен в модели сообщения.  
---|---  
[PrepareForReplaceAsync(Guid, Guid, Guid, String,
CancellationToken)](M_Tessa_Forums_IForumUserNamingStrategy_PrepareForReplaceAsync.htm)|
Осуществляет замену имени указанного пользователя при формировании служебных
сообщений в следующих методах:
  * [AddParticipantsAsync(Guid, IReadOnlyCollection<Guid>, Boolean, ParticipantType, Boolean, ForumServiceMessageMode, CancellationToken)](M_Tessa_Forums_IForumProvider_AddParticipantsAsync.htm)
  * [RemoveParticipantsAsync(Guid, IReadOnlyCollection<Guid>, CancellationToken)](M_Tessa_Forums_IForumProvider_RemoveParticipantsAsync.htm)
[ReplaceAsync(IReadOnlyList<ITopicNotificationInfo>,
CancellationToken)](M_Tessa_Forums_IForumUserNamingStrategy_ReplaceAsync.htm)|
Заменяет имена в отправляемых уведомлениях.
Используется в методе [GetNotificationsInfoAsync(DateTime, DateTime,
CancellationToken)](M_Tessa_Forums_Notifications_ITopicNotificationService_GetNotificationsInfoAsync.htm),
который вызывается при подготовке к отправке почтовых уведомлений по
обсуждениям.  
[ReplaceAsync(Guid, IReadOnlyList<NotificationModel>,
CancellationToken)](M_Tessa_Forums_IForumUserNamingStrategy_ReplaceAsync_1.htm)|
Заменяет имена в моделях уведомлений.
Используется в следующих методах:
  * [GetNotificationsAsync(Nullable<DateTime>, CancellationToken)](M_Tessa_Forums_Notifications_IFmNotificationStrategy_GetNotificationsAsync.htm) \- для замены имен в индикаторе уведомлений по обсуждениям 
  * [AddServiceMessageInNotificationsAsync(MessageModel, CancellationToken)](M_Tessa_Forums_Notifications_IFmNotificationStrategy_AddServiceMessageInNotificationsAsync.htm) \- для замены имен в служебных сообщениях, отправляемых в ленту уведомлений. 
[ReplaceAsync(Guid, Guid, IReadOnlyList<MessageModel>,
CancellationToken)](M_Tessa_Forums_IForumUserNamingStrategy_ReplaceAsync_2.htm)|
Заменяет имена в моделях сообщений.
Используется в следующих методах:
  * [GetMessagesAsync(Guid, Boolean, Int32, Int32, Nullable<Guid>, Nullable<DateTime>, Boolean, String, Boolean, CancellationToken)](M_Tessa_Forums_IForumProvider_GetMessagesAsync.htm) \- для замены имен в сообщениях указанного топика 
  * [GetTopicsWithMessagesAsync(Guid, Boolean, Int32, DateTime, Nullable<Guid>, CancellationToken)](M_Tessa_Forums_IForumProvider_GetTopicsWithMessagesAsync.htm) \- для замены имен в последних сообщениях нескольких топиков. 
## __См. также
#### Ссылки
[Tessa.Forums - пространство имён](N_Tessa_Forums.htm)
