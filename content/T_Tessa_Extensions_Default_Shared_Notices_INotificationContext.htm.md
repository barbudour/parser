# INotificationContext - интерфейс
Контекст, в котором выполняется отправка уведомлений
[INotification](T_Tessa_Extensions_Default_Shared_Notices_INotification.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Notices](N_Tessa_Extensions_Default_Shared_Notices.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public interface INotificationContext
VB __Копировать
     Public Interface INotificationContext
C++ __Копировать
     public interface class INotificationContext
F# __Копировать
     type INotificationContext = interface end
##  __Свойства
[CardDigest](P_Tessa_Extensions_Default_Shared_Notices_INotificationContext_CardDigest.htm)|
Digest карточки или null, если Digest недоступен. Локализация должна быть
выполнена индивидуально для каждого уведомления на языке пользователя, который
получит уведомление. Локализацию требуется выполнять методом
[Format(String)](M_Tessa_Localization_LocalizationManager_Format.htm).  
---|---  
[CardID](P_Tessa_Extensions_Default_Shared_Notices_INotificationContext_CardID.htm)|
Идентификатор карточки.  
[CardTypeID](P_Tessa_Extensions_Default_Shared_Notices_INotificationContext_CardTypeID.htm)|
Идентификатор типа карточки.  
[DbScope](P_Tessa_Extensions_Default_Shared_Notices_INotificationContext_DbScope.htm)|
Объект, обеспечивающий взаимодействие с базой данных.  
[LicenseManager](P_Tessa_Extensions_Default_Shared_Notices_INotificationContext_LicenseManager.htm)|
Объект, управляющий лицензиями.  
[MailService](P_Tessa_Extensions_Default_Shared_Notices_INotificationContext_MailService.htm)|
Сервис отправки почтовых сообщений.  
[Session](P_Tessa_Extensions_Default_Shared_Notices_INotificationContext_Session.htm)|
Сессия текущего пользователя.  
[UnityContainer](P_Tessa_Extensions_Default_Shared_Notices_INotificationContext_UnityContainer.htm)|
Контейнер Unity.  
[ValidationResult](P_Tessa_Extensions_Default_Shared_Notices_INotificationContext_ValidationResult.htm)|
Результат валидации, содержащий сообщения.  
[WebAddress](P_Tessa_Extensions_Default_Shared_Notices_INotificationContext_WebAddress.htm)|
Нормализованная ссылка на базовый адрес веб-сервера, заданная в настройках.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Shared.Notices - пространство
имён](N_Tessa_Extensions_Default_Shared_Notices.htm)
