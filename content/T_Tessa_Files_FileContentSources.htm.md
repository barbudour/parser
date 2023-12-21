# FileContentSources - класс
Источники контента файла, доступные в системе.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class FileContentSources
VB __Копировать
     Public NotInheritable Class FileContentSources
C++ __Копировать
     public ref class FileContentSources abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type FileContentSources = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FileContentSources
##  __Поля
[Database](F_Tessa_Files_FileContentSources_Database.htm)|  Контент файла
размещается в базе данных. Такое местоположение принято в системе с
настройками по умолчанию и может не соответстовать действительным настройкам
сервера.  
---|---  
[Default](F_Tessa_Files_FileContentSources_Default.htm)|  Источник контента
файла, устанавливаемый по умолчанию для токена
[IFileVersionCreationToken](T_Tessa_Files_IFileVersionCreationToken.htm). В
текущей версии системы это значение
[Database](F_Tessa_Files_FileContentSources_Database.htm). Рекомендуется явно
указывать значение источника контента для всех создаваемых версий файлов.  
[FileSystem](F_Tessa_Files_FileContentSources_FileSystem.htm)|  Контент файла
размещается в файловой системе. Такое местоположение принято в системе с
настройками по умолчанию и может не соответстовать действительным настройкам
сервера.  
## __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
