# Chronos.Platform.IPC - пространство имён
API для межпроцессного взаимодействия хост-процесса и процессов плагинов.
##  __Классы
[DefaultGlobalEvent](T_Chronos_Platform_IPC_DefaultGlobalEvent.htm)|  Событие
с глобально уникальным именем, используемое для синхронизации между
процессами. Эта версия использует стандартный объект
[EventWaitHandle](https://learn.microsoft.com/dotnet/api/system.threading.eventwaithandle)
с глобальным именем, который будет функционировать только при запуске на
Windows.  
---|---  
[DefaultGlobalMutex](T_Chronos_Platform_IPC_DefaultGlobalMutex.htm)|  Мьютекс
с глобально уникальным именем, используемый для синхронизации между
процессами. Эта версия использует стандартный объект
[Mutex](https://learn.microsoft.com/dotnet/api/system.threading.mutex) с
глобальным именем, который будет функционировать только при запуске на
Windows.  
[GlobalEventAwaiter](T_Chronos_Platform_IPC_GlobalEventAwaiter.htm)|  Объект,
выполняющий ожидание глобального события
[IGlobalEvent](T_Chronos_Platform_IPC_IGlobalEvent.htm) совместно с другими
объектами
[WaitHandle](https://learn.microsoft.com/dotnet/api/system.threading.waithandle).  
[GlobalEventBase](T_Chronos_Platform_IPC_GlobalEventBase.htm)|  Базовая
реализация интерфейса [IGlobalEvent](T_Chronos_Platform_IPC_IGlobalEvent.htm).  
[GlobalMutexBase](T_Chronos_Platform_IPC_GlobalMutexBase.htm)|  Базовая
реализация интерфейса [IGlobalMutex](T_Chronos_Platform_IPC_IGlobalMutex.htm).  
[LinuxGlobalEvent](T_Chronos_Platform_IPC_LinuxGlobalEvent.htm)|  Событие с
глобально уникальным именем, используемое для синхронизации между процессами в
Linux.  
[LinuxGlobalMutex](T_Chronos_Platform_IPC_LinuxGlobalMutex.htm)|  Событие с
глобально уникальным именем, используемое для синхронизации между процессами в
Linux.  
## __Интерфейсы
[IGlobalEvent](T_Chronos_Platform_IPC_IGlobalEvent.htm)|  Событие с глобально
уникальным именем, используемое для синхронизации между процессами.  
---|---  
[IGlobalMutex](T_Chronos_Platform_IPC_IGlobalMutex.htm)|  Мьютекс с глобально
уникальным именем, используемый для синхронизации между процессами.
