# WorkplacesExtension - конструктор
Инициализирует новый экземпляр класса
[WorkplacesExtension](T_Tessa_Extensions_Platform_Client_Application_WorkplacesExtension.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Application](N_Tessa_Extensions_Platform_Client_Application.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public WorkplacesExtension(
    	[OptionalDependencyAttribute][CanBeNullAttribute] Func<IAdvancedTessaShell> resolveShellFunc,
    	[NotNullAttribute] ISession session,
    	[NotNullAttribute] IUserSettings settings,
    	[OptionalDependencyAttribute][CanBeNullAttribute] IDocumentTabManager documentTabManager,
    	[OptionalDependencyAttribute][CanBeNullAttribute] IWorkplaceService workplaceService,
    	[OptionalDependencyAttribute][CanBeNullAttribute] IIconContainer iconContainer,
    	[OptionalDependencyAttribute][CanBeNullAttribute] OpenWorkplaceCommand openWorkplaceCommand,
    	[OptionalDependencyAttribute][CanBeNullAttribute] WorkplaceMetadataFilter workplaceMetadataFilter
    )
VB __Копировать
     Public Sub New ( 
    	<OptionalDependencyAttribute><CanBeNullAttribute> resolveShellFunc As Func(Of IAdvancedTessaShell),
    	<NotNullAttribute> session As ISession,
    	<NotNullAttribute> settings As IUserSettings,
    	<OptionalDependencyAttribute><CanBeNullAttribute> documentTabManager As IDocumentTabManager,
    	<OptionalDependencyAttribute><CanBeNullAttribute> workplaceService As IWorkplaceService,
    	<OptionalDependencyAttribute><CanBeNullAttribute> iconContainer As IIconContainer,
    	<OptionalDependencyAttribute><CanBeNullAttribute> openWorkplaceCommand As OpenWorkplaceCommand,
    	<OptionalDependencyAttribute><CanBeNullAttribute> workplaceMetadataFilter As WorkplaceMetadataFilter
    )
C++ __Копировать
     public:
    WorkplacesExtension(
    	[OptionalDependencyAttribute][CanBeNullAttribute] Func<IAdvancedTessaShell^>^ resolveShellFunc, 
    	[NotNullAttribute] ISession^ session, 
    	[NotNullAttribute] IUserSettings^ settings, 
    	[OptionalDependencyAttribute][CanBeNullAttribute] IDocumentTabManager^ documentTabManager, 
    	[OptionalDependencyAttribute][CanBeNullAttribute] IWorkplaceService^ workplaceService, 
    	[OptionalDependencyAttribute][CanBeNullAttribute] IIconContainer^ iconContainer, 
    	[OptionalDependencyAttribute][CanBeNullAttribute] OpenWorkplaceCommand^ openWorkplaceCommand, 
    	[OptionalDependencyAttribute][CanBeNullAttribute] WorkplaceMetadataFilter^ workplaceMetadataFilter
    )
F# __Копировать
     new : 
            [<OptionalDependencyAttribute>][<CanBeNullAttribute>] resolveShellFunc : Func<IAdvancedTessaShell> * 
            [<NotNullAttribute>] session : ISession * 
            [<NotNullAttribute>] settings : IUserSettings * 
            [<OptionalDependencyAttribute>][<CanBeNullAttribute>] documentTabManager : IDocumentTabManager * 
            [<OptionalDependencyAttribute>][<CanBeNullAttribute>] workplaceService : IWorkplaceService * 
            [<OptionalDependencyAttribute>][<CanBeNullAttribute>] iconContainer : IIconContainer * 
            [<OptionalDependencyAttribute>][<CanBeNullAttribute>] openWorkplaceCommand : OpenWorkplaceCommand * 
            [<OptionalDependencyAttribute>][<CanBeNullAttribute>] workplaceMetadataFilter : WorkplaceMetadataFilter -> WorkplacesExtension
#### Параметры
resolveShellFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[IAdvancedTessaShell](T_Tessa_UI_Windows_IAdvancedTessaShell.htm)>
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
settings [IUserSettings](T_Tessa_UI_IUserSettings.htm)
documentTabManager
[IDocumentTabManager](T_Tessa_UI_Windows_IDocumentTabManager.htm)
workplaceService
[IWorkplaceService](T_Tessa_Views_Workplaces_IWorkplaceService.htm)
iconContainer [IIconContainer](T_Tessa_UI_IIconContainer.htm)
openWorkplaceCommand
[OpenWorkplaceCommand](T_Tessa_Extensions_Platform_Client_Application_OpenWorkplaceCommand.htm)
workplaceMetadataFilter
[WorkplaceMetadataFilter](T_Tessa_Views_Workplaces_WorkplaceMetadataFilter.htm)
## __См. также
#### Ссылки
[WorkplacesExtension -
](T_Tessa_Extensions_Platform_Client_Application_WorkplacesExtension.htm)
[Tessa.Extensions.Platform.Client.Application - пространство
имён](N_Tessa_Extensions_Platform_Client_Application.htm)
