# ILicenseValidator - интерфейс
Объект, выполняющий получение фактической информации по лицензиям для её
последующей валидации. Доступен на сервере.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Licensing](N_Tessa_Platform_Licensing.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ILicenseValidator
VB __Копировать
     Public Interface ILicenseValidator
C++ __Копировать
     public interface class ILicenseValidator
F# __Копировать
     type ILicenseValidator = interface end
##  __Методы
[GetConcurrentLicenseCountAsync](M_Tessa_Platform_Licensing_ILicenseValidator_GetConcurrentLicenseCountAsync.htm)|
Получает количество задействованных конкурентных лицензий типа concurrent.  
---|---  
[GetMobileLicenseCountAsync](M_Tessa_Platform_Licensing_ILicenseValidator_GetMobileLicenseCountAsync.htm)|
Получает количество задействованных лицензий мобильного согласования.  
[GetPersonalLicenseCountAsync](M_Tessa_Platform_Licensing_ILicenseValidator_GetPersonalLicenseCountAsync.htm)|
Получает количество задействованных персональных лицензий типа personal.  
[HasMobileLicenseAsync](M_Tessa_Platform_Licensing_ILicenseValidator_HasMobileLicenseAsync.htm)|
Возвращает признак того, что пользователь с заданным идентификатором имеет
лицензию мобильного согласования.  
[HasPersonalLicenseAsync](M_Tessa_Platform_Licensing_ILicenseValidator_HasPersonalLicenseAsync.htm)|
Возвращает признак того, что пользователь с заданным идентификатором имеет
персональную лицензию.  
[WillIncreaseConcurrentLicenseCountAsync](M_Tessa_Platform_Licensing_ILicenseValidator_WillIncreaseConcurrentLicenseCountAsync.htm)|
Возвращает признак того, что сессия с заданными параметрами будет потреблять
на одну конкурентную лицензию больше, чем до создания сессии. Сессия может не
увеличивать количество потребляемых лицензий, если вход выполняется для того
же сотрудника и производится с того же IP адреса.  
## __См. также
#### Ссылки
[Tessa.Platform.Licensing - пространство имён](N_Tessa_Platform_Licensing.htm)
