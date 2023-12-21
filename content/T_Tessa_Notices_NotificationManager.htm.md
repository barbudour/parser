# NotificationManager - класс
Объект для отправки уведомлений, построенных по карточке уведомления.
## __Definition
 **Пространство имён:** [Tessa.Notices](N_Tessa_Notices.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class NotificationManager : INotificationManager
VB __Копировать
     Public Class NotificationManager
    	Implements INotificationManager
C++ __Копировать
     public ref class NotificationManager : INotificationManager
F# __Копировать
     type NotificationManager = 
        class
            interface INotificationManager
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ NotificationManager
Derived
[Tessa.Notices.DeferredNotificationManager](T_Tessa_Notices_DeferredNotificationManager.htm)
Implements
    [INotificationManager](T_Tessa_Notices_INotificationManager.htm)
##  __Конструкторы
[NotificationManager](M_Tessa_Notices_NotificationManager__ctor.htm)|
Инициализирует новый экземпляр класса NotificationManager  
---|---  
##  __Свойства
[CardMetadata](P_Tessa_Notices_NotificationManager_CardMetadata.htm)|  
---|---  
[CardRepository](P_Tessa_Notices_NotificationManager_CardRepository.htm)|  
[ConditionCache](P_Tessa_Notices_NotificationManager_ConditionCache.htm)|  
[ConditionExecutor](P_Tessa_Notices_NotificationManager_ConditionExecutor.htm)|  
[Container](P_Tessa_Notices_NotificationManager_Container.htm)|  
[DbScope](P_Tessa_Notices_NotificationManager_DbScope.htm)|  
[EmailSourceProvider](P_Tessa_Notices_NotificationManager_EmailSourceProvider.htm)|  
[GetPlaceholderManagerFunc](P_Tessa_Notices_NotificationManager_GetPlaceholderManagerFunc.htm)|  
[LanguagePicker](P_Tessa_Notices_NotificationManager_LanguagePicker.htm)|  
[LicenseManager](P_Tessa_Notices_NotificationManager_LicenseManager.htm)|  
[MailService](P_Tessa_Notices_NotificationManager_MailService.htm)|  
[PermissionsProvider](P_Tessa_Notices_NotificationManager_PermissionsProvider.htm)|  
[PlaceholderCompilationDependencies](P_Tessa_Notices_NotificationManager_PlaceholderCompilationDependencies.htm)|  
[PlaceholderScriptDependencies](P_Tessa_Notices_NotificationManager_PlaceholderScriptDependencies.htm)|  
[RecipientsSourceProvider](P_Tessa_Notices_NotificationManager_RecipientsSourceProvider.htm)|  
[Session](P_Tessa_Notices_NotificationManager_Session.htm)|  
[TransactionStrategy](P_Tessa_Notices_NotificationManager_TransactionStrategy.htm)|  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
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
[SendAsync](M_Tessa_Notices_NotificationManager_SendAsync.htm)|  Метод для
отправки уведомления.  
[SendCoreAsync](M_Tessa_Notices_NotificationManager_SendCoreAsync.htm)|  
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
[SendAsync](M_Tessa_Notices_NoticesExtensions_SendAsync.htm)|  Метод для
отправки уведомления.  
(Определяется [NoticesExtensions](T_Tessa_Notices_NoticesExtensions.htm))  
[SendAsync](M_Tessa_Notices_NoticesExtensions_SendAsync_3.htm)|  Метод для
отправки уведомления.  
(Определяется [NoticesExtensions](T_Tessa_Notices_NoticesExtensions.htm))  
[SendAsync](M_Tessa_Notices_NoticesExtensions_SendAsync_2.htm)|  Метод для
отправки уведомления.  
(Определяется [NoticesExtensions](T_Tessa_Notices_NoticesExtensions.htm))  
[SendAsync](M_Tessa_Notices_NoticesExtensions_SendAsync_1.htm)|  Метод для
отправки уведомления.  
(Определяется [NoticesExtensions](T_Tessa_Notices_NoticesExtensions.htm))  
[SendUsersAsync](M_Tessa_Notices_NoticesExtensions_SendUsersAsync.htm)|  Метод
для отправки уведомления.  
(Определяется [NoticesExtensions](T_Tessa_Notices_NoticesExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Notices - пространство имён](N_Tessa_Notices.htm)
