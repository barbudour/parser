# WorkflowHelper.GetProcessCycle - метод
Возвращает номер текущего цикла процесса согласования.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static int GetProcessCycle(
    	IDictionary<string, Object> processHash,
    	int defaultValue = 1
    )
VB __Копировать
     Public Shared Function GetProcessCycle ( 
    	processHash As IDictionary(Of String, Object),
    	Optional defaultValue As Integer = 1
    ) As Integer
C++ __Копировать
     public:
    static int GetProcessCycle(
    	IDictionary<String^, Object^>^ processHash, 
    	int defaultValue = 1
    )
F# __Копировать
     static member GetProcessCycle : 
            processHash : IDictionary<string, Object> * 
            ?defaultValue : int 
    (* Defaults:
            let _defaultValue = defaultArg defaultValue 1
    *)
    -> int 
#### Параметры
processHash
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Параметры процесса.
defaultValue [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
(Optional)
    Номер цикла по умолчанию. Значение по умолчанию: 1.
#### Возвращаемое значение
[Int32](https://learn.microsoft.com/dotnet/api/system.int32)  
Номер текущего цикла процесса согласования. Если не найден в параметрах
процесса, то считается равным defaultValue.
##  __См. также
#### Ссылки
[WorkflowHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)
[ProcessCycle](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowConstants_NamesKeys_ProcessCycle.htm)
