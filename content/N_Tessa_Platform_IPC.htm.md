# Tessa.Platform.IPC - пространство имён
Средства синхронизации между процессами (InterProcess Communication).
##  __Классы
[DefaultGlobalEvent](T_Tessa_Platform_IPC_DefaultGlobalEvent.htm)|  Событие с
глобально уникальным именем, используемое для синхронизации между процессами.
Эта версия использует стандартный объект
[EventWaitHandle](https://learn.microsoft.com/dotnet/api/system.threading.eventwaithandle)
с глобальным именем, который будет функционировать только при запуске на
Windows.  
---|---  
[DefaultGlobalMutex](T_Tessa_Platform_IPC_DefaultGlobalMutex.htm)|  Мьютекс с
глобально уникальным именем, используемый для синхронизации между процессами.
Эта версия использует стандартный объект
[Mutex](https://learn.microsoft.com/dotnet/api/system.threading.mutex) с
глобальным именем, который будет функционировать только при запуске на
Windows.  
[DefaultGlobalStorage](T_Tessa_Platform_IPC_DefaultGlobalStorage.htm)|
Реализация [IGlobalStorage](T_Tessa_Platform_IPC_IGlobalStorage.htm) по
умолчанию с разделяемым хранилищем в памяти, которое реализовано посредством
объекта
[MemoryMappedFile](https://learn.microsoft.com/dotnet/api/system.io.memorymappedfiles.memorymappedfile).  
[FileSystemGlobalStorage](T_Tessa_Platform_IPC_FileSystemGlobalStorage.htm)|
Хранилище данных, реализованное в виде временного файла, содержимое которого
разделяется между процессами.  
[GlobalEventAwaiter](T_Tessa_Platform_IPC_GlobalEventAwaiter.htm)|  Объект,
выполняющий ожидание глобального события
[IGlobalEvent](T_Tessa_Platform_IPC_IGlobalEvent.htm) совместно с другими
объектами
[WaitHandle](https://learn.microsoft.com/dotnet/api/system.threading.waithandle).  
[GlobalEventBase](T_Tessa_Platform_IPC_GlobalEventBase.htm)|  Базовая
реализация интерфейса [IGlobalEvent](T_Tessa_Platform_IPC_IGlobalEvent.htm).  
[GlobalMutexBase](T_Tessa_Platform_IPC_GlobalMutexBase.htm)|  Базовая
реализация интерфейса [IGlobalMutex](T_Tessa_Platform_IPC_IGlobalMutex.htm).  
[GlobalStorageBase](T_Tessa_Platform_IPC_GlobalStorageBase.htm)|  Базовая
реализация интерфейса
[IGlobalStorage](T_Tessa_Platform_IPC_IGlobalStorage.htm).  
[LinuxGlobalEvent](T_Tessa_Platform_IPC_LinuxGlobalEvent.htm)|  Событие с
глобально уникальным именем, используемое для синхронизации между процессами в
Linux.  
[LinuxGlobalMutex](T_Tessa_Platform_IPC_LinuxGlobalMutex.htm)|  Событие с
глобально уникальным именем, используемое для синхронизации между процессами в
Linux.  
[RedisConnectionProvider](T_Tessa_Platform_IPC_RedisConnectionProvider.htm)|
Объект, предоставляющий доступ к соединению Redis.  
[RedisEventSubscriber<TEventArgs>](T_Tessa_Platform_IPC_RedisEventSubscriber_1.htm)|
Объект, реализующий подписку на уведомление о событиях, а также рассылку
уведомлений, выполняемую для всех событий и подписчиков с заданными именами
независимо от того, располагаются ли такие подписчики в том же приложении или
в другом процессе. Рассылка уведомлений осуществляется посредством Redis.  
[ServerSettingsSharedEventSubscriberFactory](T_Tessa_Platform_IPC_ServerSettingsSharedEventSubscriberFactory.htm)|
Фабрика объектов
[ISharedEventSubscriber<TEventArgs>](T_Tessa_Platform_IPC_ISharedEventSubscriber_1.htm),
создаваемых в зависимости от настроек сервера
[ITessaServerSettings](T_Tessa_Platform_ITessaServerSettings.htm).  
[SharedEventArgs](T_Tessa_Platform_IPC_SharedEventArgs.htm)|  Базовый класс
для аргументов события, разделяемых между процессами.  
[SharedEventIDContainer](T_Tessa_Platform_IPC_SharedEventIDContainer.htm)|
Содержит информацию об уникальном идентификатора произошедшего события,
синхронизация которого выполняется между процессами.  
[SharedEventInstanceList<TEventArgs>](T_Tessa_Platform_IPC_SharedEventInstanceList_1.htm)|
Список, содержащий информацию о произошедшем событии, синхронизация которого
выполняется из различных процессов.  
[SharedEventNotifier<TEventArgs>](T_Tessa_Platform_IPC_SharedEventNotifier_1.htm)|
Объект, реализующий рассылку уведомлений, выполняемую для всех событий и
подписчиков с заданными именами независимо от того, располагаются ли такие
подписчики в том же приложении или в другом процессе.  
[SharedEventSubscriber<TEventArgs>](T_Tessa_Platform_IPC_SharedEventSubscriber_1.htm)|
Объект, реализующий подписку на уведомление о событиях, а также рассылку
уведомлений, выполняемую для всех событий и подписчиков с заданными именами
независимо от того, располагаются ли такие подписчики в том же приложении или
в другом процессе.  
[SharedEventSubscriberFactory](T_Tessa_Platform_IPC_SharedEventSubscriberFactory.htm)|
Фабрика объектов
[ISharedEventSubscriber<TEventArgs>](T_Tessa_Platform_IPC_ISharedEventSubscriber_1.htm)
по умолчанию, использующая глобальные события посредством объекта
[SharedEventSubscriber<TEventArgs>](T_Tessa_Platform_IPC_SharedEventSubscriber_1.htm).  
[SharedInstanceList](T_Tessa_Platform_IPC_SharedInstanceList.htm)|  Список,
содержащий информацию об экземплярах, синхронизация которых выполняется из
различных процессов.  
[SharedNameFactory](T_Tessa_Platform_IPC_SharedNameFactory.htm)|  Фабрика,
предоставляющая средства для создания глобальных имён, которые возможно
использовать для синхронизации между потоками и процессами.  
[SharedNotificationHelper](T_Tessa_Platform_IPC_SharedNotificationHelper.htm)|
Вспомогательные методы для реализации подписки и уведомлений по событиям,
которые синхронизируются между процессами.  
[SharedNotificationObject](T_Tessa_Platform_IPC_SharedNotificationObject.htm)|
Базовый класс для объектов, реализующих уведомление о событиях или подписку на
уведомления, которые рассылаются для всех подписчиков с заданным именем
независимо от того, располагаются ли такие подписчики в том же приложении или
в другом процессе.  
[SharedStorage](T_Tessa_Platform_IPC_SharedStorage.htm)|  Разделяемое между
процессами хранилище данных, представленных в бинарной форме.  
[SharedStorageInitializer](T_Tessa_Platform_IPC_SharedStorageInitializer.htm)|
Объект, выполняющий инициализацию разделенного хранилища данных.  
## __Интерфейсы
[IGlobalEvent](T_Tessa_Platform_IPC_IGlobalEvent.htm)|  Событие с глобально
уникальным именем, используемое для синхронизации между процессами.  
---|---  
[IGlobalMutex](T_Tessa_Platform_IPC_IGlobalMutex.htm)|  Мьютекс с глобально
уникальным именем, используемый для синхронизации между процессами.  
[IGlobalStorage](T_Tessa_Platform_IPC_IGlobalStorage.htm)|  Хранилище данных,
обычно располагающееся в памяти, содержимое которого разделяется между
процессами.  
[IRedisConnectionProvider](T_Tessa_Platform_IPC_IRedisConnectionProvider.htm)|
Объект, предоставляющий доступ к соединению Redis.  
[ISharedEventArgs](T_Tessa_Platform_IPC_ISharedEventArgs.htm)|  Аргументы
события, разделяемые между процессами. Каждый подписчик получает копию
аргументов события.  
[ISharedEventSubscriber<TEventArgs>](T_Tessa_Platform_IPC_ISharedEventSubscriber_1.htm)|
Объект, реализующий подписку на уведомление о событиях, а также рассылку
уведомлений, выполняемую для всех событий и подписчиков с заданными именами
независимо от того, располагаются ли такие подписчики в том же приложении или
в другом процессе.  
[ISharedEventSubscriberFactory](T_Tessa_Platform_IPC_ISharedEventSubscriberFactory.htm)|
Фабрика объектов
[ISharedEventSubscriber<TEventArgs>](T_Tessa_Platform_IPC_ISharedEventSubscriber_1.htm).  
[ISharedNotificationObject](T_Tessa_Platform_IPC_ISharedNotificationObject.htm)|
Объект, реализующий уведомление о событиях или подписку на уведомление.  
[ISharedStorageInitializer](T_Tessa_Platform_IPC_ISharedStorageInitializer.htm)|
Объект, выполняющий инициализацию разделенного хранилища данных.
