# PipeInstanceResolver - класс
Объект, управляющий временем жизни экземпляров объектов, реализующих бизнес-
логику для использования в канале.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class PipeInstanceResolver : IPipeInstanceResolver, 
    	IAsyncDisposable, IDisposable
VB __Копировать
     Public Class PipeInstanceResolver
    	Implements IPipeInstanceResolver, IAsyncDisposable, IDisposable
C++ __Копировать
     public ref class PipeInstanceResolver : IPipeInstanceResolver, 
    	IAsyncDisposable, IDisposable
F# __Копировать
     type PipeInstanceResolver = 
        class
            interface IPipeInstanceResolver
            interface IAsyncDisposable
            interface IDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PipeInstanceResolver
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [IPipeInstanceResolver](T_Tessa_Platform_Pipes_IPipeInstanceResolver.htm)
##  __Заметки
Наследники класса могут переопределить методы и свойства класса.
## __Конструкторы
[PipeInstanceResolver](M_Tessa_Platform_Pipes_PipeInstanceResolver__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
## __Свойства
[InstanceFactory](P_Tessa_Platform_Pipes_PipeInstanceResolver_InstanceFactory.htm)|
Фабрика экземпляров объектов, используемых в канале, время жизни которых
контролируется текущим объектом.  
---|---  
[Instances](P_Tessa_Platform_Pipes_PipeInstanceResolver_Instances.htm)|
Экземпляры, созданные текущим объектом.  
## __Методы
[Dispose](M_Tessa_Platform_Pipes_PipeInstanceResolver_Dispose.htm)| Performs
application-defined tasks associated with freeing, releasing, or resetting
unmanaged resources.  
---|---  
[DisposeAsync](M_Tessa_Platform_Pipes_PipeInstanceResolver_DisposeAsync.htm)|
Performs application-defined tasks associated with freeing, releasing, or
resetting unmanaged resources asynchronously.  
[DisposeCoreAsync](M_Tessa_Platform_Pipes_PipeInstanceResolver_DisposeCoreAsync.htm)|
Performs application-defined tasks associated with freeing, releasing, or
resetting unmanaged resources asynchronously.  
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
[ResolveAsync](M_Tessa_Platform_Pipes_PipeInstanceResolver_ResolveAsync.htm)|
Возвращает экземпляр объекта по заданному типу. Для экземпляра выполняется
инициализация [IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm),
а при освобождении текущего экземпляра
[IPipeInstanceResolver](T_Tessa_Platform_Pipes_IPipeInstanceResolver.htm)
освобождаются все созданные им объекты, которые реализуют
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable)
или [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable).
Тип объекта должен быть предварительно зарегистрирован в фабрике
[IPipeInstanceFactory](T_Tessa_Platform_Pipes_IPipeInstanceFactory.htm).  
[ResolveCoreAsync](M_Tessa_Platform_Pipes_PipeInstanceResolver_ResolveCoreAsync.htm)|
Возвращает экземпляр объекта по заданному типу. Для экземпляра выполняется
инициализация [IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm),
а при освобождении текущего экземпляра
[IPipeInstanceResolver](T_Tessa_Platform_Pipes_IPipeInstanceResolver.htm)
освобождаются все созданные им объекты, которые реализуют
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable)
или [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable).
Тип объекта должен быть предварительно зарегистрирован в фабрике
[IPipeInstanceFactory](T_Tessa_Platform_Pipes_IPipeInstanceFactory.htm).  
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
[ResolveAsync<T>](M_Tessa_Platform_Pipes_PipesExtensions_ResolveAsync__1.htm)|
Возвращает экземпляр объекта по заданному типу. Для экземпляра выполняется
инициализация [IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm),
а при освобождении текущего экземпляра
[IPipeInstanceResolver](T_Tessa_Platform_Pipes_IPipeInstanceResolver.htm)
освобождаются все созданные им объекты, которые реализуют
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable)
или [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable).
Тип объекта должен быть предварительно зарегистрирован в фабрике
[IPipeInstanceFactory](T_Tessa_Platform_Pipes_IPipeInstanceFactory.htm).  
(Определяется [PipesExtensions](T_Tessa_Platform_Pipes_PipesExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
