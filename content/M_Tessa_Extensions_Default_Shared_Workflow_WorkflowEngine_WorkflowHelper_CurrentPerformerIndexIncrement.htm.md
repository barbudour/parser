# WorkflowHelper.CurrentPerformerIndexIncrement - метод
Увеличивает на указанное число порядковый номер текущего исполнителя.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static int CurrentPerformerIndexIncrement(
    	IDictionary<string, Object> actionHash,
    	int value = 1
    )
VB __Копировать
     Public Shared Function CurrentPerformerIndexIncrement ( 
    	actionHash As IDictionary(Of String, Object),
    	Optional value As Integer = 1
    ) As Integer
C++ __Копировать
     public:
    static int CurrentPerformerIndexIncrement(
    	IDictionary<String^, Object^>^ actionHash, 
    	int value = 1
    )
F# __Копировать
     static member CurrentPerformerIndexIncrement : 
            actionHash : IDictionary<string, Object> * 
            ?value : int 
    (* Defaults:
            let _value = defaultArg value 1
    *)
    -> int 
#### Параметры
actionHash
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Параметры действия.
value [Int32](https://learn.microsoft.com/dotnet/api/system.int32) (Optional)
    Значение на которое выполняется увеличение.
#### Возвращаемое значение
[Int32](https://learn.microsoft.com/dotnet/api/system.int32)  
Новое значение.
##  __См. также
#### Ссылки
[WorkflowHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)
[CurrentPerformerIndex](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowConstants_NamesKeys_CurrentPerformerIndex.htm)
