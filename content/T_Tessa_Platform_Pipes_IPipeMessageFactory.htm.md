# IPipeMessageFactory - интерфейс
Фабрика объектов, используемых для создания сообщений, передаваемых по каналу.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPipeMessageFactory
VB __Копировать
     Public Interface IPipeMessageFactory
C++ __Копировать
     public interface class IPipeMessageFactory
F# __Копировать
     type IPipeMessageFactory = interface end
##  __Методы
[CreateBinaryRequest](M_Tessa_Platform_Pipes_IPipeMessageFactory_CreateBinaryRequest.htm)|
Создаёт сообщение-запрос, передаваемое по каналу и содержащее массив байт,
передаваемый отдельным сообщением без кодирования.  
---|---  
[CreateBinaryResponse](M_Tessa_Platform_Pipes_IPipeMessageFactory_CreateBinaryResponse.htm)|
Создаёт сообщениеявляющееся ответом на запрос, передаваемое по каналу и
содержащее массив байт, передаваемый отдельным сообщением без кодирования.  
[CreateExceptionResponse](M_Tessa_Platform_Pipes_IPipeMessageFactory_CreateExceptionResponse.htm)|
Создаёт сообщение, являющееся ответом на запрос с сериализованным исключением
и передаваемое по каналу.  
[CreateRequest](M_Tessa_Platform_Pipes_IPipeMessageFactory_CreateRequest.htm)|
Создаёт сообщение-запрос, передаваемое по каналу.  
[CreateResponse](M_Tessa_Platform_Pipes_IPipeMessageFactory_CreateResponse.htm)|
Создаёт сообщение, являющееся ответом на запрос и передаваемое по каналу.  
## __См. также
#### Ссылки
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
