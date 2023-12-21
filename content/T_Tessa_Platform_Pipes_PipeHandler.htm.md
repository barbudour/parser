# PipeHandler - класс
Базовый класс для объекта, выполняющего обработку сообщений, полученных по
каналу.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class PipeHandler : IPipeHandler
VB __Копировать
     Public MustInherit Class PipeHandler
    	Implements IPipeHandler
C++ __Копировать
     public ref class PipeHandler abstract : IPipeHandler
F# __Копировать
     [<AbstractClassAttribute>]
    type PipeHandler = 
        class
            interface IPipeHandler
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PipeHandler
Derived
[Tessa.Platform.Pipes.PipeMethodHandler](T_Tessa_Platform_Pipes_PipeMethodHandler.htm)
Implements
    [IPipeHandler](T_Tessa_Platform_Pipes_IPipeHandler.htm)
##  __Конструкторы
[PipeHandler](M_Tessa_Platform_Pipes_PipeHandler__ctor.htm)| Инициализирует
новый экземпляр класса PipeHandler  
---|---  
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
[TryHandleAsync](M_Tessa_Platform_Pipes_PipeHandler_TryHandleAsync.htm)|
Выполняет обработку сообщения, полученного по каналу. Возвращает null, если
обработка не выполнена, например, если подходящий метод не был
зарегистрирован.  
[TryHandleCoreAsync](M_Tessa_Platform_Pipes_PipeHandler_TryHandleCoreAsync.htm)|
Выполняет обработку сообщения, полученного по каналу. Возвращает null, если
обработка не выполнена, например, если подходящий метод не был
зарегистрирован.  
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
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
