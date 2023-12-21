# WfHelper.SetSatelliteID - метод
Устанавливает идентификатор карточки-сателлита Workflow в контексте
[IWorkflowContext](T_Tessa_Cards_Workflow_IWorkflowContext.htm). Установка
значения, равного null, удаляет информацию из контекста.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.Wf](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetSatelliteID(
    	IWorkflowContext context,
    	Guid? satelliteID
    )
VB __Копировать
     Public Shared Sub SetSatelliteID ( 
    	context As IWorkflowContext,
    	satelliteID As Guid?
    )
C++ __Копировать
     public:
    static void SetSatelliteID(
    	IWorkflowContext^ context, 
    	Nullable<Guid> satelliteID
    )
F# __Копировать
     static member SetSatelliteID : 
            context : IWorkflowContext * 
            satelliteID : Nullable<Guid> -> unit 
#### Параметры
context [IWorkflowContext](T_Tessa_Cards_Workflow_IWorkflowContext.htm)
     Контекст, для которого требуется установить идентификатор карточки-сателлита Workflow. 
satelliteID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
     Идентификатор карточки-сателлита Workflow или null, если информацию по идентификатору требуется удалить. 
## __См. также
#### Ссылки
[WfHelper - ](T_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)
