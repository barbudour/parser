# ViewException - класс
Исключение произошедшее при выполнении представления.
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public class ViewException : ApplicationException
VB __Копировать
    <SerializableAttribute>
    Public Class ViewException
    	Inherits ApplicationException
C++ __Копировать
    [SerializableAttribute]
    public ref class ViewException : public ApplicationException
F# __Копировать
     [<SerializableAttribute>]
    type ViewException = 
        class
            inherit ApplicationException
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[Exception](https://learn.microsoft.com/dotnet/api/system.exception) __[ApplicationException](https://learn.microsoft.com/dotnet/api/system.applicationexception) __ ViewException
##  __Конструкторы
[ViewException(String)](M_Tessa_Views_ViewException__ctor_1.htm)|  Создаёт
экземпляр класса с указанием сообщения.  
---|---  
[ViewException(SerializationInfo,
StreamingContext)](M_Tessa_Views_ViewException__ctor.htm)|  Создаёт экземпляр
класса, десериализованный с использованием переданного объекта
[System.Runtime.Serialization.SerializationInfo].  
[ViewException(String, Boolean,
Exception)](M_Tessa_Views_ViewException__ctor_2.htm)|  Создаёт экземпляр
класса с указанием внутреннего исключения, послужившее причиной этому.  
## __Свойства
[Data](https://learn.microsoft.com/dotnet/api/system.exception.data#system-
exception-data)| Gets a collection of key/value pairs that provide additional
user-defined information about the exception.  
(Унаследован от
[Exception](https://learn.microsoft.com/dotnet/api/system.exception))  
---|---  
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
[IsLogged](P_Tessa_Views_ViewException_IsLogged.htm)|  Значение, показывающее,
было ли исключение залогировано или нет.  
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
[GetObjectData](M_Tessa_Views_ViewException_GetObjectData.htm)|  Записывает
сериализованные данные текущего объекта в указанный объект
[System.Runtime.Serialization.SerializationInfo].  
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
[Tessa.Views - пространство имён](N_Tessa_Views.htm)
