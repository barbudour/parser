# IFileSource - методы
##  __Методы
[BuildFile](M_Tessa_Files_IFileSource_BuildFile.htm)|  Возвращает объект,
выполняющий поэтапное создание файла с возможностью последующего добавления в
заданную коллекцию. По умолчанию файл создаётся с использованием текущего
источника.  
---|---  
[CanUploadFileAsync](M_Tessa_Files_IFileSource_CanUploadFileAsync.htm)|
Проверяет, возможно ли загрузить в систему файл по заданному пути, например,
подходит ли он под ограничения по размеру файла. Если возвращённый объект
содержит ошибки, то загрузка запрещена. Обычно вызывается на клиенте для
проверки файла перед добавлением в элемент управления. Проверки на сервере
выполняются другими средствами (расширениями на сохранение карточки).  
[CopyAsync](M_Tessa_Files_IFileSource_CopyAsync.htm)|  Создаёт копию заданного
файла, при этом копируются свойства файла, последняя версия и её контент.
Скопированный файл ссылается на копируемый файл как на исходный через свойство
[Tessa.Files.IFile.Origin].  
[CreateFileAsync](M_Tessa_Files_IFileSource_CreateFileAsync.htm)| Создаёт файл
по заданному токену.  
[CreateSignatureAsync](M_Tessa_Files_IFileSource_CreateSignatureAsync.htm)|
Создаёт подпись для версии файла по заданному токену.  
[CreateVersionAsync](M_Tessa_Files_IFileSource_CreateVersionAsync.htm)|
Создаёт версию для файла по заданному токену.  
[GetContentAsync](M_Tessa_Files_IFileSource_GetContentAsync.htm)|  Загружает
контент версии файла из внешней подсистемы.  
[GetFileCreationTokenAsync](M_Tessa_Files_IFileSource_GetFileCreationTokenAsync.htm)|
Создаёт токен, используемый для создания файлов посредством источника файлов
[IFileSource].  
[GetFilesAsync](M_Tessa_Files_IFileSource_GetFilesAsync.htm)| Возвращает
коллекцию доступных файлов.  
[GetFileTagsAsync](M_Tessa_Files_IFileSource_GetFileTagsAsync.htm)|
Возвращает список тегов для файла. Обычно используется при добавлении файла на
клиенте. При сохранении карточки с файлами необходимые теги файлов добавляются
автоматически, независимо от результата метода. Возвращённое значение не равно
null.  
[GetLinkAsync(IFile,
CancellationToken)](M_Tessa_Files_IFileSource_GetLinkAsync.htm)| Возвращает
ссылку на файл.  
[GetLinkAsync(IFileVersion,
CancellationToken)](M_Tessa_Files_IFileSource_GetLinkAsync_1.htm)| Возвращает
ссылку на версию файла.  
[GetNewFilePermissionsAsync](M_Tessa_Files_IFileSource_GetNewFilePermissionsAsync.htm)|
Получает разрешения для создаваемого файла.  
[GetSignatureCreationTokenAsync](M_Tessa_Files_IFileSource_GetSignatureCreationTokenAsync.htm)|
Создаёт токен, используемый для создания подписей для версий файлов
посредством источника файлов [IFileSource]. Некоторые поля заполняются
автоматически, такие как кто и когда создал подпись (текущий пользователь в
данный момент).  
[GetSignaturesAsync](M_Tessa_Files_IFileSource_GetSignaturesAsync.htm)|
Возвращает коллекцию доступных подписей для заданной версии файла.  
[GetVersionCreationTokenAsync](M_Tessa_Files_IFileSource_GetVersionCreationTokenAsync.htm)|
Создаёт токен, используемый для создания версий файлов посредством источника
файлов [IFileSource]. Некоторые поля заполняются автоматически, такие как кто
и когда создал версию (текущий пользователь в данный момент).  
[GetVersionsAsync](M_Tessa_Files_IFileSource_GetVersionsAsync.htm)| Возвращает
коллекцию доступных версий для заданного файла.  
[NotifyAsync(IFile, FileNotificationType,
CancellationToken)](M_Tessa_Files_IFileSource_NotifyAsync.htm)| Уведомляет
подсистему о том, что с файлом было произведено указанное действие.  
[NotifyAsync(IFileSignature, FileSignatureNotificationType,
CancellationToken)](M_Tessa_Files_IFileSource_NotifyAsync_1.htm)| Уведомляет
подсистему о том, что с подписью файла было произведено указанное действие.  
[TryCreateRemoteContentAsync](M_Tessa_Files_IFileSource_TryCreateRemoteContentAsync.htm)|
Создаёт объект контента, обеспечивающий доступ к файлу удалённо, т.е. без
копирования во временную папку. Возвращает null, если не удалось создать
контент для заданной версии. Любой запрос к контенту файла может привести к
запросу к серверу или к другому способу создать контент.  
[TryGetSourceObjectID](M_Tessa_Files_IFileSource_TryGetSourceObjectID.htm)|
Получает идентификатор объекта-хранилища для указанного файла.  
##  __Методы расширения
[CreateFileAsync](M_Tessa_Files_FileExtensions_CreateFileAsync.htm)|  Создаёт
файл с указанными параметрами и единственной версией. Возвращает созданный
файл или null, если создать файл не удалось.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
---|---  
[CreateFileAsync](M_Tessa_Files_FileExtensions_CreateFileAsync_3.htm)|
Создаёт файл с указанными параметрами и единственной версией. Возвращает
созданный файл или null, если создать файл не удалось.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[CreateFileAsync](M_Tessa_Files_FileExtensions_CreateFileAsync_2.htm)|
Создаёт файл с указанными параметрами и единственной версией. Это
вспомогательный метод, который нельзя переопределить. Возвращает созданный
файл или null, если создать файл не удалось.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[CreateFileAsync](M_Tessa_Files_FileExtensions_CreateFileAsync_1.htm)|
Создаёт файл с указанными параметрами и единственной версией. Это
вспомогательный метод, который нельзя переопределить. Возвращает созданный
файл или null, если создать файл не удалось.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
##  __См. также
#### Ссылки
[IFileSource - ](T_Tessa_Files_IFileSource.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
