# IPipeRequestProvider - интерфейс
Объект, предоставляющий средства создания и подготовки запросов.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPipeRequestProvider
VB __Копировать
     Public Interface IPipeRequestProvider
C++ __Копировать
     public interface class IPipeRequestProvider
F# __Копировать
     type IPipeRequestProvider = interface end
##  __Методы
[CreateBinaryRequestAsync](M_Tessa_Platform_Pipes_IPipeRequestProvider_CreateBinaryRequestAsync.htm)|
Создаёт сообщение-запрос, который используется совместно с методом подготовки
[PrepareRequestAsync(IPipeRequest, Type, String,
CancellationToken)](M_Tessa_Platform_Pipes_IPipeRequestProvider_PrepareRequestAsync.htm)
для передачи сообщения с массивом байт
[BinaryData](P_Tessa_Platform_Pipes_IPipeBinaryMessage_BinaryData.htm).  
---|---  
[CreateRequestAsync](M_Tessa_Platform_Pipes_IPipeRequestProvider_CreateRequestAsync.htm)|
Создаёт сообщение-запрос, который используется совместно с методом подготовки
[PrepareRequestAsync(IPipeRequest, Type, String,
CancellationToken)](M_Tessa_Platform_Pipes_IPipeRequestProvider_PrepareRequestAsync.htm).  
[PrepareRequestAsync](M_Tessa_Platform_Pipes_IPipeRequestProvider_PrepareRequestAsync.htm)|
Подготавливает поля запроса, связанные с маршрутизацией, с учётом указанных
типа сервиса и имени метода.  
## __Методы расширения
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
##  __См. также
#### Ссылки
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
