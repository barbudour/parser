# PipeMethodHandler - класс
Объект, выполняющий обработку сообщений, полученных по каналу. Предоставляет
метод регистрации обработчика по имени метода.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class PipeMethodHandler : PipeHandler, 
    	IPipeMethodHandler, IPipeHandler
VB __Копировать
     Public Class PipeMethodHandler
    	Inherits PipeHandler
    	Implements IPipeMethodHandler, IPipeHandler
C++ __Копировать
     public ref class PipeMethodHandler : public PipeHandler, 
    	IPipeMethodHandler, IPipeHandler
F# __Копировать
     type PipeMethodHandler = 
        class
            inherit PipeHandler
            interface IPipeMethodHandler
            interface IPipeHandler
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[PipeHandler](T_Tessa_Platform_Pipes_PipeHandler.htm) __ PipeMethodHandler
Implements
    [IPipeHandler](T_Tessa_Platform_Pipes_IPipeHandler.htm), [IPipeMethodHandler](T_Tessa_Platform_Pipes_IPipeMethodHandler.htm)
##  __Заметки
Наследники класса могут переопределить методы и свойства, а также добавить
дополнительные методы.
## __Конструкторы
[PipeMethodHandler](M_Tessa_Platform_Pipes_PipeMethodHandler__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
## __Свойства
[HandlersByMethodNames](P_Tessa_Platform_Pipes_PipeMethodHandler_HandlersByMethodNames.htm)|
Обработчики запросов, зарегистрированные по имени метода.  
---|---  
[RequestMapping](P_Tessa_Platform_Pipes_PipeMethodHandler_RequestMapping.htm)|
Объект, преобразующий параметры запроса, связанные с методом сервиса.  
## __Методы
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
[Register](M_Tessa_Platform_Pipes_PipeMethodHandler_Register.htm)|  Выполняет
регистрацию метода обработки по имени.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryHandleAsync](M_Tessa_Platform_Pipes_PipeHandler_TryHandleAsync.htm)|
Выполняет обработку сообщения, полученного по каналу. Возвращает null, если
обработка не выполнена, например, если подходящий метод не был
зарегистрирован.  
(Унаследован от [PipeHandler](T_Tessa_Platform_Pipes_PipeHandler.htm))  
[TryHandleCoreAsync](M_Tessa_Platform_Pipes_PipeMethodHandler_TryHandleCoreAsync.htm)|
Выполняет обработку сообщения, полученного по каналу. Возвращает null, если
обработка не выполнена, например, если подходящий метод не был
зарегистрирован.  
(Переопределяет [PipeHandler.TryHandleCoreAsync(IPipeRequest, IPipeResponse,
CancellationToken)](M_Tessa_Platform_Pipes_PipeHandler_TryHandleCoreAsync.htm))  
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
[Register<T>](M_Tessa_Platform_Pipes_PipesExtensions_Register__1_1.htm)|
Выполняет регистрацию метода обработки по имени, в который передаётся
экземпляр объекта T, время жизни которого контролируется объектом
instanceResolver. Используйте объект
[PipeContextualInstanceResolver](T_Tessa_Platform_Pipes_PipeContextualInstanceResolver.htm)
(container.[GetContextualInstanceResolver(IUnityContainer)](M_Tessa_Platform_Pipes_PipesExtensions_GetContextualInstanceResolver.htm)),
чтобы время жизни экземпляра объекта, передаваемого в метод обработки
сообщения handleAsync, определялось временем жизни соединения сервера с
клиентом.  
(Определяется [PipesExtensions](T_Tessa_Platform_Pipes_PipesExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
