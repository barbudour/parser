# StorageHelper.OverrideSuffix - поле
Если ключ в хеш-таблице заканчивается на этот суффикс, то при объединении
структуры объектов посредством методов Merge значение по этому ключу
перезаписывает значение в исходном объекте, а не объединяется с ним. При этом
суффикс удаляется из ключа.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public const string OverrideSuffix = "!!"
VB __Копировать
     Public Const OverrideSuffix As String = "!!"
C++ __Копировать
     public:
    literal String^ OverrideSuffix = "!!"
F# __Копировать
     static val mutable OverrideSuffix: string
#### Значение поля
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __См. также
#### Ссылки
[StorageHelper - ](T_Chronos_Platform_StorageHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
