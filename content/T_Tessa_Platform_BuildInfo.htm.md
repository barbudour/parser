# BuildInfo - класс
Информация по версии сборки.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class BuildInfo
VB __Копировать
     Public NotInheritable Class BuildInfo
C++ __Копировать
     public ref class BuildInfo abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type BuildInfo = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ BuildInfo
##  __Свойства
[Date](P_Tessa_Platform_BuildInfo_Date.htm)|  Дата сборки.  
---|---  
[MajorVersion](P_Tessa_Platform_BuildInfo_MajorVersion.htm)|  Основная версия
сборки.  
[MinorVersion](P_Tessa_Platform_BuildInfo_MinorVersion.htm)|  Дополнительная
версия сборки с ведущей точкой.  
[Version](P_Tessa_Platform_BuildInfo_Version.htm)|  Полная строка версии
сборки.  
[VersionSuffix](P_Tessa_Platform_BuildInfo_VersionSuffix.htm)|  Суффикс
версии, например, "alpha" или "beta". Равен пустой строке, если суффикс
отсутствует.  
## __Методы
[GetVersionObject](M_Tessa_Platform_BuildInfo_GetVersionObject.htm)|
Возвращает версию сборки в виде объекта
[Version](https://learn.microsoft.com/dotnet/api/system.version). Такая версия
не содержит суффикс
[VersionSuffix](P_Tessa_Platform_BuildInfo_VersionSuffix.htm).  
---|---  
## __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
