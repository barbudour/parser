# JobProcessManager - конструктор
Создаёт экземпляр класса с указанием объекта WinAPI Job, в который будут
добавлены все создаваемые процессы.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Processes](N_Chronos_Platform_Processes.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public JobProcessManager(
    	ProcessJob processJob
    )
VB __Копировать
     Public Sub New ( 
    	processJob As ProcessJob
    )
C++ __Копировать
     public:
    JobProcessManager(
    	ProcessJob^ processJob
    )
F# __Копировать
     new : 
            processJob : ProcessJob -> JobProcessManager
#### Параметры
processJob [ProcessJob](T_Chronos_Platform_Processes_ProcessJob.htm)
    Объект WinAPI Job, в который будут добавлены все создаваемые процессы.
##  __См. также
#### Ссылки
[JobProcessManager - ](T_Chronos_Platform_Processes_JobProcessManager.htm)
[Chronos.Platform.Processes - пространство
имён](N_Chronos_Platform_Processes.htm)
