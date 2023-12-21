# CardDeleteExtension - класс
Базовый класс расширений для процесса удаления карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class CardDeleteExtension : ICardDeleteExtension, 
    	ICardExtension, IExtension
VB __Копировать
     Public MustInherit Class CardDeleteExtension
    	Implements ICardDeleteExtension, ICardExtension, IExtension
C++ __Копировать
     public ref class CardDeleteExtension abstract : ICardDeleteExtension, 
    	ICardExtension, IExtension
F# __Копировать
     [<AbstractClassAttribute>]
    type CardDeleteExtension = 
        class
            interface ICardDeleteExtension
            interface ICardExtension
            interface IExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardDeleteExtension
Derived
[Tessa.Cards.Extensions.Templates.CardSatelliteDeleteExtension](T_Tessa_Cards_Extensions_Templates_CardSatelliteDeleteExtension.htm)
[Tessa.Cards.Extensions.Templates.CardSatelliteRestoreExtension](T_Tessa_Cards_Extensions_Templates_CardSatelliteRestoreExtension.htm)
[Tessa.Cards.Extensions.Templates.MultitypeSatelliteDeleteExtension](T_Tessa_Cards_Extensions_Templates_MultitypeSatelliteDeleteExtension.htm)
[Tessa.Cards.Extensions.Templates.TaskSatelliteRestoreExtension](T_Tessa_Cards_Extensions_Templates_TaskSatelliteRestoreExtension.htm)
[Tessa.Extensions.Default.Client.Cards.KrDocStateClientDeleteExtension](T_Tessa_Extensions_Default_Client_Cards_KrDocStateClientDeleteExtension.htm)
[Tessa.Extensions.Default.Server.Acquaintance.AcquaintanceDeleteExtension](T_Tessa_Extensions_Default_Server_Acquaintance_AcquaintanceDeleteExtension.htm)
[Tessa.Extensions.Default.Server.Cards.CardPermissionsDeleteExtension](T_Tessa_Extensions_Default_Server_Cards_CardPermissionsDeleteExtension.htm)
[Tessa.Extensions.Default.Server.Cards.DefaultConfigurationVersionDeleteExtension](T_Tessa_Extensions_Default_Server_Cards_DefaultConfigurationVersionDeleteExtension.htm)
[Tessa.Extensions.Default.Server.Cards.FileTemplateInvalidateCacheDeleteExtension](T_Tessa_Extensions_Default_Server_Cards_FileTemplateInvalidateCacheDeleteExtension.htm)
[Tessa.Extensions.Default.Server.Cards.KrDocStateDeleteExtension](T_Tessa_Extensions_Default_Server_Cards_KrDocStateDeleteExtension.htm)
[Tessa.Extensions.Default.Server.Cards.KrPermissionRuleDeleteExtension](T_Tessa_Extensions_Default_Server_Cards_KrPermissionRuleDeleteExtension.htm)
[Tessa.Extensions.Default.Server.Cards.KrVirtualFileDeleteExtension](T_Tessa_Extensions_Default_Server_Cards_KrVirtualFileDeleteExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.Requests.KrCompileSourceDeleteExtension](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrCompileSourceDeleteExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.KrPermissions.KrPermissionsDeleteExtension](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsDeleteExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.KrStrictSecurityCardDeleteExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrStrictSecurityCardDeleteExtension.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.KrDocTypeInvalidateSettingsCacheDeleteExtension](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrDocTypeInvalidateSettingsCacheDeleteExtension.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.KrSettingsInvalidateTypeCacheDeleteExtension](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrSettingsInvalidateTypeCacheDeleteExtension.htm)
[Tessa.Extensions.Platform.Client.Cards.SetDigestDeleteExtension](T_Tessa_Extensions_Platform_Client_Cards_SetDigestDeleteExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.ActionHistoryDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_ActionHistoryDeleteExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.BackupCardDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_BackupCardDeleteExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.BusinessProcessCardDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardDeleteExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.CardStrictSecurityDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_CardStrictSecurityDeleteExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.CheckRequestDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_CheckRequestDeleteExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.CompletionOptionDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_CompletionOptionDeleteExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.ConditionTypeDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_ConditionTypeDeleteExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.ConfigurationVersionDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_ConfigurationVersionDeleteExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.DeletedCardDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_DeletedCardDeleteExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.ErrorDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_ErrorDeleteExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.FileTemplateDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_FileTemplateDeleteExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.FunctionRoleDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_FunctionRoleDeleteExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.NotificationDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_NotificationDeleteExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.NotificationSubscriptionsCardDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_NotificationSubscriptionsCardDeleteExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.NotificationTypeDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_NotificationTypeDeleteExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.PrepareCardDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_PrepareCardDeleteExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.Satellites.UniversalSatelliteDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_Satellites_UniversalSatelliteDeleteExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.Satellites.UniversalSatelliteRestoreExtension](T_Tessa_Extensions_Platform_Server_Cards_Satellites_UniversalSatelliteRestoreExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.SealedApplicationDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_SealedApplicationDeleteExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.SealedSingletonDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_SealedSingletonDeleteExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.ServerInstanceDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_ServerInstanceDeleteExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.SingletonDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_SingletonDeleteExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.TemplateDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_TemplateDeleteExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.WorkflowInstanceCardDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_WorkflowInstanceCardDeleteExtension.htm)
[Tessa.Extensions.Platform.Server.Numbers.NumberDeleteExtension](T_Tessa_Extensions_Platform_Server_Numbers_NumberDeleteExtension.htm)
[Tessa.Extensions.Platform.Server.Numbers.NumberFinalDeleteExtension](T_Tessa_Extensions_Platform_Server_Numbers_NumberFinalDeleteExtension.htm)
[Tessa.Extensions.Platform.Server.Roles.PersonalRoleDeleteExtension](T_Tessa_Extensions_Platform_Server_Roles_PersonalRoleDeleteExtension.htm)
[Tessa.Extensions.Platform.Server.Roles.PersonalRoleNotificationSubscriptionsDeleteExtension](T_Tessa_Extensions_Platform_Server_Roles_PersonalRoleNotificationSubscriptionsDeleteExtension.htm)
[Tessa.Extensions.Platform.Server.Roles.RemoveUserFromRolesDeleteExtension](T_Tessa_Extensions_Platform_Server_Roles_RemoveUserFromRolesDeleteExtension.htm)
[Tessa.Extensions.Platform.Server.TimeZones.TimeZonesDeleteExtension](T_Tessa_Extensions_Platform_Server_TimeZones_TimeZonesDeleteExtension.htm)
[Tessa.Extensions.Platform.Server.Workflow.WorkflowEngineDeleteExtension](T_Tessa_Extensions_Platform_Server_Workflow_WorkflowEngineDeleteExtension.htm)
[Tessa.Extensions.Platform.Shared.Cards.InvalidateSingletonDeleteExtension](T_Tessa_Extensions_Platform_Shared_Cards_InvalidateSingletonDeleteExtension.htm)
[Tessa.Extensions.Platform.Shared.Roles.InvalidateContextRoleDeleteExtension](T_Tessa_Extensions_Platform_Shared_Roles_InvalidateContextRoleDeleteExtension.htm)
Подробнее __Less __
Implements
    [ICardDeleteExtension](T_Tessa_Cards_Extensions_ICardDeleteExtension.htm), [ICardExtension](T_Tessa_Cards_Extensions_ICardExtension.htm), [IExtension](T_Tessa_Extensions_IExtension.htm)
