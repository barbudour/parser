# ApplicationCommandExecuteFunc - делегат
Выполняет заданную команду. Возвращает признак того, что обработчик команды
был найден и выполнен.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate bool ApplicationCommandExecuteFunc(
    	IApplicationContext context,
    	IApplicationCommand command
    )
VB __Копировать
     Public Delegate Function ApplicationCommandExecuteFunc ( 
    	context As IApplicationContext,
    	command As IApplicationCommand
    ) As Boolean
C++ __Копировать
     public delegate bool ApplicationCommandExecuteFunc(
    	IApplicationContext^ context, 
    	IApplicationCommand^ command
    )
F# __Копировать
     type ApplicationCommandExecuteFunc = 
        delegate of 
            context : IApplicationContext * 
            command : IApplicationCommand -> bool
#### Параметры
context
[IApplicationContext](T_Tessa_Platform_Runtime_IApplicationContext.htm)
    Контекст, связанный с запуском приложения.
command
[IApplicationCommand](T_Tessa_Platform_Runtime_IApplicationCommand.htm)
    Команда, которую требуется выполнить.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если обработчик команды был найден и выполнен; false в противном случае.
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
