# DeferredNotificationManager - класс
Версия реализации
[INotificationManager](T_Tessa_Notices_INotificationManager.htm) с отложенной
отправкой уведомлений.
## __Definition
 **Пространство имён:** [Tessa.Notices](N_Tessa_Notices.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class DeferredNotificationManager : NotificationManager
VB __Копировать
     Public NotInheritable Class DeferredNotificationManager
    	Inherits NotificationManager
C++ __Копировать
     public ref class DeferredNotificationManager sealed : public NotificationManager
F# __Копировать
     [<SealedAttribute>]
    type DeferredNotificationManager = 
        class
            inherit NotificationManager
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NotificationManager](T_Tessa_Notices_NotificationManager.htm) __ DeferredNotificationManager
##  __Конструкторы
[DeferredNotificationManager](M_Tessa_Notices_DeferredNotificationManager__ctor.htm)|
Инициализирует новый экземпляр класса DeferredNotificationManager  
---|---  
##  __Свойства
[CardMetadata](P_Tessa_Notices_NotificationManager_CardMetadata.htm)|  
(Унаследован от
[NotificationManager](T_Tessa_Notices_NotificationManager.htm))  
---|---  
[CardRepository](P_Tessa_Notices_NotificationManager_CardRepository.htm)|  
(Унаследован от
[NotificationManager](T_Tessa_Notices_NotificationManager.htm))  
[ConditionCache](P_Tessa_Notices_NotificationManager_ConditionCache.htm)|  
(Унаследован от
[NotificationManager](T_Tessa_Notices_NotificationManager.htm))  
[ConditionExecutor](P_Tessa_Notices_NotificationManager_ConditionExecutor.htm)|  
(Унаследован от
[NotificationManager](T_Tessa_Notices_NotificationManager.htm))  
[Container](P_Tessa_Notices_NotificationManager_Container.htm)|  
(Унаследован от
[NotificationManager](T_Tessa_Notices_NotificationManager.htm))  
[DbScope](P_Tessa_Notices_NotificationManager_DbScope.htm)|  
(Унаследован от
[NotificationManager](T_Tessa_Notices_NotificationManager.htm))  
[EmailSourceProvider](P_Tessa_Notices_NotificationManager_EmailSourceProvider.htm)|  
(Унаследован от
[NotificationManager](T_Tessa_Notices_NotificationManager.htm))  
[GetPlaceholderManagerFunc](P_Tessa_Notices_NotificationManager_GetPlaceholderManagerFunc.htm)|  
(Унаследован от
[NotificationManager](T_Tessa_Notices_NotificationManager.htm))  
[LanguagePicker](P_Tessa_Notices_NotificationManager_LanguagePicker.htm)|  
(Унаследован от
[NotificationManager](T_Tessa_Notices_NotificationManager.htm))  
[LicenseManager](P_Tessa_Notices_NotificationManager_LicenseManager.htm)|  
(Унаследован от
[NotificationManager](T_Tessa_Notices_NotificationManager.htm))  
[MailService](P_Tessa_Notices_NotificationManager_MailService.htm)|  
(Унаследован от
[NotificationManager](T_Tessa_Notices_NotificationManager.htm))  
[PermissionsProvider](P_Tessa_Notices_NotificationManager_PermissionsProvider.htm)|  
(Унаследован от
[NotificationManager](T_Tessa_Notices_NotificationManager.htm))  
[PlaceholderCompilationDependencies](P_Tessa_Notices_NotificationManager_PlaceholderCompilationDependencies.htm)|  
(Унаследован от
[NotificationManager](T_Tessa_Notices_NotificationManager.htm))  
[PlaceholderScriptDependencies](P_Tessa_Notices_NotificationManager_PlaceholderScriptDependencies.htm)|  
(Унаследован от
[NotificationManager](T_Tessa_Notices_NotificationManager.htm))  
[RecipientsSourceProvider](P_Tessa_Notices_NotificationManager_RecipientsSourceProvider.htm)|  
(Унаследован от
[NotificationManager](T_Tessa_Notices_NotificationManager.htm))  
[Session](P_Tessa_Notices_NotificationManager_Session.htm)|  
(Унаследован от
[NotificationManager](T_Tessa_Notices_NotificationManager.htm))  
[TransactionStrategy](P_Tessa_Notices_NotificationManager_TransactionStrategy.htm)|  
(Унаследован от
[NotificationManager](T_Tessa_Notices_NotificationManager.htm))  
##  __Методы
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
(Унаследован от
[NotificationManager](T_Tessa_Notices_NotificationManager.htm))  
[SendCoreAsync](M_Tessa_Notices_DeferredNotificationManager_SendCoreAsync.htm)|  
(Переопределяет [NotificationManager.SendCoreAsync(NotificationEmail,
IEnumerable<NotificationRecipient>, INotificationSendContext,
CancellationToken)](M_Tessa_Notices_NotificationManager_SendCoreAsync.htm))  
[SendDeferredMessagesAsync](M_Tessa_Notices_DeferredNotificationManager_SendDeferredMessagesAsync.htm)|  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Поля
[DeferredNotificationListKey](F_Tessa_Notices_DeferredNotificationManager_DeferredNotificationListKey.htm)|  
---|---  
## __Методы расширения
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
[Tessa.Notices - пространство имён](N_Tessa_Notices.htm)
