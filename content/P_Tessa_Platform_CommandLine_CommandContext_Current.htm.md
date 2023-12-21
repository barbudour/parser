# CommandContext.Current - свойство
Gets the current context for the current command thread.
## __Definition
 **Пространство имён:**
[Tessa.Platform.CommandLine](N_Tessa_Platform_CommandLine.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CommandContext Current { get; }
VB __Копировать
     Public Shared ReadOnly Property Current As CommandContext
    	Get
C++ __Копировать
     public:
    static property CommandContext^ Current {
    	CommandContext^ get ();
    }
F# __Копировать
     static member Current : CommandContext with get
#### Значение свойства
[CommandContext](T_Tessa_Platform_CommandLine_CommandContext.htm)  
The CommandContext that represents the current command context of the current
method.
##  __См. также
#### Ссылки
[CommandContext - ](T_Tessa_Platform_CommandLine_CommandContext.htm)
[Tessa.Platform.CommandLine - пространство
имён](N_Tessa_Platform_CommandLine.htm)
