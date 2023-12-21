# RedisEventSubscriber<TEventArgs> \- класс
Объект, реализующий подписку на уведомление о событиях, а также рассылку
уведомлений, выполняемую для всех событий и подписчиков с заданными именами
независимо от того, располагаются ли такие подписчики в том же приложении или
в другом процессе. Рассылка уведомлений осуществляется посредством Redis.
## __Definition
 **Пространство имён:** [Tessa.Platform.IPC](N_Tessa_Platform_IPC.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class RedisEventSubscriber<TEventArgs> : SharedNotificationObject, 
    	ISharedEventSubscriber<TEventArgs>, ISharedNotificationObject
    where TEventArgs : class, new(), ISharedEventArgs
VB __Копировать
     Public Class RedisEventSubscriber(Of TEventArgs As {Class, New, ISharedEventArgs})
    	Inherits SharedNotificationObject
    	Implements ISharedEventSubscriber(Of TEventArgs), ISharedNotificationObject
C++ __Копировать
    generic<typename TEventArgs>
    where TEventArgs : ref class, gcnew(), ISharedEventArgs
    public ref class RedisEventSubscriber : public SharedNotificationObject, 
    	ISharedEventSubscriber<TEventArgs>, ISharedNotificationObject
F# __Копировать
     type RedisEventSubscriber<'TEventArgs when 'TEventArgs : not struct, new() and ISharedEventArgs> = 
        class
            inherit SharedNotificationObject
            interface ISharedEventSubscriber<'TEventArgs>
            interface ISharedNotificationObject
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[SharedNotificationObject](T_Tessa_Platform_IPC_SharedNotificationObject.htm) __ RedisEventSubscriber<TEventArgs>
Implements
    [ISharedEventSubscriber](T_Tessa_Platform_IPC_ISharedEventSubscriber_1.htm)<TEventArgs>, [ISharedNotificationObject](T_Tessa_Platform_IPC_ISharedNotificationObject.htm)
#### Параметры типа
TEventArgs
     Ссылочный тип аргументов события, содержащий конструктор по умолчанию. Все экземпляры класса, созданные для одного и того же события, должны иметь один и тот же тип TEventArgs во избежание нарушения рассылки уведомлений между событиями. 
## __Заметки
Все открытые методы, кроме
[DisposeAsync()](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync), являются потокобезопасными.
## __Конструкторы
[RedisEventSubscriber<TEventArgs>](M_Tessa_Platform_IPC_RedisEventSubscriber_1__ctor.htm)|
Создаёт экземпляр класса с указанием имени события, а также имени и типа
подписчика.  
---|---  
## __Свойства
[ChannelName](P_Tessa_Platform_IPC_RedisEventSubscriber_1_ChannelName.htm)|
Имя канала в Redis, используемое для подписки и отправки уведомлений.  
---|---  
[ConnectionProvider](P_Tessa_Platform_IPC_RedisEventSubscriber_1_ConnectionProvider.htm)|
Объект, предоставляющий доступ к соединению Redis.  
[EventName](P_Tessa_Platform_IPC_SharedNotificationObject_EventName.htm)|
Семантическое имя события.  
(Унаследован от
[SharedNotificationObject](T_Tessa_Platform_IPC_SharedNotificationObject.htm))  
[InstanceName](P_Tessa_Platform_IPC_SharedNotificationObject_InstanceName.htm)|
Имя экземпляра класса, являющееся глобально уникальным для экземпляров того же
типа, расположенных в различных процессах.  
(Унаследован от
[SharedNotificationObject](T_Tessa_Platform_IPC_SharedNotificationObject.htm))  
[InstanceType](P_Tessa_Platform_IPC_SharedNotificationObject_InstanceType.htm)|
Тип объекта, используемый для синхронизации экземпляров между потоками и
процессами.  
(Унаследован от
[SharedNotificationObject](T_Tessa_Platform_IPC_SharedNotificationObject.htm))  
[IsDisposed](P_Tessa_Platform_IPC_SharedNotificationObject_IsDisposed.htm)|
Признак того, что ресурсы объекта были освобождены.  
(Унаследован от
[SharedNotificationObject](T_Tessa_Platform_IPC_SharedNotificationObject.htm))  
[IsSubscribed](P_Tessa_Platform_IPC_RedisEventSubscriber_1_IsSubscribed.htm)|
Признак того, что в данный момент объект подписан на событие и получает
уведомления.  
[NameFactory](P_Tessa_Platform_IPC_SharedNotificationObject_NameFactory.htm)|
Фабрика, предоставляющая средства для создания глобальных имён, которые
возможно использовать для синхронизации между потоками и процессами.  
(Унаследован от
[SharedNotificationObject](T_Tessa_Platform_IPC_SharedNotificationObject.htm))  
##  __Методы
[CheckDisposed](M_Tessa_Platform_IPC_SharedNotificationObject_CheckDisposed.htm)|
Выбрасывает исключение [ObjectDisposedException], если ресурсы текущего
объекта были освобождены.  
(Унаследован от
[SharedNotificationObject](T_Tessa_Platform_IPC_SharedNotificationObject.htm))  
---|---  
[CreateSubscriberAsync](M_Tessa_Platform_IPC_RedisEventSubscriber_1_CreateSubscriberAsync.htm)|
Создаёт объект для управления подписками Redis.  
[DisposeAsync()](M_Tessa_Platform_IPC_SharedNotificationObject_DisposeAsync.htm)|
Освобождает ресурсы, занимаемые объектом.  
(Унаследован от
[SharedNotificationObject](T_Tessa_Platform_IPC_SharedNotificationObject.htm))  
[DisposeAsync(Boolean)](M_Tessa_Platform_IPC_RedisEventSubscriber_1_DisposeAsync.htm)|
Освобождает ресурсы, занимаемые объектом.  
(Переопределяет
[SharedNotificationObject.DisposeAsync(Boolean)](M_Tessa_Platform_IPC_SharedNotificationObject_DisposeAsync_1.htm))  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetOrCreateSubscriberAsync](M_Tessa_Platform_IPC_RedisEventSubscriber_1_GetOrCreateSubscriberAsync.htm)|
Создаёт объект для управления подписками Redis, или возвращает ранее созданный
объект.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[NotifyAsync](M_Tessa_Platform_IPC_RedisEventSubscriber_1_NotifyAsync.htm)|
Уведомляет все подписанные процессы о событии с заданными аргументами.  
[NotifyCoreAsync](M_Tessa_Platform_IPC_RedisEventSubscriber_1_NotifyCoreAsync.htm)|
Уведомляет все подписанные процессы о событии с заданными аргументами.  
[SerializeToStringAsync](M_Tessa_Platform_IPC_RedisEventSubscriber_1_SerializeToStringAsync.htm)|
Сериализует аргументы события в строку для передачи в Redis.  
[SubscribeAsync](M_Tessa_Platform_IPC_RedisEventSubscriber_1_SubscribeAsync.htm)|
Выполняет подписку на уведомления, поступающие для события, если подписка ещё
не была выполнена.  
[SubscribeCoreAsync](M_Tessa_Platform_IPC_RedisEventSubscriber_1_SubscribeCoreAsync.htm)|
Выполняет подписку на уведомления, поступающие для события, если подписка ещё
не была выполнена.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryDeserializeFromStringAsync](M_Tessa_Platform_IPC_RedisEventSubscriber_1_TryDeserializeFromStringAsync.htm)|
Десериализует аргументы события из строки для получения из Redis.  
[UnsubscribeAsync](M_Tessa_Platform_IPC_RedisEventSubscriber_1_UnsubscribeAsync.htm)|
Выполняет отписку от уведомлений, поступающих для события, если подписка уже
была выполнена.  
[UnsubscribeCoreAsync](M_Tessa_Platform_IPC_RedisEventSubscriber_1_UnsubscribeCoreAsync.htm)|
Выполняет отписку от уведомлений, поступающих для события, если подписка уже
была выполнена.  
## __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.IPC - пространство имён](N_Tessa_Platform_IPC.htm)
