# KrProcessClientCommand(String, Dictionary<String, Object>) - конструктор
Инициализируе новый экземпляр класса
[KrProcessClientCommand](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessClientCommand.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public KrProcessClientCommand(
    	string commandType,
    	Dictionary<string, Object> parameters = null
    )
VB __Копировать
     Public Sub New ( 
    	commandType As String,
    	Optional parameters As Dictionary(Of String, Object) = Nothing
    )
C++ __Копировать
     public:
    KrProcessClientCommand(
    	String^ commandType, 
    	Dictionary<String^, Object^>^ parameters = nullptr
    )
F# __Копировать
     new : 
            commandType : string * 
            ?parameters : Dictionary<string, Object> 
    (* Defaults:
            let _parameters = defaultArg parameters null
    *)
    -> KrProcessClientCommand
#### Параметры
commandType [String](https://learn.microsoft.com/dotnet/api/system.string)
    Тип команды.
parameters
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)> (Optional)
    Параметры команды.
##  __См. также
#### Ссылки
[KrProcessClientCommand -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessClientCommand.htm)
[KrProcessClientCommand -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessClientCommand__ctor.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
