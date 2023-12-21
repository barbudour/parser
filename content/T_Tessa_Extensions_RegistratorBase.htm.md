# RegistratorBase - класс
Базовый класс для объектов регистраторов, реализующих интерфейс
[IRegistrator](T_Tessa_Extensions_IRegistrator.htm).
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class RegistratorBase : IRegistrator, 
    	ISealable
VB __Копировать
     Public MustInherit Class RegistratorBase
    	Implements IRegistrator, ISealable
C++ __Копировать
     public ref class RegistratorBase abstract : IRegistrator, 
    	ISealable
F# __Копировать
     [<AbstractClassAttribute>]
    type RegistratorBase = 
        class
            interface IRegistrator
            interface ISealable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ RegistratorBase
Derived
[Tessa.Extensions.Default.Chronos.Notices.Registrator](T_Tessa_Extensions_Default_Chronos_Notices_Registrator.htm)
[Tessa.Extensions.Default.Chronos.OnlyOffice.Registrator](T_Tessa_Extensions_Default_Chronos_OnlyOffice_Registrator.htm)
[Tessa.Extensions.Default.Chronos.Workflow.Registrator](T_Tessa_Extensions_Default_Chronos_Workflow_Registrator.htm)
[Tessa.Extensions.Default.Client.Acquaintance.Registrator](T_Tessa_Extensions_Default_Client_Acquaintance_Registrator.htm)
[Tessa.Extensions.Default.Client.Cards.Registrator](T_Tessa_Extensions_Default_Client_Cards_Registrator.htm)
[Tessa.Extensions.Default.Client.DocLoad.Registrator](T_Tessa_Extensions_Default_Client_DocLoad_Registrator.htm)
[Tessa.Extensions.Default.Client.Documents.Registrator](T_Tessa_Extensions_Default_Client_Documents_Registrator.htm)
[Tessa.Extensions.Default.Client.EDS.Registrator](T_Tessa_Extensions_Default_Client_EDS_Registrator.htm)
[Tessa.Extensions.Default.Client.Extensions.Registrator](T_Tessa_Extensions_Default_Client_Extensions_Registrator.htm)
[Tessa.Extensions.Default.Client.ExternalFiles.Registrator](T_Tessa_Extensions_Default_Client_ExternalFiles_Registrator.htm)
[Tessa.Extensions.Default.Client.Files.Registrator](T_Tessa_Extensions_Default_Client_Files_Registrator.htm)
[Tessa.Extensions.Default.Client.Forums.Registrator](T_Tessa_Extensions_Default_Client_Forums_Registrator.htm)
[Tessa.Extensions.Default.Client.Initialization.Registrator](T_Tessa_Extensions_Default_Client_Initialization_Registrator.htm)
[Tessa.Extensions.Default.Client.Notifications.Registrator](T_Tessa_Extensions_Default_Client_Notifications_Registrator.htm)
[Tessa.Extensions.Default.Client.Pdf.Registrator](T_Tessa_Extensions_Default_Client_Pdf_Registrator.htm)
[Tessa.Extensions.Default.Client.Registrator](T_Tessa_Extensions_Default_Client_Registrator.htm)
[Tessa.Extensions.Default.Client.Scanning.Registrator](T_Tessa_Extensions_Default_Client_Scanning_Registrator.htm)
[Tessa.Extensions.Default.Client.Tiles.Registrator](T_Tessa_Extensions_Default_Client_Tiles_Registrator.htm)
[Tessa.Extensions.Default.Client.UI.KrProcess.StageHandlers.Registrator](T_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_Registrator.htm)
[Tessa.Extensions.Default.Client.UI.Registrator](T_Tessa_Extensions_Default_Client_UI_Registrator.htm)
[Tessa.Extensions.Default.Client.Views.Registrator](T_Tessa_Extensions_Default_Client_Views_Registrator.htm)
[Tessa.Extensions.Default.Client.Workflow.KrCompilers.Registrator](T_Tessa_Extensions_Default_Client_Workflow_KrCompilers_Registrator.htm)
[Tessa.Extensions.Default.Client.Workflow.KrPermissions.Registrator](T_Tessa_Extensions_Default_Client_Workflow_KrPermissions_Registrator.htm)
[Tessa.Extensions.Default.Client.Workflow.KrProcess.CommandInterpreter.Registrator](T_Tessa_Extensions_Default_Client_Workflow_KrProcess_CommandInterpreter_Registrator.htm)
[Tessa.Extensions.Default.Client.Workflow.KrProcess.Initialization.Registrator](T_Tessa_Extensions_Default_Client_Workflow_KrProcess_Initialization_Registrator.htm)
[Tessa.Extensions.Default.Client.Workflow.KrProcess.Registrator](T_Tessa_Extensions_Default_Client_Workflow_KrProcess_Registrator.htm)
[Tessa.Extensions.Default.Client.Workflow.KrProcess.Requests.Registrator](T_Tessa_Extensions_Default_Client_Workflow_KrProcess_Requests_Registrator.htm)
[Tessa.Extensions.Default.Client.Workflow.KrProcess.SecondRegistrator](T_Tessa_Extensions_Default_Client_Workflow_KrProcess_SecondRegistrator.htm)
[Tessa.Extensions.Default.Client.Workflow.Wf.Registrator](T_Tessa_Extensions_Default_Client_Workflow_Wf_Registrator.htm)
[Tessa.Extensions.Default.Client.Workflow.WorkflowEngine.Registrator](T_Tessa_Extensions_Default_Client_Workflow_WorkflowEngine_Registrator.htm)
[Tessa.Extensions.Default.Client.WorkflowViewer.Registrator](T_Tessa_Extensions_Default_Client_WorkflowViewer_Registrator.htm)
[Tessa.Extensions.Default.Console.CheckService.OperationRegistrator](T_Tessa_Extensions_Default_Console_CheckService_OperationRegistrator.htm)
[Tessa.Extensions.Default.Console.ConvertCards.OperationRegistrator](T_Tessa_Extensions_Default_Console_ConvertCards_OperationRegistrator.htm)
[Tessa.Extensions.Default.Console.ConvertConfiguration.OperationRegistrator](T_Tessa_Extensions_Default_Console_ConvertConfiguration_OperationRegistrator.htm)
[Tessa.Extensions.Default.Console.CreateFromTemplate.OperationRegistrator](T_Tessa_Extensions_Default_Console_CreateFromTemplate_OperationRegistrator.htm)
[Tessa.Extensions.Default.Console.DeleteCards.OperationRegistrator](T_Tessa_Extensions_Default_Console_DeleteCards_OperationRegistrator.htm)
[Tessa.Extensions.Default.Console.ExportCards.OperationRegistrator](T_Tessa_Extensions_Default_Console_ExportCards_OperationRegistrator.htm)
[Tessa.Extensions.Default.Console.ExportLocalization.OperationRegistrator](T_Tessa_Extensions_Default_Console_ExportLocalization_OperationRegistrator.htm)
[Tessa.Extensions.Default.Console.ExportScheme.OperationRegistrator](T_Tessa_Extensions_Default_Console_ExportScheme_OperationRegistrator.htm)
[Tessa.Extensions.Default.Console.ExportSearchQueries.OperationRegistrator](T_Tessa_Extensions_Default_Console_ExportSearchQueries_OperationRegistrator.htm)
[Tessa.Extensions.Default.Console.ExportTypes.OperationRegistrator](T_Tessa_Extensions_Default_Console_ExportTypes_OperationRegistrator.htm)
[Tessa.Extensions.Default.Console.ExportViews.OperationRegistrator](T_Tessa_Extensions_Default_Console_ExportViews_OperationRegistrator.htm)
[Tessa.Extensions.Default.Console.ExportWorkplaces.OperationRegistrator](T_Tessa_Extensions_Default_Console_ExportWorkplaces_OperationRegistrator.htm)
[Tessa.Extensions.Default.Console.FileSource.OperationRegistrator](T_Tessa_Extensions_Default_Console_FileSource_OperationRegistrator.htm)
[Tessa.Extensions.Default.Console.ImportCards.OperationRegistrator](T_Tessa_Extensions_Default_Console_ImportCards_OperationRegistrator.htm)
[Tessa.Extensions.Default.Console.ImportLocalization.OperationRegistrator](T_Tessa_Extensions_Default_Console_ImportLocalization_OperationRegistrator.htm)
[Tessa.Extensions.Default.Console.ImportScheme.OperationRegistrator](T_Tessa_Extensions_Default_Console_ImportScheme_OperationRegistrator.htm)
[Tessa.Extensions.Default.Console.ImportSearchQueries.OperationRegistrator](T_Tessa_Extensions_Default_Console_ImportSearchQueries_OperationRegistrator.htm)
[Tessa.Extensions.Default.Console.ImportTypes.OperationRegistrator](T_Tessa_Extensions_Default_Console_ImportTypes_OperationRegistrator.htm)
[Tessa.Extensions.Default.Console.ImportUsers.OperationRegistrator](T_Tessa_Extensions_Default_Console_ImportUsers_OperationRegistrator.htm)
[Tessa.Extensions.Default.Console.ImportViews.OperationRegistrator](T_Tessa_Extensions_Default_Console_ImportViews_OperationRegistrator.htm)
[Tessa.Extensions.Default.Console.ImportWorkplaces.OperationRegistrator](T_Tessa_Extensions_Default_Console_ImportWorkplaces_OperationRegistrator.htm)
[Tessa.Extensions.Default.Console.IncrementVersion.OperationRegistrator](T_Tessa_Extensions_Default_Console_IncrementVersion_OperationRegistrator.htm)
[Tessa.Extensions.Default.Console.InvalidateCache.OperationRegistrator](T_Tessa_Extensions_Default_Console_InvalidateCache_OperationRegistrator.htm)
[Tessa.Extensions.Default.Console.ManageRoles.OperationRegistrator](T_Tessa_Extensions_Default_Console_ManageRoles_OperationRegistrator.htm)
[Tessa.Extensions.Default.Console.RebuildCalendar.OperationRegistrator](T_Tessa_Extensions_Default_Console_RebuildCalendar_OperationRegistrator.htm)
[Tessa.Extensions.Default.Console.TimeZone.OperationRegistrator](T_Tessa_Extensions_Default_Console_TimeZone_OperationRegistrator.htm)
[Tessa.Extensions.Default.Console.User.OperationRegistrator](T_Tessa_Extensions_Default_Console_User_OperationRegistrator.htm)
[Tessa.Extensions.Default.Server.Acquaintance.Registrator](T_Tessa_Extensions_Default_Server_Acquaintance_Registrator.htm)
[Tessa.Extensions.Default.Server.BusinessCalendar.Registrator](T_Tessa_Extensions_Default_Server_BusinessCalendar_Registrator.htm)
[Tessa.Extensions.Default.Server.Caching.Registrator](T_Tessa_Extensions_Default_Server_Caching_Registrator.htm)
[Tessa.Extensions.Default.Server.Cards.Registrator](T_Tessa_Extensions_Default_Server_Cards_Registrator.htm)
[Tessa.Extensions.Default.Server.DocLoad.Registrator](T_Tessa_Extensions_Default_Server_DocLoad_Registrator.htm)
[Tessa.Extensions.Default.Server.EDS.Registrator](T_Tessa_Extensions_Default_Server_EDS_Registrator.htm)
[Tessa.Extensions.Default.Server.Files.Registrator](T_Tessa_Extensions_Default_Server_Files_Registrator.htm)
[Tessa.Extensions.Default.Server.Files.VirtualFiles.Registrator](T_Tessa_Extensions_Default_Server_Files_VirtualFiles_Registrator.htm)
[Tessa.Extensions.Default.Server.Forums.Notifications.Registrator](T_Tessa_Extensions_Default_Server_Forums_Notifications_Registrator.htm)
[Tessa.Extensions.Default.Server.Forums.Registrator](T_Tessa_Extensions_Default_Server_Forums_Registrator.htm)
[Tessa.Extensions.Default.Server.Initialization.Registrator](T_Tessa_Extensions_Default_Server_Initialization_Registrator.htm)
[Tessa.Extensions.Default.Server.Notices.Registrator](T_Tessa_Extensions_Default_Server_Notices_Registrator.htm)
[Tessa.Extensions.Default.Server.OnlyOffice.Registrator](T_Tessa_Extensions_Default_Server_OnlyOffice_Registrator.htm)
[Tessa.Extensions.Default.Server.References.Registrator](T_Tessa_Extensions_Default_Server_References_Registrator.htm)
[Tessa.Extensions.Default.Server.Test.Registrator](T_Tessa_Extensions_Default_Server_Test_Registrator.htm)
[Tessa.Extensions.Default.Server.Views.Registrator](T_Tessa_Extensions_Default_Server_Views_Registrator.htm)
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.Registrator](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Registrator.htm)
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.Requests.Registrator](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_Registrator.htm)
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.SourceBuilders.Registrator](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_Registrator.htm)
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.SqlProcessing.Registrator](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_Registrator.htm)
[Tessa.Extensions.Default.Server.Workflow.KrObjectModel.Registrator](T_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Registrator.htm)
[Tessa.Extensions.Default.Server.Workflow.KrPermissions.Registrator](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_Registrator.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Actions.Registrator](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Actions_Registrator.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Events.Registrator](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_Registrator.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Initialization.Registrator](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Initialization_Registrator.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Registrator](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Registrator.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Requests.Registrator](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Requests_Registrator.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Satellite.Registrator](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Satellite_Registrator.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Scope.Registrator](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_Registrator.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Serialization.Registrator](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_Registrator.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.StageTypeRequests.Registrator](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_StageTypeRequests_Registrator.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.GlobalSignals.Registrator](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_GlobalSignals_Registrator.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers.Registrator](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_Registrator.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Registrator](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Registrator.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.StateMachine.Registrator](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_StateMachine_Registrator.htm)
[Tessa.Extensions.Default.Server.Workflow.Registrator](T_Tessa_Extensions_Default_Server_Workflow_Registrator.htm)
[Tessa.Extensions.Default.Server.Workflow.TestProcess.Registrator](T_Tessa_Extensions_Default_Server_Workflow_TestProcess_Registrator.htm)
[Tessa.Extensions.Default.Server.Workflow.Wf.Registrator](T_Tessa_Extensions_Default_Server_Workflow_Wf_Registrator.htm)
[Tessa.Extensions.Default.Server.Workflow.WorkflowEngine.Registrator](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_Registrator.htm)
[Tessa.Extensions.Default.Server.Workflow.WorkflowViewer.Registrator](T_Tessa_Extensions_Default_Server_Workflow_WorkflowViewer_Registrator.htm)
[Tessa.Extensions.Default.Shared.Conditions.Registrator](T_Tessa_Extensions_Default_Shared_Conditions_Registrator.htm)
[Tessa.Extensions.Default.Shared.EDS.Registrator](T_Tessa_Extensions_Default_Shared_EDS_Registrator.htm)
[Tessa.Extensions.Default.Shared.Initialization.ConsoleRegistrator](T_Tessa_Extensions_Default_Shared_Initialization_ConsoleRegistrator.htm)
[Tessa.Extensions.Default.Shared.Notices.Registrator](T_Tessa_Extensions_Default_Shared_Notices_Registrator.htm)
[Tessa.Extensions.Default.Shared.Numbers.Registrator](T_Tessa_Extensions_Default_Shared_Numbers_Registrator.htm)
[Tessa.Extensions.Default.Shared.Registrator](T_Tessa_Extensions_Default_Shared_Registrator.htm)
[Tessa.Extensions.Default.Shared.Settings.ClientMetadataRegistrator](T_Tessa_Extensions_Default_Shared_Settings_ClientMetadataRegistrator.htm)
[Tessa.Extensions.Default.Shared.Settings.Registrator](T_Tessa_Extensions_Default_Shared_Settings_Registrator.htm)
[Tessa.Extensions.Default.Shared.StorageMapping.Registrator](T_Tessa_Extensions_Default_Shared_StorageMapping_Registrator.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions.ClientMetadataRegistrator](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_ClientMetadataRegistrator.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions.Registrator](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_Registrator.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions.RepairRegistrator](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_RepairRegistrator.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.ClientCommandInterpreter.Registrator](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter_Registrator.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.ClientRegistrator](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientRegistrator.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters.StageTypeFormattersRegistrator](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_StageTypeFormattersRegistrator.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Registrator](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Registrator.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.RepairRegistrator](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_RepairRegistrator.htm)
[Tessa.Extensions.Default.Shared.Workflow.Wf.ClientMetadataRegistrator](T_Tessa_Extensions_Default_Shared_Workflow_Wf_ClientMetadataRegistrator.htm)
[Tessa.Extensions.Default.Shared.Workflow.Wf.RepairRegistrator](T_Tessa_Extensions_Default_Shared_Workflow_Wf_RepairRegistrator.htm)
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine.Registrator](T_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_Registrator.htm)
[Tessa.Extensions.Platform.Client.Application.Registrator](T_Tessa_Extensions_Platform_Client_Application_Registrator.htm)
[Tessa.Extensions.Platform.Client.Cards.Registrator](T_Tessa_Extensions_Platform_Client_Cards_Registrator.htm)
[Tessa.Extensions.Platform.Client.Files.Registrator](T_Tessa_Extensions_Platform_Client_Files_Registrator.htm)
[Tessa.Extensions.Platform.Client.Initialization.AppManagerRegistrator](T_Tessa_Extensions_Platform_Client_Initialization_AppManagerRegistrator.htm)
[Tessa.Extensions.Platform.Client.Initialization.Registrator](T_Tessa_Extensions_Platform_Client_Initialization_Registrator.htm)
[Tessa.Extensions.Platform.Client.Links.Registrator](T_Tessa_Extensions_Platform_Client_Links_Registrator.htm)
[Tessa.Extensions.Platform.Client.Registrator](T_Tessa_Extensions_Platform_Client_Registrator.htm)
[Tessa.Extensions.Platform.Client.Scanning.Registrator](T_Tessa_Extensions_Platform_Client_Scanning_Registrator.htm)
[Tessa.Extensions.Platform.Client.Tiles.Registrator](T_Tessa_Extensions_Platform_Client_Tiles_Registrator.htm)
[Tessa.Extensions.Platform.Client.UI.CleanupFields.Registrator](T_Tessa_Extensions_Platform_Client_UI_CleanupFields_Registrator.htm)
[Tessa.Extensions.Platform.Client.UI.Registrator](T_Tessa_Extensions_Platform_Client_UI_Registrator.htm)
[Tessa.Extensions.Platform.Client.UI.TimeZones.Registrator](T_Tessa_Extensions_Platform_Client_UI_TimeZones_Registrator.htm)
[Tessa.Extensions.Platform.Client.Workflow.Registrator](T_Tessa_Extensions_Platform_Client_Workflow_Registrator.htm)
[Tessa.Extensions.Platform.Server.AdSync.Registrator](T_Tessa_Extensions_Platform_Server_AdSync_Registrator.htm)
[Tessa.Extensions.Platform.Server.BusinessCalendar.Registrator](T_Tessa_Extensions_Platform_Server_BusinessCalendar_Registrator.htm)
[Tessa.Extensions.Platform.Server.Caching.Registrator](T_Tessa_Extensions_Platform_Server_Caching_Registrator.htm)
[Tessa.Extensions.Platform.Server.Cards.Registrator](T_Tessa_Extensions_Platform_Server_Cards_Registrator.htm)
[Tessa.Extensions.Platform.Server.Cards.Satellites.Registrator](T_Tessa_Extensions_Platform_Server_Cards_Satellites_Registrator.htm)
[Tessa.Extensions.Platform.Server.Cards.Satellites.RegistratorShared](T_Tessa_Extensions_Platform_Server_Cards_Satellites_RegistratorShared.htm)
[Tessa.Extensions.Platform.Server.DocLoad.Registrator](T_Tessa_Extensions_Platform_Server_DocLoad_Registrator.htm)
[Tessa.Extensions.Platform.Server.Forums.Registrator](T_Tessa_Extensions_Platform_Server_Forums_Registrator.htm)
[Tessa.Extensions.Platform.Server.Initialization.Registrator](T_Tessa_Extensions_Platform_Server_Initialization_Registrator.htm)
[Tessa.Extensions.Platform.Server.Numbers.Registrator](T_Tessa_Extensions_Platform_Server_Numbers_Registrator.htm)
[Tessa.Extensions.Platform.Server.Placeholders.Registrator](T_Tessa_Extensions_Platform_Server_Placeholders_Registrator.htm)
[Tessa.Extensions.Platform.Server.Plugins.Registrator](T_Tessa_Extensions_Platform_Server_Plugins_Registrator.htm)
[Tessa.Extensions.Platform.Server.Roles.Registrator](T_Tessa_Extensions_Platform_Server_Roles_Registrator.htm)
[Tessa.Extensions.Platform.Server.TimeZones.Registrator](T_Tessa_Extensions_Platform_Server_TimeZones_Registrator.htm)
[Tessa.Extensions.Platform.Server.Views.Registrator](T_Tessa_Extensions_Platform_Server_Views_Registrator.htm)
[Tessa.Extensions.Platform.Server.Workflow.Registrator](T_Tessa_Extensions_Platform_Server_Workflow_Registrator.htm)
[Tessa.Extensions.Platform.Server.Workflow.RegistratorShared](T_Tessa_Extensions_Platform_Server_Workflow_RegistratorShared.htm)
[Tessa.Extensions.Platform.Shared.Cards.ClientAndConsoleRegistrator](T_Tessa_Extensions_Platform_Shared_Cards_ClientAndConsoleRegistrator.htm)
[Tessa.Extensions.Platform.Shared.Cards.ClientMetadataRegistrator](T_Tessa_Extensions_Platform_Shared_Cards_ClientMetadataRegistrator.htm)
[Tessa.Extensions.Platform.Shared.Cards.RepairRegistrator](T_Tessa_Extensions_Platform_Shared_Cards_RepairRegistrator.htm)
[Tessa.Extensions.Platform.Shared.Conditions.RepairRegistrator](T_Tessa_Extensions_Platform_Shared_Conditions_RepairRegistrator.htm)
[Tessa.Extensions.Platform.Shared.Initialization.Registrator](T_Tessa_Extensions_Platform_Shared_Initialization_Registrator.htm)
[Tessa.Extensions.Platform.Shared.Placeholders.Registrator](T_Tessa_Extensions_Platform_Shared_Placeholders_Registrator.htm)
[Tessa.Extensions.Platform.Shared.Roles.ClientAndConsoleRegistrator](T_Tessa_Extensions_Platform_Shared_Roles_ClientAndConsoleRegistrator.htm)
[Tessa.Extensions.Platform.Shared.Settings.Registrator](T_Tessa_Extensions_Platform_Shared_Settings_Registrator.htm)
Подробнее __Less __
Implements
    [IRegistrator](T_Tessa_Extensions_IRegistrator.htm), [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Конструкторы
[RegistratorBase](M_Tessa_Extensions_RegistratorBase__ctor.htm)|
Инициализирует новый экземпляр класса RegistratorBase  
---|---  
##  __Свойства
[InstanceName](P_Tessa_Extensions_RegistratorBase_InstanceName.htm)|  Имя
экземпляра сервера или null, если регистрация выполняется на клиенте.  
---|---  
[IsPlatform](P_Tessa_Extensions_RegistratorBase_IsPlatform.htm)|  Признак
того, что объект выполняет регистрацию платформенных расширений. Этот признак
используется системой, не рекомендуется его устанавливать.  
[IsSealed](P_Tessa_Extensions_RegistratorBase_IsSealed.htm)| Признак того, что
объект был защищён от изменений.  
[SessionType](P_Tessa_Extensions_RegistratorBase_SessionType.htm)| Тип сессии.  
[Tag](P_Tessa_Extensions_RegistratorBase_Tag.htm)|  Флаговое перечисление с
тегами регистратора, которые ограничивают область его использования. По
умолчанию используются теги [Tessa.Extensions.RegistratorTag.Default].  
[UnityContainer](P_Tessa_Extensions_RegistratorBase_UnityContainer.htm)|
Контейнер Unity, в котором выполняется регистрация. Гарантированно не равен
null.  
## __Методы
[CheckSealed](M_Tessa_Extensions_RegistratorBase_CheckSealed.htm)|
Выбрасывает исключение [Tessa.Platform.ObjectSealedException], если объект был
защищён от изменений.  
---|---  
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
[FinalizeRegistration](M_Tessa_Extensions_RegistratorBase_FinalizeRegistration.htm)|
Завершает регистрацию. В этом методе рекомендуется получить зависимости из
Unity и выполнить их настройку.  
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
[InitializeExtensions](M_Tessa_Extensions_RegistratorBase_InitializeExtensions.htm)|
Выполняет инициализацию заданного контейнера расширений. Рекомендуется не
выполнять регистрацию Unity в этом объекте.  
[InitializeRegistration](M_Tessa_Extensions_RegistratorBase_InitializeRegistration.htm)|
Инициализирует регистрацию. В этом методе рекомендуется зарегистрировать
зависимости в Unity, которые необходимы уже на момент регистрации расширений.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[RegisterExtensions](M_Tessa_Extensions_RegistratorBase_RegisterExtensions.htm)|
Выполняет регистрацию расширений. Рекомендуется не выполнять регистрацию Unity
в этом объекте.  
[RegisterUnity](M_Tessa_Extensions_RegistratorBase_RegisterUnity.htm)|
Выполняет регистрацию объектов расширений и их зависимостей в контейнере
Unity.  
[Seal](M_Tessa_Extensions_RegistratorBase_Seal.htm)| Защищает объект от
изменений.  
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
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
