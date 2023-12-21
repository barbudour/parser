# KrProcessInstance(Guid, Nullable<Guid>, String, Byte[]) - конструктор
Инициализирует новый экземпляр объекта
[KrProcessInstance](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessInstance.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public KrProcessInstance(
    	Guid processID,
    	Guid? cardID,
    	string serializedWorkflowProcess,
    	byte[] signature
    )
VB __Копировать
     Public Sub New ( 
    	processID As Guid,
    	cardID As Guid?,
    	serializedWorkflowProcess As String,
    	signature As Byte()
    )
C++ __Копировать
     public:
    KrProcessInstance(
    	Guid processID, 
    	Nullable<Guid> cardID, 
    	String^ serializedWorkflowProcess, 
    	array<unsigned char>^ signature
    )
F# __Копировать
     new : 
            processID : Guid * 
            cardID : Nullable<Guid> * 
            serializedWorkflowProcess : string * 
            signature : byte[] -> KrProcessInstance
#### Параметры
processID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор процесса.
cardID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Идентификатор карточки в которой запущен процесс.
serializedWorkflowProcess
[String](https://learn.microsoft.com/dotnet/api/system.string)
    Сериализованная объектная модель процесса.
signature [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
    Подпись serializedWorkflowProcess.
##  __См. также
#### Ссылки
[KrProcessInstance -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessInstance.htm)
[KrProcessInstance -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessInstance__ctor.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
