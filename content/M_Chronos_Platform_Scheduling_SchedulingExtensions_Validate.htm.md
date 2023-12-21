# SchedulingExtensions.Validate - метод
Выполняет проверку корректности заданных метаданных, и генерирует исключение в
случае ошибки.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static void Validate(
    	this IPluginMetadata metadata
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub Validate ( 
    	metadata As IPluginMetadata
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void Validate(
    	IPluginMetadata^ metadata
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member Validate : 
            metadata : IPluginMetadata -> unit 
#### Параметры
metadata [IPluginMetadata](T_Chronos_Contracts_IPluginMetadata.htm)
    Метаданные плагина, корректность которых требуется проверить.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [IPluginMetadata](T_Chronos_Contracts_IPluginMetadata.htm). При
вызове метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|
Параметр metadata равен null.  
---|---  
[InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception)|
Метаданные не прошли проверку на корректность.  
##  __См. также
#### Ссылки
[SchedulingExtensions -
](T_Chronos_Platform_Scheduling_SchedulingExtensions.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
