# ScanningExtensions - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public static class ScanningExtensions
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class ScanningExtensions
C++ __Копировать
    [ExtensionAttribute]
    public ref class ScanningExtensions abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type ScanningExtensions = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ScanningExtensions
##  __Методы
[RegisterScanningExtensionTypes](M_Tessa_Extensions_Platform_Client_Scanning_ScanningExtensions_RegisterScanningExtensionTypes.htm)|  
---|---  
[WhenScanDialogFunc](M_Tessa_Extensions_Platform_Client_Scanning_ScanningExtensions_WhenScanDialogFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[IScanDialogExtension](T_Tessa_Extensions_Platform_Client_Scanning_IScanDialogExtension.htm)
в соответствии с функцией isAllowedFunc, которая проверяет контекст
расширений. Если зарегистрировано несколько политик, то должны выполняться все
из них.  
## __См. также
#### Ссылки
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
