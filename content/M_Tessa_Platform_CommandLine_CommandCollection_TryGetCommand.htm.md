# CommandCollection.TryGetCommand - метод
Gets the command with the specified name.
## __Definition
 **Пространство имён:**
[Tessa.Platform.CommandLine](N_Tessa_Platform_CommandLine.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool TryGetCommand(
    	string name,
    	out Command command
    )
VB __Копировать
     Public Function TryGetCommand ( 
    	name As String,
    	<OutAttribute> ByRef command As Command
    ) As Boolean
C++ __Копировать
     public:
    bool TryGetCommand(
    	String^ name, 
    	[OutAttribute] Command^% command
    )
F# __Копировать
     member TryGetCommand : 
            name : string * 
            command : Command byref -> bool 
#### Параметры
name [String](https://learn.microsoft.com/dotnet/api/system.string)
    The key of the value to get.
command [Command](T_Tessa_Platform_CommandLine_Command.htm)
    When this method returns, contains the command with the specified key, if the key is found; otherwise, null. This parameter is passed uninitialized.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true if the CommandCollection contains an command with the specified name;
otherwise, false.
##  __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|
name is null.  
---|---  
##  __См. также
#### Ссылки
[CommandCollection - ](T_Tessa_Platform_CommandLine_CommandCollection.htm)
[Tessa.Platform.CommandLine - пространство
имён](N_Tessa_Platform_CommandLine.htm)
