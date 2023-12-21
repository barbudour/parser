# WorkflowHelper.ProcessCycleIncrement - метод
Увеличивает номер цикла процесса согласования, содержащийся в параметрах
процесса, на указанное значение.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static int ProcessCycleIncrement(
    	IDictionary<string, Object> processHash,
    	int value = 1
    )
VB __Копировать
     Public Shared Function ProcessCycleIncrement ( 
    	processHash As IDictionary(Of String, Object),
    	Optional value As Integer = 1
    ) As Integer
C++ __Копировать
     public:
    static int ProcessCycleIncrement(
    	IDictionary<String^, Object^>^ processHash, 
    	int value = 1
    )
F# __Копировать
     static member ProcessCycleIncrement : 
            processHash : IDictionary<string, Object> * 
            ?value : int 
    (* Defaults:
            let _value = defaultArg value 1
    *)
    -> int 
#### Параметры
processHash
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Параметры процесса.
value [Int32](https://learn.microsoft.com/dotnet/api/system.int32) (Optional)
    Значение на которое увеличивается номер цикла согласования.
#### Возвращаемое значение
[Int32](https://learn.microsoft.com/dotnet/api/system.int32)  
Новое значение номера цикла согласования.
##  __Заметки
Задавая в параметре value отрицательные значения, можно реализовать декремент.
##  __См. также
#### Ссылки
[WorkflowHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)
[ProcessCycle](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowConstants_NamesKeys_ProcessCycle.htm)
