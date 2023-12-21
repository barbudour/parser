# NotificationHelper - класс
Вспомогательные средства для использования в уведомлениях.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Notices](N_Tessa_Extensions_Default_Shared_Notices.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static class NotificationHelper
VB __Копировать
     Public NotInheritable Class NotificationHelper
C++ __Копировать
     public ref class NotificationHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type NotificationHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ NotificationHelper
##  __Методы
[AddNotification<T>(CardInfoStorageObject,
T[])](M_Tessa_Extensions_Default_Shared_Notices_NotificationHelper_AddNotification__1_1.htm)|  
---|---  
[AddNotification<T>(IDictionary<String, Object>,
T[])](M_Tessa_Extensions_Default_Shared_Notices_NotificationHelper_AddNotification__1.htm)|  
[GetApprovalRef](M_Tessa_Extensions_Default_Shared_Notices_NotificationHelper_GetApprovalRef.htm)|  
[GetCardLinkHtmlFooter](M_Tessa_Extensions_Default_Shared_Notices_NotificationHelper_GetCardLinkHtmlFooter.htm)|
Возвращает текст со ссылкой на карточку в desktop-клиенте или в web-клиенте в
формате html, который обычно добавляется снизу от основного содержимого
уведомления. Перед ссылкой может выводиться разделитель от выше расположенного
контента. Ссылка локализуется на текущий или заданный язык cultureInfo.  
[GetCompleteRef](M_Tessa_Extensions_Default_Shared_Notices_NotificationHelper_GetCompleteRef.htm)|  
[GetInfoWithTask](M_Tessa_Extensions_Default_Shared_Notices_NotificationHelper_GetInfoWithTask.htm)|  
[GetMobileApprovalEmailAsync](M_Tessa_Extensions_Default_Shared_Notices_NotificationHelper_GetMobileApprovalEmailAsync.htm)|  
[GetNameForLink](M_Tessa_Extensions_Default_Shared_Notices_NotificationHelper_GetNameForLink.htm)|
Формирует строку для параметра Name для использования в ссылках  
[GetRef](M_Tessa_Extensions_Default_Shared_Notices_NotificationHelper_GetRef.htm)|  
[GetSigningRef](M_Tessa_Extensions_Default_Shared_Notices_NotificationHelper_GetSigningRef.htm)|  
[HasNotifications](M_Tessa_Extensions_Default_Shared_Notices_NotificationHelper_HasNotifications.htm)|  
[ModifyEmailForMobileApprovers](M_Tessa_Extensions_Default_Shared_Notices_NotificationHelper_ModifyEmailForMobileApprovers.htm)|  
[ModifyTaskCaption](M_Tessa_Extensions_Default_Shared_Notices_NotificationHelper_ModifyTaskCaption.htm)|  
[SendNotificationsAsync](M_Tessa_Extensions_Default_Shared_Notices_NotificationHelper_SendNotificationsAsync.htm)|  
## __Поля
[DefaultCss](F_Tessa_Extensions_Default_Shared_Notices_NotificationHelper_DefaultCss.htm)|  
---|---  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Shared.Notices - пространство
имён](N_Tessa_Extensions_Default_Shared_Notices.htm)
