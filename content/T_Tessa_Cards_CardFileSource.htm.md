# CardFileSource - класс
Настройки по местоположению контента файла.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardFileSource : ICardFileSource
VB __Копировать
     Public NotInheritable Class CardFileSource
    	Implements ICardFileSource
C++ __Копировать
     public ref class CardFileSource sealed : ICardFileSource
F# __Копировать
     [<SealedAttribute>]
    type CardFileSource = 
        class
            interface ICardFileSource
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardFileSource
Implements
    [ICardFileSource](T_Tessa_Cards_ICardFileSource.htm)
##  __Конструкторы
[CardFileSource](M_Tessa_Cards_CardFileSource__ctor.htm)|  Создаёт экземпляр
класса с указанием значений его свойств.  
---|---  
## __Свойства
[FileExtensions](P_Tessa_Cards_CardFileSource_FileExtensions.htm)|  Строка со
списком расширений, которые рекомендуется использовать с этим источником
файлов. Расширения разделены пробелами и обычно без ведущей точки. Строка
может быть равна null.  
---|---  
[IsDatabase](P_Tessa_Cards_CardFileSource_IsDatabase.htm)| Признак того, что
местоположение соответствует базе данных, а не файловой папке.  
[MaxSize](P_Tessa_Cards_CardFileSource_MaxSize.htm)|  Максимальный размер
занятого места в местоположении. Не заполняется и не используется системой,
возможно использование в расширениях.  
[Name](P_Tessa_Cards_CardFileSource_Name.htm)| Отображаемое имя
местоположения.  
[Path](P_Tessa_Cards_CardFileSource_Path.htm)|  Путь к местоположению.
Соответствует имени строки подключения к БД из конфигурационного файла или
полному путь к файловой папке.  
[Size](P_Tessa_Cards_CardFileSource_Size.htm)|  Текущий размер занятого места
в байтах в местоположении. Не заполняется и не используется системой, возможно
использование в расширениях.  
[Type](P_Tessa_Cards_CardFileSource_Type.htm)| Тип местоположения.  
[UseSimpleNamingScheme](P_Tessa_Cards_CardFileSource_UseSimpleNamingScheme.htm)|
Признак того, что используется упрощённая схема именования папок, где для
карточек не создаются дополнительные подпапки. Значение true не рекомендуется,
если в системе возможны миллионы карточек с файлами, т.к. это приведёт к
миллионам подпапок внутри одной папки в файловой системе. Значение неактуально
для файлов в базе данных.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
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
[IsRecommendedExtension](M_Tessa_Cards_CardFileSource_IsRecommendedExtension.htm)|
Возвращает признак того, что заданное расширение файла является рекомендуемым
для использования совместно с этим источником файлов.  
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
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
