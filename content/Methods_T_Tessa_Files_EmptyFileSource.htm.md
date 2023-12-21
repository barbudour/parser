# EmptyFileSource - методы
##  __Методы
[BuildFile](M_Tessa_Files_FileSource_BuildFile.htm)|  Возвращает объект,
выполняющий поэтапное создание файла с возможностью последующего добавления в
заданную коллекцию. По умолчанию файл создаётся с использованием текущего
источника.  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
---|---  
[BuildFileCore](M_Tessa_Files_FileSource_BuildFileCore.htm)|  Возвращает
объект, выполняющий поэтапное создание файла с возможностью последующего
добавления в заданную коллекцию. По умолчанию файл создаётся с использованием
текущего источника.  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[CanUploadFileAsync](M_Tessa_Files_FileSource_CanUploadFileAsync.htm)|
Проверяет, возможно ли загрузить в систему файл по заданному пути, например,
подходит ли он под ограничения по размеру файла. Если возвращённый объект
содержит ошибки, то загрузка запрещена. Обычно вызывается на клиенте для
проверки файла перед добавлением в элемент управления. Проверки на сервере
выполняются другими средствами (расширениями на сохранение карточки).  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[CanUploadFileCoreAsync](M_Tessa_Files_FileSource_CanUploadFileCoreAsync.htm)|
Проверяет, возможно ли загрузить в систему файл по заданному пути, например,
подходит ли он под ограничения по размеру файла. Если возвращённый объект
содержит ошибки, то загрузка запрещена. Обычно вызывается на клиенте для
проверки файла перед добавлением в элемент управления. Проверки на сервере
выполняются другими средствами (расширениями на сохранение карточки).  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[CopyAsync](M_Tessa_Files_FileSource_CopyAsync.htm)|  Создаёт копию заданного
файла, при этом копируются свойства файла, последняя версия и её контент.
Скопированный файл ссылается на копируемый файл как на исходный через свойство
[Tessa.Files.IFile.Origin].  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[CopyCoreAsync](M_Tessa_Files_FileSource_CopyCoreAsync.htm)|  Создаёт копию
заданного файла, при этом копируются свойства файла, последняя версия и её
контент. Скопированный файл ссылается на копируемый файл как на исходный через
свойство [Tessa.Files.IFile.Origin].  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[CreateFileAsync](M_Tessa_Files_FileSource_CreateFileAsync.htm)| Создаёт файл
по заданному токену.  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[CreateFileCoreAsync](M_Tessa_Files_FileSource_CreateFileCoreAsync.htm)|
Создаёт файл по заданному токену.  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[CreateSignatureAsync](M_Tessa_Files_FileSource_CreateSignatureAsync.htm)|
Создаёт подпись для версии файла по заданному токену.  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[CreateSignatureCoreAsync](M_Tessa_Files_FileSource_CreateSignatureCoreAsync.htm)|
Создаёт подпись для версии файла по заданному токену.  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[CreateVersionAsync](M_Tessa_Files_FileSource_CreateVersionAsync.htm)| Создаёт
версию для файла по заданному токену.  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[CreateVersionCoreAsync](M_Tessa_Files_FileSource_CreateVersionCoreAsync.htm)|
Создаёт версию для файла по заданному токену.  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetContentAsync](M_Tessa_Files_FileSource_GetContentAsync.htm)|  Загружает
контент версии файла из внешней подсистемы.  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[GetContentCoreAsync](M_Tessa_Files_FileSource_GetContentCoreAsync.htm)|
Загружает контент версии файла из внешней подсистемы.  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[GetFileCreationTokenAsync](M_Tessa_Files_FileSource_GetFileCreationTokenAsync.htm)|
Создаёт токен, используемый для создания файлов посредством источника файлов
[IFileSource].  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[GetFileCreationTokenCoreAsync](M_Tessa_Files_FileSource_GetFileCreationTokenCoreAsync.htm)|
Создаёт токен, используемый для создания файлов посредством источника файлов
[IFileSource].  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[GetFilesAsync](M_Tessa_Files_FileSource_GetFilesAsync.htm)| Возвращает
коллекцию доступных файлов.  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[GetFilesCoreAsync](M_Tessa_Files_FileSource_GetFilesCoreAsync.htm)|
Возвращает коллекцию доступных файлов.  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[GetFileTagsAsync](M_Tessa_Files_FileSource_GetFileTagsAsync.htm)|  Возвращает
список тегов для файла. Обычно используется при добавлении файла на клиенте.
При сохранении карточки с файлами необходимые теги файлов добавляются
автоматически, независимо от результата метода. Возвращённое значение не равно
null.  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[GetFileTagsCoreAsync](M_Tessa_Files_FileSource_GetFileTagsCoreAsync.htm)|
Возвращает список тегов для файла. Обычно используется при добавлении файла на
клиенте. При сохранении карточки с файлами необходимые теги файлов добавляются
автоматически, независимо от результата метода. Возвращённое значение не равно
null.  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetLinkAsync(IFile,
CancellationToken)](M_Tessa_Files_FileSource_GetLinkAsync.htm)| Возвращает
ссылку на файл.  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[GetLinkAsync(IFileVersion,
CancellationToken)](M_Tessa_Files_FileSource_GetLinkAsync_1.htm)| Возвращает
ссылку на версию файла.  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[GetLinkCoreAsync(IFile,
CancellationToken)](M_Tessa_Files_FileSource_GetLinkCoreAsync.htm)| Возвращает
ссылку на файл.  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[GetLinkCoreAsync(IFileVersion,
CancellationToken)](M_Tessa_Files_FileSource_GetLinkCoreAsync_1.htm)|
Возвращает ссылку на версию файла.  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[GetNewFilePermissionsAsync](M_Tessa_Files_FileSource_GetNewFilePermissionsAsync.htm)|
Получает разрешения для создаваемого файла.  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[GetSignatureCreationTokenAsync](M_Tessa_Files_FileSource_GetSignatureCreationTokenAsync.htm)|
Создаёт токен, используемый для создания подписей для версий файлов
посредством источника файлов [IFileSource]. Некоторые поля заполняются
автоматически, такие как кто и когда создал подпись (текущий пользователь в
данный момент).  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[GetSignatureCreationTokenCoreAsync](M_Tessa_Files_FileSource_GetSignatureCreationTokenCoreAsync.htm)|
Создаёт токен, используемый для создания подписей для версий файлов
посредством источника файлов [IFileSource]. Некоторые поля заполняются
автоматически, такие как кто и когда создал подпись (текущий пользователь в
данный момент).  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[GetSignaturesAsync](M_Tessa_Files_FileSource_GetSignaturesAsync.htm)|
Возвращает коллекцию доступных подписей для заданной версии файла.  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[GetSignaturesCoreAsync](M_Tessa_Files_FileSource_GetSignaturesCoreAsync.htm)|
Возвращает коллекцию доступных подписей для заданной версии файла.  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetVersionCreationTokenAsync](M_Tessa_Files_FileSource_GetVersionCreationTokenAsync.htm)|
Создаёт токен, используемый для создания версий файлов посредством источника
файлов [IFileSource]. Некоторые поля заполняются автоматически, такие как кто
и когда создал версию (текущий пользователь в данный момент).  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[GetVersionCreationTokenCoreAsync](M_Tessa_Files_FileSource_GetVersionCreationTokenCoreAsync.htm)|
Создаёт токен, используемый для создания версий файлов посредством источника
файлов [IFileSource]. Некоторые поля заполняются автоматически, такие как кто
и когда создал версию (текущий пользователь в данный момент).  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[GetVersionsAsync](M_Tessa_Files_FileSource_GetVersionsAsync.htm)| Возвращает
коллекцию доступных версий для заданного файла.  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[GetVersionsCoreAsync](M_Tessa_Files_FileSource_GetVersionsCoreAsync.htm)|
Возвращает коллекцию доступных версий для заданного файла.  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[NotifyAsync(IFile, FileNotificationType,
CancellationToken)](M_Tessa_Files_FileSource_NotifyAsync.htm)| Уведомляет
подсистему о том, что с файлом было произведено указанное действие.  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[NotifyAsync(IFileSignature, FileSignatureNotificationType,
CancellationToken)](M_Tessa_Files_FileSource_NotifyAsync_1.htm)| Уведомляет
подсистему о том, что с подписью файла было произведено указанное действие.  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[NotifyCoreAsync(IFile, FileNotificationType,
CancellationToken)](M_Tessa_Files_FileSource_NotifyCoreAsync.htm)| Уведомляет
подсистему о том, что с файлом было произведено указанное действие.  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[NotifyCoreAsync(IFileSignature, FileSignatureNotificationType,
CancellationToken)](M_Tessa_Files_FileSource_NotifyCoreAsync_1.htm)|
Уведомляет подсистему о том, что с подписью файла было произведено указанное
действие.  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryCreateRemoteContentAsync](M_Tessa_Files_FileSource_TryCreateRemoteContentAsync.htm)|
Создаёт объект контента, обеспечивающий доступ к файлу удалённо, т.е. без
копирования во временную папку. Возвращает null, если не удалось создать
контент для заданной версии. Любой запрос к контенту файла может привести к
запросу к серверу или к другому способу создать контент.  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[TryCreateRemoteContentCoreAsync](M_Tessa_Files_FileSource_TryCreateRemoteContentCoreAsync.htm)|
Создаёт объект контента, обеспечивающий доступ к файлу удалённо, т.е. без
копирования во временную папку. Возвращает null, если не удалось создать
контент для заданной версии. Любой запрос к контенту файла может привести к
запросу к серверу или к другому способу создать контент.  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
[TryGetSourceObjectID](M_Tessa_Files_FileSource_TryGetSourceObjectID.htm)|
Получает идентификатор объекта-хранилища для указанного файла.  
(Унаследован от [FileSource](T_Tessa_Files_FileSource.htm))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[EmptyFileSource - ](T_Tessa_Files_EmptyFileSource.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
