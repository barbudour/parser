# PipeServiceRouter - класс
Объект, выполняющий маршрутизацию сообщений, полученных по каналу.
Предоставляет метод регистрации обработчика по типу сервиса.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class PipeServiceRouter : PipeRouter, 
    	IPipeServiceRouter, IPipeRouter
VB __Копировать
     Public Class PipeServiceRouter
    	Inherits PipeRouter
    	Implements IPipeServiceRouter, IPipeRouter
C++ __Копировать
     public ref class PipeServiceRouter : public PipeRouter, 
    	IPipeServiceRouter, IPipeRouter
F# __Копировать
     type PipeServiceRouter = 
        class
            inherit PipeRouter
            interface IPipeServiceRouter
            interface IPipeRouter
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[PipeRouter](T_Tessa_Platform_Pipes_PipeRouter.htm) __ PipeServiceRouter
Implements
    [IPipeRouter](T_Tessa_Platform_Pipes_IPipeRouter.htm), [IPipeServiceRouter](T_Tessa_Platform_Pipes_IPipeServiceRouter.htm)
##  __Заметки
Наследники класса могут переопределить методы и свойства, а также добавить
дополнительные методы.
## __Конструкторы
[PipeServiceRouter](M_Tessa_Platform_Pipes_PipeServiceRouter__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
## __Свойства
[HandlersByServiceTypes](P_Tessa_Platform_Pipes_PipeServiceRouter_HandlersByServiceTypes.htm)|
Обработчики запросов, зарегистрированные по имени типа сервиса.  
---|---  
[RequestMapping](P_Tessa_Platform_Pipes_PipeServiceRouter_RequestMapping.htm)|
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
[Register](M_Tessa_Platform_Pipes_PipeServiceRouter_Register.htm)|  Выполняет
регистрацию обработчика по типу сервиса.  
[RemoveRegistration](M_Tessa_Platform_Pipes_PipeServiceRouter_RemoveRegistration.htm)|
Удаляет регистрацию обработчика для заданного сервиса.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetHandlerAsync](M_Tessa_Platform_Pipes_PipeRouter_TryGetHandlerAsync.htm)|
Возвращает объект, выполняющий обработку запроса в канале, или null, если
подходящий объект не зарегистрирован.  
(Унаследован от [PipeRouter](T_Tessa_Platform_Pipes_PipeRouter.htm))  
[TryGetHandlerCoreAsync](M_Tessa_Platform_Pipes_PipeServiceRouter_TryGetHandlerCoreAsync.htm)|
Возвращает объект, выполняющий обработку запроса в канале, или null, если
подходящий объект не зарегистрирован.  
(Переопределяет [PipeRouter.TryGetHandlerCoreAsync(IPipeRequest,
CancellationToken)](M_Tessa_Platform_Pipes_PipeRouter_TryGetHandlerCoreAsync.htm))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[HandleAsync](M_Tessa_Platform_Pipes_PipesExtensions_HandleAsync.htm)|
Выполняет обработку сообщения по каналу и возвращает ответ на запрос,
отправленный по каналу. Не возвращает null, в случае невозможности обработки
выбрасывается исключение
[InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception).  
(Определяется [PipesExtensions](T_Tessa_Platform_Pipes_PipesExtensions.htm))  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Register](M_Tessa_Platform_Pipes_PipesExtensions_Register.htm)|  Выполняет
регистрацию обработчика по типу сервиса.  
(Определяется [PipesExtensions](T_Tessa_Platform_Pipes_PipesExtensions.htm))  
[Register<T>](M_Tessa_Platform_Pipes_PipesExtensions_Register__1_2.htm)|
Выполняет регистрацию обработчика по типу сервиса.  
(Определяется [PipesExtensions](T_Tessa_Platform_Pipes_PipesExtensions.htm))  
[Register<T>](M_Tessa_Platform_Pipes_PipesExtensions_Register__1_3.htm)|
Выполняет регистрацию обработчика по типу сервиса.  
(Определяется [PipesExtensions](T_Tessa_Platform_Pipes_PipesExtensions.htm))  
[RemoveRegistration<T>](M_Tessa_Platform_Pipes_PipesExtensions_RemoveRegistration__1.htm)|
Удаляет регистрацию обработчика для заданного сервиса.  
(Определяется [PipesExtensions](T_Tessa_Platform_Pipes_PipesExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
