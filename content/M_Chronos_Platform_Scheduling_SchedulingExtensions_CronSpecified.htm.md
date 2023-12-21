# SchedulingExtensions.CronSpecified - метод
Возвращает признак того, что метаданные содержат информацию о строке в формате
Cron.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool CronSpecified(
    	this IPluginMetadataTrigger trigger
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function CronSpecified ( 
    	trigger As IPluginMetadataTrigger
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool CronSpecified(
    	IPluginMetadataTrigger^ trigger
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member CronSpecified : 
            trigger : IPluginMetadataTrigger -> bool 
#### Параметры
trigger
[IPluginMetadataTrigger](T_Chronos_Contracts_IPluginMetadataTrigger.htm)
    Метаданные триггера.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если метаданные содержат информацию о строке в формате Cron; false в
противном случае.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[IPluginMetadataTrigger](T_Chronos_Contracts_IPluginMetadataTrigger.htm). При
вызове метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[SchedulingExtensions -
](T_Chronos_Platform_Scheduling_SchedulingExtensions.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
