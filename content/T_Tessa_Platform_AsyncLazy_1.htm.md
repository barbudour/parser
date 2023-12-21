# AsyncLazy<T> \- класс
Объект, поддерживающий асинхронную ленивую инициализацию значения типа T в
виде задачи Task<T>. Пример: T value = await someLazy;
##  __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class AsyncLazy<T> : Lazy<Task<T>>
VB __Копировать
     Public Class AsyncLazy(Of T)
    	Inherits Lazy(Of Task(Of T))
C++ __Копировать
    generic<typename T>
    public ref class AsyncLazy : public Lazy<Task<T>^>
F# __Копировать
     type AsyncLazy<'T> = 
        class
            inherit Lazy<Task<'T>>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[Lazy](https://learn.microsoft.com/dotnet/api/system.lazy-1)<[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<T>> __ AsyncLazy<T>
#### Параметры типа
T
    Тип значения, который инициализируется асинхронно.
##  __Конструкторы
[AsyncLazy<T>(Func<T>)](M_Tessa_Platform_AsyncLazy_1__ctor_1.htm)|
Инициализирует новый экземпляр класса AsyncLazy<T>  
---|---  
[AsyncLazy<T>(Func<Task<T>>)](M_Tessa_Platform_AsyncLazy_1__ctor.htm)|
Инициализирует новый экземпляр класса AsyncLazy<T>  
##  __Свойства
[IsValueCreated](https://learn.microsoft.com/dotnet/api/system.lazy-1.isvaluecreated#system-
lazy-1-isvaluecreated)| Gets a value that indicates whether a value has been
created for this
[Lazy<T>](https://learn.microsoft.com/dotnet/api/system.lazy-1) instance.  
(Унаследован от
[Lazy](https://learn.microsoft.com/dotnet/api/system.lazy-1)<[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<T>>)  
---|---  
[Value](https://learn.microsoft.com/dotnet/api/system.lazy-1.value#system-
lazy-1-value)| Gets the lazily initialized value of the current
[Lazy<T>](https://learn.microsoft.com/dotnet/api/system.lazy-1) instance.  
(Унаследован от
[Lazy](https://learn.microsoft.com/dotnet/api/system.lazy-1)<[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<T>>)  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetAwaiter](M_Tessa_Platform_AsyncLazy_1_GetAwaiter.htm)|  
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
[ToString](https://learn.microsoft.com/dotnet/api/system.lazy-1.tostring#system-
lazy-1-tostring)| Creates and returns a string representation of the
[Value](https://learn.microsoft.com/dotnet/api/system.lazy-1.value#system-
lazy-1-value) property for this instance.  
(Унаследован от
[Lazy](https://learn.microsoft.com/dotnet/api/system.lazy-1)<[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<T>>)  
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
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
