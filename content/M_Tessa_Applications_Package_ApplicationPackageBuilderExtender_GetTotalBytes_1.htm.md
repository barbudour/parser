# ApplicationPackageBuilderExtender.GetTotalBytes(ApplicationPackage) - метод
Подсчитывает размер файлов в пакете приложения
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static long GetTotalBytes(
    	[NotNullAttribute] this ApplicationPackage package
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetTotalBytes ( 
    	<NotNullAttribute> package As ApplicationPackage
    ) As Long
C++ __Копировать
     public:
    [ExtensionAttribute]
    static long long GetTotalBytes(
    	[NotNullAttribute] ApplicationPackage^ package
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetTotalBytes : 
            [<NotNullAttribute>] package : ApplicationPackage -> int64 
#### Параметры
package
[ApplicationPackage](T_Tessa_Applications_Package_ApplicationPackage.htm)
     Пакет приложения 
#### Возвращаемое значение
[Int64](https://learn.microsoft.com/dotnet/api/system.int64)  
Размер файлов
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[ApplicationPackage](T_Tessa_Applications_Package_ApplicationPackage.htm). При
вызове метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[ApplicationPackageBuilderExtender -
](T_Tessa_Applications_Package_ApplicationPackageBuilderExtender.htm)
[GetTotalBytes -
перегрузка](Overload_Tessa_Applications_Package_ApplicationPackageBuilderExtender_GetTotalBytes.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
