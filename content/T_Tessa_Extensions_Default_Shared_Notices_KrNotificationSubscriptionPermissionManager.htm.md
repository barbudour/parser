# KrNotificationSubscriptionPermissionManager - класс
Объект, отвечающий за проверку доступа к подпискам на уведомления.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Notices](N_Tessa_Extensions_Default_Shared_Notices.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public class KrNotificationSubscriptionPermissionManager : NotificationSubscriptionPermissionManager
VB __Копировать
     Public Class KrNotificationSubscriptionPermissionManager
    	Inherits NotificationSubscriptionPermissionManager
C++ __Копировать
     public ref class KrNotificationSubscriptionPermissionManager : public NotificationSubscriptionPermissionManager
F# __Копировать
     type KrNotificationSubscriptionPermissionManager = 
        class
            inherit NotificationSubscriptionPermissionManager
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NotificationSubscriptionPermissionManager](T_Tessa_Notices_NotificationSubscriptionPermissionManager.htm) __ KrNotificationSubscriptionPermissionManager
Derived
[Tessa.Extensions.Default.Server.Notices.KrNotificationSubscriptionPermissionManagerServer](T_Tessa_Extensions_Default_Server_Notices_KrNotificationSubscriptionPermissionManagerServer.htm)
##  __Конструкторы
[KrNotificationSubscriptionPermissionManager](M_Tessa_Extensions_Default_Shared_Notices_KrNotificationSubscriptionPermissionManager__ctor.htm)|
Инициализирует новый экземпляр класса
KrNotificationSubscriptionPermissionManager  
---|---  
##  __Методы
[CheckAccessAsync(Card, IValidationResultBuilder,
CancellationToken)](M_Tessa_Extensions_Default_Shared_Notices_KrNotificationSubscriptionPermissionManager_CheckAccessAsync.htm)|
Метод для проверки доступа по объекту карточки для текущего сотрудника. Данный
метод доступен как на стороне сервера, так и клиента.  
(Переопределяет
[NotificationSubscriptionPermissionManager.CheckAccessAsync(Card,
IValidationResultBuilder,
CancellationToken)](M_Tessa_Notices_NotificationSubscriptionPermissionManager_CheckAccessAsync_1.htm))  
---|---  
[CheckAccessAsync(Guid, IValidationResultBuilder,
CancellationToken)](M_Tessa_Notices_NotificationSubscriptionPermissionManager_CheckAccessAsync.htm)|
Метод для проверки доступа по идентификатору карточки для текущего сотрудника.
Данный метод доступен только на серверной стороне.  
(Унаследован от
[NotificationSubscriptionPermissionManager](T_Tessa_Notices_NotificationSubscriptionPermissionManager.htm))  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[SetAccessAsync](M_Tessa_Notices_NotificationSubscriptionPermissionManager_SetAccessAsync.htm)|
Метод для установки в карточку информации о том, что по ней есть доступ на
создание подписок на уведомления.  
(Унаследован от
[NotificationSubscriptionPermissionManager](T_Tessa_Notices_NotificationSubscriptionPermissionManager.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Shared.Notices - пространство
имён](N_Tessa_Extensions_Default_Shared_Notices.htm)
