# IClientCommandInterpreter.RegisterHandler(String, Type) - метод
Добавляет обработчик команды с указанным типом.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.ClientCommandInterpreter](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     IClientCommandInterpreter RegisterHandler(
    	string commandType,
    	Type handlerType
    )
VB __Копировать
     Function RegisterHandler ( 
    	commandType As String,
    	handlerType As Type
    ) As IClientCommandInterpreter
C++ __Копировать
    IClientCommandInterpreter^ RegisterHandler(
    	String^ commandType, 
    	Type^ handlerType
    )
F# __Копировать
     abstract RegisterHandler : 
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
##  __См. также
#### Ссылки
[IClientCommandInterpreter -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter_IClientCommandInterpreter.htm)
[RegisterHandler -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter_IClientCommandInterpreter_RegisterHandler.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.ClientCommandInterpreter -
пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter.htm)
