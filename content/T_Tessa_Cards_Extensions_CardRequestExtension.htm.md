# CardRequestExtension - класс
Базовый класс расширений для процесса универсального взаимодействия с сервисом
карточек.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class CardRequestExtension : ICardRequestExtension, 
    	ICardExtension, IExtension
VB __Копировать
     Public MustInherit Class CardRequestExtension
    	Implements ICardRequestExtension, ICardExtension, IExtension
C++ __Копировать
     public ref class CardRequestExtension abstract : ICardRequestExtension, 
    	ICardExtension, IExtension
F# __Копировать
     [<AbstractClassAttribute>]
    type CardRequestExtension = 
        class
            interface ICardRequestExtension
            interface ICardExtension
            interface IExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardRequestExtension
Derived
[Tessa.Cards.Extensions.CardTypedRequestExtension<TRequest,
TResponse>](T_Tessa_Cards_Extensions_CardTypedRequestExtension_2.htm)
[Tessa.Extensions.Default.Client.Workflow.KrProcess.Requests.KrClientCommandCustomExtension](T_Tessa_Extensions_Default_Client_Workflow_KrProcess_Requests_KrClientCommandCustomExtension.htm)
[Tessa.Extensions.Default.Server.Acquaintance.AcquaintanceRequestExtension](T_Tessa_Extensions_Default_Server_Acquaintance_AcquaintanceRequestExtension.htm)
[Tessa.Extensions.Default.Server.Caching.DefaultInvalidateCacheRequestExtension](T_Tessa_Extensions_Default_Server_Caching_DefaultInvalidateCacheRequestExtension.htm)
[Tessa.Extensions.Default.Server.Cards.GetDocTypeInfoRequestExtension](T_Tessa_Extensions_Default_Server_Cards_GetDocTypeInfoRequestExtension.htm)
[Tessa.Extensions.Default.Server.Cards.KrResetUserSettingsRequestExtension](T_Tessa_Extensions_Default_Server_Cards_KrResetUserSettingsRequestExtension.htm)
[Tessa.Extensions.Default.Server.Cards.MoveFileRequestExtension](T_Tessa_Extensions_Default_Server_Cards_MoveFileRequestExtension.htm)
[Tessa.Extensions.Default.Server.EDS.CAdESSignatureRequestExtension](T_Tessa_Extensions_Default_Server_EDS_CAdESSignatureRequestExtension.htm)
[Tessa.Extensions.Default.Server.Files.MailSentRequestExtension](T_Tessa_Extensions_Default_Server_Files_MailSentRequestExtension.htm)
[Tessa.Extensions.Default.Server.Test.TestDataRequestExtension](T_Tessa_Extensions_Default_Server_Test_TestDataRequestExtension.htm)
[Tessa.Extensions.Default.Server.Test.XmlFrom1CRequestExtension](T_Tessa_Extensions_Default_Server_Test_XmlFrom1CRequestExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.KrPermissions.KrGetUnavailableTypesForCreationGetExtension](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrGetUnavailableTypesForCreationGetExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.KrGetDocTypesCardExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrGetDocTypesCardExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Requests.KrLaunchProcessCustomExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Requests_KrLaunchProcessCustomExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.StageTypeRequests.DialogCardExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_StageTypeRequests_DialogCardExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.Wf.WfGetResolutionVisualizationDataRequestExtension](T_Tessa_Extensions_Default_Server_Workflow_Wf_WfGetResolutionVisualizationDataRequestExtension.htm)
[Tessa.Extensions.Platform.Client.Cards.CompletionOptionGetTypeIDListRequestExtension](T_Tessa_Extensions_Platform_Client_Cards_CompletionOptionGetTypeIDListRequestExtension.htm)
[Tessa.Extensions.Platform.Client.Cards.FunctionRoleGetTypeIDListRequestExtension](T_Tessa_Extensions_Platform_Client_Cards_FunctionRoleGetTypeIDListRequestExtension.htm)
[Tessa.Extensions.Platform.Server.BusinessCalendar.AddWorkingDaysToDateExactRequestExtension](T_Tessa_Extensions_Platform_Server_BusinessCalendar_AddWorkingDaysToDateExactRequestExtension.htm)
[Tessa.Extensions.Platform.Server.BusinessCalendar.AddWorkingDaysToDateRequestExtension](T_Tessa_Extensions_Platform_Server_BusinessCalendar_AddWorkingDaysToDateRequestExtension.htm)
[Tessa.Extensions.Platform.Server.BusinessCalendar.AddWorkingQuantsToDateRequestExtension](T_Tessa_Extensions_Platform_Server_BusinessCalendar_AddWorkingQuantsToDateRequestExtension.htm)
[Tessa.Extensions.Platform.Server.BusinessCalendar.GetDateDiffRequestExtension](T_Tessa_Extensions_Platform_Server_BusinessCalendar_GetDateDiffRequestExtension.htm)
[Tessa.Extensions.Platform.Server.BusinessCalendar.GetFirstQuantStartRequestExtension](T_Tessa_Extensions_Platform_Server_BusinessCalendar_GetFirstQuantStartRequestExtension.htm)
[Tessa.Extensions.Platform.Server.BusinessCalendar.GetLastQuantEndRequestExtension](T_Tessa_Extensions_Platform_Server_BusinessCalendar_GetLastQuantEndRequestExtension.htm)
[Tessa.Extensions.Platform.Server.BusinessCalendar.GetRoleUtcOffsetRequestExtension](T_Tessa_Extensions_Platform_Server_BusinessCalendar_GetRoleUtcOffsetRequestExtension.htm)
[Tessa.Extensions.Platform.Server.BusinessCalendar.IsWorkTimeRequestExtension](T_Tessa_Extensions_Platform_Server_BusinessCalendar_IsWorkTimeRequestExtension.htm)
[Tessa.Extensions.Platform.Server.BusinessCalendar.RebuildCalendarRequestExtension](T_Tessa_Extensions_Platform_Server_BusinessCalendar_RebuildCalendarRequestExtension.htm)
[Tessa.Extensions.Platform.Server.BusinessCalendar.ValidateCalendarRequestExtension](T_Tessa_Extensions_Platform_Server_BusinessCalendar_ValidateCalendarRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Caching.FinalizeInvalidateCacheRequestExtension](T_Tessa_Extensions_Platform_Server_Caching_FinalizeInvalidateCacheRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Caching.InitializeInvalidateCacheRequestExtension](T_Tessa_Extensions_Platform_Server_Caching_InitializeInvalidateCacheRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Caching.PlatformInvalidateCacheRequestExtension](T_Tessa_Extensions_Platform_Server_Caching_PlatformInvalidateCacheRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.ConditionRepairManagerRequestExtension](T_Tessa_Extensions_Platform_Server_Cards_ConditionRepairManagerRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.DefaultFileSourceRequestExtension](T_Tessa_Extensions_Platform_Server_Cards_DefaultFileSourceRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.DeleteNotificationSubscriptionRequestExtension](T_Tessa_Extensions_Platform_Server_Cards_DeleteNotificationSubscriptionRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.FileTemplateCompileAllRequestExtension](T_Tessa_Extensions_Platform_Server_Cards_FileTemplateCompileAllRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.FixNumberWhenSavingTemplateRequestExtension](T_Tessa_Extensions_Platform_Server_Cards_FixNumberWhenSavingTemplateRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.GetTypeIDListRequestExtension](T_Tessa_Extensions_Platform_Server_Cards_GetTypeIDListRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.GetVersionSignaturesRequestExtension](T_Tessa_Extensions_Platform_Server_Cards_GetVersionSignaturesRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.MySettingsNotificationPlaceholderCardRequest](T_Tessa_Extensions_Platform_Server_Cards_MySettingsNotificationPlaceholderCardRequest.htm)
[Tessa.Extensions.Platform.Server.Cards.ResetUserSettingsRequestExtension](T_Tessa_Extensions_Platform_Server_Cards_ResetUserSettingsRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.ResolveUserCipherInfoRequestExtension](T_Tessa_Extensions_Platform_Server_Cards_ResolveUserCipherInfoRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.TemplateEditCardRequestExtension](T_Tessa_Extensions_Platform_Server_Cards_TemplateEditCardRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.TemplateSaveCardRequestExtension](T_Tessa_Extensions_Platform_Server_Cards_TemplateSaveCardRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.TemplateUniqueValidatorRequestExtension](T_Tessa_Extensions_Platform_Server_Cards_TemplateUniqueValidatorRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Forums.FmNotificationRequestExtension](T_Tessa_Extensions_Platform_Server_Forums_FmNotificationRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Forums.ForumPermissionsProviderRequestExtension](T_Tessa_Extensions_Platform_Server_Forums_ForumPermissionsProviderRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Forums.ForumProviderRequestExtension](T_Tessa_Extensions_Platform_Server_Forums_ForumProviderRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Numbers.SequenceProviderRequestExtension](T_Tessa_Extensions_Platform_Server_Numbers_SequenceProviderRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Roles.ApplyUserSettingsToRolesRequestExtension](T_Tessa_Extensions_Platform_Server_Roles_ApplyUserSettingsToRolesRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Roles.ChangePasswordRequestExtension](T_Tessa_Extensions_Platform_Server_Roles_ChangePasswordRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Roles.RecalcDynamicRoleRequestExtension](T_Tessa_Extensions_Platform_Server_Roles_RecalcDynamicRoleRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Roles.RecalcRoleGeneratorRequestExtension](T_Tessa_Extensions_Platform_Server_Roles_RecalcRoleGeneratorRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Roles.SaveCardModelSettingsRequestExtension](T_Tessa_Extensions_Platform_Server_Roles_SaveCardModelSettingsRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Roles.SyncAllDeputiesRequestExtension](T_Tessa_Extensions_Platform_Server_Roles_SyncAllDeputiesRequestExtension.htm)
[Tessa.Extensions.Platform.Server.TimeZones.CheckTimeZonesInheritanceRequestExtension](T_Tessa_Extensions_Platform_Server_TimeZones_CheckTimeZonesInheritanceRequestExtension.htm)
[Tessa.Extensions.Platform.Server.TimeZones.GenerateTimeZonesRequestExtension](T_Tessa_Extensions_Platform_Server_TimeZones_GenerateTimeZonesRequestExtension.htm)
[Tessa.Extensions.Platform.Server.TimeZones.SetDefaultTimeZoneRequestExtension](T_Tessa_Extensions_Platform_Server_TimeZones_SetDefaultTimeZoneRequestExtension.htm)
[Tessa.Extensions.Platform.Server.TimeZones.UpdateZonesOffsetsRequestExtension](T_Tessa_Extensions_Platform_Server_TimeZones_UpdateZonesOffsetsRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Workflow.BusinessProcessChangeBlockRequestExtension](T_Tessa_Extensions_Platform_Server_Workflow_BusinessProcessChangeBlockRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Workflow.BusinessProcessGetBlockStatusRequestExtension](T_Tessa_Extensions_Platform_Server_Workflow_BusinessProcessGetBlockStatusRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Workflow.BusinessProcessGetVersionDataRequestExtension](T_Tessa_Extensions_Platform_Server_Workflow_BusinessProcessGetVersionDataRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Workflow.BusinessProcessSetIsDefaultRequestExtension](T_Tessa_Extensions_Platform_Server_Workflow_BusinessProcessSetIsDefaultRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Workflow.WorkflowEngineCompilerRequestExtension](T_Tessa_Extensions_Platform_Server_Workflow_WorkflowEngineCompilerRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Workflow.WorkflowEngineGetSourcesRequestExtension](T_Tessa_Extensions_Platform_Server_Workflow_WorkflowEngineGetSourcesRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Workflow.WorkflowEngineProcessorRequestExtension](T_Tessa_Extensions_Platform_Server_Workflow_WorkflowEngineProcessorRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Workflow.WorkflowEngineStartProcessExtension](T_Tessa_Extensions_Platform_Server_Workflow_WorkflowEngineStartProcessExtension.htm)
[Tessa.Extensions.Platform.Server.Workflow.WorkflowServiceRequestExtension](T_Tessa_Extensions_Platform_Server_Workflow_WorkflowServiceRequestExtension.htm)
[Tessa.Extensions.Platform.Shared.Cards.CardDigestRequestExtension](T_Tessa_Extensions_Platform_Shared_Cards_CardDigestRequestExtension.htm)
[Tessa.Extensions.Platform.Shared.Cards.NoServerInGetDigestRequestExtension](T_Tessa_Extensions_Platform_Shared_Cards_NoServerInGetDigestRequestExtension.htm)
[Tessa.Extensions.Platform.Shared.Cards.SingletonDigestRequestExtension](T_Tessa_Extensions_Platform_Shared_Cards_SingletonDigestRequestExtension.htm)
[Tessa.Extensions.Platform.Shared.Numbers.NumberDigestRequestExtension](T_Tessa_Extensions_Platform_Shared_Numbers_NumberDigestRequestExtension.htm)
[Tessa.Extensions.Platform.Shared.Roles.RoleDeputiesManagementDigestRequestExtension](T_Tessa_Extensions_Platform_Shared_Roles_RoleDeputiesManagementDigestRequestExtension.htm)
Подробнее __Less __
Implements
    [ICardExtension](T_Tessa_Cards_Extensions_ICardExtension.htm), [ICardRequestExtension](T_Tessa_Cards_Extensions_ICardRequestExtension.htm), [IExtension](T_Tessa_Extensions_IExtension.htm)
##  __Конструкторы
[CardRequestExtension](M_Tessa_Cards_Extensions_CardRequestExtension__ctor.htm)|
Инициализирует новый экземпляр класса CardRequestExtension  
---|---  
##  __Методы
[AfterRequest](M_Tessa_Cards_Extensions_CardRequestExtension_AfterRequest.htm)|
Действие, выполняемое после универсального взаимодействия с сервисом карточек
как при успешном, так и при неудачном результате.  
---|---  
[AfterRequestFinally](M_Tessa_Cards_Extensions_CardRequestExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после универсального
взаимодействия с сервисом карточек как при успешном, так и при неудачном
результате. Необработанные исключения не прерывают выполнение цепочки
расширений.  
[BeforeRequest](M_Tessa_Cards_Extensions_CardRequestExtension_BeforeRequest.htm)|
Действие, выполняемое перед универсальным взаимодействием с сервисом карточек
стандартными средствами. Может установить ответ на запрос для того, чтобы
взаимодействие с сервисом карточек стандартными средствами не выполнялось.  
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
