# WorkflowProcessInstanceUIExtension - конструктор
Инициализирует новый экземпляр класса
[WorkflowProcessInstanceUIExtension](T_Tessa_Extensions_Platform_Client_UI_WorkflowProcessInstanceUIExtension.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI](N_Tessa_Extensions_Platform_Client_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public WorkflowProcessInstanceUIExtension(
    	IViewService viewService,
    	IUIHost uiHost,
    	Func<WorkflowInstanceCardContext> contextFactory
    )
VB __Копировать
     Public Sub New ( 
    	viewService As IViewService,
    	uiHost As IUIHost,
    	contextFactory As Func(Of WorkflowInstanceCardContext)
    )
C++ __Копировать
     public:
    WorkflowProcessInstanceUIExtension(
    	IViewService^ viewService, 
    	IUIHost^ uiHost, 
    	Func<WorkflowInstanceCardContext^>^ contextFactory
    )
F# __Копировать
     new : 
            viewService : IViewService * 
            uiHost : IUIHost * 
            contextFactory : Func<WorkflowInstanceCardContext> -> WorkflowProcessInstanceUIExtension
#### Параметры
viewService [IViewService](T_Tessa_Views_IViewService.htm)
uiHost [IUIHost](T_Tessa_UI_IUIHost.htm)
contextFactory
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[WorkflowInstanceCardContext](T_Tessa_Extensions_Platform_Client_Workflow_WorkflowInstanceCardContext.htm)>
## __См. также
#### Ссылки
[WorkflowProcessInstanceUIExtension -
](T_Tessa_Extensions_Platform_Client_UI_WorkflowProcessInstanceUIExtension.htm)
[Tessa.Extensions.Platform.Client.UI - пространство
имён](N_Tessa_Extensions_Platform_Client_UI.htm)
