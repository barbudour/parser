# AssemblyHelper - класс
Предоставляет вспомогательные методы для работы со сборками.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class AssemblyHelper
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class AssemblyHelper
C++ __Копировать
    [ExtensionAttribute]
    public ref class AssemblyHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type AssemblyHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ AssemblyHelper
##  __Методы
[ConvertToEmbeddedResourcePath](M_Tessa_Platform_AssemblyHelper_ConvertToEmbeddedResourcePath.htm)|
Преобразует указанный путь в формат пути к встроенному в сборку ресурсу.  
---|---  
[GetEnumerableFilePatternFromEmbeddedResources(String,
String)](M_Tessa_Platform_AssemblyHelper_GetEnumerableFilePatternFromEmbeddedResources_1.htm)|
Возвращает регулярное выражение, с помощью которого можно определить
встроенные ресурсы, расположенные по пути.  
[GetEnumerableFilePatternFromEmbeddedResources(Assembly, String,
String)](M_Tessa_Platform_AssemblyHelper_GetEnumerableFilePatternFromEmbeddedResources.htm)|
Возвращает регулярное выражение, с помощью которого можно определить
встроенные ресурсы, расположенные по пути.  
[GetFileNameEnumerableFromEmbeddedResources](M_Tessa_Platform_AssemblyHelper_GetFileNameEnumerableFromEmbeddedResources.htm)|
Возвращает перечисление имён файлов, расположенных в встроенных ресурсах по
заданному пути.  
[GetResourcePath(Assembly,
String)](M_Tessa_Platform_AssemblyHelper_GetResourcePath.htm)|  Возвращает
полный путь к ресурсу для указанной сборки по относительному пути.  
[GetResourcePath(String,
String)](M_Tessa_Platform_AssemblyHelper_GetResourcePath_1.htm)|  Возвращает
полный путь к ресурсу для указанной сборки по относительному пути.  
[GetResourceStream](M_Tessa_Platform_AssemblyHelper_GetResourceStream.htm)|
Возвращает Stream для указанного файла в ресурсах манифеста указанной сборки.  
[GetResourceTextFile](M_Tessa_Platform_AssemblyHelper_GetResourceTextFile.htm)|
Возвращает содержимое текстового файла, включённого во встроенные ресурсы
сборки и располагающегося по заданному относительному пути.  
[GetSimpleAssemblyName](M_Tessa_Platform_AssemblyHelper_GetSimpleAssemblyName.htm)|
Возвращает простое имя сборки.  
[SaveEmbeddedResourcesToFileAsync](M_Tessa_Platform_AssemblyHelper_SaveEmbeddedResourcesToFileAsync.htm)|
Сохраняет содержимое встроенного ресурса в указанном файле.  
## __Поля
[EmbeddedResourcePathSeparator](F_Tessa_Platform_AssemblyHelper_EmbeddedResourcePathSeparator.htm)|
Разделитель элементов пути к встроенному в сборку ресурсу.  
---|---  
[EmbeddedResourcePathSeparatorChar](F_Tessa_Platform_AssemblyHelper_EmbeddedResourcePathSeparatorChar.htm)|
Разделитель элементов пути к встроенному в сборку ресурсу.  
## __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
