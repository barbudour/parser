# WorkflowSignal - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:** [Tessa.Cards.Workflow](N_Tessa_Cards_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public WorkflowSignal(
    	string processTypeName,
    	string name = null,
    	int number = 0,
    	WorkflowSignalType type = null,
    	Guid? processID = null,
    	Guid? id = null
    )
VB __Копировать
     Public Sub New ( 
    	processTypeName As String,
    	Optional name As String = Nothing,
    	Optional number As Integer = 0,
    	Optional type As WorkflowSignalType = Nothing,
    	Optional processID As Guid? = Nothing,
    	Optional id As Guid? = Nothing
    )
C++ __Копировать
     public:
    WorkflowSignal(
    	String^ processTypeName, 
    	String^ name = nullptr, 
    	int number = 0, 
    	WorkflowSignalType^ type = nullptr, 
    	Nullable<Guid> processID = nullptr, 
    	Nullable<Guid> id = nullptr
    )
F# __Копировать
     new : 
            processTypeName : string * 
            ?name : string * 
            ?number : int * 
            ?type : WorkflowSignalType * 
            ?processID : Nullable<Guid> * 
            ?id : Nullable<Guid> 
    (* Defaults:
            let _name = defaultArg name null
            let _number = defaultArg number 0
            let _type = defaultArg type null
            let _processID = defaultArg processID null
            let _id = defaultArg id null
    *)
    -> WorkflowSignal
#### Параметры
processTypeName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя типа подпроцесса, на экземпляр которого отправляется сигнал. Актуально для процессов, существующих в единственном экземпляре для карточки. Если в текущий момент активно несколько подпроцессов данного типа, то только один экземпляр (случайный) получит сигнал для обработки. 
name [String](https://learn.microsoft.com/dotnet/api/system.string) (Optional)
     Имя (алиас) сигнала, с которым может быть связана произвольная логика обработки, т.е. сигналы одного типа с разными именами могут обрабатываться по-разному. 
number [Int32](https://learn.microsoft.com/dotnet/api/system.int32) (Optional)
     Номер сигнала, по которому может определяться способ его прохождения. Можно задать совместно или вместо имени сигнала [Name](P_Tessa_Cards_Workflow_WorkflowSignal_Name.htm). 
type [WorkflowSignalType](T_Tessa_Cards_Workflow_WorkflowSignalType.htm)
(Optional)
     Тип сигнала, влияет на способ его обработки, или null, если используется сигнал по умолчанию [Default](F_Tessa_Cards_Workflow_WorkflowSignalTypes_Default.htm). 
processID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
     Идентификатор подпроцесса, к которому относится сигнал, или null, если подпроцесс определяется не по идентификатору, а по имени типа processTypeName. 
id
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
     Идентификатор сигнала или null, если создаётся сигнал с новым идентификатором. 
## __См. также
#### Ссылки
[WorkflowSignal - ](T_Tessa_Cards_Workflow_WorkflowSignal.htm)
[Tessa.Cards.Workflow - пространство имён](N_Tessa_Cards_Workflow.htm)
