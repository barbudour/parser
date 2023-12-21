# GlobalCacheInvalidator<TEventArgs> \- класс
Производит сброс всех экземпляров кэша
[GlobalCache<TEventArgs>](T_Tessa_Platform_Caching_GlobalCache_1.htm) с
заданными именем и типом.
## __Definition
 **Пространство имён:** [Tessa.Platform.Caching](N_Tessa_Platform_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class GlobalCacheInvalidator<TEventArgs> : IAsyncDisposable
    where TEventArgs : class, new(), ISharedEventArgs
VB __Копировать
     Public NotInheritable Class GlobalCacheInvalidator(Of TEventArgs As {Class, New, ISharedEventArgs})
    	Implements IAsyncDisposable
C++ __Копировать
    generic<typename TEventArgs>
    where TEventArgs : ref class, gcnew(), ISharedEventArgs
    public ref class GlobalCacheInvalidator sealed : IAsyncDisposable
F# __Копировать
     [<SealedAttribute>]
    type GlobalCacheInvalidator<'TEventArgs when 'TEventArgs : not struct, new() and ISharedEventArgs> = 
        class
            interface IAsyncDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ GlobalCacheInvalidator<TEventArgs>
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable)
#### Параметры типа
TEventArgs
     Аргументы события, сериализуемые между процессами. Тип должен реализовывать интерфейс [ISharedEventArgs](T_Tessa_Platform_IPC_ISharedEventArgs.htm). 
## __Заметки
Все методы, кроме
[DisposeAsync()](M_Tessa_Platform_Caching_GlobalCacheInvalidator_1_DisposeAsync.htm),
являются потокобезопасными.
## __Конструкторы
[GlobalCacheInvalidator<TEventArgs>(String,
String)](M_Tessa_Platform_Caching_GlobalCacheInvalidator_1__ctor.htm)|
Создаёт экземпляр класса с указанием глобального имени экземпляров кэша,
которые требуется уведомлять о сбросе кэша.  
---|---  
[GlobalCacheInvalidator<TEventArgs>(Type,
String)](M_Tessa_Platform_Caching_GlobalCacheInvalidator_1__ctor_2.htm)|
Создаёт экземпляр класса с указанием типов экземпляров кэша, которые требуется
уведомлять о сбросе кэша при условии, что они созданы с именем по умолчанию
[Default](F_Tessa_Platform_Caching_GlobalCacheNames_Default.htm).  
[GlobalCacheInvalidator<TEventArgs>(String, Type,
String)](M_Tessa_Platform_Caching_GlobalCacheInvalidator_1__ctor_1.htm)|
Создаёт экземпляр класса с указанием имени экземпляров кэша с заданными
типами, которые требуется уведомлять о сбросе кэша.  
## __Свойства
[InstanceName](P_Tessa_Platform_Caching_GlobalCacheInvalidator_1_InstanceName.htm)|
Имя экземпляра класса, являющееся глобально уникальным для экземпляров кэша
того же типа, расположенных в различных процессах.  
---|---  
[InstanceType](P_Tessa_Platform_Caching_GlobalCacheInvalidator_1_InstanceType.htm)|
Тип объекта, используемый для синхронизации экземпляров между потоками и
процессами.  
## __Методы
[DisposeAsync](M_Tessa_Platform_Caching_GlobalCacheInvalidator_1_DisposeAsync.htm)|
Освобождает ресурсы, занимаемые объектом.  
---|---  
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
[InvalidateAsync](M_Tessa_Platform_Caching_GlobalCacheInvalidator_1_InvalidateAsync.htm)|
Уведомляет экземпляры кэша о том, что их значения устарели и требуется сброс
кэша. Выполнение метода может занять неопределённое время, прежде чем сброс
экземпляров кэша в действительности произойдёт во всех процессах. По
завершении выполнения кэш будет гарантированно очищен.  
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
[Tessa.Platform.Caching - пространство имён](N_Tessa_Platform_Caching.htm)
