# IChronosPlatformDependencies.CreateProcessManagerWithJob - метод
Создаёт объект [Chronos.Platform.Processes.IProcessManager] для создания
других процессов. При наличии возможности будет создан объект, объединяющий
текущий и дочерние процессы в Job. Метод может вызываться даже в том случае,
платформой не поддерживается [ChronosPlatformFeature.ProcessJob].
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     IProcessManager CreateProcessManagerWithJob()
VB __Копировать
     Function CreateProcessManagerWithJob As IProcessManager
C++ __Копировать
    IProcessManager^ CreateProcessManagerWithJob()
F# __Копировать
     abstract CreateProcessManagerWithJob : unit -> IProcessManager 
#### Возвращаемое значение
[IProcessManager](T_Chronos_Platform_Processes_IProcessManager.htm)  
Созданный объект. Не должен быть равен null.
## __См. также
#### Ссылки
[IChronosPlatformDependencies -
](T_Chronos_Platform_IChronosPlatformDependencies.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
