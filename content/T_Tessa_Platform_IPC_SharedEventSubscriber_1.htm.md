# SharedEventSubscriber<TEventArgs> \- класс
Объект, реализующий подписку на уведомление о событиях, а также рассылку
уведомлений, выполняемую для всех событий и подписчиков с заданными именами
независимо от того, располагаются ли такие подписчики в том же приложении или
в другом процессе.
## __Definition
 **Пространство имён:** [Tessa.Platform.IPC](N_Tessa_Platform_IPC.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class SharedEventSubscriber<TEventArgs> : SharedNotificationObject, 
    	ISharedEventSubscriber<TEventArgs>, ISharedNotificationObject
    where TEventArgs : class, new(), ISharedEventArgs
VB __Копировать
     Public NotInheritable Class SharedEventSubscriber(Of TEventArgs As {Class, New, ISharedEventArgs})
    	Inherits SharedNotificationObject
    	Implements ISharedEventSubscriber(Of TEventArgs), ISharedNotificationObject
C++ __Копировать
    generic<typename TEventArgs>
    where TEventArgs : ref class, gcnew(), ISharedEventArgs
    public ref class SharedEventSubscriber sealed : public SharedNotificationObject, 
    	ISharedEventSubscriber<TEventArgs>, ISharedNotificationObject
F# __Копировать
     [<SealedAttribute>]
    type SharedEventSubscriber<'TEventArgs when 'TEventArgs : not struct, new() and ISharedEventArgs> = 
        class
            inherit SharedNotificationObject
            interface ISharedEventSubscriber<'TEventArgs>
            interface ISharedNotificationObject
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[SharedNotificationObject](T_Tessa_Platform_IPC_SharedNotificationObject.htm) __ SharedEventSubscriber<TEventArgs>
Implements
    [ISharedEventSubscriber](T_Tessa_Platform_IPC_ISharedEventSubscriber_1.htm)<TEventArgs>, [ISharedNotificationObject](T_Tessa_Platform_IPC_ISharedNotificationObject.htm)
#### Параметры типа
TEventArgs
     Ссылочный тип аргументов события, содержащий конструктор по умолчанию. Все экземпляры класса, созданные для одного и того же события, должны иметь один и тот же тип TEventArgs во избежание нарушения рассылки уведомлений между событиями. 
## __Заметки
Все методы, кроме
[DisposeAsync(Boolean)](M_Tessa_Platform_IPC_SharedEventSubscriber_1_DisposeAsync.htm),
являются потокобезопасными. Свойство
[IsSubscribed](P_Tessa_Platform_IPC_SharedEventSubscriber_1_IsSubscribed.htm)
не является потокобезопасным.
## __Конструкторы
[SharedEventSubscriber<TEventArgs>](M_Tessa_Platform_IPC_SharedEventSubscriber_1__ctor.htm)|
Создаёт экземпляр класса с указанием имени события, а также имени и типа
подписчика.  
---|---  
## __Свойства
[EventName](P_Tessa_Platform_IPC_SharedNotificationObject_EventName.htm)|
Семантическое имя события.  
(Унаследован от
[SharedNotificationObject](T_Tessa_Platform_IPC_SharedNotificationObject.htm))  
---|---  
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
[IsSubscribed](P_Tessa_Platform_IPC_SharedEventSubscriber_1_IsSubscribed.htm)|
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
[DisposeAsync()](M_Tessa_Platform_IPC_SharedNotificationObject_DisposeAsync.htm)|
Освобождает ресурсы, занимаемые объектом.  
(Унаследован от
[SharedNotificationObject](T_Tessa_Platform_IPC_SharedNotificationObject.htm))  
[DisposeAsync(Boolean)](M_Tessa_Platform_IPC_SharedEventSubscriber_1_DisposeAsync.htm)|
Освобождает ресурсы, занимаемые объектом.  
(Переопределяет
[SharedNotificationObject.DisposeAsync(Boolean)](M_Tessa_Platform_IPC_SharedNotificationObject_DisposeAsync_1.htm))  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ExecuteInMutexAsync](M_Tessa_Platform_IPC_SharedEventSubscriber_1_ExecuteInMutexAsync.htm)|
Выполняет заданное действие в синхронизации с глобальным мьютексом, созданным
для события. Метод рекомендуется использовать в том случае, если одновременно
с методами SubscribeAsync или UnsubscribeAsync требуется выполнить другие
действия, гарантированно синхронизованные как внутри текущего экземпляра, так
и между процессами.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[NotifyAsync](M_Tessa_Platform_IPC_SharedEventSubscriber_1_NotifyAsync.htm)|
Уведомляет все подписанные процессы о событии с заданными аргументами.  
[SubscribeAsync(Func<TEventArgs, CancellationToken, ValueTask>,
CancellationToken)](M_Tessa_Platform_IPC_SharedEventSubscriber_1_SubscribeAsync_1.htm)|
Выполняет подписку на уведомления, поступающие для события, если подписка ещё
не была выполнена.  
[SubscribeAsync(Func<TEventArgs, CancellationToken, ValueTask>, Boolean,
CancellationToken)](M_Tessa_Platform_IPC_SharedEventSubscriber_1_SubscribeAsync.htm)|
Выполняет подписку на уведомления, поступающие для события, если подписка ещё
не была выполнена.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[UnsubscribeAsync(CancellationToken)](M_Tessa_Platform_IPC_SharedEventSubscriber_1_UnsubscribeAsync_1.htm)|
Выполняет отписку от уведомлений, поступающих для события, если подписка уже
была выполнена.  
[UnsubscribeAsync(Boolean,
CancellationToken)](M_Tessa_Platform_IPC_SharedEventSubscriber_1_UnsubscribeAsync.htm)|
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
