# Tessa.Platform.Pipes - пространство имён
## __Классы
[PipeAggregateClientTraceListener](T_Tessa_Platform_Pipes_PipeAggregateClientTraceListener.htm)|
Объект, уведомляющих о событиях, происходящих в канале со стороны клиента,
несколько указанных объектов
[IPipeClientTraceListener](T_Tessa_Platform_Pipes_IPipeClientTraceListener.htm).  
---|---  
[PipeAggregateServerTraceListener](T_Tessa_Platform_Pipes_PipeAggregateServerTraceListener.htm)|
Объект, уведомляющих о событиях, происходящих в канале со стороны сервера,
несколько указанных объектов
[IPipeServerTraceListener](T_Tessa_Platform_Pipes_IPipeServerTraceListener.htm).  
[PipeBinaryXmlRequest](T_Tessa_Platform_Pipes_PipeBinaryXmlRequest.htm)|
Сообщение-запрос, передаваемое по каналу, для которого дополнительно
передаётся массив байт отдельным сообщением
[IPipeBinaryMessage](T_Tessa_Platform_Pipes_IPipeBinaryMessage.htm).  
[PipeBinaryXmlResponse](T_Tessa_Platform_Pipes_PipeBinaryXmlResponse.htm)|
Сообщение-ответ, полученное по каналу, для которого дополнительно загружается
массив байт отдельным сообщением
[IPipeBinaryMessage](T_Tessa_Platform_Pipes_IPipeBinaryMessage.htm).  
[PipeClient](T_Tessa_Platform_Pipes_PipeClient.htm)|  Клиент, выполняющий
отправку сообщений по каналу. Использует объект настроек
[PipeClientOptions](T_Tessa_Platform_Pipes_PipeClientOptions.htm).  
[PipeClientConnection](T_Tessa_Platform_Pipes_PipeClientConnection.htm)|
Объект соединения клиента с сервером по каналу, по которому клиент может
отправлять сообщения серверу.  
[PipeClientOptions](T_Tessa_Platform_Pipes_PipeClientOptions.htm)|  Настройки
для установления клиентского соединения с каналом посредством объекта
[PipeClient](T_Tessa_Platform_Pipes_PipeClient.htm).  
[PipeClientTraceListener](T_Tessa_Platform_Pipes_PipeClientTraceListener.htm)|
Объект, уведомляемый о событиях, происходящих в канале со стороны клиента.  
[PipeContextualInstanceResolver](T_Tessa_Platform_Pipes_PipeContextualInstanceResolver.htm)|
Объект, запрашивающий экземпляры из текущего контекста
[Current](P_Tessa_Platform_Pipes_PipeInstanceContext_Current.htm). Метод
[ResolveAsync(Type,
CancellationToken)](M_Tessa_Platform_Pipes_PipeContextualInstanceResolver_ResolveAsync.htm)
должен использоваться только при наличии такого контекста, например, в методах
обработки запросов на сервере
[IPipeServer](T_Tessa_Platform_Pipes_IPipeServer.htm),
[IPipeRouter](T_Tessa_Platform_Pipes_IPipeRouter.htm),
[IPipeHandler](T_Tessa_Platform_Pipes_IPipeHandler.htm). Метод
[DisposeAsync()](M_Tessa_Platform_Pipes_PipeContextualInstanceResolver_DisposeAsync.htm)
не выполняет действий. Используйте метод
[GetContextualInstanceResolver(IUnityContainer)](M_Tessa_Platform_Pipes_PipesExtensions_GetContextualInstanceResolver.htm)
для запроса экземпляра объекта из Unity или запросите экземпляр
[IPipeInstanceResolver](T_Tessa_Platform_Pipes_IPipeInstanceResolver.htm) по
имени "PipeContextualInstanceResolver".  
[PipeDelegateClientTraceListener](T_Tessa_Platform_Pipes_PipeDelegateClientTraceListener.htm)|
Объект, уведомляемый о событиях, происходящих в канале со стороны клиента, где
обработчики событий передаются как делегаты в конструкторе.  
[PipeDelegateServerTraceListener](T_Tessa_Platform_Pipes_PipeDelegateServerTraceListener.htm)|
Объект, уведомляемый о событиях, происходящих в канале со стороны сервера, где
обработчики событий передаются как делегаты в конструкторе.  
[PipeHandler](T_Tessa_Platform_Pipes_PipeHandler.htm)|  Базовый класс для
объекта, выполняющего обработку сообщений, полученных по каналу.  
[PipeHelper](T_Tessa_Platform_Pipes_PipeHelper.htm)|  Вспомогательные методы
для использования совместно с каналами API Pipes.  
[PipeInstanceContext](T_Tessa_Platform_Pipes_PipeInstanceContext.htm)|
Контекст, управляющий временем жизни экземпляров объектов, используемых в
канале.  
[PipeInstanceFactory](T_Tessa_Platform_Pipes_PipeInstanceFactory.htm)|
Фабрика экземпляров объектов, используемых в канале, время жизни которых
контролируется объектом
[IPipeInstanceResolver](T_Tessa_Platform_Pipes_IPipeInstanceResolver.htm).  
[PipeInstanceResolver](T_Tessa_Platform_Pipes_PipeInstanceResolver.htm)|
Объект, управляющий временем жизни экземпляров объектов, реализующих бизнес-
логику для использования в канале.  
[PipeInstanceResolverFactory](T_Tessa_Platform_Pipes_PipeInstanceResolverFactory.htm)|
Фабрика объектов
[IPipeInstanceResolver](T_Tessa_Platform_Pipes_IPipeInstanceResolver.htm).  
[PipeLoggerClientTraceListener](T_Tessa_Platform_Pipes_PipeLoggerClientTraceListener.htm)|
Объект, выполняющий логирование событий, происходящих с каналом со стороны
сервера.  
[PipeLoggerServerTraceListener](T_Tessa_Platform_Pipes_PipeLoggerServerTraceListener.htm)|
Объект, выполняющий логирование событий, происходящих с каналом со стороны
сервера.  
[PipeMessageFactory](T_Tessa_Platform_Pipes_PipeMessageFactory.htm)|  Фабрика
объектов, используемых для создания сообщений, передаваемых по каналу.  
[PipeMethodHandler](T_Tessa_Platform_Pipes_PipeMethodHandler.htm)|  Объект,
выполняющий обработку сообщений, полученных по каналу. Предоставляет метод
регистрации обработчика по имени метода.  
[PipeRequestProvider](T_Tessa_Platform_Pipes_PipeRequestProvider.htm)|
Объект, предоставляющий средства создания и подготовки запросов.  
[PipeRouteFactory](T_Tessa_Platform_Pipes_PipeRouteFactory.htm)|  Фабрика
объектов, используемых для маршрутизации и обработки сообщений, полученных по
каналу.  
[PipeRouter](T_Tessa_Platform_Pipes_PipeRouter.htm)|  Базовый класс для
объекта, выполняющего маршрутизацию сообщений, полученных по каналу.  
[PipeSerializer](T_Tessa_Platform_Pipes_PipeSerializer.htm)|  Объект,
выполняющий сериализацию и десериализацию текстовых сообщений по каналу
[PipeStream](https://learn.microsoft.com/dotnet/api/system.io.pipes.pipestream).  
[PipeServer](T_Tessa_Platform_Pipes_PipeServer.htm)|  Сервер, выполняющий
обработку сообщений, полученных по каналу.  
[PipeServerOptions](T_Tessa_Platform_Pipes_PipeServerOptions.htm)|  Настройки
для установления серверного соединения с каналом посредством объекта
[PipeServer](T_Tessa_Platform_Pipes_PipeServer.htm).  
[PipeServerPool](T_Tessa_Platform_Pipes_PipeServerPool.htm)|  Пул серверов,
который поддерживает сразу несколько соединений
[IPipeServer](T_Tessa_Platform_Pipes_IPipeServer.htm) с автоматическим
расширением количества соединений. Объект не является синглтоном, создавайте
экземпляр объекта для каждого пула соединений.  
[PipeServerTraceListener](T_Tessa_Platform_Pipes_PipeServerTraceListener.htm)|
Объект, уведомляемый о событиях, происходящих в канале со стороны сервера.  
[PipeServiceRequestMapping](T_Tessa_Platform_Pipes_PipeServiceRequestMapping.htm)|
Объект, преобразующий параметры запроса, связанные с методом сервиса.  
[PipeServiceRouter](T_Tessa_Platform_Pipes_PipeServiceRouter.htm)|  Объект,
выполняющий маршрутизацию сообщений, полученных по каналу. Предоставляет метод
регистрации обработчика по типу сервиса.  
[PipesExtensions](T_Tessa_Platform_Pipes_PipesExtensions.htm)|  Методы-
расширения для пространства имён Tessa.Platform.Pipes.  
[PipeXmlExceptionResponse](T_Tessa_Platform_Pipes_PipeXmlExceptionResponse.htm)|
Ответ на запрос по каналу, используемый при возникновении исключения на
сервере.  
[PipeXmlMessage](T_Tessa_Platform_Pipes_PipeXmlMessage.htm)|  Базовый класс
для сообщения, передаваемого по каналу.  
[PipeXmlRequest](T_Tessa_Platform_Pipes_PipeXmlRequest.htm)|  Сообщение-
запрос, передаваемое по каналу.  
[PipeXmlRequestParser](T_Tessa_Platform_Pipes_PipeXmlRequestParser.htm)|
Объект, выполняющий десериализацию объекта запроса из текста.  
[PipeXmlResponse](T_Tessa_Platform_Pipes_PipeXmlResponse.htm)|  Сообщение-
ответ, полученное по каналу.  
[PipeXmlResponseParser](T_Tessa_Platform_Pipes_PipeXmlResponseParser.htm)|
Объект, выполняющий десериализацию объекта ответа на запрос из текста.  
[PipeXmlSerializer](T_Tessa_Platform_Pipes_PipeXmlSerializer.htm)|  Объект,
управляющий сериализацией в XML для параметров и возвращаемых значений
методов, передаваемых по каналу.  
## __Интерфейсы
[IPipeBinaryMessage](T_Tessa_Platform_Pipes_IPipeBinaryMessage.htm)|
Сообщение, содержащее массив байт, который записывается после основного
сообщения отдельным сообщением.  
---|---  
[IPipeBinaryRequest](T_Tessa_Platform_Pipes_IPipeBinaryRequest.htm)|
Сообщение-запрос, передаваемое по каналу, для которого дополнительно
передаётся массив байт отдельным сообщением
[IPipeBinaryMessage](T_Tessa_Platform_Pipes_IPipeBinaryMessage.htm).  
[IPipeBinaryResponse](T_Tessa_Platform_Pipes_IPipeBinaryResponse.htm)|
Сообщение-ответ, полученное по каналу, для которого дополнительно загружается
массив байт отдельным сообщением
[IPipeBinaryMessage](T_Tessa_Platform_Pipes_IPipeBinaryMessage.htm).  
[IPipeClient](T_Tessa_Platform_Pipes_IPipeClient.htm)|  Клиент, выполняющий
отправку сообщений по каналу.  
[IPipeClientConnection](T_Tessa_Platform_Pipes_IPipeClientConnection.htm)|
Объект соединения клиента с сервером по каналу, по которому клиент может
отправлять сообщения серверу.  
[IPipeClientTraceListener](T_Tessa_Platform_Pipes_IPipeClientTraceListener.htm)|
Объект, уведомляемый о событиях, происходящих в канале со стороны клиента.  
[IPipeExceptionResponse](T_Tessa_Platform_Pipes_IPipeExceptionResponse.htm)|
Ответ на запрос по каналу, используемый при возникновении исключения на
сервере.  
[IPipeHandler](T_Tessa_Platform_Pipes_IPipeHandler.htm)|  Объект, выполняющий
обработку сообщений, полученных по каналу.  
[IPipeInstanceContext](T_Tessa_Platform_Pipes_IPipeInstanceContext.htm)|
Контекст, управляющий временем жизни экземпляров объектов, используемых в
канале.  
[IPipeInstanceFactory](T_Tessa_Platform_Pipes_IPipeInstanceFactory.htm)|
Фабрика экземпляров объектов, используемых в канале, время жизни которых
контролируется объектом
[IPipeInstanceResolver](T_Tessa_Platform_Pipes_IPipeInstanceResolver.htm).  
[IPipeInstanceResolver](T_Tessa_Platform_Pipes_IPipeInstanceResolver.htm)|
Объект, управляющий временем жизни экземпляров объектов, реализующих бизнес-
логику для использования в канале.  
[IPipeInstanceResolverFactory](T_Tessa_Platform_Pipes_IPipeInstanceResolverFactory.htm)|
Фабрика объектов
[IPipeInstanceResolver](T_Tessa_Platform_Pipes_IPipeInstanceResolver.htm).  
[IPipeMessage](T_Tessa_Platform_Pipes_IPipeMessage.htm)|  Сообщение,
передаваемое по каналу.  
[IPipeMessageFactory](T_Tessa_Platform_Pipes_IPipeMessageFactory.htm)|
Фабрика объектов, используемых для создания сообщений, передаваемых по каналу.  
[IPipeMethodHandler](T_Tessa_Platform_Pipes_IPipeMethodHandler.htm)|  Объект,
выполняющий обработку сообщений, полученных по каналу. Предоставляет метод
регистрации обработчика по имени метода.  
[IPipeRequest](T_Tessa_Platform_Pipes_IPipeRequest.htm)|  Сообщение-запрос,
передаваемое по каналу.  
[IPipeRequestParser](T_Tessa_Platform_Pipes_IPipeRequestParser.htm)|  Объект,
выполняющий десериализацию объекта запроса из текста.  
[IPipeRequestProvider](T_Tessa_Platform_Pipes_IPipeRequestProvider.htm)|
Объект, предоставляющий средства создания и подготовки запросов.  
[IPipeResponse](T_Tessa_Platform_Pipes_IPipeResponse.htm)|  Сообщение-ответ,
полученное по каналу.  
[IPipeResponseParser](T_Tessa_Platform_Pipes_IPipeResponseParser.htm)|
Объект, выполняющий десериализацию объекта ответа на запрос из текста.  
[IPipeRouteFactory](T_Tessa_Platform_Pipes_IPipeRouteFactory.htm)|  Фабрика
объектов, используемых для маршрутизации и обработки сообщений, полученных по
каналу.  
[IPipeRouter](T_Tessa_Platform_Pipes_IPipeRouter.htm)|  Объект, выполняющий
маршрутизацию сообщений, полученных по каналу.  
[IPipeSerializer](T_Tessa_Platform_Pipes_IPipeSerializer.htm)|  Объект,
выполняющий сериализацию и десериализацию текстовых сообщений по каналу
[PipeStream](https://learn.microsoft.com/dotnet/api/system.io.pipes.pipestream).  
[IPipeServer](T_Tessa_Platform_Pipes_IPipeServer.htm)|  Сервер, выполняющий
обработку сообщений, полученных по каналу.  
[IPipeServerPool](T_Tessa_Platform_Pipes_IPipeServerPool.htm)|  Пул серверов,
который поддерживает сразу несколько соединений
[IPipeServer](T_Tessa_Platform_Pipes_IPipeServer.htm) с автоматическим
расширением количества соединений. Объект не является синглтоном, создавайте
экземпляр объекта для каждого пула соединений.  
[IPipeServerTraceListener](T_Tessa_Platform_Pipes_IPipeServerTraceListener.htm)|
Объект, уведомляемый о событиях, происходящих в канале со стороны сервера.  
[IPipeServiceRequestMapping](T_Tessa_Platform_Pipes_IPipeServiceRequestMapping.htm)|
Объект, преобразующий параметры запроса, связанные с методом сервиса.  
[IPipeServiceRouter](T_Tessa_Platform_Pipes_IPipeServiceRouter.htm)|  Объект,
выполняющий маршрутизацию сообщений, полученных по каналу. Предоставляет метод
регистрации обработчика по типу сервиса.  
[IPipeXmlMessage](T_Tessa_Platform_Pipes_IPipeXmlMessage.htm)|  Сообщение,
передаваемое по каналу с возможностью XML-сериализации.  
[IPipeXmlSerializer](T_Tessa_Platform_Pipes_IPipeXmlSerializer.htm)|  Объект,
управляющий сериализацией в XML для параметров и возвращаемых значений
методов, передаваемых по каналу.
