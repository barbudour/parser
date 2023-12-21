# FileHelper - класс
Вспомогательные методы для взаимодействия с файлами.
## __Definition
 **Пространство имён:** [Tessa.Platform.IO](N_Tessa_Platform_IO.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class FileHelper
VB __Копировать
     Public NotInheritable Class FileHelper
C++ __Копировать
     public ref class FileHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type FileHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FileHelper
##  __Свойства
[FileHtmlSanitizer](P_Tessa_Platform_IO_FileHelper_FileHtmlSanitizer.htm)|
Объект, используемый для обработки содержимого html-файлов перед их открытием
в браузере. При этом удаляются скрипты и опасные html-конструкции для
предотвращения XSS-атак.  
---|---  
## __Методы
[AcquireFilePath(FileSpecialFolder,
String)](M_Tessa_Platform_IO_FileHelper_AcquireFilePath.htm)|  Получает путь к
файлу в заданной специальной папке, который может использоваться для
произвольных нужд. Для файла уже создаётся папка, поэтому файл можно сразу
использовать. Файл рекомендуется удалить вызовом [ReleaseFilePath(String,
Boolean)](M_Tessa_Platform_IO_FileHelper_ReleaseFilePath.htm). Файл будет
удалён при очередном запуске приложения спустя сутки после того, как он не
использовался.  
---|---  
[AcquireFilePath(FileSpecialFolder, String,
String)](M_Tessa_Platform_IO_FileHelper_AcquireFilePath_1.htm)|  Получает путь
к файлу в заданной специальной папке, который может использоваться для
произвольных нужд. Для файла уже создаётся папка, поэтому файл можно сразу
использовать. Файл рекомендуется удалить вызовом [ReleaseFilePath(String,
Boolean)](M_Tessa_Platform_IO_FileHelper_ReleaseFilePath.htm). Файл будет
удалён при очередном запуске приложения спустя сутки после того, как он не
использовался.  
[AcquireStreamingStringBuilder](M_Tessa_Platform_IO_FileHelper_AcquireStreamingStringBuilder.htm)|
В отличии от
[Acquire(Int32)](M_Tessa_Platform_StringBuilderHelper_Acquire.htm), этот метод
нужен для потокового чтения потенциально больших строк (до
[DefaultStreamingBufferSize](F_Tessa_Platform_IO_FileHelper_DefaultStreamingBufferSize.htm)).
Используется совместно с
[ReleaseStreamingStringBuilder(StringBuilder)](M_Tessa_Platform_IO_FileHelper_ReleaseStreamingStringBuilder.htm)
и
[ToStringAndReleaseStreamingStringBuilder(StringBuilder)](M_Tessa_Platform_IO_FileHelper_ToStringAndReleaseStreamingStringBuilder.htm).  
[AddHtmlIEBrowserCompatibilityMeta](M_Tessa_Platform_IO_FileHelper_AddHtmlIEBrowserCompatibilityMeta.htm)|
Устанавливает тэг совместимости с последними версиями браузера IE в заголовке
html-документа. Возвращает исходный текст, если тэг уже присутствует или не
найден раздел для добавления тэга.
<meta http-equiv="X-UA-Compatible" content="IE=Edge" />
Рекомендуется для использования при просмотре в контроле WebBrowser.  
[CheckFileName](M_Tessa_Platform_IO_FileHelper_CheckFileName.htm)|  Выполняет
проверку на то, что имя файла задано корректно, т.е. не содержит недопустимых
символов и указание пути к файлу.  
[CheckHasAccess](M_Tessa_Platform_IO_FileHelper_CheckHasAccess.htm)|
Возвращает информацию по тому, возможно ли открытие файла с указанным доступом
fileAccess.  
[CheckHasReaderAccess](M_Tessa_Platform_IO_FileHelper_CheckHasReaderAccess.htm)|
Выполняет проверку того, что файл доступен для чтения его содержимого, и
возвращает признак того, что проверка выполнена успешно: файл можно прочитать
или файл отсутствует при указанном canBeMissing.  
[CopyAsync(String, String,
CancellationToken)](M_Tessa_Platform_IO_FileHelper_CopyAsync_1.htm)|
Выполняет асинхронное копирование файла на диске.  
[CopyAsync(String, String, Boolean,
CancellationToken)](M_Tessa_Platform_IO_FileHelper_CopyAsync.htm)|  Выполняет
асинхронное копирование файла на диске.  
[Create](M_Tessa_Platform_IO_FileHelper_Create.htm)|  Открывает файл для
записи с указанным размером буфера. Если файл не существует, то он создаётся.
Существующий файл открывается с перезаписью содержимого с начала файла.
Разрешает асинхронные чтение и запись для такого файла.  
[CreateDirectoryIfNotExists](M_Tessa_Platform_IO_FileHelper_CreateDirectoryIfNotExists.htm)|
Создаёт папку, если она не существует. Возвращает признак того, что папка уже
существует или была создана в результате вызова этого метода.  
[CreateSubFolderPath(FileSpecialFolder)](M_Tessa_Platform_IO_FileHelper_CreateSubFolderPath_1.htm)|
Создаёт и возвращает путь к уникальной по имени папке в заданной специальной
папке. Сама папка не создаётся.  
[CreateSubFolderPath(String)](M_Tessa_Platform_IO_FileHelper_CreateSubFolderPath.htm)|
Создаёт и возвращает путь к уникальной по имени папке в заданной папке. Сама
папка не создаётся.  
[DeleteFileSafe](M_Tessa_Platform_IO_FileHelper_DeleteFileSafe.htm)|  Удаляет
файл по заданному пути. Возвращает признак того, что файл был успешно удалён
или не существовал. Не выбрасывает исключений. Не удаляет папку, в которой
находился файл, даже если в папке других файлов не было.  
[DeleteFilesByPatterns](M_Tessa_Platform_IO_FileHelper_DeleteFilesByPatterns.htm)|
Осуществляет удаление файлов из каталога folderPath в соответствии с шаблонами
searchPatterns.  
[DeleteOldFiles](M_Tessa_Platform_IO_FileHelper_DeleteOldFiles.htm)|  Очищает
папку с файлами, которые были созданы более суток назад с использованием
методов API и хранятся во временной папке пользователя. Не выбрасывает
исключений, если папку не удалось удалить.  
[FileExtensionsToString](M_Tessa_Platform_IO_FileHelper_FileExtensionsToString.htm)|
Преобразует список расширений файлов в строку, разделённую пробелами. Символ
ведущей точки при этом удаляется.  
[FinalizeAsync](M_Tessa_Platform_IO_FileHelper_FinalizeAsync.htm)|  Выполняет
финализацию файлового API при завершении приложения. Используйте метод, чтобы
ожидать завершения асинхронных задач в файловом API, таких как отложенное
освобождение содержимого файлов. Вызов метода является необязательным, но
рекомендован для таких приложений, как TessaClient и TessaAdmin.  
[FindFilesByPatterns](M_Tessa_Platform_IO_FileHelper_FindFilesByPatterns.htm)|
В каталоге folderPath находит файлы, соответствующие шаблонам: в соответствии
с шаблонами searchPatterns.  
[GetExtension](M_Tessa_Platform_IO_FileHelper_GetExtension.htm)|  Возвращает
расширение файла с учётом того, что в имени файла могут быть некорректные
символы.  
[GetFileName](M_Tessa_Platform_IO_FileHelper_GetFileName.htm)|  Возвращает имя
файла с расширением, но без пути к файлу с учётом того, что в имени файла
могут быть некорректные символы.  
[GetFileNameWithoutExtension](M_Tessa_Platform_IO_FileHelper_GetFileNameWithoutExtension.htm)|
Возвращает имя файла без расширения и без пути к файлу с учётом того, что в
имени файла могут быть некорректные символы.  
[GetPath](M_Tessa_Platform_IO_FileHelper_GetPath.htm)|  Возвращает полный путь
к заданной специальной папке.  
[GetWindowsLockingProcesses](M_Tessa_Platform_IO_FileHelper_GetWindowsLockingProcesses.htm)|
Возвращает список процессов, блокирующих файл. Если файл не блокируется, то
возвращается пустой список процессов. Метод доступен только для Windows.  
[Initialize](M_Tessa_Platform_IO_FileHelper_Initialize.htm)|  Выполняет
инициализацию файлового API при старте приложения. Вызов метода является
необязательным, но рекомендован для таких приложений, как TessaClient и
TessaAdmin.  
[IsLocked](M_Tessa_Platform_IO_FileHelper_IsLocked.htm)|  Возвращает признак
того, что файл заблокирован, по исключению, возникшему при открытии файла.  
[OpenFolderAndSelectFile](M_Tessa_Platform_IO_FileHelper_OpenFolderAndSelectFile.htm)|
Открывает окно проводника в папке с заданным файлом и выбирает в нём этот
файл.  
[OpenRead](M_Tessa_Platform_IO_FileHelper_OpenRead.htm)|  Открывает файл для
чтения с указанным размером буфера. Разрешает асинхронное чтение для такого
файла, если не указано обратного.  
[OpenWrite](M_Tessa_Platform_IO_FileHelper_OpenWrite.htm)|  Открывает файл для
записи с указанным размером буфера. Если файл не существует, то он создаётся.
Существующий файл открывается без перезаписи с начала файла. Разрешает
асинхронную запись для такого файла.  
[ParseFileExtensions](M_Tessa_Platform_IO_FileHelper_ParseFileExtensions.htm)|
Получает из строки со списком расширений, разделённых пробелами, массив с
этими расширениями, каждое из которых начинается с ведущей точки. Возвращаемый
массив не равен null.  
[ReleaseFilePath(String,
Boolean)](M_Tessa_Platform_IO_FileHelper_ReleaseFilePath.htm)|  Удаляет
временный файл по заданному пути, который был получен вызовом метода
[AcquireFilePath(FileSpecialFolder,
String)](M_Tessa_Platform_IO_FileHelper_AcquireFilePath.htm). Возвращает
признак того, что файл был успешно удалён или не существовал. Не выбрасывает
исключений.  
[ReleaseFilePath(String, Boolean,
Exception)](M_Tessa_Platform_IO_FileHelper_ReleaseFilePath_1.htm)|  Удаляет
временный файл по заданному пути, который был получен вызовом метода
[AcquireFilePath(FileSpecialFolder,
String)](M_Tessa_Platform_IO_FileHelper_AcquireFilePath.htm). Возвращает
признак того, что файл был успешно удалён или не существовал. Не выбрасывает
исключений.  
[ReleaseFolderPath](M_Tessa_Platform_IO_FileHelper_ReleaseFolderPath.htm)|
Удаляет папку, доступную по заданному пути, а также все файлы и подпапки в
ней. Возвращает признак того, что папка была успешно удалена или не
существовала. Не выбрасывает исключений.  
[ReleaseStreamingStringBuilder](M_Tessa_Platform_IO_FileHelper_ReleaseStreamingStringBuilder.htm)|
В отличии от
[Release(StringBuilder)](M_Tessa_Platform_StringBuilderHelper_Release.htm),
этот метод используется совместно с
[AcquireStreamingStringBuilder()](M_Tessa_Platform_IO_FileHelper_AcquireStreamingStringBuilder.htm).  
[RemoveInvalidFileNameChars](M_Tessa_Platform_IO_FileHelper_RemoveInvalidFileNameChars.htm)|
Возвращает имя файла, в котором удалены все некорректные для имени файла
символы. При этом удаляются начальные и конечные пробелы.  
[SetFileAttribute](M_Tessa_Platform_IO_FileHelper_SetFileAttribute.htm)|
Устанавливает или сбрасывает атрибут файла.  
[ToStringAndReleaseStreamingStringBuilder](M_Tessa_Platform_IO_FileHelper_ToStringAndReleaseStreamingStringBuilder.htm)|
В отличии от
[ToStringAndRelease(StringBuilder)](M_Tessa_Platform_StringBuilderHelper_ToStringAndRelease.htm),
этот метод используется совместно с
[AcquireStreamingStringBuilder()](M_Tessa_Platform_IO_FileHelper_AcquireStreamingStringBuilder.htm).  
## __Поля
[DefaultCopyBufferSize](F_Tessa_Platform_IO_FileHelper_DefaultCopyBufferSize.htm)|
Размер буфера по умолчанию для операций копирования содержимого файлов (методы
Copy, CopyAsync). Соответствует значению по умолчанию в текущей версии .NET -
Stream.DefaultCopyBufferSize.  
---|---  
[DefaultFileBufferSize](F_Tessa_Platform_IO_FileHelper_DefaultFileBufferSize.htm)|
Размер буфера по умолчанию для операций с файлами. Соответствует значению по
умолчанию в текущей версии .NET - FileStream.DefaultBufferSize.  
[DefaultStreamingBufferSize](F_Tessa_Platform_IO_FileHelper_DefaultStreamingBufferSize.htm)|
Размер буфера по умолчанию для операция с потоками
[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream).  
[InvalidCharReplacement](F_Tessa_Platform_IO_FileHelper_InvalidCharReplacement.htm)|
Рекомендуемая строка для замены невалидных символов в имени файла. Используйте
эту строку, когда требуется не просто удалить такие символы, а заменить их,
чтобы при использовании имени файлов, состоящего целиком из невалидных
символов, не было ошибок.  
[WindowsMaxDirectoryLength](F_Tessa_Platform_IO_FileHelper_WindowsMaxDirectoryLength.htm)|
Максимальная длина пути к папке. Аналогично константе MAX_DIRECTORY_PATH.  
[WindowsMaxPathLength](F_Tessa_Platform_IO_FileHelper_WindowsMaxPathLength.htm)|
Максимальная длина пути к файлу. Аналогично константе MAX_PATH.  
## __См. также
#### Ссылки
[Tessa.Platform.IO - пространство имён](N_Tessa_Platform_IO.htm)
