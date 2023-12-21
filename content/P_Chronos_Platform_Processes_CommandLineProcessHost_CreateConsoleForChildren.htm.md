# CommandLineProcessHost.CreateConsoleForChildren - свойство
Признак того, нужно ли показывать окно консоли для плагинов, запускаемых с
помощью метода
[StartChildProcess(String[])](M_Chronos_Platform_Processes_CommandLineProcessHost_StartChildProcess.htm).
## __Definition
 **Пространство имён:**
[Chronos.Platform.Processes](N_Chronos_Platform_Processes.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     protected bool CreateConsoleForChildren { get; set; }
VB __Копировать
     Protected Property CreateConsoleForChildren As Boolean
    	Get
    	Set
C++ __Копировать
     protected:
    property bool CreateConsoleForChildren {
    	bool get ();
    	void set (bool value);
    }
F# __Копировать
     member CreateConsoleForChildren : bool with get, set
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
По умолчанию равно false.
##  __См. также
#### Ссылки
[CommandLineProcessHost -
](T_Chronos_Platform_Processes_CommandLineProcessHost.htm)
[Chronos.Platform.Processes - пространство
имён](N_Chronos_Platform_Processes.htm)
