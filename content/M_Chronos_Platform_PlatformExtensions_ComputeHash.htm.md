# PlatformExtensions.ComputeHash - метод
Возвращает массив байт с криптостойким хеш-значением для заданного массива
байт с данными.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static byte[] ComputeHash(
    	this byte[] data
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function ComputeHash ( 
    	data As Byte()
    ) As Byte()
C++ __Копировать
     public:
    [ExtensionAttribute]
    static array<unsigned char>^ ComputeHash(
    	array<unsigned char>^ data
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member ComputeHash : 
            data : byte[] -> byte[] 
#### Параметры
data [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
     Массив байт с данными. Если массив равен null, то возвращаемое значение также равно null. 
#### Возвращаемое значение
[Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]  
Криптостойкое хеш-значение.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]. При
вызове метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[PlatformExtensions - ](T_Chronos_Platform_PlatformExtensions.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
