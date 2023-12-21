# Tessa.Applications.Services.PlatformApplication - пространство имён
API управления приложениями для netpipe-сервиса взаимодействия приложения с
менеджером приложений со стороны приложений.
##  __Классы
[ApplicationRegistrationException](T_Tessa_Applications_Services_PlatformApplication_ApplicationRegistrationException.htm)|
Исключение возникающее при ошибке регистрации приложения  
---|---  
[MessageReceivedEventArgs](T_Tessa_Applications_Services_PlatformApplication_MessageReceivedEventArgs.htm)|
Параметры события о получении сообщения приложением  
[TessaApplicationAddressGenerator](T_Tessa_Applications_Services_PlatformApplication_TessaApplicationAddressGenerator.htm)|
Объект
[IHostServiceAddressGenerator](T_Tessa_Host_IHostServiceAddressGenerator.htm)
для определения адреса клиентского приложения с указанием идентификатора
процесса. Например: Syntellect/Tessa/App_4422 (где 4422 \- идентификатор
процесса для приложения)  
[TessaApplicationClientAddressGenerator](T_Tessa_Applications_Services_PlatformApplication_TessaApplicationClientAddressGenerator.htm)|
Объект
[IHostServiceAddressGenerator](T_Tessa_Host_IHostServiceAddressGenerator.htm)
для определения адреса клиентского приложения со стороны AppManager. В метод
[GetNextServiceAddress(Object,
String)](M_Tessa_Applications_Services_PlatformApplication_TessaApplicationClientAddressGenerator_GetNextServiceAddress.htm)
должен быть передан
[ITessaApplicationServiceHost](T_Tessa_Applications_Services_PlatformApplication_ITessaApplicationServiceHost.htm)
для корректного определения адреса клиентского приложения, или в противном
случае будет возвращён адрес текущего приложения как клиентского
[TessaApplicationAddressGenerator](T_Tessa_Applications_Services_PlatformApplication_TessaApplicationAddressGenerator.htm).
Например: Syntellect/Tessa/App_4422 (где 4422 \- идентификатор процесса для
приложения)  
[TessaApplicationExtensions](T_Tessa_Applications_Services_PlatformApplication_TessaApplicationExtensions.htm)|  
[TessaApplicationProcessServiceClient](T_Tessa_Applications_Services_PlatformApplication_TessaApplicationProcessServiceClient.htm)|  
[TessaApplicationProcessServiceHost](T_Tessa_Applications_Services_PlatformApplication_TessaApplicationProcessServiceHost.htm)|  
[TessaApplicationProcessVersionServiceHost](T_Tessa_Applications_Services_PlatformApplication_TessaApplicationProcessVersionServiceHost.htm)|
Объект, запускающий или останавливающий сервис в соответствии с версией API.
Выбор версии выполняется на основании указанных в конструкторе функций.  
[TessaApplicationServiceProxyFactory](T_Tessa_Applications_Services_PlatformApplication_TessaApplicationServiceProxyFactory.htm)|
Вспомогательный класс для создания клиентов к сервису приложений  
## __Интерфейсы
[ITessaApplicationService](T_Tessa_Applications_Services_PlatformApplication_ITessaApplicationService.htm)|
Интерфейс сервиса, предоставляемого приложением  
---|---  
[ITessaApplicationServiceHost](T_Tessa_Applications_Services_PlatformApplication_ITessaApplicationServiceHost.htm)|
Описание интерфейса для объектов осуществляющих размещение сервиса
платформенного приложения осуществляющего взаимодействие с диспетчером
приложений.  
## __Делегаты
[TessaApplicationServiceProxyFactoryDelegate](T_Tessa_Applications_Services_PlatformApplication_TessaApplicationServiceProxyFactoryDelegate.htm)|
Делегат создания прокси-клиента для взаимодействия с сервисом экземпляра
приложения.  
---|---
