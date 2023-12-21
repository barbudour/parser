# WorkflowHelper.SetProcessCycle - метод
Устанавливает номер цикла процесса согласования в параметры процесса.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetProcessCycle(
    	IDictionary<string, Object> processHash,
    	int cycle
    )
VB __Копировать
     Public Shared Sub SetProcessCycle ( 
    	processHash As IDictionary(Of String, Object),
    	cycle As Integer
    )
C++ __Копировать
     public:
    static void SetProcessCycle(
    	IDictionary<String^, Object^>^ processHash, 
    	int cycle
    )
F# __Копировать
     static member SetProcessCycle : 
            processHash : IDictionary<string, Object> * 
            cycle : int -> unit 
#### Параметры
processHash
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Параметры процесса.
cycle [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
    Номер цикла согласования.
##  __См. также
#### Ссылки
[WorkflowHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)
[ProcessCycle](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowConstants_NamesKeys_ProcessCycle.htm)
