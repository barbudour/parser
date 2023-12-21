# LicensingExtensions - класс
Расширения для пространства имён Tessa.Platform.Licensing.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Licensing](N_Tessa_Platform_Licensing.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class LicensingExtensions
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class LicensingExtensions
C++ __Копировать
    [ExtensionAttribute]
    public ref class LicensingExtensions abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type LicensingExtensions = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ LicensingExtensions
##  __Методы
[GetValidToLastDateTime](M_Tessa_Platform_Licensing_LicensingExtensions_GetValidToLastDateTime.htm)|
Возвращает дату и время окончания лицензии. Определяется как дата в формате
UTC, указанная в лицензии, плюс время 23:59:59.  
---|---  
[HasEnterpriseOrContains](M_Tessa_Platform_Licensing_LicensingExtensions_HasEnterpriseOrContains.htm)|
Возвращает признак того, что коллекция содержит модуль лицензии с указанным
идентификатором moduleID или что лицензия является Enterprise-редакцией, в
соответствии с которой модуль должен быть добавлен автоматически.  
[RegisterLicensingOnClient](M_Tessa_Platform_Licensing_LicensingExtensions_RegisterLicensingOnClient.htm)|
Выполняет регистрацию API лицензий на клиенте.  
[RegisterLicensingOnServer(IUnityContainer)](M_Tessa_Platform_Licensing_LicensingExtensions_RegisterLicensingOnServer.htm)|
Выполняет регистрацию API лицензий на сервере. Путь к файлу лицензии
определяется из конфигурации
[ITessaServerSettings](T_Tessa_Platform_ITessaServerSettings.htm).  
[RegisterLicensingOnServer(IUnityContainer, Func<IUnityContainer,
CancellationToken,
ValueTask<Byte[]>>)](M_Tessa_Platform_Licensing_LicensingExtensions_RegisterLicensingOnServer_1.htm)|
Выполняет регистрацию API лицензий на сервере с указанием метода, получающего
сериализованную информацию по лицензии.  
[RegisterLicensingOnServer(IUnityContainer,
String)](M_Tessa_Platform_Licensing_LicensingExtensions_RegisterLicensingOnServer_2.htm)|
Выполняет регистрацию API лицензий на сервере с указанием пути к файлу с
лицензией.  
[RegisterLicensingOnServer(IUnityContainer, String, Func<IUnityContainer,
CancellationToken,
ValueTask<Byte[]>>)](M_Tessa_Platform_Licensing_LicensingExtensions_RegisterLicensingOnServer_3.htm)|
Выполняет регистрацию API лицензий на сервере с указанием параметров лицензии.  
[ToLicense](M_Tessa_Platform_Licensing_LicensingExtensions_ToLicense.htm)|
Преобразует тип объекта [ILicense](T_Tessa_Platform_Licensing_ILicense.htm) в
[License](T_Tessa_Platform_Licensing_License.htm) или создаёт новый объект
[License](T_Tessa_Platform_Licensing_License.htm), свойства которого получены
из заданного объекта.  
[ToLicenseModule](M_Tessa_Platform_Licensing_LicensingExtensions_ToLicenseModule.htm)|
Преобразует тип объекта
[ILicenseModule](T_Tessa_Platform_Licensing_ILicenseModule.htm) в
[LicenseModule](T_Tessa_Platform_Licensing_LicenseModule.htm) или создаёт
новый объект [LicenseModule](T_Tessa_Platform_Licensing_LicenseModule.htm),
свойства которого получены из заданного объекта.  
[ToLicenseModuleCollection](M_Tessa_Platform_Licensing_LicensingExtensions_ToLicenseModuleCollection.htm)|
Преобразует тип объекта
[ILicenseModuleCollection](T_Tessa_Platform_Licensing_ILicenseModuleCollection.htm)
в
[LicenseModuleCollection](T_Tessa_Platform_Licensing_LicenseModuleCollection.htm)
или создаёт новый объект
[LicenseModuleCollection](T_Tessa_Platform_Licensing_LicenseModuleCollection.htm),
свойства которого получены из заданного объекта.  
[ValidateLicenseRegistrations](M_Tessa_Platform_Licensing_LicensingExtensions_ValidateLicenseRegistrations.htm)|
Проверяет, что все серверные регистрации, связанные с проверкой лицензий, не
были подменены в расширениях. Если проверки не пройдены, то выбрасывается
исключение
[InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception).  
[ValidateType](M_Tessa_Platform_Licensing_LicensingExtensions_ValidateType.htm)|
Проверяет, что тип объекта является допустимым. Это гарантирует, что объект не
был нигде подменён злоумышленником.  
[ValidateTypeOnClient](M_Tessa_Platform_Licensing_LicensingExtensions_ValidateTypeOnClient.htm)|
Проверяет, что тип объекта является допустимым на клиенте. Это гарантирует,
что объект не был нигде подменён злоумышленником.  
[ValidateTypeOnServer](M_Tessa_Platform_Licensing_LicensingExtensions_ValidateTypeOnServer.htm)|
Проверяет, что тип объекта является допустимым на сервере. Это гарантирует,
что объект не был нигде подменён злоумышленником.  
## __См. также
#### Ссылки
[Tessa.Platform.Licensing - пространство имён](N_Tessa_Platform_Licensing.htm)
