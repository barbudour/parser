# ApplicationCommandParseFunc - делегат
Выполняет разбор заданного аргумента командной строки. Возвращает команду,
соответствующую аргументу, или null, если подходящая команда не найдена.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate IApplicationCommand ApplicationCommandParseFunc(
    	IApplicationContext context,
    	string name,
    	string parameter
    )
VB __Копировать
     Public Delegate Function ApplicationCommandParseFunc ( 
    	context As IApplicationContext,
    	name As String,
    	parameter As String
    ) As IApplicationCommand
C++ __Копировать
     public delegate IApplicationCommand^ ApplicationCommandParseFunc(
    	IApplicationContext^ context, 
    	String^ name, 
    	String^ parameter
    )
F# __Копировать
     type ApplicationCommandParseFunc = 
        delegate of 
            context : IApplicationContext * 
            name : string * 
            parameter : string -> IApplicationCommand
#### Параметры
context
[IApplicationContext](T_Tessa_Platform_Runtime_IApplicationContext.htm)
    Контекст, связанный с запуском приложения.
name [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя команды в командной строке.
parameter [String](https://learn.microsoft.com/dotnet/api/system.string)
    Параметр команды в командной строке.
#### Возвращаемое значение
[IApplicationCommand](T_Tessa_Platform_Runtime_IApplicationCommand.htm)  
Команда, соответствующая аргументу, или null, если подходящая команда не
найдена.
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
