# SchedulingExtensions.ValidateMany - метод
Выполняет проверку на корректность каждого из перечисленных объектов,
содержащий информацию о плагине.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static void ValidateMany(
    	this IEnumerable<PluginImportingItem> pluginImportItems
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub ValidateMany ( 
    	pluginImportItems As IEnumerable(Of PluginImportingItem)
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void ValidateMany(
    	IEnumerable<PluginImportingItem^>^ pluginImportItems
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member ValidateMany : 
            pluginImportItems : IEnumerable<PluginImportingItem> -> unit 
#### Параметры
pluginImportItems
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[PluginImportingItem](T_Chronos_Platform_Scheduling_PluginImportingItem.htm)>
     Перечисление объектов, информацию о плагине которых требуется проверить на корректность. 
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[PluginImportingItem](T_Chronos_Platform_Scheduling_PluginImportingItem.htm)>.
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|
Параметр pluginImportItems равен null.  
---|---  
[InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception)|
Информация не прошла проверку на корректность.  
##  __См. также
#### Ссылки
[SchedulingExtensions -
](T_Chronos_Platform_Scheduling_SchedulingExtensions.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
