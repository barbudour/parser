# FileSource - методы
##  __Методы
[BuildFile](M_Tessa_Files_FileSource_BuildFile.htm)|  Возвращает объект,
выполняющий поэтапное создание файла с возможностью последующего добавления в
заданную коллекцию. По умолчанию файл создаётся с использованием текущего
источника.  
---|---  
[BuildFileCore](M_Tessa_Files_FileSource_BuildFileCore.htm)|  Возвращает
объект, выполняющий поэтапное создание файла с возможностью последующего
добавления в заданную коллекцию. По умолчанию файл создаётся с использованием
текущего источника.  
[CanUploadFileAsync](M_Tessa_Files_FileSource_CanUploadFileAsync.htm)|
Проверяет, возможно ли загрузить в систему файл по заданному пути, например,
подходит ли он под ограничения по размеру файла. Если возвращённый объект
содержит ошибки, то загрузка запрещена. Обычно вызывается на клиенте для
проверки файла перед добавлением в элемент управления. Проверки на сервере
выполняются другими средствами (расширениями на сохранение карточки).  
[CanUploadFileCoreAsync](M_Tessa_Files_FileSource_CanUploadFileCoreAsync.htm)|
Проверяет, возможно ли загрузить в систему файл по заданному пути, например,
подходит ли он под ограничения по размеру файла. Если возвращённый объект
содержит ошибки, то загрузка запрещена. Обычно вызывается на клиенте для
проверки файла перед добавлением в элемент управления. Проверки на сервере
выполняются другими средствами (расширениями на сохранение карточки).  
[CopyAsync](M_Tessa_Files_FileSource_CopyAsync.htm)|  Создаёт копию заданного
файла, при этом копируются свойства файла, последняя версия и её контент.
Скопированный файл ссылается на копируемый файл как на исходный через свойство
[Tessa.Files.IFile.Origin].  
[CopyCoreAsync](M_Tessa_Files_FileSource_CopyCoreAsync.htm)|  Создаёт копию
заданного файла, при этом копируются свойства файла, последняя версия и её
контент. Скопированный файл ссылается на копируемый файл как на исходный через
свойство [Tessa.Files.IFile.Origin].  
[CreateFileAsync](M_Tessa_Files_FileSource_CreateFileAsync.htm)| Создаёт файл
по заданному токену.  
[CreateFileCoreAsync](M_Tessa_Files_FileSource_CreateFileCoreAsync.htm)|
Создаёт файл по заданному токену.  
[CreateSignatureAsync](M_Tessa_Files_FileSource_CreateSignatureAsync.htm)|
Создаёт подпись для версии файла по заданному токену.  
[CreateSignatureCoreAsync](M_Tessa_Files_FileSource_CreateSignatureCoreAsync.htm)|
Создаёт подпись для версии файла по заданному токену.  
[CreateVersionAsync](M_Tessa_Files_FileSource_CreateVersionAsync.htm)| Создаёт
версию для файла по заданному токену.  
[CreateVersionCoreAsync](M_Tessa_Files_FileSource_CreateVersionCoreAsync.htm)|
Создаёт версию для файла по заданному токену.  
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
[GetContentCoreAsync](M_Tessa_Files_FileSource_GetContentCoreAsync.htm)|
Загружает контент версии файла из внешней подсистемы.  
[GetFileCreationTokenAsync](M_Tessa_Files_FileSource_GetFileCreationTokenAsync.htm)|
Создаёт токен, используемый для создания файлов посредством источника файлов
[IFileSource].  
[GetFileCreationTokenCoreAsync](M_Tessa_Files_FileSource_GetFileCreationTokenCoreAsync.htm)|
Создаёт токен, используемый для создания файлов посредством источника файлов
[IFileSource].  
[GetFilesAsync](M_Tessa_Files_FileSource_GetFilesAsync.htm)| Возвращает
коллекцию доступных файлов.  
[GetFilesCoreAsync](M_Tessa_Files_FileSource_GetFilesCoreAsync.htm)|
Возвращает коллекцию доступных файлов.  
[GetFileTagsAsync](M_Tessa_Files_FileSource_GetFileTagsAsync.htm)|  Возвращает
список тегов для файла. Обычно используется при добавлении файла на клиенте.
При сохранении карточки с файлами необходимые теги файлов добавляются
автоматически, независимо от результата метода. Возвращённое значение не равно
null.  
[GetFileTagsCoreAsync](M_Tessa_Files_FileSource_GetFileTagsCoreAsync.htm)|
Возвращает список тегов для файла. Обычно используется при добавлении файла на
клиенте. При сохранении карточки с файлами необходимые теги файлов добавляются
автоматически, независимо от результата метода. Возвращённое значение не равно
null.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetLinkAsync(IFile,
CancellationToken)](M_Tessa_Files_FileSource_GetLinkAsync.htm)| Возвращает
ссылку на файл.  
[GetLinkAsync(IFileVersion,
CancellationToken)](M_Tessa_Files_FileSource_GetLinkAsync_1.htm)| Возвращает
ссылку на версию файла.  
[GetLinkCoreAsync(IFile,
CancellationToken)](M_Tessa_Files_FileSource_GetLinkCoreAsync.htm)| Возвращает
ссылку на файл.  
[GetLinkCoreAsync(IFileVersion,
CancellationToken)](M_Tessa_Files_FileSource_GetLinkCoreAsync_1.htm)|
Возвращает ссылку на версию файла.  
[GetNewFilePermissionsAsync](M_Tessa_Files_FileSource_GetNewFilePermissionsAsync.htm)|
Получает разрешения для создаваемого файла.  
[GetSignatureCreationTokenAsync](M_Tessa_Files_FileSource_GetSignatureCreationTokenAsync.htm)|
Создаёт токен, используемый для создания подписей для версий файлов
посредством источника файлов [IFileSource]. Некоторые поля заполняются
автоматически, такие как кто и когда создал подпись (текущий пользователь в
данный момент).  
[GetSignatureCreationTokenCoreAsync](M_Tessa_Files_FileSource_GetSignatureCreationTokenCoreAsync.htm)|
Создаёт токен, используемый для создания подписей для версий файлов
посредством источника файлов [IFileSource]. Некоторые поля заполняются
автоматически, такие как кто и когда создал подпись (текущий пользователь в
данный момент).  
[GetSignaturesAsync](M_Tessa_Files_FileSource_GetSignaturesAsync.htm)|
Возвращает коллекцию доступных подписей для заданной версии файла.  
[GetSignaturesCoreAsync](M_Tessa_Files_FileSource_GetSignaturesCoreAsync.htm)|
Возвращает коллекцию доступных подписей для заданной версии файла.  
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
[GetVersionCreationTokenCoreAsync](M_Tessa_Files_FileSource_GetVersionCreationTokenCoreAsync.htm)|
Создаёт токен, используемый для создания версий файлов посредством источника
файлов [IFileSource]. Некоторые поля заполняются автоматически, такие как кто
и когда создал версию (текущий пользователь в данный момент).  
[GetVersionsAsync](M_Tessa_Files_FileSource_GetVersionsAsync.htm)| Возвращает
коллекцию доступных версий для заданного файла.  
[GetVersionsCoreAsync](M_Tessa_Files_FileSource_GetVersionsCoreAsync.htm)|
Возвращает коллекцию доступных версий для заданного файла.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[NotifyAsync(IFile, FileNotificationType,
CancellationToken)](M_Tessa_Files_FileSource_NotifyAsync.htm)| Уведомляет
подсистему о том, что с файлом было произведено указанное действие.  
[NotifyAsync(IFileSignature, FileSignatureNotificationType,
CancellationToken)](M_Tessa_Files_FileSource_NotifyAsync_1.htm)| Уведомляет
подсистему о том, что с подписью файла было произведено указанное действие.  
[NotifyCoreAsync(IFile, FileNotificationType,
CancellationToken)](M_Tessa_Files_FileSource_NotifyCoreAsync.htm)| Уведомляет
подсистему о том, что с файлом было произведено указанное действие.  
[NotifyCoreAsync(IFileSignature, FileSignatureNotificationType,
CancellationToken)](M_Tessa_Files_FileSource_NotifyCoreAsync_1.htm)|
Уведомляет подсистему о том, что с подписью файла было произведено указанное
действие.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryCreateRemoteContentAsync](M_Tessa_Files_FileSource_TryCreateRemoteContentAsync.htm)|
Создаёт объект контента, обеспечивающий доступ к файлу удалённо, т.е. без
копирования во временную папку. Возвращает null, если не удалось создать
контент для заданной версии. Любой запрос к контенту файла может привести к
запросу к серверу или к другому способу создать контент.  
[TryCreateRemoteContentCoreAsync](M_Tessa_Files_FileSource_TryCreateRemoteContentCoreAsync.htm)|
Создаёт объект контента, обеспечивающий доступ к файлу удалённо, т.е. без
копирования во временную папку. Возвращает null, если не удалось создать
контент для заданной версии. Любой запрос к контенту файла может привести к
запросу к серверу или к другому способу создать контент.  
[TryGetSourceObjectID](M_Tessa_Files_FileSource_TryGetSourceObjectID.htm)|
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
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
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
[FileSource - ](T_Tessa_Files_FileSource.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
