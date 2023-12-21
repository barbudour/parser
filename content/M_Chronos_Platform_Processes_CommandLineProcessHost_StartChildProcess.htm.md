# CommandLineProcessHost.StartChildProcess - метод
Запускает дочерний процесс и возвращает ссылку на него.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Processes](N_Chronos_Platform_Processes.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public Process StartChildProcess(
    	params string[] args
    )
VB __Копировать
     Public Function StartChildProcess ( 
    	ParamArray args As String()
    ) As Process
C++ __Копировать
     public:
    virtual Process^ StartChildProcess(
    	... array<String^>^ args
    ) sealed
F# __Копировать
     abstract StartChildProcess : 
            args : string[] -> Process 
    override StartChildProcess : 
            args : string[] -> Process 
#### Параметры
args [String](https://learn.microsoft.com/dotnet/api/system.string)[]
    Аргументы командной строки, передаваемые дочернему процессу.
#### Возвращаемое значение
[Process](https://learn.microsoft.com/dotnet/api/system.diagnostics.process)  
Ссылка на запущенный дочерний процесс.
#### Реализации
[IProcessHost.StartChildProcess(String[])](M_Chronos_Platform_Processes_IProcessHost_StartChildProcess.htm)  
##  __См. также
#### Ссылки
[CommandLineProcessHost -
](T_Chronos_Platform_Processes_CommandLineProcessHost.htm)
[Chronos.Platform.Processes - пространство
имён](N_Chronos_Platform_Processes.htm)
