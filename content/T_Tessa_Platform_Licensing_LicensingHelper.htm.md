# LicensingHelper - класс
Вспомогательные средства для управления лицензиями.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Licensing](N_Tessa_Platform_Licensing.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class LicensingHelper
VB __Копировать
     Public NotInheritable Class LicensingHelper
C++ __Копировать
     public ref class LicensingHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type LicensingHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ LicensingHelper
##  __Методы
[CheckForumLicense](M_Tessa_Platform_Licensing_LicensingHelper_CheckForumLicense.htm)|  
---|---  
[CheckWorkflowViewerLicense](M_Tessa_Platform_Licensing_LicensingHelper_CheckWorkflowViewerLicense.htm)|
Проверяет наличие модуля лицензии на визуализатор
[WorkflowViewerID](F_Tessa_Platform_Licensing_LicenseModules_WorkflowViewerID.htm)
и срок его действия.  
[CreateTempLicense](M_Tessa_Platform_Licensing_LicensingHelper_CreateTempLicense.htm)|
Создаёт временный объект лицензии на одного сотрудника со всеми модулями.
Используется для работы утилит, которые выполняют серверную обработку и не
должны требовать лицензию.  
[GenerateKeyPair](M_Tessa_Platform_Licensing_LicensingHelper_GenerateKeyPair.htm)|
Создаёт пару ключей для использования в криптографических средствах для
управления лицензиями.  
[GetDateToCompareWithValidTo](M_Tessa_Platform_Licensing_LicensingHelper_GetDateToCompareWithValidTo.htm)|
Возвращает дату в формате, подходящим для сравнения с датой окончания
лицензии, полученной методом
[GetValidToLastDateTime(ILicense)](M_Tessa_Platform_Licensing_LicensingExtensions_GetValidToLastDateTime.htm).  
[GetLicenseDataAsync](M_Tessa_Platform_Licensing_LicensingHelper_GetLicenseDataAsync.htm)|
Возвращает бинарное представление текущей лицензии.  
[GetNowDateToCompareWithValidTo](M_Tessa_Platform_Licensing_LicensingHelper_GetNowDateToCompareWithValidTo.htm)|
Возвращает текущую дату в формате, подходящим для сравнения с датой окончания
лицензии, полученной методом
[GetValidToLastDateTime(ILicense)](M_Tessa_Platform_Licensing_LicensingExtensions_GetValidToLastDateTime.htm).  
[GetPublicKey](M_Tessa_Platform_Licensing_LicensingHelper_GetPublicKey.htm)|
Возвращает публичный ключ для управления лицензиями, встроенный в сборку.  
[GetWarning](M_Tessa_Platform_Licensing_LicensingHelper_GetWarning.htm)|
Возвращает сообщение-предупреждение для лицензий, которые просрочены или скоро
будут просрочены. Возвращает null, если предупреждения отсутствуют. При
возникновении исключения при доступе к лицензии оно поглощается, при этом
метод возвращает null.  
[ShouldBeUpgraded](M_Tessa_Platform_Licensing_LicensingHelper_ShouldBeUpgraded.htm)|
Возвращает признак того, что лицензию следует попытаться проапгрейдить
посредством
[ILicenseMigrationManager](T_Tessa_Platform_Licensing_ILicenseMigrationManager.htm).  
## __Поля
[CurrentVersion](F_Tessa_Platform_Licensing_LicensingHelper_CurrentVersion.htm)|
Версия формата лицензии, поддерживаемая текущим сервисом.  
---|---  
## __См. также
#### Ссылки
[Tessa.Platform.Licensing - пространство имён](N_Tessa_Platform_Licensing.htm)
