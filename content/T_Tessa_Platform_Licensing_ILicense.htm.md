# ILicense - интерфейс
Лицензия на платформу Tessa.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Licensing](N_Tessa_Platform_Licensing.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ILicense
VB __Копировать
     Public Interface ILicense
C++ __Копировать
     public interface class ILicense
F# __Копировать
     type ILicense = interface end
##  __Свойства
[CompanyAddress](P_Tessa_Platform_Licensing_ILicense_CompanyAddress.htm)|
Адрес компании, для которой выдана лицензия.  
---|---  
[CompanyName](P_Tessa_Platform_Licensing_ILicense_CompanyName.htm)| Имя
компании, для которой выдана лицензия.  
[ConcurrentCount](P_Tessa_Platform_Licensing_ILicense_ConcurrentCount.htm)|
Максимальное количество конкурентных сессий.  
[ID](P_Tessa_Platform_Licensing_ILicense_ID.htm)| Уникальный идентификатор
лицензии.  
[IssuedBy](P_Tessa_Platform_Licensing_ILicense_IssuedBy.htm)| Имя компании,
которая выдала лицензию.  
[Modules](P_Tessa_Platform_Licensing_ILicense_Modules.htm)| Коллекция модулей,
добавленных в лицензию. Каждый модуль содержит собственные настройки.  
[PersonalCount](P_Tessa_Platform_Licensing_ILicense_PersonalCount.htm)|
Максимальное количество персональных сессий.  
[ReceiveUpdatesTo](P_Tessa_Platform_Licensing_ILicense_ReceiveUpdatesTo.htm)|
Дата окончания получения обновлений платформы.  
[ValidFrom](P_Tessa_Platform_Licensing_ILicense_ValidFrom.htm)| Дата выдачи
лицензии.  
[ValidTo](P_Tessa_Platform_Licensing_ILicense_ValidTo.htm)| Дата окончания
лицензии.  
[Version](P_Tessa_Platform_Licensing_ILicense_Version.htm)| Версия формата
лицензии.  
##  __Методы
[AsReadOnly](M_Tessa_Platform_Licensing_ILicense_AsReadOnly.htm)|  Возвращает
доступную только для чтения обёртку для текущего объекта. При изменении
коллекции модулей текущего объекта [Tessa.Platform.Licensing.ILicense.Modules]
коллекция в создаваемом объекте не будет изменяться.  
---|---  
[GetMobileCount](M_Tessa_Platform_Licensing_ILicense_GetMobileCount.htm)|
Возвращает максимальное количество лицензий для мобильного согласования.  
##  __Методы расширения
[GetLicenseCount](M_Tessa_Platform_Runtime_RuntimeExtensions_GetLicenseCount.htm)|
Возвращает количество доступных лицензий для заданного типа licenseType. Для
типа [Unspecified](T_Tessa_Platform_Runtime_SessionLicenseType.htm)
возвращается -1.  
(Определяется
[RuntimeExtensions](T_Tessa_Platform_Runtime_RuntimeExtensions.htm))  
---|---  
[GetValidToLastDateTime](M_Tessa_Platform_Licensing_LicensingExtensions_GetValidToLastDateTime.htm)|
Возвращает дату и время окончания лицензии. Определяется как дата в формате
UTC, указанная в лицензии, плюс время 23:59:59.  
(Определяется
[LicensingExtensions](T_Tessa_Platform_Licensing_LicensingExtensions.htm))  
[ToLicense](M_Tessa_Platform_Licensing_LicensingExtensions_ToLicense.htm)|
Преобразует тип объекта ILicense в
[License](T_Tessa_Platform_Licensing_License.htm) или создаёт новый объект
[License](T_Tessa_Platform_Licensing_License.htm), свойства которого получены
из заданного объекта.  
(Определяется
[LicensingExtensions](T_Tessa_Platform_Licensing_LicensingExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Licensing - пространство имён](N_Tessa_Platform_Licensing.htm)
