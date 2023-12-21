#
ApplicationPackageBuilderExtender.GetTotalBytes(IList<ApplicationPackageFile>)
- метод
Подсчитывает размер файлов в пакете приложения
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static long GetTotalBytes(
    	[NotNullAttribute] this IList<ApplicationPackageFile> files
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetTotalBytes ( 
    	<NotNullAttribute> files As IList(Of ApplicationPackageFile)
    ) As Long
C++ __Копировать
     public:
    [ExtensionAttribute]
    static long long GetTotalBytes(
    	[NotNullAttribute] IList<ApplicationPackageFile^>^ files
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetTotalBytes : 
            [<NotNullAttribute>] files : IList<ApplicationPackageFile> -> int64 
#### Параметры
files
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[ApplicationPackageFile](T_Tessa_Applications_Package_ApplicationPackageFile.htm)>
     Список файлов 
#### Возвращаемое значение
[Int64](https://learn.microsoft.com/dotnet/api/system.int64)  
Размер файлов
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[ApplicationPackageFile](T_Tessa_Applications_Package_ApplicationPackageFile.htm)>.
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|
source or selector is null.  
---|---  
[OverflowException](https://learn.microsoft.com/dotnet/api/system.overflowexception)|
The sum is larger than
[MaxValue](https://learn.microsoft.com/dotnet/api/system.int64.maxvalue).  
##  __См. также
#### Ссылки
[ApplicationPackageBuilderExtender -
](T_Tessa_Applications_Package_ApplicationPackageBuilderExtender.htm)
[GetTotalBytes -
перегрузка](Overload_Tessa_Applications_Package_ApplicationPackageBuilderExtender_GetTotalBytes.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
