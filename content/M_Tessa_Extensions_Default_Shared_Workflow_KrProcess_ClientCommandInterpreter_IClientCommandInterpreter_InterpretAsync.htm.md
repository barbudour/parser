# IClientCommandInterpreter.InterpretAsync - метод
Асинхронно интерпретирует набор команд.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.ClientCommandInterpreter](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     Task InterpretAsync(
    	IEnumerable<KrProcessClientCommand> commands,
    	Object outerContext,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function InterpretAsync ( 
    	commands As IEnumerable(Of KrProcessClientCommand),
    	outerContext As Object,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ InterpretAsync(
    	IEnumerable<KrProcessClientCommand^>^ commands, 
    	Object^ outerContext, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract InterpretAsync : 
            commands : IEnumerable<KrProcessClientCommand> * 
            outerContext : Object * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
commands
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[KrProcessClientCommand](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessClientCommand.htm)>
    Набор интерпретируемых команд.
outerContext [Object](https://learn.microsoft.com/dotnet/api/system.object)
    Некоторый внешний контекст, доступный для обработчкиов команд.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[IClientCommandInterpreter -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter_IClientCommandInterpreter.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.ClientCommandInterpreter -
пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter.htm)
