# FileBuilder - класс
Выполняет поэтапное создание файла с возможностью последующего добавления в
коллекцию файлов.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class FileBuilder : IFileBuilder
VB __Копировать
     Public Class FileBuilder
    	Implements IFileBuilder
C++ __Копировать
     public ref class FileBuilder : IFileBuilder
F# __Копировать
     type FileBuilder = 
        class
            interface IFileBuilder
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FileBuilder
Implements
    [IFileBuilder](T_Tessa_Files_IFileBuilder.htm)
##  __Заметки
Классы-наследники могут переопределить значения его методов, а также добавить
новые методы.
## __Конструкторы
[FileBuilder](M_Tessa_Files_FileBuilder__ctor.htm)|  Создаёт экземпляр класса
с указанием коллекции, в которую может быть добавлен файл с уведомлением об
изменениях.  
---|---  
## __Свойства
[Author](P_Tessa_Files_FileBuilder_Author.htm)|  Автор файла, т.е.
пользователь, создавший файл, или null, если автором является текущий
пользователь.  
---|---  
[Category](P_Tessa_Files_FileBuilder_Category.htm)|  Категория файла или null,
если категория не указана.  
[ContentActionAsync](P_Tessa_Files_FileBuilder_ContentActionAsync.htm)|
Метод, инициализирующий контент файла для способа создания контента
[Action](T_Tessa_Files_FileBuilder_ContentCreationType.htm).  
[ContentFactoryAsync](P_Tessa_Files_FileBuilder_ContentFactoryAsync.htm)|
Функция, создающая контент файла для способа создания контента
[Factory](T_Tessa_Files_FileBuilder_ContentCreationType.htm).  
[ContentPath](P_Tessa_Files_FileBuilder_ContentPath.htm)|  Полный путь к
контенту файла для способа создания контента
[Path](T_Tessa_Files_FileBuilder_ContentCreationType.htm).  
[ContentStream](P_Tessa_Files_FileBuilder_ContentStream.htm)|  Полный путь к
потоку с контентом файла для способа создания контента
[Stream](T_Tessa_Files_FileBuilder_ContentCreationType.htm).  
[ContentType](P_Tessa_Files_FileBuilder_ContentType.htm)|  Способ создания
контента файла. По умолчанию значение
[Undefined](T_Tessa_Files_FileBuilder_ContentCreationType.htm) запрещает
создание файла.  
[Files](P_Tessa_Files_FileBuilder_Files.htm)|  Коллекция, в которую может быть
добавлен файл с уведомлением об изменениях.  
[FileTokenActionAsync](P_Tessa_Files_FileBuilder_FileTokenActionAsync.htm)|
Метод, выполняющий дополнительное изменение токена на создание файла перед
тем, как объект файла будет создан.  
[Modified](P_Tessa_Files_FileBuilder_Modified.htm)|  Дата и время последнего
изменения файла.  
[ModifiedByID](P_Tessa_Files_FileBuilder_ModifiedByID.htm)|  Идентификатор
пользователя изменившего файл.  
[ModifiedByName](P_Tessa_Files_FileBuilder_ModifiedByName.htm)|  Имя
пользователя изменившего файл.  
[Name](P_Tessa_Files_FileBuilder_Name.htm)|  Имя файла или null, если имя не
задано. Для значения null имя может быть автоматически определено по пути к
файлу [ContentPath](P_Tessa_Files_FileBuilder_ContentPath.htm).  
[Permissions](P_Tessa_Files_FileBuilder_Permissions.htm)|  Разрешения на
редактирование файла или null, если будут использоваться разрешения по
умолчанию. По умолчанию разрешения определяются источником файлов, но обычно
это файл со всеми разрешениями.  
[Source](P_Tessa_Files_FileBuilder_Source.htm)|  Источник файлов, используемый
для создания файла.  
[Type](P_Tessa_Files_FileBuilder_Type.htm)|  Тип файла или null, если тип
файла не указан. Для значения null источник файлов может указать стандартный
тип файла.  
[VersionTokenActionAsync](P_Tessa_Files_FileBuilder_VersionTokenActionAsync.htm)|
Метод, выполняющий дополнительное изменение токена на создание версии файла
перед тем, как объект версия будет создана.  
## __Методы
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
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
