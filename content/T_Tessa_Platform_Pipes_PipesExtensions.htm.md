# PipesExtensions - класс
Методы-расширения для пространства имён Tessa.Platform.Pipes.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class PipesExtensions
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class PipesExtensions
C++ __Копировать
    [ExtensionAttribute]
    public ref class PipesExtensions abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type PipesExtensions = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PipesExtensions
##  __Методы
[CreateBinaryRequestAsync(IPipeRequestProvider, Type, String,
CancellationToken, ValueTuple<String,
Object>[])](M_Tessa_Platform_Pipes_PipesExtensions_CreateBinaryRequestAsync.htm)|
Создаёт и подготавливает запрос для отправки к методу заданного сервиса,
причём сообщение кодируется вместе с массивом байт
[BinaryData](P_Tessa_Platform_Pipes_IPipeBinaryMessage_BinaryData.htm).  
---|---  
[CreateBinaryRequestAsync<T>(IPipeRequestProvider, String, CancellationToken,
ValueTuple<String,
Object>[])](M_Tessa_Platform_Pipes_PipesExtensions_CreateBinaryRequestAsync__1.htm)|
Создаёт и подготавливает запрос для отправки к методу заданного сервиса,
причём сообщение кодируется вместе с массивом байт
[BinaryData](P_Tessa_Platform_Pipes_IPipeBinaryMessage_BinaryData.htm).  
[CreateInstanceAsync<T>](M_Tessa_Platform_Pipes_PipesExtensions_CreateInstanceAsync__1.htm)|
Создаёт экземпляр объекта, который ранее был зарегистрирован по заданному
типу. Возвращённый объект приводится к типу T и не равен null.  
[CreateRequestAsync(IPipeRequestProvider, Type, String, CancellationToken,
ValueTuple<String,
Object>[])](M_Tessa_Platform_Pipes_PipesExtensions_CreateRequestAsync.htm)|
Создаёт и подготавливает запрос для отправки к методу заданного сервиса.  
[CreateRequestAsync<T>(IPipeRequestProvider, String, CancellationToken,
ValueTuple<String,
Object>[])](M_Tessa_Platform_Pipes_PipesExtensions_CreateRequestAsync__1.htm)|
Создаёт и подготавливает запрос для отправки к методу заданного сервиса.  
[GetContextualInstanceResolver](M_Tessa_Platform_Pipes_PipesExtensions_GetContextualInstanceResolver.htm)|
Запрашивает экземпляр объекта
[IPipeInstanceResolver](T_Tessa_Platform_Pipes_IPipeInstanceResolver.htm),
привязанный к текущему контексту
[Current](P_Tessa_Platform_Pipes_PipeInstanceContext_Current.htm). Используйте
на сервере для регистрации методов обработчиков
[IPipeHandler](T_Tessa_Platform_Pipes_IPipeHandler.htm).  
[HandleAsync](M_Tessa_Platform_Pipes_PipesExtensions_HandleAsync.htm)|
Выполняет обработку сообщения по каналу и возвращает ответ на запрос,
отправленный по каналу. Не возвращает null, в случае невозможности обработки
выбрасывается исключение
[InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception).  
[PipeIsBroken](M_Tessa_Platform_Pipes_PipesExtensions_PipeIsBroken.htm)|
Возвращает признак того, что исключение связано с остановкой канала, например,
если клиент разорвал подключение, а метод пытается передать сообщение клиенту.
Обычно соответствует ошибке с текстом "Pipe is broken". Учитывает наличие
вложенных исключений и
[AggregateException](https://learn.microsoft.com/dotnet/api/system.aggregateexception).  
[Register(IPipeServiceRouter, Type,
IPipeHandler)](M_Tessa_Platform_Pipes_PipesExtensions_Register.htm)|
Выполняет регистрацию обработчика по типу сервиса.  
[Register<T>(IPipeInstanceFactory, Func<CancellationToken,
ValueTask<T>>)](M_Tessa_Platform_Pipes_PipesExtensions_Register__1.htm)|
Регистрирует функцию создания экземпляра объекта по заданному типу T.  
[Register<T>(IPipeServiceRouter, Func<IPipeRequest, CancellationToken,
ValueTask<IPipeHandler>>)](M_Tessa_Platform_Pipes_PipesExtensions_Register__1_2.htm)|
Выполняет регистрацию обработчика по типу сервиса.  
[Register<T>(IPipeServiceRouter,
IPipeHandler)](M_Tessa_Platform_Pipes_PipesExtensions_Register__1_3.htm)|
Выполняет регистрацию обработчика по типу сервиса.  
[Register<T>(IPipeMethodHandler, IPipeInstanceResolver, String, Func<T,
IPipeRequest, IPipeResponse, CancellationToken,
ValueTask<IPipeResponse>>)](M_Tessa_Platform_Pipes_PipesExtensions_Register__1_1.htm)|
Выполняет регистрацию метода обработки по имени, в который передаётся
экземпляр объекта T, время жизни которого контролируется объектом
instanceResolver. Используйте объект
[PipeContextualInstanceResolver](T_Tessa_Platform_Pipes_PipeContextualInstanceResolver.htm)
(container.[GetContextualInstanceResolver(IUnityContainer)](M_Tessa_Platform_Pipes_PipesExtensions_GetContextualInstanceResolver.htm)),
чтобы время жизни экземпляра объекта, передаваемого в метод обработки
сообщения handleAsync, определялось временем жизни соединения сервера с
клиентом.  
[RegisterPipes](M_Tessa_Platform_Pipes_PipesExtensions_RegisterPipes.htm)|
Выполняет регистрацию зависимостей для поддержки каналов Pipes, таких как
named pipe.  
[RemoveRegistration<T>](M_Tessa_Platform_Pipes_PipesExtensions_RemoveRegistration__1.htm)|
Удаляет регистрацию обработчика для заданного сервиса.  
[ResolveAsync<T>](M_Tessa_Platform_Pipes_PipesExtensions_ResolveAsync__1.htm)|
Возвращает экземпляр объекта по заданному типу. Для экземпляра выполняется
инициализация [IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm),
а при освобождении текущего экземпляра
[IPipeInstanceResolver](T_Tessa_Platform_Pipes_IPipeInstanceResolver.htm)
освобождаются все созданные им объекты, которые реализуют
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable)
или [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable).
Тип объекта должен быть предварительно зарегистрирован в фабрике
[IPipeInstanceFactory](T_Tessa_Platform_Pipes_IPipeInstanceFactory.htm).  
[UpdateHasBinaryData](M_Tessa_Platform_Pipes_PipesExtensions_UpdateHasBinaryData.htm)|
Обновляет свойство
[HasBinaryData](P_Tessa_Platform_Pipes_IPipeBinaryMessage_HasBinaryData.htm)
для сообщения
[IPipeBinaryMessage](T_Tessa_Platform_Pipes_IPipeBinaryMessage.htm) на
основании текущего значения свойства
[BinaryData](P_Tessa_Platform_Pipes_IPipeBinaryMessage_BinaryData.htm). Этот
метод автоматически вызывается перед отправкой сообщения по каналу, вызывать
его вручную не требуется.  
## __См. также
#### Ссылки
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
