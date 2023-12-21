# OpenWorkflowEditorOnDoubleClickExtension - конструктор
Инициализирует новый экземпляр класса
[OpenWorkflowEditorOnDoubleClickExtension](T_Tessa_Extensions_Platform_Client_Cards_OpenWorkflowEditorOnDoubleClickExtension.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Cards](N_Tessa_Extensions_Platform_Client_Cards.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public OpenWorkflowEditorOnDoubleClickExtension(
    	ISession session,
    	IUIHost uiHost,
    	Func<WorkflowInstanceCardContext> contextFactory
    )
VB __Копировать
     Public Sub New ( 
    	session As ISession,
    	uiHost As IUIHost,
    	contextFactory As Func(Of WorkflowInstanceCardContext)
    )
C++ __Копировать
     public:
    OpenWorkflowEditorOnDoubleClickExtension(
    	ISession^ session, 
    	IUIHost^ uiHost, 
    	Func<WorkflowInstanceCardContext^>^ contextFactory
    )
F# __Копировать
     new : 
            session : ISession * 
            uiHost : IUIHost * 
            contextFactory : Func<WorkflowInstanceCardContext> -> OpenWorkflowEditorOnDoubleClickExtension
#### Параметры
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
uiHost [IUIHost](T_Tessa_UI_IUIHost.htm)
contextFactory
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[WorkflowInstanceCardContext](T_Tessa_Extensions_Platform_Client_Workflow_WorkflowInstanceCardContext.htm)>
## __См. также
#### Ссылки
[OpenWorkflowEditorOnDoubleClickExtension -
](T_Tessa_Extensions_Platform_Client_Cards_OpenWorkflowEditorOnDoubleClickExtension.htm)
[Tessa.Extensions.Platform.Client.Cards - пространство
имён](N_Tessa_Extensions_Platform_Client_Cards.htm)
