# IApplicationManagerService - интерфейс
Локальный сервис обрабатывающий сообщения поступающие приложений. Является
WCF-Сервисом.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.ApplicationManager](N_Tessa_Applications_Services_ApplicationManager.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [ServiceContractAttribute]
    public interface IApplicationManagerService
VB __Копировать
    <ServiceContractAttribute>
    Public Interface IApplicationManagerService
C++ __Копировать
    [ServiceContractAttribute]
    public interface class IApplicationManagerService
F# __Копировать
     [<ServiceContractAttribute>]
    type IApplicationManagerService = interface end
##  __Методы
[Activate](M_Tessa_Applications_Services_ApplicationManager_IApplicationManagerService_Activate.htm)|
Активизирует приложение - выводит на передний план  
---|---  
[ActivateByNewInstance](M_Tessa_Applications_Services_ApplicationManager_IApplicationManagerService_ActivateByNewInstance.htm)|
Активизирует приложение с уведомлением о запуске от нового экземпляра
приложения  
[ProcessLink](M_Tessa_Applications_Services_ApplicationManager_IApplicationManagerService_ProcessLink.htm)|
Производит обработку ссылок.  
[RegisterApplication](M_Tessa_Applications_Services_ApplicationManager_IApplicationManagerService_RegisterApplication.htm)|
Регистрация клиентского приложения  
[UnRegisterApplication](M_Tessa_Applications_Services_ApplicationManager_IApplicationManagerService_UnRegisterApplication.htm)|
Отмена регистрации приложения  
## __См. также
#### Ссылки
[Tessa.Applications.Services.ApplicationManager - пространство
имён](N_Tessa_Applications_Services_ApplicationManager.htm)
