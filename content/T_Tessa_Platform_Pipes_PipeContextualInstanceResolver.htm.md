# PipeContextualInstanceResolver - класс
Объект, запрашивающий экземпляры из текущего контекста
[Current](P_Tessa_Platform_Pipes_PipeInstanceContext_Current.htm). Метод
[ResolveAsync(Type,
CancellationToken)](M_Tessa_Platform_Pipes_PipeContextualInstanceResolver_ResolveAsync.htm)
должен использоваться только при наличии такого контекста, например, в методах
обработки запросов на сервере
[IPipeServer](T_Tessa_Platform_Pipes_IPipeServer.htm),
[IPipeRouter](T_Tessa_Platform_Pipes_IPipeRouter.htm),
[IPipeHandler](T_Tessa_Platform_Pipes_IPipeHandler.htm). Метод
[DisposeAsync()](M_Tessa_Platform_Pipes_PipeContextualInstanceResolver_DisposeAsync.htm)
не выполняет действий. Используйте метод
[GetContextualInstanceResolver(IUnityContainer)](M_Tessa_Platform_Pipes_PipesExtensions_GetContextualInstanceResolver.htm)
для запроса экземпляра объекта из Unity или запросите экземпляр
[IPipeInstanceResolver](T_Tessa_Platform_Pipes_IPipeInstanceResolver.htm) по
имени "PipeContextualInstanceResolver".
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class PipeContextualInstanceResolver : IPipeInstanceResolver, 
    	IAsyncDisposable, IDisposable
VB __Копировать
     Public NotInheritable Class PipeContextualInstanceResolver
    	Implements IPipeInstanceResolver, IAsyncDisposable, IDisposable
C++ __Копировать
     public ref class PipeContextualInstanceResolver sealed : IPipeInstanceResolver, 
    	IAsyncDisposable, IDisposable
F# __Копировать
     [<SealedAttribute>]
    type PipeContextualInstanceResolver = 
        class
            interface IPipeInstanceResolver
            interface IAsyncDisposable
            interface IDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PipeContextualInstanceResolver
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [IPipeInstanceResolver](T_Tessa_Platform_Pipes_IPipeInstanceResolver.htm)
##  __Конструкторы
[PipeContextualInstanceResolver](M_Tessa_Platform_Pipes_PipeContextualInstanceResolver__ctor.htm)|
Инициализирует новый экземпляр класса PipeContextualInstanceResolver  
---|---  
##  __Методы
[Dispose](M_Tessa_Platform_Pipes_PipeContextualInstanceResolver_Dispose.htm)|
Performs application-defined tasks associated with freeing, releasing, or
resetting unmanaged resources.  
---|---  
[DisposeAsync](M_Tessa_Platform_Pipes_PipeContextualInstanceResolver_DisposeAsync.htm)|
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
[ResolveAsync](M_Tessa_Platform_Pipes_PipeContextualInstanceResolver_ResolveAsync.htm)|
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
