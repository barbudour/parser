# ClientCommandInterpreter.RegisterHandler(String, Type) - метод
Добавляет обработчик команды с указанным типом.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.ClientCommandInterpreter](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public IClientCommandInterpreter RegisterHandler(
    	string commandType,
    	Type handlerType
    )
VB __Копировать
     Public Function RegisterHandler ( 
    	commandType As String,
    	handlerType As Type
    ) As IClientCommandInterpreter
C++ __Копировать
     public:
    virtual IClientCommandInterpreter^ RegisterHandler(
    	String^ commandType, 
    	Type^ handlerType
    ) sealed
F# __Копировать
     abstract RegisterHandler : 
            commandType : string * 
            handlerType : Type -> IClientCommandInterpreter 
    override RegisterHandler : 
            commandType : string * 
            handlerType : Type -> IClientCommandInterpreter 
#### Параметры
commandType [String](https://learn.microsoft.com/dotnet/api/system.string)
    Тип команды.
handlerType [Type](https://learn.microsoft.com/dotnet/api/system.type)
    Тип обработчика.
#### Возвращаемое значение
[IClientCommandInterpreter](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter_IClientCommandInterpreter.htm)  
Этот интерпретатор клиентских команд.
#### Реализации
[IClientCommandInterpreter.RegisterHandler(String,
Type)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter_IClientCommandInterpreter_RegisterHandler.htm)  
##  __См. также
#### Ссылки
[ClientCommandInterpreter -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter_ClientCommandInterpreter.htm)
[RegisterHandler -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter_ClientCommandInterpreter_RegisterHandler.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.ClientCommandInterpreter -
пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter.htm)
