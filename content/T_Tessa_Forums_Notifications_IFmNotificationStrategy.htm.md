# IFmNotificationStrategy - интерфейс
Объект, обрабатывающий всплывающие уведомления по обсуждениям для индикатора
сообщений со стороны сервера.
## __Definition
 **Пространство имён:**
[Tessa.Forums.Notifications](N_Tessa_Forums_Notifications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFmNotificationStrategy : IFmNotificationProvider
VB __Копировать
     Public Interface IFmNotificationStrategy
    	Inherits IFmNotificationProvider
C++ __Копировать
     public interface class IFmNotificationStrategy : IFmNotificationProvider
F# __Копировать
     type IFmNotificationStrategy = 
        interface
            interface IFmNotificationProvider
        end
Implements
    [IFmNotificationProvider](T_Tessa_Forums_Notifications_IFmNotificationProvider.htm)
##  __Методы
[AddReadMessageAsync](M_Tessa_Forums_Notifications_IFmNotificationProvider_AddReadMessageAsync.htm)|
Отмечает сообщение как прочитанное.  
(Унаследован от
[IFmNotificationProvider](T_Tessa_Forums_Notifications_IFmNotificationProvider.htm))  
---|---  
[AddServiceMessageInNotificationsAsync](M_Tessa_Forums_Notifications_IFmNotificationStrategy_AddServiceMessageInNotificationsAsync.htm)|
Добавляет служебное сообщение в ленту уведомлений. Само служебное сообщение
содержит в себе список пользователей, которым отправляются эти уведомления.  
[ClearNotificationsAsync](M_Tessa_Forums_Notifications_IFmNotificationProvider_ClearNotificationsAsync.htm)|
Очищает ленту уведомлений.  
(Унаследован от
[IFmNotificationProvider](T_Tessa_Forums_Notifications_IFmNotificationProvider.htm))  
[GetNotificationsAsync(Nullable<DateTime>,
CancellationToken)](M_Tessa_Forums_Notifications_IFmNotificationStrategy_GetNotificationsAsync.htm)|
Получает уведомления для индикатора сообщений.  
[GetNotificationsAsync(IForumData, DateTime,
CancellationToken)](M_Tessa_Forums_Notifications_IFmNotificationProvider_GetNotificationsAsync.htm)|
Получает уведомления для индикатора сообщений.  
(Унаследован от
[IFmNotificationProvider](T_Tessa_Forums_Notifications_IFmNotificationProvider.htm))  
[GetReadTopicStatusListFromNotificationAsync](M_Tessa_Forums_Notifications_IFmNotificationStrategy_GetReadTopicStatusListFromNotificationAsync.htm)|
Возвращает информацию по прочитанным сообщениям в топиках.  
[RemoveReadMessageAsync](M_Tessa_Forums_Notifications_IFmNotificationProvider_RemoveReadMessageAsync.htm)|
Отмечает сообщение как непрочитанное.  
(Унаследован от
[IFmNotificationProvider](T_Tessa_Forums_Notifications_IFmNotificationProvider.htm))  
[UpdateNotificationsAsync](M_Tessa_Forums_Notifications_IFmNotificationProvider_UpdateNotificationsAsync.htm)|
Добавляет сообщение в ленту уведомлений для текущего пользователя. Функция
умеет переключать активный батч. При необходимости создаются уведомления.  
(Унаследован от
[IFmNotificationProvider](T_Tessa_Forums_Notifications_IFmNotificationProvider.htm))  
##  __См. также
#### Ссылки
[Tessa.Forums.Notifications - пространство
имён](N_Tessa_Forums_Notifications.htm)
