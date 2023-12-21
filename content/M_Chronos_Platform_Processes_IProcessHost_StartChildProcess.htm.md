# IProcessHost.StartChildProcess - метод
Запускает дочерний процесс и возвращает ссылку на него.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Processes](N_Chronos_Platform_Processes.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     Process StartChildProcess(
    	params string[] args
    )
VB __Копировать
     Function StartChildProcess ( 
    	ParamArray args As String()
    ) As Process
C++ __Копировать
    Process^ StartChildProcess(
    	... array<String^>^ args
    )
F# __Копировать
     abstract StartChildProcess : 
            args : string[] -> Process 
#### Параметры
args [String](https://learn.microsoft.com/dotnet/api/system.string)[]
    Аргументы командной строки, передаваемые дочернему процессу.
#### Возвращаемое значение
[Process](https://learn.microsoft.com/dotnet/api/system.diagnostics.process)  
Ссылка на запущенный дочерний процесс.
##  __См. также
#### Ссылки
[IProcessHost - ](T_Chronos_Platform_Processes_IProcessHost.htm)
[Chronos.Platform.Processes - пространство
имён](N_Chronos_Platform_Processes.htm)
