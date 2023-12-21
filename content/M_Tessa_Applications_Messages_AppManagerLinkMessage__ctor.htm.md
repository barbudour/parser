# AppManagerLinkMessage(String, String, String, String, Int32) - конструктор
Initializes a new instance of the
[AppManagerLinkMessage](T_Tessa_Applications_Messages_AppManagerLinkMessage.htm)
class. Initializes a new instance of the
[ApplicationLinkMessage](T_Tessa_Applications_Messages_ApplicationLinkMessage.htm)
class.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Messages](N_Tessa_Applications_Messages.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public AppManagerLinkMessage(
    	[NotNullAttribute] string alias,
    	[NotNullAttribute] string linkArgs,
    	[CanBeNullAttribute] string serverCode = "",
    	[CanBeNullAttribute] string instanceName = "",
    	int processId = 0
    )
VB __Копировать
     Public Sub New ( 
    	<NotNullAttribute> alias As String,
    	<NotNullAttribute> linkArgs As String,
    	<CanBeNullAttribute> Optional serverCode As String = "",
    	<CanBeNullAttribute> Optional instanceName As String = "",
    	Optional processId As Integer = 0
    )
C++ __Копировать
     public:
    AppManagerLinkMessage(
    	[NotNullAttribute] String^ alias, 
    	[NotNullAttribute] String^ linkArgs, 
    	[CanBeNullAttribute] String^ serverCode = L"", 
    	[CanBeNullAttribute] String^ instanceName = L"", 
    	int processId = 0
    )
F# __Копировать
     new : 
            [<NotNullAttribute>] alias : string * 
            [<NotNullAttribute>] linkArgs : string * 
            [<CanBeNullAttribute>] ?serverCode : string * 
            [<CanBeNullAttribute>] ?instanceName : string * 
            ?processId : int 
    (* Defaults:
            let _serverCode = defaultArg serverCode ""
            let _instanceName = defaultArg instanceName ""
            let _processId = defaultArg processId 0
    *)
    -> AppManagerLinkMessage
#### Параметры
alias [String](https://learn.microsoft.com/dotnet/api/system.string)
     Псевдоним приложения 
linkArgs [String](https://learn.microsoft.com/dotnet/api/system.string)
     Аргументы ссылки 
serverCode [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
     Код сервиса 
instanceName [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
     Имя экземпляра сервиса 
processId [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
(Optional)
    Идентификатор процесса
##  __См. также
#### Ссылки
[AppManagerLinkMessage -
](T_Tessa_Applications_Messages_AppManagerLinkMessage.htm)
[AppManagerLinkMessage -
перегрузка](Overload_Tessa_Applications_Messages_AppManagerLinkMessage__ctor.htm)
[Tessa.Applications.Messages - пространство
имён](N_Tessa_Applications_Messages.htm)
