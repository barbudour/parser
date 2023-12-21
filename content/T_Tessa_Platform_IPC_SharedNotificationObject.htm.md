# SharedNotificationObject - класс
Базовый класс для объектов, реализующих уведомление о событиях или подписку на
уведомления, которые рассылаются для всех подписчиков с заданным именем
независимо от того, располагаются ли такие подписчики в том же приложении или
в другом процессе.
## __Definition
 **Пространство имён:** [Tessa.Platform.IPC](N_Tessa_Platform_IPC.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class SharedNotificationObject : ISharedNotificationObject, 
    	IAsyncDisposable
VB __Копировать
     Public MustInherit Class SharedNotificationObject
    	Implements ISharedNotificationObject, IAsyncDisposable
C++ __Копировать
     public ref class SharedNotificationObject abstract : ISharedNotificationObject, 
    	IAsyncDisposable
F# __Копировать
     [<AbstractClassAttribute>]
    type SharedNotificationObject = 
        class
            interface ISharedNotificationObject
            interface IAsyncDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SharedNotificationObject
Derived
[Tessa.Platform.IPC.RedisEventSubscriber<TEventArgs>](T_Tessa_Platform_IPC_RedisEventSubscriber_1.htm)
[Tessa.Platform.IPC.SharedEventNotifier<TEventArgs>](T_Tessa_Platform_IPC_SharedEventNotifier_1.htm)
[Tessa.Platform.IPC.SharedEventSubscriber<TEventArgs>](T_Tessa_Platform_IPC_SharedEventSubscriber_1.htm)
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [ISharedNotificationObject](T_Tessa_Platform_IPC_ISharedNotificationObject.htm)
##  __Конструкторы
[SharedNotificationObject](M_Tessa_Platform_IPC_SharedNotificationObject__ctor.htm)|
Создаёт экземпляр класса с указанием имени события, а также имени и типа
подписчика.  
---|---  
## __Свойства
[EventName](P_Tessa_Platform_IPC_SharedNotificationObject_EventName.htm)|
Семантическое имя события.  
---|---  
[InstanceName](P_Tessa_Platform_IPC_SharedNotificationObject_InstanceName.htm)|
Имя экземпляра класса, являющееся глобально уникальным для экземпляров того же
типа, расположенных в различных процессах.  
[InstanceType](P_Tessa_Platform_IPC_SharedNotificationObject_InstanceType.htm)|
Тип объекта, используемый для синхронизации экземпляров между потоками и
процессами.  
[IsDisposed](P_Tessa_Platform_IPC_SharedNotificationObject_IsDisposed.htm)|
Признак того, что ресурсы объекта были освобождены.  
[Logger](P_Tessa_Platform_IPC_SharedNotificationObject_Logger.htm)|  Объект,
выполняющий логирование.  
[NameFactory](P_Tessa_Platform_IPC_SharedNotificationObject_NameFactory.htm)|
Фабрика, предоставляющая средства для создания глобальных имён, которые
возможно использовать для синхронизации между потоками и процессами.  
## __Методы
[CheckDisposed](M_Tessa_Platform_IPC_SharedNotificationObject_CheckDisposed.htm)|
Выбрасывает исключение [ObjectDisposedException], если ресурсы текущего
объекта были освобождены.  
---|---  
[DisposeAsync()](M_Tessa_Platform_IPC_SharedNotificationObject_DisposeAsync.htm)|
Освобождает ресурсы, занимаемые объектом.  
[DisposeAsync(Boolean)](M_Tessa_Platform_IPC_SharedNotificationObject_DisposeAsync_1.htm)|
Освобождает ресурсы, занимаемые объектом.  
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
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
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
