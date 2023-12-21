# SettingsExtensions - класс
Методы-расширения для пространства имён Tessa.Platform.Settings.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Settings](N_Tessa_Platform_Settings.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class SettingsExtensions
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class SettingsExtensions
C++ __Копировать
    [ExtensionAttribute]
    public ref class SettingsExtensions abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type SettingsExtensions = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SettingsExtensions
##  __Методы
[BuildAsync](M_Tessa_Platform_Settings_SettingsExtensions_BuildAsync.htm)|
Выполняет построение объекта настроек. Возвращаемое значение гарантированно не
равно null. Выбрасывает исключение при невозможности его построить.  
---|---  
[Get<T>](M_Tessa_Platform_Settings_SettingsExtensions_Get__1.htm)|  Получает
объект с настройками заданного типа. Результирующий объект гарантированно не
равен null. Если объект не зарегистрирован, то выбрасывает
[KeyNotFoundException](https://learn.microsoft.com/dotnet/api/system.collections.generic.keynotfoundexception).  
[RegisterSettingsExtensionTypes](M_Tessa_Platform_Settings_SettingsExtensions_RegisterSettingsExtensionTypes.htm)|
Выполняет регистрацию стандартных типов расширений для системы настроек
расширений. Расширения могут использоваться на клиенте или на сервере.  
[RegisterSettingsOnClient](M_Tessa_Platform_Settings_SettingsExtensions_RegisterSettingsOnClient.htm)|
Выполняет регистрацию API настроек расширений на клиенте.  
[RegisterSettingsOnServer](M_Tessa_Platform_Settings_SettingsExtensions_RegisterSettingsOnServer.htm)|
Выполняет регистрацию API настроек расширений на сервере.  
[TryGet<T>](M_Tessa_Platform_Settings_SettingsExtensions_TryGet__1.htm)|
Получает объект с настройками заданного типа или null, если объект не
зарегистрирован.  
[WhenSettingsFunc](M_Tessa_Platform_Settings_SettingsExtensions_WhenSettingsFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[ISettingsExtension](T_Tessa_Platform_Settings_ISettingsExtension.htm) в
соответствии с функцией isAllowedFunc, которая проверяет контекст расширений.
Если зарегистрировано несколько политик, то должны выполняться все из них.  
## __См. также
#### Ссылки
[Tessa.Platform.Settings - пространство имён](N_Tessa_Platform_Settings.htm)
