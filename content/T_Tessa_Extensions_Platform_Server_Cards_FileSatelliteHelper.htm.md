# FileSatelliteHelper - класс
Класс с вспомогательными методами для удобной работы с файловым сателлитом.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Cards](N_Tessa_Extensions_Platform_Server_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class FileSatelliteHelper
VB __Копировать
     Public NotInheritable Class FileSatelliteHelper
C++ __Копировать
     public ref class FileSatelliteHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type FileSatelliteHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FileSatelliteHelper
##  __Методы
[DeleteTaskFilesAsync](M_Tessa_Extensions_Platform_Server_Cards_FileSatelliteHelper_DeleteTaskFilesAsync.htm)|
Удаляет файлы, относящиеся к задания (файлы из диалогов, файлы из контролов
RichTextBox).  
---|---  
[GetFileSatelliteAsync(ICardStoreExtensionContext, ICardRepository,
Boolean)](M_Tessa_Extensions_Platform_Server_Cards_FileSatelliteHelper_GetFileSatelliteAsync.htm)|
Возвращает карточку файлового сателлита из контекста обработки расширений. При
первом вызове загружает файловый сателлит, при последующих использует объект
из контекста.  
[GetFileSatelliteAsync(ICardRepository, Guid, IValidationResultBuilder,
Boolean,
CancellationToken)](M_Tessa_Extensions_Platform_Server_Cards_FileSatelliteHelper_GetFileSatelliteAsync_1.htm)|
Возвращает карточку файлового сателлита из базы данных. Если карточки
файлового сателлита еще нет, то создает ее.  
[GetFileSatelliteIDAsync](M_Tessa_Extensions_Platform_Server_Cards_FileSatelliteHelper_GetFileSatelliteIDAsync.htm)|
Возвращает идентификатор карточки файлового сателлита из базы данных. Если
карточки файлового сателлита еще нет, то создает ее.  
[MoveFilesToFileSatelliteAsync](M_Tessa_Extensions_Platform_Server_Cards_FileSatelliteHelper_MoveFilesToFileSatelliteAsync.htm)|
Перемещает файлы из основной карточки в карточку сателлита. Автоматически
загружает и создает карточку сателлита, если ее еще не было.  
[StoreFileSatelliteAsync](M_Tessa_Extensions_Platform_Server_Cards_FileSatelliteHelper_StoreFileSatelliteAsync.htm)|
Сохраняет файловый сателлит, содержащийся в context. Вызывает фактическое
сохранение только, если ранее был вызван метод
[MoveFilesToFileSatelliteAsync(ICardStoreExtensionContext, ICardRepository,
Boolean)](M_Tessa_Extensions_Platform_Server_Cards_FileSatelliteHelper_MoveFilesToFileSatelliteAsync.htm).  
## __Поля
[FileSatelliteFileContentKey](F_Tessa_Extensions_Platform_Server_Cards_FileSatelliteHelper_FileSatelliteFileContentKey.htm)|
Ключ, по которому можно определить, при запросе контента файла, что этот
контент надо искать в FileSatellite.  
---|---  
[FileSatelliteFileKey](F_Tessa_Extensions_Platform_Server_Cards_FileSatelliteHelper_FileSatelliteFileKey.htm)|
Ключ, по которому хранится информация о том, что файл является файлом для
файлового сателлита.  
[FileSatelliteKey](F_Tessa_Extensions_Platform_Server_Cards_FileSatelliteHelper_FileSatelliteKey.htm)|
Ключ, по которому хранится карточка файлового сателлита в контексте сохранения
основной карточки.  
[KeepFileMark](F_Tessa_Extensions_Platform_Server_Cards_FileSatelliteHelper_KeepFileMark.htm)|
Метка, которая ставится в [Options](P_Tessa_Cards_CardFile_Options.htm), если
требуется, чтобы файл, который относится к заданию, не удалялся вместе с
заданием.  
## __См. также
#### Ссылки
[Tessa.Extensions.Platform.Server.Cards - пространство
имён](N_Tessa_Extensions_Platform_Server_Cards.htm)
