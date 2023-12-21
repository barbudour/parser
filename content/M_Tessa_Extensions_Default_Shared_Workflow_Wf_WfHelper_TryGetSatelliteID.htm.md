# WfHelper.TryGetSatelliteID - метод
Возвращает идентификатор карточки-сателлита Workflow, сохранённого в заданном
контексте [IWorkflowContext](T_Tessa_Cards_Workflow_IWorkflowContext.htm), или
null, если идентификатор не был установлен.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.Wf](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static Guid? TryGetSatelliteID(
    	IWorkflowContext context
    )
VB __Копировать
     Public Shared Function TryGetSatelliteID ( 
    	context As IWorkflowContext
    ) As Guid?
C++ __Копировать
     public:
    static Nullable<Guid> TryGetSatelliteID(
    	IWorkflowContext^ context
    )
F# __Копировать
     static member TryGetSatelliteID : 
            context : IWorkflowContext -> Nullable<Guid> 
#### Параметры
context [IWorkflowContext](T_Tessa_Cards_Workflow_IWorkflowContext.htm)
     Контекст, для которого требуется получить идентификатор карточки-сателлита Workflow. 
#### Возвращаемое значение
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>  
Идентификатор карточки-сателлита Workflow, сохранённого в заданном контексте
[IWorkflowContext](T_Tessa_Cards_Workflow_IWorkflowContext.htm), или null,
если идентификатор не был установлен.
## __См. также
#### Ссылки
[WfHelper - ](T_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)
