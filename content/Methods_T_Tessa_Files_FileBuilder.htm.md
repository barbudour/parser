# FileBuilder - методы
##  __Методы
[AddWithNotificationAsync](M_Tessa_Files_FileBuilder_AddWithNotificationAsync.htm)|
Создаёт файл, в случае успешного создания добавляет его в коллекцию с
уведомлением источника о добавлении, а затем возвращает файл. При
возникновении ошибок возвращает null, причём файл не добавляется в коллекцию.
Вторым значением возвращает результат создания файла, который содержит
описание возникших ошибок, если они возникли.  
---|---  
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
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ReturnAsync](M_Tessa_Files_FileBuilder_ReturnAsync.htm)|  Создаёт и
возвращает файл. При возникновении ошибок возвращает null. Вторым значением
возвращает результат создания файла, который содержит описание возникших
ошибок, если они возникли.  
[SetAuthor](M_Tessa_Files_FileBuilder_SetAuthor.htm)|  Устанавливает автора
файла, т.е. пользователя, создавшего файл. По умолчанию файл считается
созданным текущим пользователем. Как правило, информация по автору файла
используется только в объекте файла (например, в других расширениях или в UI),
т.к. стандартное API игнорирует её и использует текущего пользователя в
качестве автора при сохранении в БД.  
[SetCategory](M_Tessa_Files_FileBuilder_SetCategory.htm)|  Устанавливает
категорию файла. По умолчанию создаётся файл без категории.  
[SetContent(Func<CancellationToken,
ValueTask<IFileContent>>)](M_Tessa_Files_FileBuilder_SetContent.htm)|
Устанавливает функцию, создающую контент для создаваемого файла.  
[SetContent(Func<IFileContent, CancellationToken,
ValueTask>)](M_Tessa_Files_FileBuilder_SetContent_1.htm)| Устанавливает
действие, выполняющее инициализацию контента создаваемого файла.  
[SetContent(Stream)](M_Tessa_Files_FileBuilder_SetContent_2.htm)|
Устанавливает контент файла посредством чтения данных из заданного потока.  
[SetContent(String)](M_Tessa_Files_FileBuilder_SetContent_3.htm)|
Устанавливает контент файла по полному пути к файлу на диске. Если у
создаваемого файла не было задано имя, то оно будет определено как имя файла
по заданному пути.  
[SetFileToken](M_Tessa_Files_FileBuilder_SetFileToken.htm)| Устанавливает
метод, изменяющий токен на создание файла перед тем, как по нему будет создан
файл.  
[SetModified](M_Tessa_Files_FileBuilder_SetModified.htm)|  Устанавливает дату
и время последнего изменения файла, а также ID и имя автора этих изменений.  
[SetName](M_Tessa_Files_FileBuilder_SetName.htm)|  Устанавливает имя файла.
Имя файла можно не указывать, если контент файла определяется как путь к файлу
на диске.  
[SetPermissions](M_Tessa_Files_FileBuilder_SetPermissions.htm)|  Устанавливает
разрешения на файл. По умолчанию разрешения определяются источником файлов, но
обычно это файл со всеми разрешениями.  
[SetSource](M_Tessa_Files_FileBuilder_SetSource.htm)|  Устанавливает заданный
источник как используемый при создании файла. По умолчанию файл создаётся с
источником, заданным при создании объекта.  
[SetType](M_Tessa_Files_FileBuilder_SetType.htm)|  Устанавливает тип файла. По
умолчанию тип может определяться источником файлов.  
[SetVersionToken](M_Tessa_Files_FileBuilder_SetVersionToken.htm)|
Устанавливает метод, изменяющий токен на создание версии файла перед тем, как
по нему будет создана версия.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[SetCategory](M_Tessa_Files_FileExtensions_SetCategory.htm)|  Устанавливает
категорию файла в виде строки без указания идентификатора категории.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[SetCategory](M_Tessa_Files_FileExtensions_SetCategory_1.htm)|  Устанавливает
категорию файла в виде строки без указания идентификатора категории.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[SetContent](M_Tessa_Files_FileExtensions_SetContent_3.htm)|  Устанавливает
содержимое создаваемого файла по заданному объекту контента
[IFileContent](T_Tessa_Files_IFileContent.htm). Содержимое и размер
создаваемого файла будут вычисляться на основании заданного объекта.
Содержимое является нелокальным, т.е. не сохраняется во временную папку.
Поэтому не используйте его на клиенте, если файл будет доступен пользователю в
UI.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[SetContent](M_Tessa_Files_FileExtensions_SetContent.htm)|  Устанавливает
содержимое создаваемого файла по заданному массиву байт.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[SetContent](M_Tessa_Files_FileExtensions_SetContent_1.htm)|  Устанавливает
содержимое создаваемого файла по функции, возвращающей контент, и по функции,
возвращающей его размер. Содержимое является нелокальным, т.е. не сохраняется
во временную папку. Поэтому не используйте его на клиенте, если файл будет
доступен пользователю в UI.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[SetContent](M_Tessa_Files_FileExtensions_SetContent_2.htm)|  Устанавливает
содержимое создаваемого файла по функции, возвращающей контент, и по
фиксированному (заранее вычисленному) размеру. Содержимое является
нелокальным, т.е. не сохраняется во временную папку. Поэтому не используйте
его на клиенте, если файл будет доступен пользователю в UI.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[SetContentReadOnly](M_Tessa_Files_FileExtensions_SetContentReadOnly.htm)|
Устанавливает содержимое создаваемого файла на основании локального файла,
который не копируется в папку с кэшем. Рекомендуется использовать этот способ,
если файл создаётся только для чтения, например, для того, чтобы сохраниться
на сервер. Содержимое является нелокальным, т.е. не сохраняется во временную
папку. Поэтому не используйте его на клиенте, если файл будет доступен
пользователю в UI.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[SetContentText](M_Tessa_Files_FileExtensions_SetContentText.htm)|
Устанавливает содержимое создаваемого файла по заданному тексту с указанием
кодировки.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
##  __См. также
#### Ссылки
[FileBuilder - ](T_Tessa_Files_FileBuilder.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
