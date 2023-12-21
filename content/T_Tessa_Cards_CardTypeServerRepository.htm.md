# CardTypeServerRepository - класс
Репозиторий для управления типами карточек.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardTypeServerRepository : ICardTypeServerRepository
VB __Копировать
     Public NotInheritable Class CardTypeServerRepository
    	Implements ICardTypeServerRepository
C++ __Копировать
     public ref class CardTypeServerRepository sealed : ICardTypeServerRepository
F# __Копировать
     [<SealedAttribute>]
    type CardTypeServerRepository = 
        class
            interface ICardTypeServerRepository
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardTypeServerRepository
Implements
    [ICardTypeServerRepository](T_Tessa_Cards_ICardTypeServerRepository.htm)
##  __Конструкторы
[CardTypeServerRepository](M_Tessa_Cards_CardTypeServerRepository__ctor.htm)|
Создаёт экземпляр класса с указанием области видимости объекта
[Tessa.Platform.Data.DbManager].  
---|---  
## __Методы
[CardTypeExistsAsync](M_Tessa_Cards_CardTypeServerRepository_CardTypeExistsAsync.htm)|
Возвращает признак того, что тип карточки с заданным идентификатором
существует.  
---|---  
[DeleteAsync(Guid,
CancellationToken)](M_Tessa_Cards_CardTypeServerRepository_DeleteAsync_1.htm)|
Удаляет тип карточки с заданным идентификатором.  
[DeleteAsync(IReadOnlyCollection<Guid>,
CancellationToken)](M_Tessa_Cards_CardTypeServerRepository_DeleteAsync.htm)|
Удаляет типы карточек с заданными идентификаторами.  
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
[GetAllCardTypesAsync](M_Tessa_Cards_CardTypeServerRepository_GetAllCardTypesAsync.htm)|
Возвращает объекты, описывающие типы всех карточек, со всей необходимой
информацией.  
[GetCardTypeAsync](M_Tessa_Cards_CardTypeServerRepository_GetCardTypeAsync.htm)|
Возвращает объект, описывающий тип карточки, со всей необходимой информацией.  
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
[InsertAsync](M_Tessa_Cards_CardTypeServerRepository_InsertAsync.htm)|
Добавляет тип карточки.  
[InsertManyAsync](M_Tessa_Cards_CardTypeServerRepository_InsertManyAsync.htm)|
Добавляет несколько типов карточек оптимальным способом.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[UpdateAsync](M_Tessa_Cards_CardTypeServerRepository_UpdateAsync.htm)|
Обновляет имя и метаданные типа карточки с идентификатором
[Tessa.Cards.CardTypeRepositoryData.ID].  
## __Методы расширения
[DeleteAsync](M_Tessa_Cards_CardExtensions_DeleteAsync_1.htm)|  Удаляет
заданный тип карточки.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
---|---  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[GetAllCardTypeCollectionAsync](M_Tessa_Cards_CardExtensions_GetAllCardTypeCollectionAsync.htm)|
Возвращает коллекцию, содержащую все типы карточек.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
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
