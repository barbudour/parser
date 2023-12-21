# ClientCommandInterpreter.InterpretAsync - метод
Асинхронно интерпретирует набор команд.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.ClientCommandInterpreter](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public Task InterpretAsync(
    	IEnumerable<KrProcessClientCommand> commands,
    	Object context,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function InterpretAsync ( 
    	commands As IEnumerable(Of KrProcessClientCommand),
    	context As Object,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ InterpretAsync(
    	IEnumerable<KrProcessClientCommand^>^ commands, 
    	Object^ context, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract InterpretAsync : 
            commands : IEnumerable<KrProcessClientCommand> * 
            context : Object * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override InterpretAsync : 
            commands : IEnumerable<KrProcessClientCommand> * 
            context : Object * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
commands
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[KrProcessClientCommand](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessClientCommand.htm)>
    Набор интерпретируемых команд.
context [Object](https://learn.microsoft.com/dotnet/api/system.object)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[IClientCommandInterpreter.InterpretAsync(IEnumerable<KrProcessClientCommand>,
Object,
CancellationToken)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter_IClientCommandInterpreter_InterpretAsync.htm)  
##  __См. также
#### Ссылки
[ClientCommandInterpreter -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter_ClientCommandInterpreter.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.ClientCommandInterpreter -
пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter.htm)
