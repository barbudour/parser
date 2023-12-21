# PipeRequestProvider - класс
Объект, предоставляющий средства создания и подготовки запросов.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class PipeRequestProvider : IPipeRequestProvider
VB __Копировать
     Public Class PipeRequestProvider
    	Implements IPipeRequestProvider
C++ __Копировать
     public ref class PipeRequestProvider : IPipeRequestProvider
F# __Копировать
     type PipeRequestProvider = 
        class
            interface IPipeRequestProvider
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PipeRequestProvider
Implements
    [IPipeRequestProvider](T_Tessa_Platform_Pipes_IPipeRequestProvider.htm)
##  __Заметки
Наследники класса могут переопределить или добавить методы.
## __Конструкторы
[PipeRequestProvider](M_Tessa_Platform_Pipes_PipeRequestProvider__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
## __Свойства
[MessageFactory](P_Tessa_Platform_Pipes_PipeRequestProvider_MessageFactory.htm)|
Фабрика объектов, используемых для создания сообщений, передаваемых по каналу.  
---|---  
[RequestMapping](P_Tessa_Platform_Pipes_PipeRequestProvider_RequestMapping.htm)|
Объект, преобразующий параметры запроса, связанные с методом сервиса.  
## __Методы
[CreateBinaryRequestAsync](M_Tessa_Platform_Pipes_PipeRequestProvider_CreateBinaryRequestAsync.htm)|
Создаёт сообщение-запрос, который используется совместно с методом подготовки
[PrepareRequestAsync(IPipeRequest, Type, String,
CancellationToken)](M_Tessa_Platform_Pipes_IPipeRequestProvider_PrepareRequestAsync.htm)
для передачи сообщения с массивом байт
[BinaryData](P_Tessa_Platform_Pipes_IPipeBinaryMessage_BinaryData.htm).  
---|---  
[CreateBinaryRequestCoreAsync](M_Tessa_Platform_Pipes_PipeRequestProvider_CreateBinaryRequestCoreAsync.htm)|
Создаёт сообщение-запрос, который используется совместно с методом подготовки
[PrepareRequestAsync(IPipeRequest, Type, String,
CancellationToken)](M_Tessa_Platform_Pipes_IPipeRequestProvider_PrepareRequestAsync.htm)
для передачи сообщения с массивом байт
[BinaryData](P_Tessa_Platform_Pipes_IPipeBinaryMessage_BinaryData.htm).  
[CreateRequestAsync](M_Tessa_Platform_Pipes_PipeRequestProvider_CreateRequestAsync.htm)|
Создаёт сообщение-запрос, который используется совместно с методом подготовки
[PrepareRequestAsync(IPipeRequest, Type, String,
CancellationToken)](M_Tessa_Platform_Pipes_IPipeRequestProvider_PrepareRequestAsync.htm).  
[CreateRequestCoreAsync](M_Tessa_Platform_Pipes_PipeRequestProvider_CreateRequestCoreAsync.htm)|
Создаёт сообщение-запрос, который используется совместно с методом подготовки
[PrepareRequestAsync(IPipeRequest, Type, String,
CancellationToken)](M_Tessa_Platform_Pipes_IPipeRequestProvider_PrepareRequestAsync.htm).  
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
[PrepareRequestAsync](M_Tessa_Platform_Pipes_PipeRequestProvider_PrepareRequestAsync.htm)|
Подготавливает поля запроса, связанные с маршрутизацией, с учётом указанных
типа сервиса и имени метода.  
[PrepareRequestCoreAsync](M_Tessa_Platform_Pipes_PipeRequestProvider_PrepareRequestCoreAsync.htm)|
Подготавливает поля запроса, связанные с маршрутизацией, с учётом указанных
типа сервиса и имени метода.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[CreateBinaryRequestAsync](M_Tessa_Platform_Pipes_PipesExtensions_CreateBinaryRequestAsync.htm)|
Создаёт и подготавливает запрос для отправки к методу заданного сервиса,
причём сообщение кодируется вместе с массивом байт
[BinaryData](P_Tessa_Platform_Pipes_IPipeBinaryMessage_BinaryData.htm).  
(Определяется [PipesExtensions](T_Tessa_Platform_Pipes_PipesExtensions.htm))  
---|---  
[CreateBinaryRequestAsync<T>](M_Tessa_Platform_Pipes_PipesExtensions_CreateBinaryRequestAsync__1.htm)|
Создаёт и подготавливает запрос для отправки к методу заданного сервиса,
причём сообщение кодируется вместе с массивом байт
[BinaryData](P_Tessa_Platform_Pipes_IPipeBinaryMessage_BinaryData.htm).  
(Определяется [PipesExtensions](T_Tessa_Platform_Pipes_PipesExtensions.htm))  
[CreateRequestAsync](M_Tessa_Platform_Pipes_PipesExtensions_CreateRequestAsync.htm)|
Создаёт и подготавливает запрос для отправки к методу заданного сервиса.  
(Определяется [PipesExtensions](T_Tessa_Platform_Pipes_PipesExtensions.htm))  
[CreateRequestAsync<T>](M_Tessa_Platform_Pipes_PipesExtensions_CreateRequestAsync__1.htm)|
Создаёт и подготавливает запрос для отправки к методу заданного сервиса.  
(Определяется [PipesExtensions](T_Tessa_Platform_Pipes_PipesExtensions.htm))  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
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
