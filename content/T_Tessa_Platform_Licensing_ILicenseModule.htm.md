# ILicenseModule - интерфейс
Модуль лицензии, описывающий дополнительную подключаемую функциональность
платформы.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Licensing](N_Tessa_Platform_Licensing.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ILicenseModule : IEquatable<ILicenseModule>
VB __Копировать
     Public Interface ILicenseModule
    	Inherits IEquatable(Of ILicenseModule)
C++ __Копировать
     public interface class ILicenseModule : IEquatable<ILicenseModule^>
F# __Копировать
     type ILicenseModule = 
        interface
            interface IEquatable<ILicenseModule>
        end
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<ILicenseModule>
##  __Свойства
[Caption](P_Tessa_Platform_Licensing_ILicenseModule_Caption.htm)| Имя модуля,
отображаемое пользователю.  
---|---  
[ID](P_Tessa_Platform_Licensing_ILicenseModule_ID.htm)| Идентификатор модуля.  
[Settings](P_Tessa_Platform_Licensing_ILicenseModule_Settings.htm)|
Сериализуемые настройки модуля.  
##  __Методы
[AsReadOnly](M_Tessa_Platform_Licensing_ILicenseModule_AsReadOnly.htm)|
Возвращает доступную только для чтения обёртку для текущего объекта.  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.iequatable-1.equals#system-
iequatable-1-equals\(-0\))| Indicates whether the current object is equal to
another object of the same type.  
(Унаследован от
[IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<ILicenseModule>)  
##  __Методы расширения
[ToLicenseModule](M_Tessa_Platform_Licensing_LicensingExtensions_ToLicenseModule.htm)|
Преобразует тип объекта ILicenseModule в
[LicenseModule](T_Tessa_Platform_Licensing_LicenseModule.htm) или создаёт
новый объект [LicenseModule](T_Tessa_Platform_Licensing_LicenseModule.htm),
свойства которого получены из заданного объекта.  
(Определяется
[LicensingExtensions](T_Tessa_Platform_Licensing_LicensingExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Platform.Licensing - пространство имён](N_Tessa_Platform_Licensing.htm)
