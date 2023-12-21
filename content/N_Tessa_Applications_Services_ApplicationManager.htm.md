# Tessa.Applications.Services.ApplicationManager - пространство имён
API управления приложениями для netpipe-сервиса взаимодействия приложения с
менеджером приложений со стороны менеджера приложений.
##  __Классы
[ApplicationManagerAddressGenerator](T_Tessa_Applications_Services_ApplicationManager_ApplicationManagerAddressGenerator.htm)|
Объект
[IHostServiceAddressGenerator](T_Tessa_Host_IHostServiceAddressGenerator.htm)
для определения адреса TessaAppManager, единого в рамках терминальной сессии.
Например: Syntellect/Tessa/AppManager_2 (где 2 \- идентификатор терминальной
сессии)  
---|---  
[ApplicationManagerExtensions](T_Tessa_Applications_Services_ApplicationManager_ApplicationManagerExtensions.htm)|  
[ApplicationManagerMultiProcessServiceHost](T_Tessa_Applications_Services_ApplicationManager_ApplicationManagerMultiProcessServiceHost.htm)|
Объект, запускающий или останавливающий группу сервисов
[IApplicationManagerServiceHost](T_Tessa_Applications_Services_ApplicationManager_IApplicationManagerServiceHost.htm).  
[ApplicationManagerProcessServiceClient](T_Tessa_Applications_Services_ApplicationManager_ApplicationManagerProcessServiceClient.htm)|  
[ApplicationManagerProcessServiceHost](T_Tessa_Applications_Services_ApplicationManager_ApplicationManagerProcessServiceHost.htm)|  
## __Интерфейсы
[IApplicationManagerService](T_Tessa_Applications_Services_ApplicationManager_IApplicationManagerService.htm)|
Локальный сервис обрабатывающий сообщения поступающие приложений. Является
WCF-Сервисом.  
---|---  
[IApplicationManagerServiceHost](T_Tessa_Applications_Services_ApplicationManager_IApplicationManagerServiceHost.htm)|
Описание интерфейса для классов осуществляющих хостинг сервиса
предоставляемого диспетчером приложений, для запущенных экземпляров сервиса
приложений  
[IApplicationMessageObserver](T_Tessa_Applications_Services_ApplicationManager_IApplicationMessageObserver.htm)|
Описание интерфейса для объектов отслеживающих сообщения от шины сообщений.  
## __Делегаты
[ApplicationManagerServiceProxyFactoryDelegate](T_Tessa_Applications_Services_ApplicationManager_ApplicationManagerServiceProxyFactoryDelegate.htm)|
Делегат создания прокси клиента для
[IApplicationManagerPipeService](T_Tessa_Applications_Pipes_IApplicationManagerPipeService.htm)  
---|---
