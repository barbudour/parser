# PipeMessageFactory - класс
Фабрика объектов, используемых для создания сообщений, передаваемых по каналу.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class PipeMessageFactory : IPipeMessageFactory
VB __Копировать
     Public Class PipeMessageFactory
    	Implements IPipeMessageFactory
C++ __Копировать
     public ref class PipeMessageFactory : IPipeMessageFactory
F# __Копировать
     type PipeMessageFactory = 
        class
            interface IPipeMessageFactory
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PipeMessageFactory
Implements
    [IPipeMessageFactory](T_Tessa_Platform_Pipes_IPipeMessageFactory.htm)
##  __Заметки
Наследники класса могут переопределить методы создания объектов.
## __Конструкторы
[PipeMessageFactory](M_Tessa_Platform_Pipes_PipeMessageFactory__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
## __Свойства
[CreateBinaryRequestFunc](P_Tessa_Platform_Pipes_PipeMessageFactory_CreateBinaryRequestFunc.htm)|
Функция, выполняющая создание объекта
[IPipeBinaryRequest](T_Tessa_Platform_Pipes_IPipeBinaryRequest.htm).  
---|---  
[CreateBinaryResponseFunc](P_Tessa_Platform_Pipes_PipeMessageFactory_CreateBinaryResponseFunc.htm)|
Функция, выполняющая создание объекта
[IPipeBinaryResponse](T_Tessa_Platform_Pipes_IPipeBinaryResponse.htm).  
[CreateExceptionResponseFunc](P_Tessa_Platform_Pipes_PipeMessageFactory_CreateExceptionResponseFunc.htm)|
Функция, выполняющая создание объекта
[IPipeExceptionResponse](T_Tessa_Platform_Pipes_IPipeExceptionResponse.htm).  
[CreateRequestFunc](P_Tessa_Platform_Pipes_PipeMessageFactory_CreateRequestFunc.htm)|
Функция, выполняющая создание объекта
[IPipeRequest](T_Tessa_Platform_Pipes_IPipeRequest.htm).  
[CreateResponseFunc](P_Tessa_Platform_Pipes_PipeMessageFactory_CreateResponseFunc.htm)|
Функция, выполняющая создание объекта
[IPipeResponse](T_Tessa_Platform_Pipes_IPipeResponse.htm).  
## __Методы
[CreateBinaryRequest](M_Tessa_Platform_Pipes_PipeMessageFactory_CreateBinaryRequest.htm)|
Создаёт сообщение-запрос, передаваемое по каналу и содержащее массив байт,
передаваемый отдельным сообщением без кодирования.  
---|---  
[CreateBinaryResponse](M_Tessa_Platform_Pipes_PipeMessageFactory_CreateBinaryResponse.htm)|
Создаёт сообщениеявляющееся ответом на запрос, передаваемое по каналу и
содержащее массив байт, передаваемый отдельным сообщением без кодирования.  
[CreateExceptionResponse](M_Tessa_Platform_Pipes_PipeMessageFactory_CreateExceptionResponse.htm)|
Создаёт сообщение, являющееся ответом на запрос с сериализованным исключением
и передаваемое по каналу.  
[CreateRequest](M_Tessa_Platform_Pipes_PipeMessageFactory_CreateRequest.htm)|
Создаёт сообщение-запрос, передаваемое по каналу.  
[CreateResponse](M_Tessa_Platform_Pipes_PipeMessageFactory_CreateResponse.htm)|
Создаёт сообщение, являющееся ответом на запрос и передаваемое по каналу.  
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
