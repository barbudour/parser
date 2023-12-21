# WorkflowConstants.NamesKeys.CompletedTaskRowID - поле
Имя ключа, по которому в
[Hash](P_Tessa_Workflow_Signals_IWorkflowEngineSignal_Hash.htm)[WorkflowEngineTaskSignal](T_Tessa_Workflow_Signals_WorkflowEngineTaskSignal.htm)
содержится идентификатор завершаемого задания, отправленного в процессе типа
[ResolutionProcessName](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionProcessName.htm).
Тип значения: [Guid](https://learn.microsoft.com/dotnet/api/system.guid).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public const string CompletedTaskRowID = ".CompletedTaskRowID"
VB __Копировать
     Public Const CompletedTaskRowID As String = ".CompletedTaskRowID"
C++ __Копировать
     public:
    literal String^ CompletedTaskRowID = ".CompletedTaskRowID"
F# __Копировать
     static val mutable CompletedTaskRowID: string
#### Значение поля
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __Заметки
Параметр используется при обработке завершения заданий в действии
[KrResolutionAction](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrResolutionAction.htm).
В параметре
[TaskIDs](P_Tessa_Workflow_Signals_WorkflowEngineTaskSignal_TaskIDs.htm)
указан идентификатор родительского задания типа
[WfResolutionProjectTypeID](F_Tessa_Extensions_Default_Shared_DefaultTaskTypes_WfResolutionProjectTypeID.htm).
## __См. также
#### Ссылки
[WorkflowConstants.NamesKeys -
](T_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowConstants_NamesKeys.htm)
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)
