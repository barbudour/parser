# ProcessRefContainer.TryKillAndRemoveAllProcesses - метод
Пытается остановить все процессы, определяемые объектами
[ProcessRef](T_Chronos_Platform_Processes_ProcessRef.htm), зарегистрированными
в контейнере. Если некоторые процессы остановить не удалось, то возвращает
false. Успешно остановленные процессы удаляются из хранилища.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Processes](N_Chronos_Platform_Processes.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public bool TryKillAndRemoveAllProcesses()
VB __Копировать
     Public Function TryKillAndRemoveAllProcesses As Boolean
C++ __Копировать
     public:
    bool TryKillAndRemoveAllProcesses()
F# __Копировать
     member TryKillAndRemoveAllProcesses : unit -> bool 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если все процессы удалось остановить; false в противном случае.
##  __См. также
#### Ссылки
[ProcessRefContainer - ](T_Chronos_Platform_Processes_ProcessRefContainer.htm)
[Chronos.Platform.Processes - пространство
имён](N_Chronos_Platform_Processes.htm)
