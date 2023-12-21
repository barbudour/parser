# FileConverterExtension - класс
Базовый класс расширения для операции по конвертированию файла.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class FileConverterExtension : IFileConverterExtension, 
    	IExtension
VB __Копировать
     Public MustInherit Class FileConverterExtension
    	Implements IFileConverterExtension, IExtension
C++ __Копировать
     public ref class FileConverterExtension abstract : IFileConverterExtension, 
    	IExtension
F# __Копировать
     [<AbstractClassAttribute>]
    type FileConverterExtension = 
        class
            interface IFileConverterExtension
            interface IExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FileConverterExtension
Implements
    [IExtension](T_Tessa_Extensions_IExtension.htm), [IFileConverterExtension](T_Tessa_FileConverters_IFileConverterExtension.htm)
##  __Конструкторы
[FileConverterExtension](M_Tessa_FileConverters_FileConverterExtension__ctor.htm)|
Инициализирует новый экземпляр класса FileConverterExtension  
---|---  
##  __Методы
[AfterRequest](M_Tessa_FileConverters_FileConverterExtension_AfterRequest.htm)|
Метод, выполняемый после конвертирования файлов, причём как в случае успеха,
так и при возникновении ошибок. Проверить успешность операции можно по
свойству context.RequestIsSuccessful. Файл после конвертации доступен в этом
методе по заданному в контексте пути. Если метод вернёт ошибку в результате
валидации или выбросит исключение, то результаты конвертации не будут
сохранены.  
---|---  
[BeforeRequest](M_Tessa_FileConverters_FileConverterExtension_BeforeRequest.htm)|
Метод, выполняемый перед конвертированием файлов. Файл после конвертации
недоступен в этом методе. Если метод вернёт ошибку в результате валидации или
выбросит исключение, то конвертация не будет выполнена.  
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
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
