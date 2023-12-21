# ILicenseManager - интерфейс
Объект, управляющий лицензиями.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Licensing](N_Tessa_Platform_Licensing.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ILicenseManager
VB __Копировать
     Public Interface ILicenseManager
C++ __Копировать
     public interface class ILicenseManager
F# __Копировать
     type ILicenseManager = interface end
##  __Методы
[GetLicenseAsync](M_Tessa_Platform_Licensing_ILicenseManager_GetLicenseAsync.htm)|
Возвращает текущую используемую лицензию.  
---|---  
##  __Методы расширения
[CheckChartLicense](M_Tessa_UI_Views_Charting_ChartsLicenseExtensions_CheckChartLicense.htm)|
Осуществляет проверку наличия лицензии для модуля диаграмм.  
(Определяется
[ChartsLicenseExtensions](T_Tessa_UI_Views_Charting_ChartsLicenseExtensions.htm))  
---|---  
[ValidateTypeOnClient](M_Tessa_Platform_Licensing_LicensingExtensions_ValidateTypeOnClient.htm)|
Проверяет, что тип объекта является допустимым на клиенте. Это гарантирует,
что объект не был нигде подменён злоумышленником.  
(Определяется
[LicensingExtensions](T_Tessa_Platform_Licensing_LicensingExtensions.htm))  
[ValidateTypeOnServer](M_Tessa_Platform_Licensing_LicensingExtensions_ValidateTypeOnServer.htm)|
Проверяет, что тип объекта является допустимым на сервере. Это гарантирует,
что объект не был нигде подменён злоумышленником.  
(Определяется
[LicensingExtensions](T_Tessa_Platform_Licensing_LicensingExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Licensing - пространство имён](N_Tessa_Platform_Licensing.htm)
