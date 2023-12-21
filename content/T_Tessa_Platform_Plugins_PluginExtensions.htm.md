# PluginExtensions - класс
Методы-расширения для пространства имён Tessa.Platform.Plugins.
## __Definition
 **Пространство имён:** [Tessa.Platform.Plugins](N_Tessa_Platform_Plugins.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class PluginExtensions
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class PluginExtensions
C++ __Копировать
    [ExtensionAttribute]
    public ref class PluginExtensions abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type PluginExtensions = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PluginExtensions
##  __Методы
[RegisterPluginExtensionTypes](M_Tessa_Platform_Plugins_PluginExtensions_RegisterPluginExtensionTypes.htm)|
Выполняет регистрацию стандартных типов расширений плагинов
[IPluginExtension](T_Tessa_Platform_Plugins_IPluginExtension.htm).  
---|---  
[WithPluginSchedulingFilter](M_Tessa_Platform_Plugins_PluginExtensions_WithPluginSchedulingFilter.htm)|
Регистрирует политику фильтрации выполнения методов расширений плагинов
[IPluginExtension](T_Tessa_Platform_Plugins_IPluginExtension.htm), указанных
посредством политики
[IPluginSchedulingPolicy](T_Tessa_Platform_Plugins_IPluginSchedulingPolicy.htm).  
[WithScheduling](M_Tessa_Platform_Plugins_PluginExtensions_WithScheduling.htm)|
Регистрирует политику фильтрации выполнения методов расширений плагинов по
заданному способу диспетчеризации. Если способ диспетчеризации не задан, то
метод расширения не выполняется. Для того, чтобы политика использовалась,
требуется зарегистрировать политику
[PluginSchedulingFilterPolicy](T_Tessa_Platform_Plugins_PluginSchedulingFilterPolicy.htm).  
## __См. также
#### Ссылки
[Tessa.Platform.Plugins - пространство имён](N_Tessa_Platform_Plugins.htm)
