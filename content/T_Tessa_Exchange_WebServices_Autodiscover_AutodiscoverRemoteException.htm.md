# AutodiscoverRemoteException - класс
Represents an exception that is thrown when the Autodiscover service returns
an error.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Autodiscover](N_Tessa_Exchange_WebServices_Autodiscover.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public class AutodiscoverRemoteException : ServiceRemoteException
VB __Копировать
     Public Class AutodiscoverRemoteException
    	Inherits ServiceRemoteException
C++ __Копировать
     public ref class AutodiscoverRemoteException : public ServiceRemoteException
F# __Копировать
     type AutodiscoverRemoteException = 
        class
            inherit ServiceRemoteException
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[Exception](https://learn.microsoft.com/dotnet/api/system.exception) __[ServiceRemoteException](T_Tessa_Exchange_WebServices_Data_ServiceRemoteException.htm) __ AutodiscoverRemoteException
##  __Конструкторы
[AutodiscoverRemoteException(AutodiscoverError)](M_Tessa_Exchange_WebServices_Autodiscover_AutodiscoverRemoteException__ctor_3.htm)|
Initializes a new instance of the AutodiscoverRemoteException class.  
---|---  
[AutodiscoverRemoteException(SerializationInfo,
StreamingContext)](M_Tessa_Exchange_WebServices_Autodiscover_AutodiscoverRemoteException__ctor.htm)|
Initializes a new instance of the AutodiscoverRemoteException class with
serialized data.  
[AutodiscoverRemoteException(String,
AutodiscoverError)](M_Tessa_Exchange_WebServices_Autodiscover_AutodiscoverRemoteException__ctor_1.htm)|
Initializes a new instance of the AutodiscoverRemoteException class.  
[AutodiscoverRemoteException(String, AutodiscoverError,
Exception)](M_Tessa_Exchange_WebServices_Autodiscover_AutodiscoverRemoteException__ctor_2.htm)|
Initializes a new instance of the AutodiscoverRemoteException class.  
## __Свойства
[Data](https://learn.microsoft.com/dotnet/api/system.exception.data#system-
exception-data)| Gets a collection of key/value pairs that provide additional
user-defined information about the exception.  
(Унаследован от
[Exception](https://learn.microsoft.com/dotnet/api/system.exception))  
---|---  
[Error](P_Tessa_Exchange_WebServices_Autodiscover_AutodiscoverRemoteException_Error.htm)|
Gets the error.  
[HelpLink](https://learn.microsoft.com/dotnet/api/system.exception.helplink#system-
exception-helplink)| Gets or sets a link to the help file associated with this
exception.  
(Унаследован от
[Exception](https://learn.microsoft.com/dotnet/api/system.exception))  
[HResult](https://learn.microsoft.com/dotnet/api/system.exception.hresult#system-
exception-hresult)| Gets or sets HRESULT, a coded numerical value that is
assigned to a specific exception.  
(Унаследован от
[Exception](https://learn.microsoft.com/dotnet/api/system.exception))  
[InnerException](https://learn.microsoft.com/dotnet/api/system.exception.innerexception#system-
exception-innerexception)| Gets the
[Exception](https://learn.microsoft.com/dotnet/api/system.exception) instance
that caused the current exception.  
(Унаследован от
[Exception](https://learn.microsoft.com/dotnet/api/system.exception))  
[Message](https://learn.microsoft.com/dotnet/api/system.exception.message#system-
exception-message)| Gets a message that describes the current exception.  
(Унаследован от
[Exception](https://learn.microsoft.com/dotnet/api/system.exception))  
[Source](https://learn.microsoft.com/dotnet/api/system.exception.source#system-
exception-source)| Gets or sets the name of the application or the object that
causes the error.  
(Унаследован от
[Exception](https://learn.microsoft.com/dotnet/api/system.exception))  
[StackTrace](https://learn.microsoft.com/dotnet/api/system.exception.stacktrace#system-
exception-stacktrace)| Gets a string representation of the immediate frames on
the call stack.  
(Унаследован от
[Exception](https://learn.microsoft.com/dotnet/api/system.exception))  
[TargetSite](https://learn.microsoft.com/dotnet/api/system.exception.targetsite#system-
exception-targetsite)| Gets the method that throws the current exception.  
(Унаследован от
[Exception](https://learn.microsoft.com/dotnet/api/system.exception))  
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
[GetBaseException](https://learn.microsoft.com/dotnet/api/system.exception.getbaseexception#system-
exception-getbaseexception)| When overridden in a derived class, returns the
[Exception](https://learn.microsoft.com/dotnet/api/system.exception) that is
the root cause of one or more subsequent exceptions.  
(Унаследован от
[Exception](https://learn.microsoft.com/dotnet/api/system.exception))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetObjectData](M_Tessa_Exchange_WebServices_Autodiscover_AutodiscoverRemoteException_GetObjectData.htm)|
Sets the
[SerializationInfo](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.serializationinfo)
object with the parameter name and additional exception information.  
(Переопределяет [Exception.GetObjectData(SerializationInfo,
StreamingContext)](https://learn.microsoft.com/dotnet/api/system.exception.getobjectdata#system-
exception-getobjectdata\(system-runtime-serialization-serializationinfo-
system-runtime-serialization-streamingcontext\)))  
[GetType](https://learn.microsoft.com/dotnet/api/system.exception.gettype#system-
exception-gettype)| Gets the runtime type of the current instance.  
(Унаследован от
[Exception](https://learn.microsoft.com/dotnet/api/system.exception))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.exception.tostring#system-
exception-tostring)| Creates and returns a string representation of the
current exception.  
(Унаследован от
[Exception](https://learn.microsoft.com/dotnet/api/system.exception))  
##  __События
[SerializeObjectState](https://learn.microsoft.com/dotnet/api/system.exception.serializeobjectstate)|
Occurs when an exception is serialized to create an exception state object
that contains serialized data about the exception.  
(Унаследован от
[Exception](https://learn.microsoft.com/dotnet/api/system.exception))  
---|---  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[GetFullText](M_Chronos_Platform_PlatformExtensions_GetFullText.htm)|
Возвращает полную информацию по заданному исключению, включая текст нескольких
исключений для
[AggregateException](https://learn.microsoft.com/dotnet/api/system.aggregateexception).
Для обычных исключений результат аналогичен вызову метода
[ToString()](https://learn.microsoft.com/dotnet/api/system.exception.tostring#system-
exception-tostring).  
(Определяется [PlatformExtensions](T_Chronos_Platform_PlatformExtensions.htm))  
[GetFullText](M_Tessa_Platform_PlatformExtensions_GetFullText.htm)|
Возвращает полную информацию по заданному исключению, включая серверный
стектрейс для
[FaultException](https://learn.microsoft.com/dotnet/api/system.servicemodel.faultexception)
и текст нескольких исключений для
[AggregateException](https://learn.microsoft.com/dotnet/api/system.aggregateexception).
Для обычных исключений результат аналогичен вызову метода
[ToString()](https://learn.microsoft.com/dotnet/api/system.exception.tostring#system-
exception-tostring).  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[GetSessionExceptionCode](M_Tessa_Platform_Runtime_RuntimeExtensions_GetSessionExceptionCode.htm)|
Возвращает код исключения, выброшенного на сервере как
[SessionException](T_Tessa_Platform_Runtime_SessionException.htm), или
[Unknown](T_Tessa_Platform_Runtime_SessionExceptionCode.htm), если код
исключения получить не удалось.  
(Определяется
[RuntimeExtensions](T_Tessa_Platform_Runtime_RuntimeExtensions.htm))  
[GetShortText](M_Tessa_Platform_PlatformExtensions_GetShortText.htm)|
Возвращает краткую информацию по заданному исключению, что обычно
соответствует
[Message](https://learn.microsoft.com/dotnet/api/system.exception.message#system-
exception-message).  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[GetStatusCode](M_Tessa_Platform_PlatformExtensions_GetStatusCode.htm)|
Возвращает код ошибки HTTP-запроса в зависимости от вида исключения. Для
неизвестных исключений возвращается
[InternalServerError](https://learn.microsoft.com/dotnet/api/system.net.httpstatuscode).  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[IsExceptionCritical](M_Tessa_Platform_Runtime_RuntimeExtensions_IsExceptionCritical.htm)|
Возвращает признак того, что указанное исключение относится в разряд
критических и должно привести к завершению приложения.  
(Определяется
[RuntimeExtensions](T_Tessa_Platform_Runtime_RuntimeExtensions.htm))  
[IsLoginHiddenException](M_Tessa_Platform_Runtime_RuntimeExtensions_IsLoginHiddenException.htm)|
Возвращает признак того, что исключение не отображается пользователю, когда
оно возникло при входе в систему. Например, пользователь не входит в домен.  
(Определяется
[RuntimeExtensions](T_Tessa_Platform_Runtime_RuntimeExtensions.htm))  
[IsUnauthorizedWebException](M_Tessa_Platform_Runtime_RuntimeExtensions_IsUnauthorizedWebException.htm)|
Возвращает признак того, что исключение является ошибкой с кодом ошибки 401:
[Unauthorized](https://learn.microsoft.com/dotnet/api/system.net.httpstatuscode).
Обычно такое исключение происходит при неудачной авторизации Windows.
Учитывает агрегирование асинхронных исключений.  
(Определяется
[RuntimeExtensions](T_Tessa_Platform_Runtime_RuntimeExtensions.htm))  
[PipeIsBroken](M_Tessa_Platform_Pipes_PipesExtensions_PipeIsBroken.htm)|
Возвращает признак того, что исключение связано с остановкой канала, например,
если клиент разорвал подключение, а метод пытается передать сообщение клиенту.
Обычно соответствует ошибке с текстом "Pipe is broken". Учитывает наличие
вложенных исключений и
[AggregateException](https://learn.microsoft.com/dotnet/api/system.aggregateexception).  
(Определяется [PipesExtensions](T_Tessa_Platform_Pipes_PipesExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[ToJson](M_Tessa_Platform_PlatformExtensions_ToJson.htm)|  Выполняет
сериализацию исключения в JSON. Может использоваться для передачи исключений
между сервером и клиентом.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[ToPlainValidationResult](M_Tessa_Platform_PlatformExtensions_ToPlainValidationResult.htm)|
Выполняет сериализацию исключения в виде объекта
[PlainValidationResult](T_Tessa_Platform_Validation_PlainValidationResult.htm).
Может использоваться для передачи исключений между сервером и клиентом.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[TryGetNestedInnerException](M_Tessa_Platform_PlatformExtensions_TryGetNestedInnerException.htm)|
Возвращает вложенное исключение для ex на любое число уровней вложенности,
которое удовлетворяет условию predicateFunc, или null, если такое вложенное
исключение не найдено.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Exchange.WebServices.Autodiscover - пространство
имён](N_Tessa_Exchange_WebServices_Autodiscover.htm)
