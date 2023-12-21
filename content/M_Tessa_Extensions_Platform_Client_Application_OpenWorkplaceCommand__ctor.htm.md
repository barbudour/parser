# OpenWorkplaceCommand - конструктор
Инициализирует новый экземпляр класса
[OpenWorkplaceCommand](T_Tessa_Extensions_Platform_Client_Application_OpenWorkplaceCommand.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Application](N_Tessa_Extensions_Platform_Client_Application.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public OpenWorkplaceCommand(
    	[NotNullAttribute] IWorkplaceService workplaceService,
    	[NotNullAttribute] IDocumentTabManager documentTabManager,
    	[NotNullAttribute] ISession session,
    	[NotNullAttribute] WorkplaceMetadataFilter workplaceMetadataFilter
    )
VB __Копировать
     Public Sub New ( 
    	<NotNullAttribute> workplaceService As IWorkplaceService,
    	<NotNullAttribute> documentTabManager As IDocumentTabManager,
    	<NotNullAttribute> session As ISession,
    	<NotNullAttribute> workplaceMetadataFilter As WorkplaceMetadataFilter
    )
C++ __Копировать
     public:
    OpenWorkplaceCommand(
    	[NotNullAttribute] IWorkplaceService^ workplaceService, 
    	[NotNullAttribute] IDocumentTabManager^ documentTabManager, 
    	[NotNullAttribute] ISession^ session, 
    	[NotNullAttribute] WorkplaceMetadataFilter^ workplaceMetadataFilter
    )
F# __Копировать
     new : 
            [<NotNullAttribute>] workplaceService : IWorkplaceService * 
            [<NotNullAttribute>] documentTabManager : IDocumentTabManager * 
            [<NotNullAttribute>] session : ISession * 
            [<NotNullAttribute>] workplaceMetadataFilter : WorkplaceMetadataFilter -> OpenWorkplaceCommand
#### Параметры
workplaceService
[IWorkplaceService](T_Tessa_Views_Workplaces_IWorkplaceService.htm)
documentTabManager
[IDocumentTabManager](T_Tessa_UI_Windows_IDocumentTabManager.htm)
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
workplaceMetadataFilter
[WorkplaceMetadataFilter](T_Tessa_Views_Workplaces_WorkplaceMetadataFilter.htm)
## __См. также
#### Ссылки
[OpenWorkplaceCommand -
](T_Tessa_Extensions_Platform_Client_Application_OpenWorkplaceCommand.htm)
[Tessa.Extensions.Platform.Client.Application - пространство
имён](N_Tessa_Extensions_Platform_Client_Application.htm)
