# SchedulingExtensions.ValidateTrigger - метод
Выполняет проверку корректности заданных метаданных триггера.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static void ValidateTrigger(
    	this IPluginMetadataTrigger trigger
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub ValidateTrigger ( 
    	trigger As IPluginMetadataTrigger
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void ValidateTrigger(
    	IPluginMetadataTrigger^ trigger
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member ValidateTrigger : 
            trigger : IPluginMetadataTrigger -> unit 
#### Параметры
trigger
[IPluginMetadataTrigger](T_Chronos_Contracts_IPluginMetadataTrigger.htm)
    Метаданные триггера, корректность которых требуется проверить.
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
##  __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|
Параметр trigger равен null.  
---|---  
[InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception)|
Метаданные не прошли проверку на корректность.  
##  __См. также
#### Ссылки
[SchedulingExtensions -
](T_Chronos_Platform_Scheduling_SchedulingExtensions.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
