# ClientCommandInterpreter.RegisterHandler<T>(String) - метод
Добавляет обработчик команды с указанным типом.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.ClientCommandInterpreter](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public IClientCommandInterpreter RegisterHandler<T>(
    	string commandType
    )
    where T : IClientCommandHandler
VB __Копировать
     Public Function RegisterHandler(Of T As IClientCommandHandler) ( 
    	commandType As String
    ) As IClientCommandInterpreter
C++ __Копировать
     public:
    generic<typename T>
    where T : IClientCommandHandler
    virtual IClientCommandInterpreter^ RegisterHandler(
    	String^ commandType
    ) sealed
F# __Копировать
     abstract RegisterHandler : 
            commandType : string -> IClientCommandInterpreter  when 'T : IClientCommandHandler
    override RegisterHandler : 
            commandType : string -> IClientCommandInterpreter  when 'T : IClientCommandHandler
#### Параметры
commandType [String](https://learn.microsoft.com/dotnet/api/system.string)
    Тип команды.
#### Параметры типа
T
    Тип обработчика.
#### Возвращаемое значение
[IClientCommandInterpreter](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter_IClientCommandInterpreter.htm)  
Этот интерпретатор клиентских команд.
#### Реализации
[IClientCommandInterpreter.RegisterHandler<T>(String)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter_IClientCommandInterpreter_RegisterHandler__1.htm)  
##  __См. также
#### Ссылки
[ClientCommandInterpreter -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter_ClientCommandInterpreter.htm)
[RegisterHandler -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter_ClientCommandInterpreter_RegisterHandler.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.ClientCommandInterpreter -
пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter.htm)
