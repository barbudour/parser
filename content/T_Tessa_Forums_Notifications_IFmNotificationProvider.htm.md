# IFmNotificationProvider - интерфейс
Объект, обрабатывающий всплывающие уведомления по обсуждениям для индикатора
сообщений.
## __Definition
 **Пространство имён:**
[Tessa.Forums.Notifications](N_Tessa_Forums_Notifications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFmNotificationProvider
VB __Копировать
     Public Interface IFmNotificationProvider
C++ __Копировать
     public interface class IFmNotificationProvider
F# __Копировать
     type IFmNotificationProvider = interface end
##  __Методы
[AddReadMessageAsync](M_Tessa_Forums_Notifications_IFmNotificationProvider_AddReadMessageAsync.htm)|
Отмечает сообщение как прочитанное.  
---|---  
[ClearNotificationsAsync](M_Tessa_Forums_Notifications_IFmNotificationProvider_ClearNotificationsAsync.htm)|
Очищает ленту уведомлений.  
[GetNotificationsAsync](M_Tessa_Forums_Notifications_IFmNotificationProvider_GetNotificationsAsync.htm)|
Получает уведомления для индикатора сообщений.  
[RemoveReadMessageAsync](M_Tessa_Forums_Notifications_IFmNotificationProvider_RemoveReadMessageAsync.htm)|
Отмечает сообщение как непрочитанное.  
[UpdateNotificationsAsync](M_Tessa_Forums_Notifications_IFmNotificationProvider_UpdateNotificationsAsync.htm)|
Добавляет сообщение в ленту уведомлений для текущего пользователя. Функция
умеет переключать активный батч. При необходимости создаются уведомления.  
## __См. также
#### Ссылки
[Tessa.Forums.Notifications - пространство
имён](N_Tessa_Forums_Notifications.htm)
