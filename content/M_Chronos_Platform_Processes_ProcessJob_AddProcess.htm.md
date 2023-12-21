# ProcessJob.AddProcess - метод
Добавляет Handle процесса в объект WinAPI Job.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Processes](N_Chronos_Platform_Processes.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public bool AddProcess(
    	IntPtr processHandle
    )
VB __Копировать
     Public Function AddProcess ( 
    	processHandle As IntPtr
    ) As Boolean
C++ __Копировать
     public:
    bool AddProcess(
    	IntPtr processHandle
    )
F# __Копировать
     member AddProcess : 
            processHandle : IntPtr -> bool 
#### Параметры
processHandle [IntPtr](https://learn.microsoft.com/dotnet/api/system.intptr)
    Handle объекта WinAPI Job.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если процесс был успешно добавлен в объект WinAPI Job; false, если
процесс добавить не удалось.
## __Исключения
[System.ObjectDisposedException]| Ресурсы, занимаемые объектом, были
освобождены.  
---|---  
##  __См. также
#### Ссылки
[ProcessJob - ](T_Chronos_Platform_Processes_ProcessJob.htm)
[Chronos.Platform.Processes - пространство
имён](N_Chronos_Platform_Processes.htm)
[System.ObjectDisposedException]