##  __Конструкторы
[CardDeleteExtension](M_Tessa_Cards_Extensions_CardDeleteExtension__ctor.htm)|
Инициализирует новый экземпляр класса CardDeleteExtension  
---|---  
##  __Методы
[AfterBeginTransaction](M_Tessa_Cards_Extensions_CardDeleteExtension_AfterBeginTransaction.htm)|
Действие, выполняемое после начала транзакции.  
---|---  
[AfterRequest](M_Tessa_Cards_Extensions_CardDeleteExtension_AfterRequest.htm)|
Действие, выполняемое после удаления карточки как при успешном, так и при
неудачном результате.  
[AfterRequestFinally](M_Tessa_Cards_Extensions_CardDeleteExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после удаления карточки
как при успешном, так и при неудачном результате. Необработанные исключения не
прерывают выполнение цепочки расширений.  
[BeforeCommitTransaction](M_Tessa_Cards_Extensions_CardDeleteExtension_BeforeCommitTransaction.htm)|
Действие, выполняемое перед коммитом транзакции.  
[BeforeRequest](M_Tessa_Cards_Extensions_CardDeleteExtension_BeforeRequest.htm)|
Действие, выполняемое перед удалением карточки стандартными средствами. Может
установить ответ на запрос для того, чтобы удаление карточки стандартными
средствами не выполнялось.  
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
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
