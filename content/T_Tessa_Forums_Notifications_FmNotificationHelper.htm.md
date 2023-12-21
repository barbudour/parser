# FmNotificationHelper - класс
Класс хелпер для обработки логики обработки уведомлений
## __Definition
 **Пространство имён:**
[Tessa.Forums.Notifications](N_Tessa_Forums_Notifications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class FmNotificationHelper
VB __Копировать
     Public NotInheritable Class FmNotificationHelper
C++ __Копировать
     public ref class FmNotificationHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type FmNotificationHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FmNotificationHelper
##  __Методы
[DefineActiveBatch](M_Tessa_Forums_Notifications_FmNotificationHelper_DefineActiveBatch.htm)|
Определяет какой batch сейчас активен и нужно ли переключить и очистить этот
батч  
---|---  
[DefineActiveBatchColumn](M_Tessa_Forums_Notifications_FmNotificationHelper_DefineActiveBatchColumn.htm)|
Определяет название колонок активного батча  
[DeserializeReadMessages](M_Tessa_Forums_Notifications_FmNotificationHelper_DeserializeReadMessages.htm)|  
[GetOtherActiveBatch](M_Tessa_Forums_Notifications_FmNotificationHelper_GetOtherActiveBatch.htm)|
возвражает не активный банч  
[GetSerializationMessage](M_Tessa_Forums_Notifications_FmNotificationHelper_GetSerializationMessage.htm)|
Формирует строку, и добавляет в начало запятую  
[SerializeReadMessageList](M_Tessa_Forums_Notifications_FmNotificationHelper_SerializeReadMessageList.htm)|  
[TryDeserializeNotification](M_Tessa_Forums_Notifications_FmNotificationHelper_TryDeserializeNotification.htm)|
Преобразует уведомления из кусочка json в список NotificationModel  
## __Поля
[FmNotificationsResponseFactory](F_Tessa_Forums_Notifications_FmNotificationHelper_FmNotificationsResponseFactory.htm)|  
---|---  
[MaxBatchMessages](F_Tessa_Forums_Notifications_FmNotificationHelper_MaxBatchMessages.htm)|
Максимальное кол-во сообщений в батче  
[NotificationsRequestFactory](F_Tessa_Forums_Notifications_FmNotificationHelper_NotificationsRequestFactory.htm)|  
## __См. также
#### Ссылки
[Tessa.Forums.Notifications - пространство
имён](N_Tessa_Forums_Notifications.htm)
