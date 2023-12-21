# CardGetExtension - класс
Базовый класс расширений для процесса получения карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class CardGetExtension : ICardGetExtension, 
    	ICardExtension, IExtension
VB __Копировать
     Public MustInherit Class CardGetExtension
    	Implements ICardGetExtension, ICardExtension, IExtension
C++ __Копировать
     public ref class CardGetExtension abstract : ICardGetExtension, 
    	ICardExtension, IExtension
F# __Копировать
     [<AbstractClassAttribute>]
    type CardGetExtension = 
        class
            interface ICardGetExtension
            interface ICardExtension
            interface IExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardGetExtension
Derived
[Tessa.Cards.Extensions.Templates.CardSatelliteBackupExtension](T_Tessa_Cards_Extensions_Templates_CardSatelliteBackupExtension.htm)
[Tessa.Cards.Extensions.Templates.CardSatelliteExportExtension](T_Tessa_Cards_Extensions_Templates_CardSatelliteExportExtension.htm)
[Tessa.Cards.Extensions.Templates.CardSatelliteGetExtension](T_Tessa_Cards_Extensions_Templates_CardSatelliteGetExtension.htm)
[Tessa.Cards.Extensions.Templates.MultitypeSatelliteBackupExtension](T_Tessa_Cards_Extensions_Templates_MultitypeSatelliteBackupExtension.htm)
[Tessa.Cards.Extensions.Templates.MultitypeSatelliteExportExtension](T_Tessa_Cards_Extensions_Templates_MultitypeSatelliteExportExtension.htm)
[Tessa.Cards.Extensions.Templates.TaskSatelliteGetExtension](T_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension.htm)
[Tessa.Cards.Extensions.Templates.TaskSatellitePermissionsGetExtension](T_Tessa_Cards_Extensions_Templates_TaskSatellitePermissionsGetExtension.htm)
[Tessa.Extensions.Default.Client.Workflow.KrPermissions.KrDontSkipEditModeGetExtension](T_Tessa_Extensions_Default_Client_Workflow_KrPermissions_KrDontSkipEditModeGetExtension.htm)
[Tessa.Extensions.Default.Client.Workflow.KrPermissions.KrKeepReadCardPermissionGetExtension](T_Tessa_Extensions_Default_Client_Workflow_KrPermissions_KrKeepReadCardPermissionGetExtension.htm)
[Tessa.Extensions.Default.Client.Workflow.Wf.WfTasksClientGetExtension](T_Tessa_Extensions_Default_Client_Workflow_Wf_WfTasksClientGetExtension.htm)
[Tessa.Extensions.Default.Server.Acquaintance.AcquaintanceGetExtension](T_Tessa_Extensions_Default_Server_Acquaintance_AcquaintanceGetExtension.htm)
[Tessa.Extensions.Default.Server.BusinessCalendar.CalendarGetExtension](T_Tessa_Extensions_Default_Server_BusinessCalendar_CalendarGetExtension.htm)
[Tessa.Extensions.Default.Server.Cards.CardPermissionsGetExtension](T_Tessa_Extensions_Default_Server_Cards_CardPermissionsGetExtension.htm)
[Tessa.Extensions.Default.Server.Cards.KrAddCycleFileInfoGetExtension](T_Tessa_Extensions_Default_Server_Cards_KrAddCycleFileInfoGetExtension.htm)
[Tessa.Extensions.Default.Server.Cards.KrAddCycleFilesCardGetExtension](T_Tessa_Extensions_Default_Server_Cards_KrAddCycleFilesCardGetExtension.htm)
[Tessa.Extensions.Default.Server.Cards.KrAddVirtualFilesGetExtension](T_Tessa_Extensions_Default_Server_Cards_KrAddVirtualFilesGetExtension.htm)
[Tessa.Extensions.Default.Server.Cards.KrDocStateGetExtension](T_Tessa_Extensions_Default_Server_Cards_KrDocStateGetExtension.htm)
[Tessa.Extensions.Default.Server.Cards.KrSettingsForumLicenseGetExtension](T_Tessa_Extensions_Default_Server_Cards_KrSettingsForumLicenseGetExtension.htm)
[Tessa.Extensions.Default.Server.Cards.TaskFilesExampleGetExtension](T_Tessa_Extensions_Default_Server_Cards_TaskFilesExampleGetExtension.htm)
[Tessa.Extensions.Default.Server.Forums.ForumGetExtension](T_Tessa_Extensions_Default_Server_Forums_ForumGetExtension.htm)
[Tessa.Extensions.Default.Server.Notices.NotificationGetExtension](T_Tessa_Extensions_Default_Server_Notices_NotificationGetExtension.htm)
[Tessa.Extensions.Default.Server.References.AddIncomingReferencesGetExtension](T_Tessa_Extensions_Default_Server_References_AddIncomingReferencesGetExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.Requests.KrSourceGetExtension](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrSourceGetExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.KrPermissions.KrPermissionsMaskDataGetExtension](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsMaskDataGetExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.KrPermissions.KrPermissionsRulesExportExtension](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsRulesExportExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.FillCommentsVirtualSectionGetExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_FillCommentsVirtualSectionGetExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.KrAdditionalApprovalCardGetExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrAdditionalApprovalCardGetExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.KrSecondaryProcessExportExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrSecondaryProcessExportExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.KrSetDefaultSettingsValuesGetExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrSetDefaultSettingsValuesGetExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.KrStagesExportExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrStagesExportExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.KrUniversalTaskSettingsGetExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrUniversalTaskSettingsGetExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Requests.KrCardGetExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Requests_KrCardGetExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Requests.KrInfoForInitiatorGetExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Requests_KrInfoForInitiatorGetExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Requests.KrTaskKindGetExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Requests_KrTaskKindGetExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.Wf.WfTasksServerGetExtension](T_Tessa_Extensions_Default_Server_Workflow_Wf_WfTasksServerGetExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.WorkflowViewer.GetCardForWorkflowViewerGetExtension](T_Tessa_Extensions_Default_Server_Workflow_WorkflowViewer_GetCardForWorkflowViewerGetExtension.htm)
[Tessa.Extensions.Platform.Client.Cards.CardTemplateGetExtension](T_Tessa_Extensions_Platform_Client_Cards_CardTemplateGetExtension.htm)
[Tessa.Extensions.Platform.Client.Cards.DeletedCardGetExtension](T_Tessa_Extensions_Platform_Client_Cards_DeletedCardGetExtension.htm)
[Tessa.Extensions.Platform.Client.Cards.FileConverterCacheClientGetExtension](T_Tessa_Extensions_Platform_Client_Cards_FileConverterCacheClientGetExtension.htm)
[Tessa.Extensions.Platform.Client.Cards.FillAuthorTaskRowIDListGetExtension](T_Tessa_Extensions_Platform_Client_Cards_FillAuthorTaskRowIDListGetExtension.htm)
[Tessa.Extensions.Platform.Client.Cards.SequenceGetExtension](T_Tessa_Extensions_Platform_Client_Cards_SequenceGetExtension.htm)
[Tessa.Extensions.Platform.Client.Cards.SetDigestGetExtension](T_Tessa_Extensions_Platform_Client_Cards_SetDigestGetExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.ActionHistoryGetExtension](T_Tessa_Extensions_Platform_Server_Cards_ActionHistoryGetExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.ActionHistoryRecordGetExtension](T_Tessa_Extensions_Platform_Server_Cards_ActionHistoryRecordGetExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.ApplicationExportExtension](T_Tessa_Extensions_Platform_Server_Cards_ApplicationExportExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.BackupForAdminGetExtension](T_Tessa_Extensions_Platform_Server_Cards_BackupForAdminGetExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.BusinessProcessCardGetExtension](T_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardGetExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.CheckRequestGetExtension](T_Tessa_Extensions_Platform_Server_Cards_CheckRequestGetExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.CheckTaskModeGetExtension](T_Tessa_Extensions_Platform_Server_Cards_CheckTaskModeGetExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.CompletionOptionGetExtension](T_Tessa_Extensions_Platform_Server_Cards_CompletionOptionGetExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.CompressCardGetExtension](T_Tessa_Extensions_Platform_Server_Cards_CompressCardGetExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.DeletedCardGetExtension](T_Tessa_Extensions_Platform_Server_Cards_DeletedCardGetExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.ErrorGetExtension](T_Tessa_Extensions_Platform_Server_Cards_ErrorGetExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.ExportCardGetExtension](T_Tessa_Extensions_Platform_Server_Cards_ExportCardGetExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.FileConverterCacheGetExtension](T_Tessa_Extensions_Platform_Server_Cards_FileConverterCacheGetExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.FunctionRoleGetExtension](T_Tessa_Extensions_Platform_Server_Cards_FunctionRoleGetExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.LicenseGetExtension](T_Tessa_Extensions_Platform_Server_Cards_LicenseGetExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.LoadFileSignaturesGetExtension](T_Tessa_Extensions_Platform_Server_Cards_LoadFileSignaturesGetExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.MakeReadonlyGetExtension](T_Tessa_Extensions_Platform_Server_Cards_MakeReadonlyGetExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.NotificationSubscriptionsBackupExtension](T_Tessa_Extensions_Platform_Server_Cards_NotificationSubscriptionsBackupExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.OperationGetExtension](T_Tessa_Extensions_Platform_Server_Cards_OperationGetExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.Satellites.UniversalSatelliteBackupExtension](T_Tessa_Extensions_Platform_Server_Cards_Satellites_UniversalSatelliteBackupExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.Satellites.UniversalSatelliteExportExtension](T_Tessa_Extensions_Platform_Server_Cards_Satellites_UniversalSatelliteExportExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.Satellites.UniversalSatelliteGetExtension](T_Tessa_Extensions_Platform_Server_Cards_Satellites_UniversalSatelliteGetExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.SequenceGetExtension](T_Tessa_Extensions_Platform_Server_Cards_SequenceGetExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.ServerInstanceGetExtension](T_Tessa_Extensions_Platform_Server_Cards_ServerInstanceGetExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.SingletonGetExtension](T_Tessa_Extensions_Platform_Server_Cards_SingletonGetExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.SortRowsGetExtension](T_Tessa_Extensions_Platform_Server_Cards_SortRowsGetExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.StorageForAdminGetExtension](T_Tessa_Extensions_Platform_Server_Cards_StorageForAdminGetExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.StorageMappingExportExtension](T_Tessa_Extensions_Platform_Server_Cards_StorageMappingExportExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.StrictSecurityStorageGetExtension](T_Tessa_Extensions_Platform_Server_Cards_StrictSecurityStorageGetExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.TaskKindGetExtension](T_Tessa_Extensions_Platform_Server_Cards_TaskKindGetExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.TemplateGetExtension](T_Tessa_Extensions_Platform_Server_Cards_TemplateGetExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.ViewCardGetExtension](T_Tessa_Extensions_Platform_Server_Cards_ViewCardGetExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.WebApplicationExportExtension](T_Tessa_Extensions_Platform_Server_Cards_WebApplicationExportExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.WorkplaceCardGetExtension](T_Tessa_Extensions_Platform_Server_Cards_WorkplaceCardGetExtension.htm)
[Tessa.Extensions.Platform.Server.Forums.FullTextSearchServerInstanceGetExtension](T_Tessa_Extensions_Platform_Server_Forums_FullTextSearchServerInstanceGetExtension.htm)
[Tessa.Extensions.Platform.Server.Roles.ContextRoleGetExtension](T_Tessa_Extensions_Platform_Server_Roles_ContextRoleGetExtension.htm)
[Tessa.Extensions.Platform.Server.Roles.FixRolesGetExtension](T_Tessa_Extensions_Platform_Server_Roles_FixRolesGetExtension.htm)
[Tessa.Extensions.Platform.Server.Roles.LimitUsersInRolesGetExtension](T_Tessa_Extensions_Platform_Server_Roles_LimitUsersInRolesGetExtension.htm)
[Tessa.Extensions.Platform.Server.Roles.PersonalRoleGetExtension](T_Tessa_Extensions_Platform_Server_Roles_PersonalRoleGetExtension.htm)
[Tessa.Extensions.Platform.Server.Roles.RoleDeputiesManagementGetExtension](T_Tessa_Extensions_Platform_Server_Roles_RoleDeputiesManagementGetExtension.htm)
[Tessa.Extensions.Platform.Server.Roles.RoleExportExtension](T_Tessa_Extensions_Platform_Server_Roles_RoleExportExtension.htm)
[Tessa.Extensions.Platform.Server.Roles.RoleUsersVirtualGetExtension](T_Tessa_Extensions_Platform_Server_Roles_RoleUsersVirtualGetExtension.htm)
[Tessa.Extensions.Platform.Server.Roles.SetDeputyDatesGetExtension](T_Tessa_Extensions_Platform_Server_Roles_SetDeputyDatesGetExtension.htm)
[Tessa.Extensions.Platform.Server.TimeZones.AllowToModifyTimeZonesGetExtension](T_Tessa_Extensions_Platform_Server_TimeZones_AllowToModifyTimeZonesGetExtension.htm)
[Tessa.Extensions.Platform.Server.TimeZones.TimeZonesGetExtension](T_Tessa_Extensions_Platform_Server_TimeZones_TimeZonesGetExtension.htm)
[Tessa.Extensions.Platform.Server.Workflow.WorkflowEngineBackupExportExtension](T_Tessa_Extensions_Platform_Server_Workflow_WorkflowEngineBackupExportExtension.htm)
[Tessa.Extensions.Platform.Server.Workflow.WorkflowProcessInstanceCardGetExtension](T_Tessa_Extensions_Platform_Server_Workflow_WorkflowProcessInstanceCardGetExtension.htm)
[Tessa.Extensions.Platform.Shared.Cards.DecompressCardGetExtension](T_Tessa_Extensions_Platform_Shared_Cards_DecompressCardGetExtension.htm)
Подробнее __Less __
Implements
    [ICardExtension](T_Tessa_Cards_Extensions_ICardExtension.htm), [ICardGetExtension](T_Tessa_Cards_Extensions_ICardGetExtension.htm), [IExtension](T_Tessa_Extensions_IExtension.htm)
##  __Конструкторы
[CardGetExtension](M_Tessa_Cards_Extensions_CardGetExtension__ctor.htm)|
Инициализирует новый экземпляр класса CardGetExtension  
---|---  
##  __Методы
[AfterRequest](M_Tessa_Cards_Extensions_CardGetExtension_AfterRequest.htm)|
Действие, выполняемое после получения карточки как при успешном, так и при
неудачном результате.  
---|---  
[AfterRequestFinally](M_Tessa_Cards_Extensions_CardGetExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после получения
карточки как при успешном, так и при неудачном результате. Необработанные
исключения не прерывают выполнение цепочки расширений.  
[BeforeRequest](M_Tessa_Cards_Extensions_CardGetExtension_BeforeRequest.htm)|
Действие, выполняемое перед получением карточки стандартными средствами. Может
установить ответ на запрос для того, чтобы получение карточки стандартными
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
