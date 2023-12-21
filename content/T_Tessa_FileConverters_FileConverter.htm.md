# FileConverter - класс
Объект, выполнющий преобразование файлов из одного формата в другой.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class FileConverter : IFileConverter
VB __Копировать
     Public NotInheritable Class FileConverter
    	Implements IFileConverter
C++ __Копировать
     public ref class FileConverter sealed : IFileConverter
F# __Копировать
     [<SealedAttribute>]
    type FileConverter = 
        class
            interface IFileConverter
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FileConverter
Implements
    [IFileConverter](T_Tessa_FileConverters_IFileConverter.htm)
##  __Конструкторы
[FileConverter](M_Tessa_FileConverters_FileConverter__ctor.htm)|  Создаёт
экземпляр класса с указанием его зависимостей.  
---|---  
## __Методы
[ConvertFileAsync](M_Tessa_FileConverters_FileConverter_ConvertFileAsync.htm)|
Выполняет асинхронную конвертацию файла карточки в заданный формат. Это
рекомендуемый способ выполнения конвертации. Возвращает асинхронный
[System.Threading.Tasks.Task], при завершении которого будет получен результат
конвертации, который предоставляет доступ к содержимому файла, для которого
была выполнена конвертация. Результат всегда не равен null, ошибки и
исключения будут сохранены в объекте результата.  
---|---  
[DeleteFileAsync](M_Tessa_FileConverters_FileConverter_DeleteFileAsync.htm)|
Удаляет сконвертированный файл из кэша файлов, если он там присутствует.
Возвращает результат удаления с сообщениями об ошибках и предупреждениями, а
также признак того, был ли файл в кэше на момент вызова метода. Используйте
метод в таких сценариях, как конвертация, инициируемая с веб-сервиса, но
фактически выполняемая в плагине Chronos, где кэш файлов требуется как способ
передачи содержимого файла после конвертации. Если известно, что операция по
конвертации уникальна и результат конвертации не будет нужен, то посредством
этого метода можно удалить содержимое файла из кэша файлов.  
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
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetRequestAsync](M_Tessa_FileConverters_FileConverter_TryGetRequestAsync.htm)|
Возвращает запрос на выполнение операции по конвертации заданной версии файла
в карточке или null, если параметры файла не найдены по идентификатору версии.
Используйте метод для физических файлов, информация по которым может быть
найдена по указанному идентификатору версии. Для виртуальных файлов создайте
объект запроса через конструктор [Tessa.FileConverters.FileConverterRequest].  
## __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[GetRequestOrThrowAsync](M_Tessa_FileConverters_FileConverterExtensions_GetRequestOrThrowAsync.htm)|
Возвращает запрос на выполнение операции по конвертации заданной версии файла
в карточке. Возвращаемое значение гарантированно не равно null. Если параметры
файла не найдены по идентификатору версии, то выбрасывается исключение.  
(Определяется
[FileConverterExtensions](T_Tessa_FileConverters_FileConverterExtensions.htm))  
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
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
