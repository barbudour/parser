# ISharedEventSubscriber<TEventArgs> \- интерфейс
Объект, реализующий подписку на уведомление о событиях, а также рассылку
уведомлений, выполняемую для всех событий и подписчиков с заданными именами
независимо от того, располагаются ли такие подписчики в том же приложении или
в другом процессе.
## __Definition
 **Пространство имён:** [Tessa.Platform.IPC](N_Tessa_Platform_IPC.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ISharedEventSubscriber<TEventArgs> : ISharedNotificationObject
    where TEventArgs : class, new(), ISharedEventArgs
VB __Копировать
     Public Interface ISharedEventSubscriber(Of TEventArgs As {Class, New, ISharedEventArgs})
    	Inherits ISharedNotificationObject
C++ __Копировать
    generic<typename TEventArgs>
    where TEventArgs : ref class, gcnew(), ISharedEventArgs
    public interface class ISharedEventSubscriber : ISharedNotificationObject
F# __Копировать
     type ISharedEventSubscriber<'TEventArgs when 'TEventArgs : not struct, new() and ISharedEventArgs> = 
        interface
            interface ISharedNotificationObject
        end
Implements
    [ISharedNotificationObject](T_Tessa_Platform_IPC_ISharedNotificationObject.htm)
#### Параметры типа
TEventArgs
     Ссылочный тип аргументов события, содержащий конструктор по умолчанию. Все экземпляры класса, созданные для одного и того же события, должны иметь один и тот же тип TEventArgs во избежание нарушения рассылки уведомлений между событиями. 
## __Свойства
[EventName](P_Tessa_Platform_IPC_ISharedNotificationObject_EventName.htm)|
Семантическое имя события.  
(Унаследован от
[ISharedNotificationObject](T_Tessa_Platform_IPC_ISharedNotificationObject.htm))  
---|---  
[InstanceName](P_Tessa_Platform_IPC_ISharedNotificationObject_InstanceName.htm)|
Имя экземпляра класса, являющееся глобально уникальным для экземпляров того же
типа, расположенных в различных процессах.  
(Унаследован от
[ISharedNotificationObject](T_Tessa_Platform_IPC_ISharedNotificationObject.htm))  
[InstanceType](P_Tessa_Platform_IPC_ISharedNotificationObject_InstanceType.htm)|
Тип объекта, используемый для синхронизации экземпляров между потоками и
процессами.  
(Унаследован от
[ISharedNotificationObject](T_Tessa_Platform_IPC_ISharedNotificationObject.htm))  
[IsSubscribed](P_Tessa_Platform_IPC_ISharedEventSubscriber_1_IsSubscribed.htm)|
Признак того, что в данный момент объект подписан на событие и получает
уведомления.  
## __Методы
[NotifyAsync](M_Tessa_Platform_IPC_ISharedEventSubscriber_1_NotifyAsync.htm)|
Уведомляет все подписанные процессы о событии с заданными аргументами.  
---|---  
[SubscribeAsync](M_Tessa_Platform_IPC_ISharedEventSubscriber_1_SubscribeAsync.htm)|
Выполняет подписку на уведомления, поступающие для события, если подписка ещё
не была выполнена.  
[UnsubscribeAsync](M_Tessa_Platform_IPC_ISharedEventSubscriber_1_UnsubscribeAsync.htm)|
Выполняет отписку от уведомлений, поступающих для события, если подписка уже
была выполнена.  
## __См. также
#### Ссылки
[Tessa.Platform.IPC - пространство имён](N_Tessa_Platform_IPC.htm)
