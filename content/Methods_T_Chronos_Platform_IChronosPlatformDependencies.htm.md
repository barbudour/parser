# IChronosPlatformDependencies - методы
##  __Методы
[CreateGlobalEvent](M_Chronos_Platform_IChronosPlatformDependencies_CreateGlobalEvent.htm)|
Создаёт событие по глобально уникальному имени, который можно использовать для
синхронизации процессов как минимум в пределах сессии пользователя и всех
процессов в ней.  
---|---  
[CreateGlobalMutex](M_Chronos_Platform_IChronosPlatformDependencies_CreateGlobalMutex.htm)|
Создаёт мьютекс по глобально уникальному имени, который можно использовать для
синхронизации процессов как минимум в пределах сессии пользователя и всех
процессов в ней.  
[CreateProcessManagerWithJob](M_Chronos_Platform_IChronosPlatformDependencies_CreateProcessManagerWithJob.htm)|
Создаёт объект [Chronos.Platform.Processes.IProcessManager] для создания
других процессов. При наличии возможности будет создан объект, объединяющий
текущий и дочерние процессы в Job. Метод может вызываться даже в том случае,
платформой не поддерживается [ChronosPlatformFeature.ProcessJob].  
[Initialize](M_Chronos_Platform_IChronosPlatformDependencies_Initialize.htm)|
Выполняет инициализацию зависимостей платформы. Метод вызывается один раз при
запуске приложения.  
## __См. также
#### Ссылки
[IChronosPlatformDependencies -
](T_Chronos_Platform_IChronosPlatformDependencies.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
