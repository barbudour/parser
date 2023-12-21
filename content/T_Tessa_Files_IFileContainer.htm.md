# IFileContainer - интерфейс
Контейнер, содержащий все доступные файлы.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFileContainer : INotifyPropertyChanged
VB __Копировать
     Public Interface IFileContainer
    	Inherits INotifyPropertyChanged
C++ __Копировать
     public interface class IFileContainer : INotifyPropertyChanged
F# __Копировать
     type IFileContainer = 
        interface
            interface INotifyPropertyChanged
        end
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged)
##  __Заметки
Реализация
[INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged)
требуется для того, чтобы не возникало утечек памяти при взаимодействии с UI.
## __Свойства
[Files](P_Tessa_Files_IFileContainer_Files.htm)| Коллекция файлов, доступных в
контейнере.  
---|---  
[Info](P_Tessa_Files_IFileContainer_Info.htm)|  Дополнительная информация по
объекту, доступная для установки в расширениях. Сохраняемая информация может
быть несериализуемой, например, можно записать ссылки на модели представлений
или любые другие объекты.  
[Permissions](P_Tessa_Files_IFileContainer_Permissions.htm)| Разрешения,
доступные для контейнера с файлами.  
[Source](P_Tessa_Files_IFileContainer_Source.htm)| Источник файлов,
обеспечивающий способ их создания по умолчанию.  
##  __События
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged.propertychanged)|
Occurs when a property value changes.  
(Унаследован от
[INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged))  
---|---  
##  __Методы расширения
[AddVirtualAsync](M_Tessa_Files_FileExtensions_AddVirtualAsync_1.htm)|
Создаёт и добавляет виртуальный файл, возвращает созданный файл. Этот метод
добавляет файл в источник по умолчанию
[Source](P_Tessa_Files_IFileContainer_Source.htm) для контейнера container.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
---|---  
[AddVirtualAsync](M_Tessa_Files_FileExtensions_AddVirtualAsync.htm)|  Создаёт
и добавляет виртуальный файл, возвращает созданный файл. Этот метод добавляет
файл в указанный источник fileSource, что позволяет, например, добавить файл в
структуру карточки [CardFile](T_Tessa_Cards_CardFile.htm), с которой не связан
контейнер файлов container.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[BuildFile](M_Tessa_Files_FileExtensions_BuildFile.htm)|  Возвращает объект,
выполняющий поэтапное создание файла с возможностью последующего добавления в
коллекцию файлов заданного контейнера. По умолчанию файл создаётся с
использованием источника [Source](P_Tessa_Files_IFileContainer_Source.htm),
заданного в контейнере. На возвращаемом объекте
[IFileBuilder](T_Tessa_Files_IFileBuilder.htm) необходимо вызвать один из
методов установки контента SetContent.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[SetFilePreviewAction](M_Tessa_UI_Files_FileUIExtensions_SetFilePreviewAction.htm)|
Устанавливает метод, определяющий параметры предпросмотра файла с
конвертацией. Метод вызывается при предпросмотре файлов, у которых ещё не
выполнена конвертация, т.е. не установлен отдельный объект
[PreviewContent](P_Tessa_Files_IFile_PreviewContent.htm), но при этом текущее
содержимое [!:IFile.Content] не отмечено, как изменённое
[IsDirty](P_Tessa_Files_IFileContent_IsDirty.htm). Если файл был открыт на
редактирование (отображается жёлтым), то стандартный предпросмотр для него
отключён.  
(Определяется [FileUIExtensions](T_Tessa_UI_Files_FileUIExtensions.htm))  
[SetNewFileAction](M_Tessa_UI_Files_FileUIExtensions_SetNewFileAction.htm)|
Устанавливает метод, определяющий параметры файла, добавляемого специальным
образом. Метод вызывается при добавлении файлов в специальных случаях, таких
как создание файла по шаблону и сохранение многостраничного документа из окна
сканирования. Метод не вызывается при типовой загрузке файлов через меню
контрола или буфер обмена.  
(Определяется [FileUIExtensions](T_Tessa_UI_Files_FileUIExtensions.htm))  
[SetNewPhysicalFileAction](M_Tessa_UI_Files_FileUIExtensions_SetNewPhysicalFileAction.htm)|
Устанавливает метод, определяющий параметры файла, добавляемого по заданному
пути на диске. Метод вызывается при добавлении файлов в типовых сценариях
(функция "Загрузить файлы", вставка из буфера обмена, drag&drop). Для
специальных случаев, таких как создание файла по шаблону или добавление из
окна сканирования, используйте методы SetNewFileAction.  
(Определяется [FileUIExtensions](T_Tessa_UI_Files_FileUIExtensions.htm))  
[TryGetFile](M_Tessa_Files_FileExtensions_TryGetFile.htm)|  Возвращает файл,
полученный по заданному идентификатору [ID](P_Tessa_Files_IFileEntity_ID.htm),
или null, если подходящий файл не был найден.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[TryGetFile](M_Tessa_Files_FileExtensions_TryGetFile_1.htm)|  Возвращает файл,
полученный по заданному имени [Name](P_Tessa_Files_IFileObject_Name.htm), или
null, если подходящий файл не был найден.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[TryGetFilePreviewAction](M_Tessa_UI_Files_FileUIExtensions_TryGetFilePreviewAction.htm)|
Возвращает метод, определяющий параметры предпросмотра файла с конвертацией,
или null, если такой метод отсутствует. Метод должен быть выполнен с указанием
текущего контекста [Current](P_Tessa_UI_UIContext_Current.htm). Метод
вызывается при предпросмотре файлов, у которых ещё не выполнена конвертация,
т.е. не установлен отдельный объект
[PreviewContent](P_Tessa_Files_IFile_PreviewContent.htm), но при этом текущее
содержимое [!:IFile.Content] не отмечено, как изменённое
[IsDirty](P_Tessa_Files_IFileContent_IsDirty.htm). Если файл был открыт на
редактирование (отображается жёлтым), то стандартный предпросмотр для него
отключён.  
(Определяется [FileUIExtensions](T_Tessa_UI_Files_FileUIExtensions.htm))  
[TryGetNewFileAction](M_Tessa_UI_Files_FileUIExtensions_TryGetNewFileAction.htm)|
Возвращает метод, определяющий параметры файла, добавляемого специальным
образом, или null, если такой метод отсутствует. Метод должен быть выполнен с
указанием текущего контекста [Current](P_Tessa_UI_UIContext_Current.htm).
Метод вызывается при добавлении файлов в специальных случаях, таких как
создание файла по шаблону и сохранение многостраничного документа из окна
сканирования. Метод не вызывается при типовой загрузке файлов через меню
контрола или буфер обмена.  
(Определяется [FileUIExtensions](T_Tessa_UI_Files_FileUIExtensions.htm))  
[TryGetNewPhysicalFileAction](M_Tessa_UI_Files_FileUIExtensions_TryGetNewPhysicalFileAction.htm)|
Возвращает метод, определяющий параметры файла, добавляемого по заданному пути
на диске, или null, если такой метод отсутствует. Метод должен быть выполнен с
указанием текущего контекста [Current](P_Tessa_UI_UIContext_Current.htm).
Метод вызывается при добавлении файлов в типовых сценариях (функция "Загрузить
файлы", вставка из буфера обмена, drag&drop). Для специальных случаев, таких
как создание файла по шаблону или добавление из окна сканирования, используйте
методы TryGetNewFileAction.  
(Определяется [FileUIExtensions](T_Tessa_UI_Files_FileUIExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
