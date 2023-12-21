# SharedNotificationHelper - класс
Вспомогательные методы для реализации подписки и уведомлений по событиям,
которые синхронизируются между процессами.
## __Definition
 **Пространство имён:** [Tessa.Platform.IPC](N_Tessa_Platform_IPC.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class SharedNotificationHelper
VB __Копировать
     Public NotInheritable Class SharedNotificationHelper
C++ __Копировать
     public ref class SharedNotificationHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type SharedNotificationHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SharedNotificationHelper
##  __Методы
[CreateEventMutex](M_Tessa_Platform_IPC_SharedNotificationHelper_CreateEventMutex.htm)|
Создаёт и возвращает мьютекс, синхронизирующий обращение по глобальному
событию сброса кэша.  
---|---  
[CreateEventStorage](M_Tessa_Platform_IPC_SharedNotificationHelper_CreateEventStorage.htm)|
Создаёт или открывает разделяемое между процессами хранилище в оперативной
памяти, используемое для хранения списка процессов, подписанных на получение
уведомлений о событии.  
[CreateNotifyMutex](M_Tessa_Platform_IPC_SharedNotificationHelper_CreateNotifyMutex.htm)|
Создаёт и возвращает мьютекс, используемый при синхронизации процессов между
установкой события сброса кэша в сигнальное, а затем в несигнальное состояния.  
[CreateNotifyStorage](M_Tessa_Platform_IPC_SharedNotificationHelper_CreateNotifyStorage.htm)|
Создаёт или открывает разделяемое между процессами хранилище в оперативной
памяти, используемое при синхронизации процессов между установкой события в
сигнальное, а затем в несигнальное состояния.  
[CreateSharedEvent](M_Tessa_Platform_IPC_SharedNotificationHelper_CreateSharedEvent.htm)|
Создаёт и возвращает объект синхронизации по глобальному событию сброса кэша.  
[ListenAsync<TEventArgs>](M_Tessa_Platform_IPC_SharedNotificationHelper_ListenAsync__1.htm)|
Выполняет ожидание уведомлений на событие в цикле, который может быть прерван
только событием disposeEvent.  
[NotifyAsync<TEventArgs>](M_Tessa_Platform_IPC_SharedNotificationHelper_NotifyAsync__1.htm)|
Уведомляет все подписанные процессы о событии с заданными параметрами.  
[SubscribeAsync](M_Tessa_Platform_IPC_SharedNotificationHelper_SubscribeAsync.htm)|
Выполняет подписку на уведомления, поступающие для события, если подписка ещё
не была выполнена. Возвращает обновлённое значение isSubscribed.  
[UnsubscribeAsync](M_Tessa_Platform_IPC_SharedNotificationHelper_UnsubscribeAsync.htm)|
Выполняет отписку от уведомлений, поступающих для события, если подписка уже
была выполнена. Возвращает обновлённое значение isSubscribed.  
## __Поля
[EventMutexName](F_Tessa_Platform_IPC_SharedNotificationHelper_EventMutexName.htm)|
Имя операции для мьютекса, синхронизирующего событие между подписчиками в
разных процессах.  
---|---  
[EventStorageName](F_Tessa_Platform_IPC_SharedNotificationHelper_EventStorageName.htm)|
Имя глобального хранилища для списка процессов, подписанных на получение
уведомлений о событии.  
[NotifyMutexName](F_Tessa_Platform_IPC_SharedNotificationHelper_NotifyMutexName.htm)|
Имя операции для мьютекса, используемого при синхронизации процессов между
установкой события в сигнальное, а затем в несигнальное состояния. Объект
существует только в процессе выполнения события.  
[NotifyStorageName](F_Tessa_Platform_IPC_SharedNotificationHelper_NotifyStorageName.htm)|
Имя глобального хранилища для списка процессов, ещё не получивших уведомление
о событии. Объект существует только в процессе выполнения события.  
[SharedEventName](F_Tessa_Platform_IPC_SharedNotificationHelper_SharedEventName.htm)|
Имя операции для события, синхронизируемого между подписчиками в разных
процессах.  
## __См. также
#### Ссылки
[Tessa.Platform.IPC - пространство имён](N_Tessa_Platform_IPC.htm)
