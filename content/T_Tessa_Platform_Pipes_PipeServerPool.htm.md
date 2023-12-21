# PipeServerPool - класс
Пул серверов, который поддерживает сразу несколько соединений
[IPipeServer](T_Tessa_Platform_Pipes_IPipeServer.htm) с автоматическим
расширением количества соединений. Объект не является синглтоном, создавайте
экземпляр объекта для каждого пула соединений.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class PipeServerPool : IPipeServerPool, 
    	IAsyncDisposable, IDisposable
VB __Копировать
     Public NotInheritable Class PipeServerPool
    	Implements IPipeServerPool, IAsyncDisposable, IDisposable
C++ __Копировать
     public ref class PipeServerPool sealed : IPipeServerPool, 
    	IAsyncDisposable, IDisposable
F# __Копировать
     [<SealedAttribute>]
    type PipeServerPool = 
        class
            interface IPipeServerPool
            interface IAsyncDisposable
            interface IDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PipeServerPool
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [IPipeServerPool](T_Tessa_Platform_Pipes_IPipeServerPool.htm)
##  __Конструкторы
[PipeServerPool](M_Tessa_Platform_Pipes_PipeServerPool__ctor.htm)|
Инициализирует новый экземпляр класса PipeServerPool  
---|---  
##  __Методы
[Dispose](M_Tessa_Platform_Pipes_PipeServerPool_Dispose.htm)| Освобождает
ресурсы, занимаемые объектом.  
---|---  
[DisposeAsync](M_Tessa_Platform_Pipes_PipeServerPool_DisposeAsync.htm)|
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
[StartListeningAsync](M_Tessa_Platform_Pipes_PipeServerPool_StartListeningAsync.htm)|
Запускает прослушивание в пуле серверов.  
[StopListeningAsync](M_Tessa_Platform_Pipes_PipeServerPool_StopListeningAsync.htm)|
Останавливает прослушивание в пуле серверов.  
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
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
