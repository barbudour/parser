# CardFileType - класс
Тип файла в карточке.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardFileType : FileType
VB __Копировать
     Public NotInheritable Class CardFileType
    	Inherits FileType
C++ __Копировать
     public ref class CardFileType sealed : public FileType
F# __Копировать
     [<SealedAttribute>]
    type CardFileType = 
        class
            inherit FileType
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[FileType](T_Tessa_Files_FileType.htm) __ CardFileType
##  __Конструкторы
[CardFileType(CardType)](M_Tessa_Cards_CardFileType__ctor_1.htm)|  Создаёт
экземпляр класса с указанием значений его свойств.  
---|---  
[CardFileType(String, String,
Nullable<Guid>)](M_Tessa_Cards_CardFileType__ctor.htm)|  Создаёт виртуальный
тип карточки с заданными уникальным и отображаемым именем. Свойство
[CardType](P_Tessa_Cards_CardFileType_CardType.htm) созданного типа будет
равно null.  
## __Свойства
[Caption](P_Tessa_Files_FileType_Caption.htm)|  Отображаемое имя типа файла,
которое видит пользователь. Не может быть равно null, пустой строке или
строке, состоящей из пробелов.  
(Унаследован от [FileType](T_Tessa_Files_FileType.htm))  
---|---  
[CardType](P_Tessa_Cards_CardFileType_CardType.htm)|  Метаинформация по типу
файла в карточке или null, если тип файла виртуальный и определяется по имени
[Name](P_Tessa_Cards_CardFileType_Name.htm).  
[ID](P_Tessa_Files_FileType_ID.htm)| Уникальный идентификатор типа файла.  
(Унаследован от [FileType](T_Tessa_Files_FileType.htm))  
[IsVirtual](P_Tessa_Cards_CardFileType_IsVirtual.htm)|  Признак того, что тип
файла является виртуальным, т.е. он отсутствует в метаинформации по карточкам.  
[Name](P_Tessa_Cards_CardFileType_Name.htm)|  Уникальное имя типа файла в
карточке.  
## __Методы
[CreateDefaultAsync](M_Tessa_Cards_CardFileType_CreateDefaultAsync.htm)|
Создаёт тип [IFileType](T_Tessa_Files_IFileType.htm) для стандартного файла
карточки с идентификатором
[FileTypeID](F_Tessa_Cards_CardHelper_FileTypeID.htm).  
---|---  
[CreateVirtual](M_Tessa_Cards_CardFileType_CreateVirtual.htm)|  Создаёт
виртуальный тип файла, который по идентификатору и отображаемому имени не
отличается от стандартного типа
[FileTypeID](F_Tessa_Cards_CardHelper_FileTypeID.htm), но отличается по
уникальному имени [Name](P_Tessa_Cards_CardFileType_Name.htm).  
[Equals(IFileType)](M_Tessa_Files_FileType_Equals_1.htm)| Сравнивает текущий
объект с заданным.  
(Унаследован от [FileType](T_Tessa_Files_FileType.htm))  
[Equals(Object)](M_Tessa_Files_FileType_Equals.htm)| Сравнивает текущий объект
с заданным.  
(Унаследован от [FileType](T_Tessa_Files_FileType.htm))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Files_FileType_GetHashCode.htm)| Возвращает хеш-код
объекта.  
(Унаследован от [FileType](T_Tessa_Files_FileType.htm))  
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
[ToString](M_Tessa_Files_FileType_ToString.htm)| Возвращает строковое
представление объекта.  
(Унаследован от [FileType](T_Tessa_Files_FileType.htm))  
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
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
