# CardDatabaseContentStrategy - класс
Стратегия управления контентом файла, который хранится в базе данных.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class CardDatabaseContentStrategy : ICardContentStrategy
VB __Копировать
     Public Class CardDatabaseContentStrategy
    	Implements ICardContentStrategy
C++ __Копировать
     public ref class CardDatabaseContentStrategy : ICardContentStrategy
F# __Копировать
     type CardDatabaseContentStrategy = 
        class
            interface ICardContentStrategy
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardDatabaseContentStrategy
Implements
    [ICardContentStrategy](T_Tessa_Cards_ComponentModel_ICardContentStrategy.htm)
##  __Заметки
В наследниках класса можно переопределить его методы.
## __Конструкторы
[CardDatabaseContentStrategy(IDbScope)](M_Tessa_Cards_ComponentModel_CardDatabaseContentStrategy__ctor.htm)|
Создаёт экземпляр класса с указанием области видимости объекта
[DbManager](T_Tessa_Platform_Data_DbManager.htm).  
---|---  
[CardDatabaseContentStrategy(IDbScope,
ICardFileSource)](M_Tessa_Cards_ComponentModel_CardDatabaseContentStrategy__ctor_1.htm)|
Создаёт экземпляр класса с указанием его области видимости объекта
[DbManager](T_Tessa_Platform_Data_DbManager.htm).  
## __Методы
[CleanCardAsync](M_Tessa_Cards_ComponentModel_CardDatabaseContentStrategy_CleanCardAsync.htm)|
Очищает место, отведённое для контента файлов, принадлежащих карточке. Метод
вызывается перед удалением карточки.  
---|---  
[CleanFileAsync](M_Tessa_Cards_ComponentModel_CardDatabaseContentStrategy_CleanFileAsync.htm)|
Очищает место, отведённое для контента файла. Метод вызывается перед удалением
файла.  
[CopyAsync](M_Tessa_Cards_ComponentModel_CardDatabaseContentStrategy_CopyAsync.htm)|
Выполняет копирование контента из исходного местоположения в целевое. Если
исходное и целевое местоположения совпадут, то метод завершится с ошибкой и
вернёт false.  
[DeleteAsync](M_Tessa_Cards_ComponentModel_CardDatabaseContentStrategy_DeleteAsync.htm)|
Удаляет контент версии файла.  
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
[GetAsync](M_Tessa_Cards_ComponentModel_CardDatabaseContentStrategy_GetAsync.htm)|
Загружает контент версии файла.  
[GetFileExtensionWithDotAsync](M_Tessa_Cards_ComponentModel_CardDatabaseContentStrategy_GetFileExtensionWithDotAsync.htm)|
Возвращает расширение указанного файла с точкой. Возвращает строку ".", если
имя файла не найдено.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetSizeAsync](M_Tessa_Cards_ComponentModel_CardDatabaseContentStrategy_GetSizeAsync.htm)|
Возвращает длину контента версии файла в байтах.  
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
[MoveAsync](M_Tessa_Cards_ComponentModel_CardDatabaseContentStrategy_MoveAsync.htm)|
Перемещает контент файла (но не записи по файлу) из исходного местоположения
sourceContext в целевое местоположение targetContext. При этом файл может
перемещаться между карточками и между разными файловыми хранилищами (если
текущая стратегия поддерживает разные хранилища). Если исходное и целевое
местоположения совпадают, то метод не выполняет действий и возвращает true.  
[MoveFileAsync](M_Tessa_Cards_ComponentModel_CardDatabaseContentStrategy_MoveFileAsync.htm)|
Перемещает контент файла sourceFileID (но не записи по файлу) из карточки с
идентификатором sourceCardID в файл targetFileID в карточку с идентификатором
targetCardID. Содержимое не может быть перемещено между разными хранилищами
посредством этого метода, для этого долежн быть создан файл, в который
копируется содержимое исходного файла.  
[MoveFilesAsync](M_Tessa_Cards_ComponentModel_CardDatabaseContentStrategy_MoveFilesAsync.htm)|
Перемещает контент файлов из карточки с идентификатором sourceCardID в
карточку с идентификатором targetCardID. При этом записи в секции по файлам не
перемещаются между карточками, для этого используйте методы
[Tessa.Cards.ComponentModel.ICardStoreStrategy.MoveFiles] или
[Tessa.Cards.ComponentModel.ICardStoreStrategy.MoveFilesAndSetTask].
Содержимое не может быть перемещено между разными хранилищами посредством
этого метода, для этого долежн быть создан файл, в который копируется
содержимое исходного файла.  
[StoreAsync](M_Tessa_Cards_ComponentModel_CardDatabaseContentStrategy_StoreAsync.htm)|
Сохраняет контент версии файла.  
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
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
