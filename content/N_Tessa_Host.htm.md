# Tessa.Host - пространство имён
API для взаимодействия с приложением-хостом, в котором могут выполняться
выделенные задачи,например, для предпросмотра файлов и для сканирования.
##  __Классы
[FakeHostLauncher](T_Tessa_Host_FakeHostLauncher.htm)|  Объект
[IHostLauncher](T_Tessa_Host_IHostLauncher.htm), не выполняющий фактический
запуск процесса. Возвращает null в качестве объекта процесса
[Process](https://learn.microsoft.com/dotnet/api/system.diagnostics.process).  
---|---  
[HandlerTypes](T_Tessa_Host_HandlerTypes.htm)|  Виды обработчиков  
[HostApplicationParameters](T_Tessa_Host_HostApplicationParameters.htm)|
Параметры приложения  
[HostConfiguration](T_Tessa_Host_HostConfiguration.htm)|  
[HostExtensions](T_Tessa_Host_HostExtensions.htm)|  Методы-расширения для
пространства имён Host.  
[HostLauncher](T_Tessa_Host_HostLauncher.htm)|  Осуществляет запуск внешнего
приложения осуществляющего хостинг некоторого сервиса используемых клиентским
приложением на клиентской стороне.  
[HostOperation<T>](T_Tessa_Host_HostOperation_1.htm)|  Базовый класс для
операции выполняемых Tessa Host  
[HostParametersConst](T_Tessa_Host_HostParametersConst.htm)|  Имя параметров
используемые для передачи параметров в приложение осуществляющие хостинг
сервиса  
[HostServiceAddressGenerator](T_Tessa_Host_HostServiceAddressGenerator.htm)|
Генератор адреса подключения для экземпляра сервиса TessaHost  
[HostServiceConnectionException](T_Tessa_Host_HostServiceConnectionException.htm)|
Ошибка соединения с сервисом приложения TessaHost  
[NamedEvents](T_Tessa_Host_NamedEvents.htm)|  Методы для взаимодействия с
именованными событиями синхронизации потоков  
[ScanException](T_Tessa_Host_ScanException.htm)|  Ошибка сканирования  
[ScanExtensions](T_Tessa_Host_ScanExtensions.htm)|  
[ScannerBusyException](T_Tessa_Host_ScannerBusyException.htm)|  Исключительная
ситуация возникающая при не завершенной сессии сканирования.  
[ScanRequest](T_Tessa_Host_ScanRequest.htm)|  Запрос к сервису сканирования  
[ScanResponse](T_Tessa_Host_ScanResponse.htm)|  Результат ответа от сервиса
сканирования  
[ScanServiceCallbackClient](T_Tessa_Host_ScanServiceCallbackClient.htm)|  
[ScanServiceCallbackServer](T_Tessa_Host_ScanServiceCallbackServer.htm)|  
[ScanServiceClient](T_Tessa_Host_ScanServiceClient.htm)|  
[ScanServiceProxy](T_Tessa_Host_ScanServiceProxy.htm)|  The scan service
proxy.  
[ScanServiceServer](T_Tessa_Host_ScanServiceServer.htm)|  
[ScanSource](T_Tessa_Host_ScanSource.htm)|  Контракт источника сканирования -
сервиса сканирования  
[ScanValidationKeys](T_Tessa_Host_ScanValidationKeys.htm)|  Ключи валидации
сканирования  
## __Интерфейсы
[IHostApplicationParameters](T_Tessa_Host_IHostApplicationParameters.htm)|
Описание интерфейса параметров запуска приложения  
---|---  
[IHostConfiguration](T_Tessa_Host_IHostConfiguration.htm)|  
[IHostLauncher](T_Tessa_Host_IHostLauncher.htm)|  Описание интерфейса
запускающего хост.  
[IHostOperation<T>](T_Tessa_Host_IHostOperation_1.htm)|  Описание интерфейса
операции приложения Tessa Host  
[IHostOperationContext](T_Tessa_Host_IHostOperationContext.htm)|  Описание
интерфейса контекста выполнения операции  
[IHostServiceAddressGenerator](T_Tessa_Host_IHostServiceAddressGenerator.htm)|
Генератор адреса подключения для экземпляра сервиса TessaHost  
[IScanRequest](T_Tessa_Host_IScanRequest.htm)|  Описание интерфейса  
[IScanService](T_Tessa_Host_IScanService.htm)|  Описание интерфейса сервиса
сканирования документов с помощью Tessa host  
[IScanServiceCallback](T_Tessa_Host_IScanServiceCallback.htm)|  Описание
интерфейса методов обратного вызова для сервиса сканирования  
[IScanServiceProxy](T_Tessa_Host_IScanServiceProxy.htm)|  Описание клиента для
взаимодействия с сервисом сканирования предоставляемым Tessa Host  
[IScanSource](T_Tessa_Host_IScanSource.htm)|  Информация по источнику
сканирования, обычно соответствует драйверу сканирования.  
[IServiceScanSource](T_Tessa_Host_IServiceScanSource.htm)|  Описание
интерфейса запроса на сканирование изображения  
## __Делегаты
[ScanServiceProxyFactory](T_Tessa_Host_ScanServiceProxyFactory.htm)|  Делегат
фабрики создания прокси-клиента для взаимодействия с сервисом сканирования  
---|---  
## __Перечисления
[ScanState](T_Tessa_Host_ScanState.htm)|  
---|---
