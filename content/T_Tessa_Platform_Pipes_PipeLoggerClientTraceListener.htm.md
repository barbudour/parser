# PipeLoggerClientTraceListener - класс
Объект, выполняющий логирование событий, происходящих с каналом со стороны
сервера.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class PipeLoggerClientTraceListener : PipeClientTraceListener
VB __Копировать
     Public Class PipeLoggerClientTraceListener
    	Inherits PipeClientTraceListener
C++ __Копировать
     public ref class PipeLoggerClientTraceListener : public PipeClientTraceListener
F# __Копировать
     type PipeLoggerClientTraceListener = 
        class
            inherit PipeClientTraceListener
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[PipeClientTraceListener](T_Tessa_Platform_Pipes_PipeClientTraceListener.htm) __ PipeLoggerClientTraceListener
##  __Заметки
Наследники класса могут переопределить его методы.
## __Конструкторы
[PipeLoggerClientTraceListener](M_Tessa_Platform_Pipes_PipeLoggerClientTraceListener__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[Logger](P_Tessa_Platform_Pipes_PipeLoggerClientTraceListener_Logger.htm)|
Объект, выполняющий логирование. Не равен null.  
---|---  
[LogLevel](P_Tessa_Platform_Pipes_PipeLoggerClientTraceListener_LogLevel.htm)|
Уровень, на котором выполняется логирование. Не равен null или пустой строке.  
[PipeName](P_Tessa_Platform_Pipes_PipeLoggerClientTraceListener_PipeName.htm)|
Название канала, для которого выполняется логирование. Не равен null или
пустой строке.  
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
[OnClientConnectedAsync](M_Tessa_Platform_Pipes_PipeLoggerClientTraceListener_OnClientConnectedAsync.htm)|
Уведомляет о событии установки соединения с сервером.  
(Переопределяет
[PipeClientTraceListener.OnClientConnectedAsync(CancellationToken)](M_Tessa_Platform_Pipes_PipeClientTraceListener_OnClientConnectedAsync.htm))  
[OnClientDisconnectedAsync](M_Tessa_Platform_Pipes_PipeLoggerClientTraceListener_OnClientDisconnectedAsync.htm)|
Уведомляет о событии закрытия соединения с сервером.  
(Переопределяет
[PipeClientTraceListener.OnClientDisconnectedAsync(CancellationToken)](M_Tessa_Platform_Pipes_PipeClientTraceListener_OnClientDisconnectedAsync.htm))  
[OnExceptionAsync](M_Tessa_Platform_Pipes_PipeLoggerClientTraceListener_OnExceptionAsync.htm)|
Уведомляет о событии возникновения исключения при обработке запроса.
Исключение от сервера приходит как
[ValidationException](T_Tessa_Platform_Validation_ValidationException.htm).  
(Переопределяет [PipeClientTraceListener.OnExceptionAsync(Exception,
CancellationToken)](M_Tessa_Platform_Pipes_PipeClientTraceListener_OnExceptionAsync.htm))  
[OnRequestPreparedAsync](M_Tessa_Platform_Pipes_PipeLoggerClientTraceListener_OnRequestPreparedAsync.htm)|
Уведомляет о событии подготовки запроса к отправке на сервер.  
(Переопределяет [PipeClientTraceListener.OnRequestPreparedAsync(IPipeRequest,
CancellationToken)](M_Tessa_Platform_Pipes_PipeClientTraceListener_OnRequestPreparedAsync.htm))  
[OnResponseReceivedAsync](M_Tessa_Platform_Pipes_PipeLoggerClientTraceListener_OnResponseReceivedAsync.htm)|
Уведомляет о событии получения ответа на запрос от сервера. Ответ на запрос не
является исключением.  
(Переопределяет [PipeClientTraceListener.OnResponseReceivedAsync(IPipeRequest,
IPipeResponse,
CancellationToken)](M_Tessa_Platform_Pipes_PipeClientTraceListener_OnResponseReceivedAsync.htm))  
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
