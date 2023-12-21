# INotificationSubscriptionPermissionManager - интерфейс
Объект, отвечающий за проверку доступа к подпискам на уведомления.
## __Definition
 **Пространство имён:** [Tessa.Notices](N_Tessa_Notices.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface INotificationSubscriptionPermissionManager
VB __Копировать
     Public Interface INotificationSubscriptionPermissionManager
C++ __Копировать
     public interface class INotificationSubscriptionPermissionManager
F# __Копировать
     type INotificationSubscriptionPermissionManager = interface end
##  __Методы
[CheckAccessAsync(Card, IValidationResultBuilder,
CancellationToken)](M_Tessa_Notices_INotificationSubscriptionPermissionManager_CheckAccessAsync_1.htm)|
Метод для проверки доступа по объекту карточки для текущего сотрудника. Данный
метод доступен как на стороне сервера, так и клиента.  
---|---  
[CheckAccessAsync(Guid, IValidationResultBuilder,
CancellationToken)](M_Tessa_Notices_INotificationSubscriptionPermissionManager_CheckAccessAsync.htm)|
Метод для проверки доступа по идентификатору карточки для текущего сотрудника.
Данный метод доступен только на серверной стороне.  
[SetAccessAsync](M_Tessa_Notices_INotificationSubscriptionPermissionManager_SetAccessAsync.htm)|
Метод для установки в карточку информации о том, что по ней есть доступ на
создание подписок на уведомления.  
## __См. также
#### Ссылки
[Tessa.Notices - пространство имён](N_Tessa_Notices.htm)
