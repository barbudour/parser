# WorkflowHelper.GetCurrentPerformerIndex - метод
Возвращает порядковый номер текущего исполнителя из параметров действия.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static int GetCurrentPerformerIndex(
    	IDictionary<string, Object> actionHash,
    	int defaultValue = 0
    )
VB __Копировать
     Public Shared Function GetCurrentPerformerIndex ( 
    	actionHash As IDictionary(Of String, Object),
    	Optional defaultValue As Integer = 0
    ) As Integer
C++ __Копировать
     public:
    static int GetCurrentPerformerIndex(
    	IDictionary<String^, Object^>^ actionHash, 
    	int defaultValue = 0
    )
F# __Копировать
     static member GetCurrentPerformerIndex : 
            actionHash : IDictionary<string, Object> * 
            ?defaultValue : int 
    (* Defaults:
            let _defaultValue = defaultArg defaultValue 0
    *)
    -> int 
#### Параметры
actionHash
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Параметры действия.
defaultValue [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
(Optional)
    Порядковый номер текущего исполнителя по умолчанию. Значение по умолчанию: 0.
#### Возвращаемое значение
[Int32](https://learn.microsoft.com/dotnet/api/system.int32)  
Порядковый номер текущего исполнителя. Если не найден в параметрах действия,
то считается равным defaultValue.
##  __См. также
#### Ссылки
[WorkflowHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)
[CurrentPerformerIndex](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowConstants_NamesKeys_CurrentPerformerIndex.htm)
