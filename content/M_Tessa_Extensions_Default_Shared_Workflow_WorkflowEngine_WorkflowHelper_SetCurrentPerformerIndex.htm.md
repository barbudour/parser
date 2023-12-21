# WorkflowHelper.SetCurrentPerformerIndex - метод
Устанавливает порядковый номер текущего исполнителя в параметрах действия.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetCurrentPerformerIndex(
    	IDictionary<string, Object> actionHash,
    	int index
    )
VB __Копировать
     Public Shared Sub SetCurrentPerformerIndex ( 
    	actionHash As IDictionary(Of String, Object),
    	index As Integer
    )
C++ __Копировать
     public:
    static void SetCurrentPerformerIndex(
    	IDictionary<String^, Object^>^ actionHash, 
    	int index
    )
F# __Копировать
     static member SetCurrentPerformerIndex : 
            actionHash : IDictionary<string, Object> * 
            index : int -> unit 
#### Параметры
actionHash
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Параметры действия.
index [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
    Порядковый номер текущего исполнителя.
##  __См. также
#### Ссылки
[WorkflowHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)
[CurrentPerformerIndex](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowConstants_NamesKeys_CurrentPerformerIndex.htm)
