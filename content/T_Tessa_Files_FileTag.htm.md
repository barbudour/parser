# FileTag - класс
Тег, связанный с версией файла. Например, признак того, что размер содержимого
файла трактуется как большой файл, поэтому файл не копируется во временную
папку.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class FileTag : IFileTag, IEquatable<IFileTag>, 
    	ISealable
VB __Копировать
     Public Class FileTag
    	Implements IFileTag, IEquatable(Of IFileTag), 
    	ISealable
C++ __Копировать
     public ref class FileTag : IFileTag, 
    	IEquatable<IFileTag^>, ISealable
F# __Копировать
     type FileTag = 
        class
            interface IFileTag
            interface IEquatable<IFileTag>
            interface ISealable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FileTag
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[IFileTag](T_Tessa_Files_IFileTag.htm)>, [IFileTag](T_Tessa_Files_IFileTag.htm), [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Заметки
Наследники класса могут добавить строготипизированные свойства.
## __Конструкторы
[FileTag](M_Tessa_Files_FileTag__ctor.htm)|  Создаёт экземпляр класса с
указанием значений его свойств.  
---|---  
## __Свойства
[Info](P_Tessa_Files_FileTag_Info.htm)| Дополнительная информация для
расширений или null, если информация не требуется.  
---|---  
[IsSealed](P_Tessa_Files_FileTag_IsSealed.htm)| Признак того, что объект был
защищён от изменений.  
[Key](P_Tessa_Files_FileTag_Key.htm)| Ключ, уникально идентифицирующий тег.
При сравнении ключей обычно не учитывается регистр символов.  
##  __Методы
[Aggregate(IEnumerable<String>)](M_Tessa_Files_FileTag_Aggregate.htm)|
Объединяет список тегов в строку, которую можно сохранить в базе данных или
передать в методы [Parse(String)](M_Tessa_Files_FileTag_Parse.htm) и
[ParseAndBox(String)](M_Tessa_Files_FileTag_ParseAndBox.htm) или обратного
преобразования. Возвращаемое значение будет равно null, если теги отсутствуют.  
---|---  
[Aggregate(IEnumerable<IFileTag>)](M_Tessa_Files_FileTag_Aggregate_1.htm)|
Объединяет список тегов в строку, которую можно сохранить в базе данных или
передать в методы [Parse(String)](M_Tessa_Files_FileTag_Parse.htm) и
[ParseAndBox(String)](M_Tessa_Files_FileTag_ParseAndBox.htm) или обратного
преобразования.  
[Box](M_Tessa_Files_FileTag_Box.htm)|  Выполняет упаковку объекта по
строковому ключу, если объект зарегистрирован как стандартный в коллекции
[BoxedTags](F_Tessa_Files_FileTag_BoxedTags.htm), например, это тег для файлов
большого размера [Large](F_Tessa_Files_FileTag_Large.htm). Если объект по
ключу не найден в коллекции, то возвращается новый объект FileTag, защищённый
от изменений, который не добавляется в список автоматически (т.е. объекты,
отсутствующие в списке [BoxedTags](F_Tessa_Files_FileTag_BoxedTags.htm), будут
создаваться каждый раз новые).  
[Equals(IFileTag)](M_Tessa_Files_FileTag_Equals_1.htm)| Сравнивает текущий
объект с заданным.  
[Equals(Object)](M_Tessa_Files_FileTag_Equals.htm)| Сравнивает текущий объект
с заданным.  
(Переопределяет
[Object.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Files_FileTag_GetHashCode.htm)| Возвращает хеш-код
объекта.  
(Переопределяет
[Object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode))  
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
[Parse](M_Tessa_Files_FileTag_Parse.htm)|  Разбирает строку, содержащую один
или несколько тэгов. Каждый тэг обрамляется в угловые скобки, например:
<tag1><tag2>. Возвращает список строк-тегов, которые затем можно передать в
метод [Box(String)](M_Tessa_Files_FileTag_Box.htm) для создания объектов
тегов.  
[ParseAndBox](M_Tessa_Files_FileTag_ParseAndBox.htm)|  Разбирает строку,
содержащую один или несколько тэгов, и возвращает список объектов
[IFileTag](T_Tessa_Files_IFileTag.htm), упакованный методом
[Box(String)](M_Tessa_Files_FileTag_Box.htm).  
[Seal](M_Tessa_Files_FileTag_Seal.htm)| Защищает объект от изменений.  
[SealInternal](M_Tessa_Files_FileTag_SealInternal.htm)|
Защищает объект от изменений.
Метод может быть переопределён в классах-наследниках.  
[ToString](M_Tessa_Files_FileTag_ToString.htm)| Возвращает строковое
представление объекта.  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
##  __Поля
[BoxedTags](F_Tessa_Files_FileTag_BoxedTags.htm)|  Коллекция стандартных
тегов, для которых доступна упаковка методом
[Box(String)](M_Tessa_Files_FileTag_Box.htm). Поиск по коллекции выполняется
без учёта регистра.  
---|---  
[Large](F_Tessa_Files_FileTag_Large.htm)|  Тег для файлов большого размера.  
## __Методы расширения
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
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
